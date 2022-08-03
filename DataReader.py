import csv
import time
from abc import ABC, abstractmethod


class Dr(ABC):
    def __init__(self, path):
        self.path = path
        self.main()

    @staticmethod
    def check_time(f):
        def meas(*args, **kwargs):
            start = time.time()
            c = f(*args, **kwargs)
            end = time.time()
            print()
            print("We've found a car for you in", round(end - start, 7), "s")
            return c

        return meas

    @check_time
    def get_data(self, av=None):
        try:
            with open(self.path, 'r') as data:
                rdr = csv.DictReader(data, delimiter=';')
                if av is not None:
                    cars = [r for r in rdr if r['available'] == 'yes']
                else:
                    cars = [r for r in rdr]
            return sorted(cars, key=lambda d: float(d['price']))[:3]
        except FileNotFoundError:
            print("Entered file doesn't exist!")
            import sys
            sys.exit(1)

    @abstractmethod
    def main(self):
        pass


class Main(Dr):
    def __init__(self, path='cars.csv'):
        super().__init__(path)
        self.cars = []

    def main(self):
        print()
        ic = input('Do you want to find the cheapest car? (y - yes, other key - exit the program)')
        if str(ic).lower() == 'y':
            ic = input('Search for currently available cars only? (y/n)')
            if str(ic).lower() == 'y':
                self.cars = self.get_data(av=True)
            elif str(ic).lower() == 'n':
                self.cars = self.get_data()
            for c in self.cars:
                print(c)
        else:
            import sys
            sys.exit()
        self.main()


