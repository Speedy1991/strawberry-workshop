import os.path
import socket
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup
from django.http import HttpRequest
from django.template.defaultfilters import safe
from django.contrib.staticfiles import finders


@dataclass(frozen=True)
class Assets:
    body: str
    head: str


@dataclass(frozen=True)
class AppLoader:
    static_path: str
    port: int
    bundle: str


    def get_static_server_assets(self) -> Assets:
        asset_file_path = finders.find(self.static_path)
        if not asset_file_path or not os.path.isfile(asset_file_path):
            raise FileNotFoundError(
                f"Vite Loader - Unable to locate bundle '{self.bundle}' with HTML file "
                f"'{self.static_path}' in the static files storage."
            )

        with open(asset_file_path, encoding='UTF-8') as asset_file:
            parsed_html = BeautifulSoup(asset_file.read(), features='lxml')
            head_section = parsed_html.head.decode_contents() if parsed_html.head else ""
            body_section = parsed_html.body.decode_contents() if parsed_html.body else ""

        return Assets(
            body=safe(body_section),
            head=safe(head_section)
        )

    def vite_dev_server_running(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection attempt
            result = s.connect_ex(('127.0.0.1', self.port))
            return result == 0  # 0 means the port is open

    def get_dev_server_assets_with_replacements(self, request: HttpRequest) -> Assets | None:
        local_server_url = f'http://127.0.0.1:{self.port}'
        external_server_url = f'http://{request.get_host().split(":")[0]}:{self.port}/'

        if not self.vite_dev_server_running():
            return None

        try:
            response = requests.get(local_server_url, timeout=1)
            if response.status_code != 200 or response.headers.get('Vite-Bundle') != self.bundle:
                return None
        except requests.exceptions.RequestException:
            return None

        parsed_html = BeautifulSoup(response.content, features='lxml')
        head_section = str(parsed_html.head.decode_contents())
        body_section = str(parsed_html.body.decode_contents())

        url_patterns_to_replace = {
            'src="/': f'src="{external_server_url}',
            '<link href="/': f'<link href="{external_server_url}',
            'import { inject } from "/': f'import {{ inject }} from "{external_server_url}',
            'base: "/",': f'base: "{external_server_url}",',
            'base: "http://127.0.0.1:8000/",': f'base: "{external_server_url}",',
            '"/@react-refresh"': f'"{external_server_url}@react-refresh"'
        }

        for original, updated in url_patterns_to_replace.items():
            head_section = head_section.replace(original, updated)
            body_section = body_section.replace(original, updated)

        return Assets(
            body=safe(body_section),
            head=safe(head_section)
        )

    def assets(self, request: HttpRequest) -> Assets:
        # if dev server is running, return the dev server stuff
        dev_assets = self.get_dev_server_assets_with_replacements(request)
        if dev_assets:
            return dev_assets
        # else return the bundled stuff from the static folder
        return self.get_static_server_assets()
