from typing import Dict, List, Optional
from ...domain.entities.product import Product
from ...domain.repositories.product_repository import ProductRepository

class MemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def save(self, product: Product) -> None:
        self.products[product.id] = product

    def find_by_id(self, product_id: str) -> Optional[Product]:
        return self.products.get(product_id)

    def find_all(self) -> List[Product]:
        return list(self.products.values())

    def delete(self, product_id: str) -> None:
        if product_id in self.products:
            del self.products[product_id]
