__author__ = 'Peipei Wei'
from readfile import *
import math

def infoGain(trainData):

    i = 0
    attrInfoGain = {}
    chiSquare = {}
    while i < len(trainData[0])-1:
        count0 = 0.0
        count1 = 0.0
        attrCount00 = 0.0
        attrCount01 = 0.0
        attrCount10 = 0.0
        attrCount11 = 0.0
        j = 1
        while j < (len(trainData)):
            if trainData[j][-1] == '0':
                count0 += 1

            if trainData[j][-1] == '1':
                count1 += 1



            if trainData[j][i] == '0' and trainData[j][-1] == '0':
                attrCount00 += 1
            if trainData[j][i] == '0' and trainData[j][-1] == '1':
                attrCount01 += 1
                #attrCount01 = count0 - attrCount00
            if trainData[j][i] == '1' and trainData[j][-1] == '0':
                attrCount10 += 1
            if trainData[j][i] == '1' and trainData[j][-1] == '1':
                attrCount11 += 1
                #attrCount11 = count1 - attrCount01

            j += 1

        entroY = entropy(count0, count1)
        entro0 = entropy(attrCount00, attrCount01)
        entro1 = entropy(attrCount10, attrCount11)
        #x = log(0.375)
        #print count0, count1, attrCount00, attrCount01, attrCount10, attrCount11, entroY, attrProb0, entro0, entro1, x
        infoGain = entroY - (attrCount00+attrCount01)/(count0+count1)*entro0 - (attrCount10+attrCount11)/(count0+count1) * entro1

        attrInfoGain[trainData[0][i]]= infoGain
        chi = chi_square(count0, count1, attrCount00, attrCount01, attrCount10, attrCount11)
        chiSquare[trainData[0][i]]= chi
        i += 1


    return attrInfoGain, chiSquare


def entropy(count0, count1):
    if count1+count0 == 0:
        return 0.0
    else:
        prob0 = count0/(count0 + count1)
        prob1 = count1/(count0 + count1)
        if prob0 == 0 and prob1 == 0:
            return 0.0
        elif prob0 == 0.0:
            return  -prob1*log(float(prob1))
        elif prob1 == 0.0:
            return  -prob0*log(float(prob0))
        else:
            return -prob0*log(float(prob0))-prob1*log(float(prob1))


def log(x):
    return math.log(x)/math.log(2)

def chi_square(count0, count1, attrCount00, attrCount01, attrCount10, attrCount11):
    if count0 ==0 or count1 == 0:
        return 0.0
    elif (attrCount00+attrCount01==0) or (attrCount10+attrCount11==0):
        return 0.0
    else:
        expected00 = count0*(attrCount00+attrCount01)/(count0+count1)
        expected01 = count1*(attrCount00+attrCount01)/(count0+count1)
        expected10 = count0*(attrCount10+attrCount11)/(count0+count1)
        expected11 = count1*(attrCount10+attrCount11)/(count0+count1)
        return (attrCount00-expected00)**2/expected00 +(attrCount01-expected01)**2/expected01+(attrCount10-expected10)**2/expected10 +(attrCount11-expected11)**2/expected11

def bestAttribute(info):
    max = 0
    keymax = ""
    for key, value in info.iteritems():
        if max < value:
            max = value
            keymax = key
    return keymax

# can't remember what this method is for
def index(key, dict):
    i = 0
    while i < (len(dict[0])-1):
        if dict[0][i]== key:
            return i
        else:
            i += 1
    return i

def main():
    trainData = read_file("training_set.csv")
    attribute_IG, chi = infoGain(trainData)
    for key, value in attribute_IG.iteritems():
        print key, value
    #keyMax = bestAttribute(attribute_IG)
    #ind = index(keyMax, trainData)
    #print ind

#main()





