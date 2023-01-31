class Main:
    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name


obj = Main("Test 1")
print(obj)
obj2 = Main("Test 2")
print(obj2)
