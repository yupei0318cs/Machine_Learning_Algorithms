__author__ = 'Peipei Wei'

import sys
import math
from readfile import *
from traindata import *


def prediction(beta,train,test):
    w0, wi =base_log_odds(beta,train)
    columnTest, dataTest = read_file(test)
    logOddsTest = []
    for row in dataTest[1:]:
        i = 0
        w = w0
        while i <= (len(dataTest[0])-2):
            if row[i] == '1':
                w += wi[i]
            i += 1
        logOddsTest.append(w)
    return logOddsTest




def oddsToProb(odds):
    Prob = []
    for odd in odds:
        Prob.append(math.pow(math.e,odd)/(1+math.pow(math.e,odd)))
    return Prob


def ProbOutput(logodds,test):
    prob = oddsToProb(logodds)
    acc = accuracy(prob,test)
    with open('output.csv', 'wb') as csvfile:
        i = 0
        outputwriter = csv.writer(csvfile, delimiter=' ')
        while i <= len(prob)-1:
            outputwriter.writerow([prob[i]])
            i += 1
        outputwriter.writerow(['Acuracy:', acc])


def accuracy(probs,test):
    columnTest, dataTest = read_file(test)
    correctCount = 0.0
    i = 0
    while i <= len(probs)-1:
        if dataTest[i+1][-1]== '1' and probs[i]>= 0.5:
            correctCount += 1
        if dataTest[i+1][-1]=='0' and probs[i]<= 0.5:
            correctCount += 1
        i += 1
    labelAccuracy = correctCount/len(probs)
    return labelAccuracy




def main():
    train = sys.argv[1]
    test = sys.argv[2]
    beta = float(sys.argv[3])
    model = sys.argv[4]
    logOdds = prediction(beta,train,test)
    output(beta, train, model)
    ProbOutput(logOdds,test)

main()





