from typing import List, Optional
from datetime import datetime
import uuid
from ..entities.product import Product
from ...core.result import Result
from ...core.error.exceptions import DomainError, DomainException, ErrorType
from ..repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def create_product(
        self, 
        name: str, 
        price: float, 
        description: Optional[str] = None
    ) -> Result[Product]:
        try:
            if not name:
                return Result.failure(
                    DomainError(
                        type=ErrorType.VALIDATION_ERROR,
                        message="Product name cannot be empty"
                    )
                )

            if price < 0:
                return Result.failure(
                    DomainError(
                        type=ErrorType.VALIDATION_ERROR,
                        message="Price cannot be negative",
                        details={"price": price}
                    )
                )

            product = Product(
                id=str(uuid.uuid4()),
                name=name,
                price=price,
                description=description,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            
            self.product_repository.save(product)
            return Result.success(product)
            
        except Exception as e:
            return Result.failure(
                DomainError(
                    type=ErrorType.UNEXPECTED_ERROR,
                    message="Failed to create product",
                    details=str(e)
                )
            )

    def update_product_price(self, product_id: str, new_price: float) -> Result[Product]:
        try:
            product = self.product_repository.find_by_id(product_id)
            
            if not product:
                return Result.failure(
                    DomainError(
                        type=ErrorType.NOT_FOUND,
                        message=f"Product with id {product_id} not found"
                    )
                )

            try:
                product.update_price(new_price)
                self.product_repository.save(product)
                return Result.success(product)
            except DomainException as de:
                return Result.failure(de.error)
                
        except Exception as e:
            return Result.failure(
                DomainError(
                    type=ErrorType.UNEXPECTED_ERROR,
                    message="Failed to update product price",
                    details=str(e)
                )
            )
