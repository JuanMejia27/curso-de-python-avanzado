class Subject:
    def __init__(self):
        self._observers = []
    def attach(self, observer):
        self._observers.append(observer)
    def detach(self, observer):
        self._observers.remove(observer)
    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


class User(Observer):
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} ha recibido el mensaje: {message}")


server = Subject()
user1 = User("Usuario 1")
user2 = User("Usuario 2")
user3 = User("Usuario 3")

server.attach(user1)
server.attach(user2)
server.attach(user3)

server.notify("El servidor esta en mantenimiento.")  # Notifica a todos los usuarios

server.detach(user2)
server.notify("El servidor esta en línea.")  # Notifica a los usuarios