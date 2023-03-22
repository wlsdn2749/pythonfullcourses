class Animal:
    
    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")



class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.run()
fish.eat()
hawk.sleep()