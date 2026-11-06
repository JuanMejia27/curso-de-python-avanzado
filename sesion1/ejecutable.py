'''class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True'''

'''from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return "Guau!"
        #print("Guau!")


class Gato(Animal):
    def hablar(self):
        return "Miau!"
        #print("Miau!")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "perro":
            return Perro()
        elif animal_type == "gato":
            return Gato()
        else:
            raise ValueError("Tipo de animal desconocido")

dog = AnimalFactory.create_animal("perro")
cat = AnimalFactory.create_animal("gato")
print(dog.hablar())
print(cat.hablar())'''

'''class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, observer): # Este método se utiliza para agregar un observador a la lista de observadores del sujeto. Cuando se llama a este método, el observador se agrega a la lista y estará listo para recibir notificaciones cuando ocurra un cambio en el sujeto.
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def update(self):
        pass


class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name
    def update(self):
        print(self.name + "Ha sido notificado.")


subject = Subject()
observer1 = ConcreteObserver("Observador 1 ")
observer2 = ConcreteObserver("Observador 2 ")

subject.attach(observer1)
subject.attach(observer2)

subject.notify()  # Notifica a todos los observadores'''

class Strategy:
    def execute(self, a, b):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)


class Context: 
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy.execute(data)

data = [5, 2, 9, 1, 5, 6]
context = Context(ConcreteStrategyA())
print(context.execute_strategy(data))  # Output: [1, 2, 5, 5, 6, 9]

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy(data))  # Output: [9, 6, 5, 5, 2, 1]