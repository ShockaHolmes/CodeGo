class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)


class Person:
        def __init__(self, name, age):
                self.name = name
                self.age = age

def say_hello(self):
	print(f"Hello, my name is {self.name}")

def have_birthday(self):
	self.age = self.age + 1
	print(f"Happy Birthday! {self.name} is now {self.age}")

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)

