class ProductError(Exception):
    pass

class Currency:
    usd = 28.00


class Product:
    idProduct = 100
    def __init__(self, name: str, weight: float, price: float):
        self.name = name
        self.weight = weight
        self.price = price * Currency.usd
        Product.idProduct+=1
        self.current_id = Product.idProduct

    @staticmethod
    def get_id():
        return Product.idProduct


    def get_current_id(self):
        return self.current_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self) -> str:
        return f"{self.name}, {self.get_current_id()}/{Product.get_id()}"

    def __repr__(self):
        return self.__str__()

class Fruits(Product):
    pass

class Order:
    def __init__(self, number: int, date):
        self.number = number
        self.date = date
        self.products = list()

    def add(self, product: Product) -> bool:
        """
        Add product in list
        :param product: Product
        :return:
        """
        if isinstance(product, Product):
            self.products.append(product)
            return True
        else:
            raise ProductError()

    def print(self):
        print(self.products)

if __name__ == '__main__':
    order_products = Order("1",1)
    order_products.add(Product("Apple1",1,2))
    order_products.add(Product("Apple2",1,2))
    order_products.add(Product("Apple3",1,2))
    order_products.add(Product("Apple4",1,2))
    order_products.add(Fruits("Banana4",1,2))

    order_products.print()
