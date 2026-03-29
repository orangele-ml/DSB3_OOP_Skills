import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, 'r') as f:
            lines = f.read().strip().split('\n')
        
        if has_header:
            lines = lines[1:]

        return[[int(x) for x in line.split(',')] for line in lines]

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails
        
        def fractions(self, heads, tails):
            total = heads + tails
            head_frac = int(heads / total * 10000) / 10000
            tail_frac = int(tails / total * 10000) / 10000
            return head_frac, tail_frac
        

class Analytics(Research.Calculations):

    def predict_random(self, num):
        predections = []
        for _ in range(num):
            rand = randint(0, 1)
            predections.append([rand, 1 - rand])
        return predections
        
    def predict_last(self):
        return self.data[-1]

if __name__ == '__main__': 
    if len(sys.argv) != 2:
        print("Ishlatish: python3 first_child.py <file_path")
        sys.exit(1)

    try:
        research = Research(sys.argv[1])
        data = research.file_reader()

        analytics = Analytics(data)

        print(data)

        heads, tails = analytics.counts()
        print(heads, tails)

        head_frac, tail_frac = analytics.fractions(heads, tails)
        print(head_frac, tail_frac)
        print(analytics.predict_random(3))
        print(analytics.predict_last())

    except Exception as e:
        print(f"Xato: {e}")
        sys.exit(1)            