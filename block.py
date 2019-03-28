class block:
    name = ""

    def __init__(self, velocity, size, weight):
        self.velocity = velocity
        self.size = size
        self.weight = weight

    def sayHello(self):
        print
        "Hello, my name is " + self.name
