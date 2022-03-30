class Client:
    # variable de clase
    yearCost = 100

    # metodo constructor de la clase
    def __init__(self, name, age, email, years) -> None:
        # variables de instancia
        self.name = name
        self.age = age
        self.email = email
        self.years = years

    def __repr__(self) -> str:
        return f"Client('{self.name}', {self.age}, '{self.email}', {self.years})"

    # metodos de instancia
    def getRetirement(self):
        return self.years * Client.yearCost

    def display(self):
        print(f"{self.name} {self.age} {self.email} ${self.getRetirement()}")

    # metodo de clase
    @classmethod
    def addYearCost(cls):
        cls.yearCost += 10


class Product:
    # metodo constructor de la clase
    def __init__(self, name, cost, brand) -> None:
        self.name = name
        self.cost = cost
        self.brand = brand

    def __repr__(self) -> str:
        return f"Product('{self.name}', {self.cost}, '{self.brand}')"
