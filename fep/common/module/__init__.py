from abc import ABCMeta, abstractmethod, abstractproperty

from typing import Any, final, Dict

from .utils.encoding import Encoding
from .utils.http import HTTP
from .utils.os import Os


class Module(
    Os,
    HTTP,
    Encoding,
    metaclass=ABCMeta,
):
    __slots__ = ("env",)

    @final
    def __init__(self, env: Dict[str, Any] = dict()) -> None:
        self.env = env

    @property
    @abstractmethod
    def data(self) -> Dict[str, str]:
        raise NotImplementedError()

    @abstractmethod
    def execute(self) -> int:
        raise NotImplementedError()
