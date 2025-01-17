from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from src.core.error.exceptions import DomainError, DomainException, ErrorType

@dataclass
class Product:
    id: str
    name: str
    price: float
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    def update_price(self, new_price: float) -> None:
        if new_price < 0:
            raise DomainException(
                DomainError(
                    type=ErrorType.VALIDATION_ERROR,
                    message="Price cannot be negative",
                    details={"price": new_price}
                )
            )
        self.price = new_price
        self.updated_at = datetime.now()
