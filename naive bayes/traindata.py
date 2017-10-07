__author__ = 'Peipei Wei'

import math
from readfile import *



def base_log_odds(beta,train):
    columnsTrain, dataTrain = read_file(train)
    count0 = 0.0
    count1 = 0.0

    for values in columnsTrain['spam']:
        if values == '0':
            count0 += 1
        else:
            count1 += 1

    classProb1 = count_to_prob(count1, count0, beta)
    classProb0 = count_to_prob(count0, count1, beta)
    classLogProb = math.log(float(classProb1/classProb0))


    global attrLogProb
    attrLogProb = []
    attrLogProbT = 0.0
    global attrWeightLogProb
    attrWeightLogProb = []

    for attribute in dataTrain[0][:-1]:
        attrCount00 = 0.0
        attrCount01 = 0.0
        attrCount10 = 0.0
        attrCount11 = 0.0
        attrWeightCount11 = 0.0
        attrWeightCount01 = 0.0
        attrWeightCount10 = 0.0
        attrWeightCount00 = 0.0
        i = 0

        while i <= (len(columnsTrain['spam'])-1):
            if columnsTrain[attribute][i] == '0' and columnsTrain['spam'][i] == '1':
                attrCount01 += 1
            if columnsTrain[attribute][i] == '1' and columnsTrain['spam'][i] == '1':
                attrCount11 += 1
            if columnsTrain[attribute][i] == '0' and columnsTrain['spam'][i] == '0':
                attrCount00 += 1
            if columnsTrain[attribute][i] == '1' and columnsTrain['spam'][i] == '0':
                attrCount10 += 1
            if columnsTrain[attribute][i] == '1' and columnsTrain['spam'][i] == '1':
                attrWeightCount11 += 1
            if columnsTrain[attribute][i] == '0' and columnsTrain['spam'][i] == '1':
                attrWeightCount01 += 1
            if columnsTrain[attribute][i] == '0' and columnsTrain['spam'][i] == '0':
                attrWeightCount00 += 1
            if columnsTrain[attribute][i] == '1' and columnsTrain['spam'][i] == '0':
                attrWeightCount10 += 1
            i += 1

        attrProb01 = count_to_prob(attrCount01,attrCount11,beta)
        attrProb00 = count_to_prob(attrCount00,attrCount10,beta)
        attrWeightProb11 = count_to_prob(attrWeightCount11,attrWeightCount01,beta)
        attrWeightProb10 = count_to_prob(attrWeightCount10,attrWeightCount00,beta)


        attrLogProb.append(math.log(float(attrProb01/attrProb00)))
        attrWeightLogProb.append(math.log(float(attrWeightProb11/attrWeightProb10)))

    for prob in attrLogProb:
        attrLogProbT += prob

    wi = attribute_weight(attrWeightLogProb,attrLogProb)

    w0 = classLogProb + attrLogProbT
    return w0, wi




def count_to_prob(count0, count1, beta):
    prob = float((count0 + beta-1) / (count1+count0+beta+beta-2))
    return prob

def attribute_weight(attrW,attrP):

    w = []
    i=0
    while i <=(len(attrW)-1):
        wi = attrW[i]-attrP[i]
        w.append(wi)
        i += 1
    return w

def output(beta, train, model):
    columnsTrain, dataTrain = read_file(train)
    W0, WI = base_log_odds(beta,train)
    with open(model, 'wb') as csvfile:
        i = 0
        modelwriter = csv.writer(csvfile, delimiter=' ')
        modelwriter.writerow(["%0.6f" % W0])
        while i <= len(WI)-1:
            modelwriter.writerow([dataTrain[0][i]] +["%0.6f" % WI[i]])
            i += 1



