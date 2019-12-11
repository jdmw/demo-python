class DefindTrueLenZero :
    def __bool__(self):
        return True

    def __len__(self):
        return 0

class DefindTrueLenOne :
    def __bool__(self):
        return True

    def __len__(self):
        return 1

class DefindFalseLenZero :
    def __bool__(self):
        return False

    def __len__(self):
        return 0

class DefindFalseLenOne :
    def __bool__(self):
        return False

    def __len__(self):
        return 1

class DefinedPass:
    pass

class DefindFalse:
    def __bool__(self):
        return False


class DefindLenZero :
    def __len__(self):
        return 0

if __name__ == '__main__':
    print(not not DefindTrueLenZero())
    print(not not DefindTrueLenOne())
    print(not not DefindFalseLenZero())
    print(not not DefindFalseLenOne())
    print(not not DefinedPass())
    print(not not DefindFalse())
    print(not not DefindLenZero())



