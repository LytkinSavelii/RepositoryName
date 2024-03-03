if __name__ == "__main__":
    # Write your solution here
    class Sportsmen:
        def __init__(self, reach: float, weight: float):
            self.reach = reach
            self.weight = weight

        @property
        def reach(self):
            return self._reach

        @reach.setter
        def reach(self, reach_x: float):
            if not isinstance(reach_x, float):
                raise TypeError("Размах должен быть задан в сантиметрах")

            if reach_x <= 0:
                raise ValueError("Размах не может быть отрицательным")

            self._reach = reach_x

        @property
        def weight(self, weight_x: float):
            if not isinstance(weight_x, float):
                raise TypeError("Вес должен быть задан в сантиметрах")

            if weight_x <= 0:
                raise ValueError("Вес не может быть отрицательным")

            self._weight = weight_x

        def __str__(self):
            return f"Спортсмен весом {self.weight!r} с размахом рук {self.reach!r}"
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(reach={self.reach}, weight={self.weight})"


    class Cruiserweighter(Sportsmen):
        def __init__(self, age: int, nation: str):

            self.age = age
            self.nation = nation

    pass
