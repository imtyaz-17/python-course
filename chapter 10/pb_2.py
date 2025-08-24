class Calcuator:

    def __init__(self, num):
        self.num = num
    
    def square(self):
        print('Square:', self.num ** 2)

    def cube(self):
        print('Cube:', self.num ** 3)
    
    def squareroot(self):
        print('Square Root:', self.num ** 0.5)


obj = Calcuator(4)

obj.square()
obj.cube()
obj.squareroot()

        