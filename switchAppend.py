# coding: utf-8
import csv

class SW(object):
    def fx(self, inputFile, outputFile, index1, str1, index2, str2):
        outfile = file(outputFile, 'wb')
        writer = csv.writer(outfile)

        rawfile = open(inputFile, 'rb')
        csvreader = csv.reader(rawfile)

        for row in csvreader:
            if '1' in row[index1]:
                row.extend([str1])
            elif '2' in row[index2]:
                row.extend([str2])
            else:
                print "ERR: args in row 14 is not 1 or 2"
                return
            writer.writerow(row)


if __name__ == "__main__":
    g = SW()
    g.fx("testdata1000.csv", "result.csv", 13, "2C00010001", 13, "2F00020001")
