class Animal():
    def sleep(self):
        print("I can sleep")
    def eat(self):
        print("i can eat")
    def height(self):
        print("i am tall")
class Dog(Animal):
    def sleep(self):
        print("I can sleep in every position")
    def bark(self):
        print("wooof")

class Horse(Animal):
    def sleep(self):
        print("I can sleep in one position")
    def speak(self):
        print("psppsps")
class Snake(Animal):
    def sleep(self):
        print("I can also sleep in one position")
    def speak(self):
        print("hissss")

dog = Dog()
dog.sleep()
dog.eat()
print()
horse = Horse()
horse.sleep()
horse.speak()
horse.eat()
print()
snake = Snake()
snake.sleep()
snake.eat()


