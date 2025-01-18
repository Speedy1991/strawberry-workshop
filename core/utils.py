import datetime
from enum import Enum
from typing import Callable, Any

import strawberry
from asgiref.sync import sync_to_async
from strawberry.extensions import FieldExtension


def convert_value(obj):
    if isinstance(obj, Enum):
        return obj.value
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    return obj


def asdict_factory(data):
    return dict((k, convert_value(v)) for k, v in data)


class UpperCaseExtension(FieldExtension):
    def resolve(self, next_: Callable[..., Any], source: Any, info: strawberry.Info, **kwargs):
        result = next_(source, info, **kwargs)
        return str(result).upper()

async def sta(qs):
    return await sync_to_async(lambda: list(qs))()
