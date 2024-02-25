class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def name(self) -> str:
        return self._name

    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name!r}. Автор - {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook:
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

        def pages(self) -> int:
            return self._pages

        def pages(self, new_pages: int) -> None:
            if not isinstance(new_pages, int):
                raise TypeError("Количество страниц должно быть задано числом")

            if new_pages <= 0:
                raise ValueError("Количество страниц должно быть больше нуля")

            self._pages = new_pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages}"

class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    def duration(self) -> float:
        return self._duration
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть задана числом")

        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть больше нуля")

        self._duration = new_duration

        def __str__(self):
            return f"Аудиокнига {self.name!r}. Автор {self.author}. Продолжительность {self.duration}"

        def __repr__(self):
            return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration}"
