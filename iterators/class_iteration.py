class Greeting:
    def __init__(self, greet):
        self.greet = greet
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.greet):
            raise StopIteration
        char = self.greet[self.index]
        self.index += 1
        return char

output = Greeting("hello")
for x in output:
    print(x)
