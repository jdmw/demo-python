class A:
    def id(self):
        return 1

class B:
    def id(self):
        return 1

if __name__ == '__main__':
    print(A() is A())