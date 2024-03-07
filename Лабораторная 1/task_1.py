
import doctest

class Animal:

    def __init__(self, name: str, diet: str, weight: float):

        if not isinstance(name, str):
            raise TypeError("Название должно быть введено строкой")
        self.name = name

        if not isinstance(diet, str):
            raise TypeError("Кормовая база должна быть введена строкой")
        self.diet = diet

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть введён как число")
        if weight < 0:
            raise ValueError("Вес должен быть положительным")
        self.weight = weight

    def anim_carn(self) -> bool:
        ...
    def anim_size(self) -> float:
        ...

class Plants:

    def __init__(self, name: str, height: float, weight: float):

        if not isinstance(name, str):
            raise TypeError("Название должно быть введено строкой")
        self.name = name

        if not isinstance(height, float):
            raise TypeError("Высота растения должна быть введена числом в м")
        self.height = height

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть введён как число")
        if weight < 0:
            raise ValueError("Вес должен быть положительным")
        self.weight = weight

    def plant_toughness(self) -> float:
        ...
    def plant_volume(self) -> float:
        ...

class Bricks:

    def __init__(self, amount: int, material: str, weight: float):

        if not isinstance(amount, int):
            raise TypeError("Количество должно быть введено в штуках")
        self.amount = amount

        if not isinstance(material, str):
            raise TypeError("Введите материал кирпичей символами")
        self.material = material

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть введён как число")
        if weight < 0:
            raise ValueError("Вес должен быть положительным")
        self.weight = weight

    def brick_volume(self) -> float:
        ...
    def brick_cost(self) -> float:
        ...

doctest.testmod()

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
