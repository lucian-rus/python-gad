class Fractie(object): 
    def __init__(self, numarator, numitor):
        self.numarator = numarator;
        self.numitor = numitor;

    def __str__(self):
        return (str(self.numarator) + "/" + str(self.numitor))

    def __add__(self, other):
        numitor_comun = self.numitor * other.numitor

        self.numarator  *= other.numitor
        other.numarator *= self.numitor

        return Fractie(self.numarator + other.numarator, numitor_comun)

    def __sub__(self, other):
        numitor_comun = self.numitor * other.numitor
               
        self.numarator  *= other.numitor
        other.numarator *= self.numitor

        return Fractie(self.numarator + other.numarator, numitor_comun)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)

# test instancing
f1 = Fractie(4, 2)
f2 = Fractie(3, 3)

# test __str__
print(f1)
print(f2)

# test __add__
print(f1 + f2)
# test __sub__
print(f1 - f2)

# test inverse() 
print(f1.inverse())
print(f2.inverse())