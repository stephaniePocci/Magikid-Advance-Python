"""
This script demonstrates Object-Oriented Programming (OOP) using a fun hierarchy of classes.
Our world is made up of all kinds of "Things"—both animate and inanimate. 
Today, we follow the journey of Po the Panda and explore the mystery of an enchanted box!
"""

class Things:
    """Base class representing all things in our world."""
    def __init__(self, name="Unknown Thing"):
        self.name = name

    def info(self):
        """Display basic info about the thing."""
        print(f"Meet {self.name}, a fascinating part of our world!")

class Inanimate(Things):
    """Represents inanimate objects that do not have life."""
    def interact(self):
        """Simulate interacting with an inanimate object."""
        print(f"You examine the {self.name} closely. It might have a hidden story!")

class Animate(Things):
    """Represents animate objects that are alive."""
    def live(self):
        """Express the liveliness of an animate object."""
        print(f"{self.name} is bursting with life and energy!")

class Boxes(Inanimate):
    """A special type of inanimate object: a box full of surprises."""
    def open_box(self):
        """Simulate opening the box."""
        print(f"You carefully open the {self.name}. What secrets will it reveal?")

class Animals(Animate):
    """Represents animals, creatures that share many behaviors."""
    def breathe(self):
        """Simulate the animal breathing."""
        print(f"{self.name} takes a deep breath, feeling the wonder of life.")

    def move(self):
        """Simulate the animal moving."""
        print(f"{self.name} moves around gracefully, ready for adventure.")

    def eat_food(self):
        """Simulate the animal eating."""
        print(f"{self.name} enjoys a delightful meal.")

class Mammals(Animals):
    """Represents mammals—a group of animals that nurture their young with milk."""
    def feed_milk(self):
        """Simulate feeding milk to offspring."""
        print(f"{self.name} lovingly feeds milk to its little ones.")

class Pandas(Mammals):
    """Represents pandas—a charming type of mammal famous for munching on bamboo."""
    def eat_bamboos(self):
        """Simulate a panda eating bamboo."""
        print(f"{self.name} happily munches on bamboo, savoring every bite!")

# Create our animated characters and objects in this little OOP world

# Panda's Adventure
panda = Pandas("Po the Panda")
print("=== Panda's Journey ===")
panda.info()
panda.live()
panda.breathe()
panda.move()
panda.eat_food()
panda.feed_milk()
panda.eat_bamboos()

# Mystery Box Adventure
mystery_box = Boxes("Enchanted Box")
print("\n=== Box Adventure ===")
mystery_box.info()
mystery_box.interact()
mystery_box.open_box()
