class Person:
  def __init__(self, name, age, no):
    self.name = name
    self.age = age
    self.no = no

  def myfunc(abc):
    print(f"Hello my name is {abc.name} and my age is {abc.age} and my number is {abc.no}")

p1 = Person("Sahil", "21", "8210924161")
p1.myfunc()