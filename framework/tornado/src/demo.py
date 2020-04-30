
class Demo :

    def demo(self,name):
        return self.hideName(name)

    def hideName(self, name):
        print(type(name))
        if len(name) == 0:
            return name
        d = name.encode('utf-8').decode('utf-8')
        str = d[0:1]
        loop = len(d) - 1
        print(str)
        while loop > 0:
            str += u'*'
            print(str)
            loop = loop - 1;
        return str


if __name__ == '__main__':

    print(Demo().demo("欠缺非"))