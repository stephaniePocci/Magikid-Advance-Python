class Things:  # Create the Things class
    pass

class Inanimate(Things):  # Create an Inanimate class, specifying Things as its parent；
    pass

class Animate(Things):  # Create an Animate class, specifying Things as its parent;
    pass

class Boxes(Inanimate):  # Create a Boxes class, specifying Inanimate as its parent;
    pass

class Animals(Animate):  # Create an Animals class, specifying Animate as its parent；
    pass

class Mammals(Animals):  # Create a Mammals class, specifying Animals as its parent;
    pass

class Pandas(Mammals):  # Create a Pandas class, specifying Mammals as its parent;
    pass

gungun = Pandas()  # Create an object of class Pandas and assign it to the variable gungun.

