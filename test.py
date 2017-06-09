class test:
    b = 0
    def __init__(self):
        print test.b
        self.a = 1
        test.b = "wertyu"
        print self.a
        print test.b
    def hehe(self):
        print test.b

w = test()
w.hehe()
