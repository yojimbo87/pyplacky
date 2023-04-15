from classes import Foo, Car

def print_values(obj_name: str, obj: Foo) -> None:
    print(f"    {obj_name} static_counter value: {obj.static_counter}")
    print(f"    {obj_name} instance_counter value: {obj.instance_counter}")

print("Creating foo1 instance")
foo1 = Foo()

print_values("foo1", foo1)

print("Calling foo1.static_counter_increment1()")
foo1.static_counter_increment1()

print("Calling foo1.instance_counter_increment()")
foo1.instance_counter_increment()

print_values("foo1", foo1)

print("Calling foo1.static_counter_increment2()")
foo1.static_counter_increment2()

print("Calling foo1.instance_counter_increment()")
foo1.instance_counter_increment()

print_values("foo1", foo1)

print("Creating foo2 instance")
foo2 = Foo()

print_values("foo1", foo1)
print_values("foo2", foo2)

print("Calling foo2.static_counter_increment1()")
foo2.static_counter_increment1()

print("Calling foo2.instance_counter_increment()")
foo2.instance_counter_increment()

print_values("foo1", foo1)
print_values("foo2", foo2)

print("Calling foo2.static_counter_increment2()")
foo2.static_counter_increment2()

print("Calling foo2.instance_counter_increment() two times")
foo2.instance_counter_increment()
foo2.instance_counter_increment()

print_values("foo1", foo1)
print_values("foo2", foo2)

print("------------------")

car = Car("Ford", "Mustang", 2022)

# Accessing protected attribute
print(car._make)  # Output: Ford

# Accessing private attribute using name mangling
print(car._Car__model)  # Output: Mustang

# Calling public method which in turn calls private method
car.start()  # Output: The engine is turned on. The car is started.

# Calling public method which in turn calls private method
car.stop()  # Output: The engine is turned off. The car is stopped.

# Using public getter method for protected attribute
print(car.get_make())  # Output: Ford

# Using public setter method for protected attribute
car.set_make("Chevrolet")
print(car.get_make())  # Output: Chevrolet

# Using public getter method for private attribute
print(car.get_model()) # Output: Mustang

# Using public property for private attribute
print(car.get_model()) # Output: Mustang

# Using public setter method for private attribute
car.set_model("Camry")
print(car.get_model()) # Output: Camry

# Accessing private attribute (won't work)
#print(car.__model)  # Raises an AttributeError
#print(car.__turn_on_engine()) # Raises an AttributeError