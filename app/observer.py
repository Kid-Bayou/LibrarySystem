from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, book_title):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, book_title):
        for observer in self._observers:
            observer.update(book_title)
