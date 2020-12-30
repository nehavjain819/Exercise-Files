#
# Example file for working with classes
#
class myclass():
        def method1(self):
            print("this method1 class method")
        def method2(self, another_args):
            print("this is method2 " + another_args)

class inheritclass(myclass):
    def method1(self):
        myclass.method1(self)
        print("this is inherited class method1")
    def method2(self, arg2):
        print("this is inherited class method2")


def main():
    c = myclass()
    c.method1()
    c.method2("this is args passing")

    c2 = inheritclass()
    c2.method1()
    c2.method2("args2 passing")

if __name__ == "__main__":
    main()

