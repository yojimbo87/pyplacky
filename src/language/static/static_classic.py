# My module

class Foo:
    cache = []

    # Static method knows nothing about the class and just deals with the parameters
    @staticmethod
    def add(num1: int, num2: int):
        res = num1 + num2
        
        Foo.cache.append(res)
        
        return res
    
    # Class method works with the class since its parameter is always the class itself
    # Works like staticmethod in principle
    @classmethod
    def sub(cls, num1: int, num2: int):
        res = num1 - num2
        
        cls.cache.append(res)
        
        return res