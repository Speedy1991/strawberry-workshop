import datetime
import json
from enum import Enum

import strawberry
from asgiref.sync import sync_to_async
from django.conf import settings
from redis.typing import EncodableT, ChannelT
import redis as redis_lib


def convert_value(obj):
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    return obj


def asdict_factory(data):
    return dict((k, convert_value(v)) for k, v in data)


def sid(identifier: str | int) -> strawberry.ID:
    return strawberry.ID(identifier)


async def sta(qs):
    return await sync_to_async(lambda: list(qs))()


class RedisSingleTone:
    __instance = None

    @classmethod
    def instance(cls):
        if RedisSingleTone.__instance is None:
            RedisSingleTone.__instance = object.__new__(cls)
            RedisSingleTone.__instance.redis = redis_lib.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=0,
                socket_connect_timeout=2,
                socket_timeout=2,
                max_connections=1000,
                socket_keepalive=True,
            )
        return RedisSingleTone.__instance

    @classmethod
    def subscribe(cls, key):
        instance = cls.instance()
        pubsub = instance.redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(key)
        return pubsub

    @classmethod
    def publish(cls, key: ChannelT, value: EncodableT):
        instance = cls.instance()
        return instance.redis.publish(key, value)

    @classmethod
    def get_data(cls, message: dict):
        if not message:
            return None
        message = message["data"].decode("utf-8")
        try:
            return json.loads(message)
        except json.decoder.JSONDecodeError:
            return message
