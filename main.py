from src.application.controllers.product_controller import ProductController
from src.application.dtos.product_dto import CreateProductDTO
from src.domain.services.product_service import ProductService
from src.infrastructure.repositories.memory_product_repository import MemoryProductRepository

def main():
    # Configuração das dependências
    product_repository = MemoryProductRepository()
    product_service = ProductService(product_repository)
    product_controller = ProductController(product_service)

    # Exemplo de uso com tratamento de erros
    product_dto = CreateProductDTO(
        name="Smartphone",
        price=999.99,
        description="Latest model smartphone"
    )

    # Criar um produto
    result = product_controller.create_product(product_dto)
    if result["success"]:
        print(f"Created product: {result['data']}")
    else:
        print(f"Error creating product: {result['error']}")

    if result["success"]:
        # Tentar atualizar com preço negativo para demonstrar tratamento de erro
        update_result = product_controller.update_product_price(
            result["data"].id, 
            -100.00
        )
        
        if update_result["success"]:
            print(f"Updated product: {update_result['data']}")
        else:
            print(f"Error updating product: {update_result['error']}")

if __name__ == "__main__":
    main()
