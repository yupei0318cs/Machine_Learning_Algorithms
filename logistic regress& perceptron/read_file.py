__author__ = 'Peipei Wei'
import csv

def read_file(path):

    #columns = {}

    data = []
    i = 0
    with open(path,'rt') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            data.append(row)

        #for attribute in data[0]:
            #columns[attribute] = []
            #for row in data[1:]:
                #columns[attribute]+= [row[i]]
            #i+=1
            #print (len(data))
    csvfile.close()
    return  data #columns
