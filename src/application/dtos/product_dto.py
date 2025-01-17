from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from src.domain.entities.product import Product

@dataclass
class CreateProductDTO:
    name: str
    price: float
    description: Optional[str] = None

@dataclass
class ProductResponseDTO:
    id: str
    name: str
    price: float
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, product: Product) -> 'ProductResponseDTO':
        return cls(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            created_at=product.created_at,
            updated_at=product.updated_at
        )
