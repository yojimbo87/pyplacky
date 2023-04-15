# https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances
# https://www.programiz.com/python-programming/methods/built-in/classmethod
import static_pythonic
from static_classic import Foo

num1: int = 3
num2: int = 2

res1 = static_pythonic.add(num1, num2)
res2 = Foo.add(num1, num2)
res3 = Foo.sub(num1, num2)

print(f"Static pythonic add: {res1}")
print(f"Static class(ic) add: {res2}")
print(f"Static class(ic) sub: {res3}")