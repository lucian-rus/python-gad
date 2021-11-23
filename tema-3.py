class Fractie(object): 
    def __init__(self, numarator, numitor):
        self.numarator = numarator;
        self.numitor = numitor;

    def __str__(self):
        return (str(self.numarator) + "/" + str(self.numitor))

    def __add__(self, other):
        return (self.numarator / self.numitor) + (other.numarator / other.numitor)

    def __sub__(self, other):
        return (self.numarator / self.numitor) - (other.numarator / other.numitor)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

# test instancing
f1 = Fractie(13, 4)
f2 = Fractie(21, 5)

# test __str__
print(f1)
print(f2)

# test __add__
print(f1 + f2)
# test __sub__
print(f1 - f2)
# test inverse() 
print(f1.inverse())