class myclass:
    __privatevar=27;

    def __privatemethod(self):
        print("i am inside class")

    def hello(self):
        print("private variable=",myclass.__privatevar)

foo=myclass()
foo.hello()
foo.__privatemethod