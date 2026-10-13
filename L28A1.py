class myClass:
    __privateVar = 27

    def __privateMeth(self):
        print("I'm inside myClass")

        def hello(self):
            print("Private variable value", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateMeth