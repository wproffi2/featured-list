#testing args 
def some_args(*args):
    print(list(args))

args = ("Sammy", "Casey", "Alex")
some_args(*args)