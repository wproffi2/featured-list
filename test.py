#testing args 

class ArgTest:
    def __init__(self, *args):
        self.args = list(args)
    
    def test(self):
        print(self.args)

args = ["Sammy", "Casey", "Alex"]
x = ArgTest(*args)
x.test()