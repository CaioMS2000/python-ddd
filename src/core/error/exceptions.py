from dataclasses import dataclass
from typing import Any, Optional
from enum import Enum

class ErrorType(Enum):
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    BUSINESS_RULE_VIOLATION = "BUSINESS_RULE_VIOLATION"
    INFRASTRUCTURE_ERROR = "INFRASTRUCTURE_ERROR"
    UNEXPECTED_ERROR = "UNEXPECTED_ERROR"

@dataclass
class DomainError:
    type: ErrorType
    message: str
    details: Optional[Any] = None

    def __str__(self) -> str:
        return f"{self.type.value}: {self.message}"

class DomainException(Exception):
    def __init__(self, error: DomainError):
        self.error = error
        super().__init__(str(error))
