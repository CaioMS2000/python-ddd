from dataclasses import dataclass
from typing import Generic, TypeVar, Union, Optional
from .error.exceptions import DomainError

T = TypeVar('T')

@dataclass
class Result(Generic[T]):
    """
    Classe para representar o resultado de uma operação que pode falhar
    """
    _value: Optional[T]
    _error: Optional[DomainError]

    @staticmethod
    def success(value: T) -> 'Result[T]':
        return Result(_value=value, _error=None)

    @staticmethod
    def failure(error: DomainError) -> 'Result[T]':
        return Result(_value=None, _error=error)

    @property
    def is_success(self) -> bool:
        return self._error is None

    @property
    def is_failure(self) -> bool:
        return self._error is not None

    @property
    def value(self) -> T:
        if self._value is None:
            raise ValueError("Cannot get value from a failed result")
        return self._value

    @property
    def error(self) -> DomainError:
        if self._error is None:
            raise ValueError("Cannot get error from a successful result")
        return self._error
