import csv
import time


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
def get_data(av=None):
    with open('cars.csv', 'r') as data:
        rdr = csv.DictReader(data, delimiter=';')
        if av is not None:
            cars = [r for r in rdr if r['available'] == 'yes']
        else:
            cars = [r for r in rdr]
    return sorted(cars, key=lambda d: float(d['price']))[:3]


def main():
    while True:
        print()
        ic = input('Do you want to find the cheapest car? (y - yes, other key - exit the program)')
        if str(ic).lower() == 'y':
            ic = input('Search for currently available cars only? (y/n)')
            cars = []
            if str(ic).lower() == 'y':
                cars = get_data(av=True)
            elif str(ic).lower() == 'n':
                cars = get_data()
            for c in cars:
                print(c)
        else:
            break


if __name__ == '__main__':
    main()
