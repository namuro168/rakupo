class TEST:
    def __init__(self, txt, txt2):
        self.txta = txt
        self.txtb = txt2
        print("__init__")
    def add(self,majiA):
        # wk1 = self.txta + txt

        print("def add")
        return self.txta,self.txtb
    ###print()

if __name__ == '__main__':
    obj = TEST(1, 5)
    obj2 = TEST(2, 6)
    print(obj)
    p1 = obj.add(obj2)
    print(p1)