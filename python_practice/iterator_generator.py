
class Iterator:

    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):

        if self.count<=0:
            raise StopIteration
        current = self.count
        self.count -= 1
        return current


def generator(count):
    while count >= 0:
        yield count
        count -= 1

def fibnocci(n):

    if n in [0,1]:
        yield 0
    a,b = 0, 1
    while n>=0:
        yield a
        a , b = b , a+b
        n -= 1

if __name__=="__main__":
    for i in generator(1):
        print(i)