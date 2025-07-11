from dataclasses import dataclass
from typing import TYPE_CHECKING

from strawberry import Info
from strawberry.types.info import RootValueType

if TYPE_CHECKING:
    from core.dataloaders import DataLoaders


@dataclass
class MyContext:
    loaders: "DataLoaders"


MyInfo = Info[MyContext, RootValueType]
