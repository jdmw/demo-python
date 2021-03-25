class ObjectDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, key, value):
        self[key] = value

if __name__ == "__main__":
    d = ObjectDict()
    d.s = 1
    print(d.s)