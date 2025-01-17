from typing import Dict, Any

from ..dtos.product_dto import CreateProductDTO, ProductResponseDTO
from ...domain.services.product_service import ProductService

class ProductController:
    def __init__(self, product_service: ProductService):
        self.product_service = product_service

    def create_product(self, product_dto: CreateProductDTO) -> Dict[str, Any]:
        result = self.product_service.create_product(
            name=product_dto.name,
            price=product_dto.price,
            description=product_dto.description
        )

        if result.is_success:
            return {
                "success": True,
                "data": ProductResponseDTO.from_entity(result.value),
                "error": None
            }
        else:
            return {
                "success": False,
                "data": None,
                "error": {
                    "type": result.error.type.value,
                    "message": result.error.message,
                    "details": result.error.details
                }
            }

    def update_product_price(self, product_id: str, new_price: float) -> Dict[str, Any]:
        result = self.product_service.update_product_price(product_id, new_price)

        if result.is_success:
            return {
                "success": True,
                "data": ProductResponseDTO.from_entity(result.value),
                "error": None
            }
        else:
            return {
                "success": False,
                "data": None,
                "error": {
                    "type": result.error.type.value,
                    "message": result.error.message,
                    "details": result.error.details
                }
            }
