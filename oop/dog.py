class Dog:
  # Class Attribute
  species = "canies familiaris"
  
  def __init__(self, name, age, breed):
    self.name = name
    self.age = age
    self.breed = breed

  # Replace the .discription() with __str__()
  def __str__(self):
    return f'{self.name} is {self.age} year old'

  # Another Instance Method
  def speak(self, sound):
    return f"{self.name} says {sound}"


class JackRusselTerrier(Dog):
  def speak(self, sound="Arf"):
    return super().speak(sound)

class Dachshund(Dog):
  def speak(self, sound="Yap"):
    return super().speak(sound)

class Bulldog(Dog):
  def speak(self, sound="Woof Woof"):
    return super().speak(sound)

class GoldenRetriever(Dog):
  def speak(self, sound="Bark"):
    return super().speak(sound)
