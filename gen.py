# coding: utf-8

import csv
import random

import datetime


class GenRandomData(object):
    def genROW(self, count):
        retVal = []
        v0 = self.randomAccount(count)
        v1 = self.randomBinary()
        v2 = self.randomYear()
        v3 = self.randomDayb4180()
        retVal.extend([v0, v1, v2, v3])
        if v1 == 0:
            v5 = random.randrange(1, 17, 1)
            v4 = self.randomBool()
            if v4 is False:
                v8 = random.randrange(16, 181, 1)
                v7 = random.randrange(15, v8, 1)
                v6 = v7
            else:  # v4 is True
                v8 = 0
                v7 = 0
                v6 = random.randrange(15, 181, 1)
            v4 = str(v4).lower()
            retVal.extend([v4, v5, v6, v7, v8])
        return retVal

    def generateCSV(self, filename, count):
        csvfile = file(filename, 'wb')
        writer = csv.writer(csvfile)
        # writer.writerow(['val1', 'val2', 'val3', 'val4', 'val5', 'val6', 'val7', 'val8'])

        for i in range(1, count, 1):
            writer.writerow(self.genROW(count))

        csvfile.close()

    def randomBool(self):
        if 0 == random.randrange(0, 2, 1):
            return False
        else:
            return True

    def randomBinary(self):
        return random.randrange(0, 2, 1)

    def randomYear(self):
        return random.randrange(1957, 2006, 1)

    def randomDay(self):
        return random.randrange(-180, 1, 1)

    def randomDayb4180(self):
        return (datetime.date.today() + datetime.timedelta(self.randomDay())).isoformat()

    def randomAccount(self, count):
        return random.randrange(1, count + 1, 1)


if __name__ == "__main__":
    g = GenRandomData()
    g.generateCSV("test.csv", 100)
    """
    print g.randomBool()
    print g.randomBinary()
    print g.randomYear()
    print datetime.date.today()
    print  datetime.date.today() + datetime.timedelta(g.randomDay())
    print g.genROW()
    print '>>>', 0 == random.randrange(0, 2, 1)
    b = True
    b = str(b).lower()
    print b
    """
