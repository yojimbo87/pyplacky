class Foo:
    # Public static property
    static_counter: int = 0

    def __init__(self) -> None:
        # Public property
        self.instance_counter: int = 0

    @classmethod
    def static_counter_increment1(cls) -> None:
        cls.static_counter += 1

    def static_counter_increment2(self) -> None:
        Foo.static_counter += 1
    
    def instance_counter_increment(self) -> None:
        self.instance_counter += 1

class Car:
    def __init__(self, make, model, year):
        self._make = make  # protected attribute
        self.__model = model  # private attribute
        self.year = year

    def start(self):
        self.__turn_on_engine()  # private method
        print("The car is started.")

    def stop(self):
        self.__turn_off_engine()  # private method
        print("The car is stopped.")

    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self.__model
    
    @property
    def model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def __turn_on_engine(self):
        print("The engine is turned on.")

    def __turn_off_engine(self):
        print("The engine is turned off.")