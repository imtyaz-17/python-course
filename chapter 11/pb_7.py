class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)


v1 = Vector([1, 2, 3, 4, 5])

print("Length of vector:", len(v1))  # Output: Length of vector: 5
