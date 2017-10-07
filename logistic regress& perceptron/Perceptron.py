__author__ = 'Peipei Wei'
from read_file import *
import sys
import ast

#trainData =  read_file("spamlineartrain.csv")
#testData =  read_file("spamlineartrain.csv")
def perceptronTrain(data, learn_rate, iterate_n ):
    trainData = data

    weights = []
    i = 0
    while i < len(trainData[0][:-1]) :## initialize wights for every attribut to be 0
        weights.append(0.0)
        i += 1

    classLabel = []
    for row in trainData[1:]:
        classLabel.append(row[-1])

    bias = 0.0 #initialize bias to 0
    k = 0
    #globalError = 0.0
    while k < iterate_n:
        errorCounter = 0
        for label, row in zip(classLabel, trainData[1:]):
            activation = dot_product(weights, row)+ bias
            if label == "0" and activation > 0.0:
                localError = float(0.0 - 1.0)
                errorCounter += 1
                j = 0
                while j < len(weights):
                    weights[j] += learn_rate * float(row[j]) * localError
                    j += 1
                bias += learn_rate * localError
            elif label == "1" and activation <= 0.0:
                localError = float(1.0 - 0.0)
                errorCounter += 1
                j = 0
                while j < len(weights):
                    weights[j] += learn_rate * float(row[j]) * localError
                    j += 1
                bias += learn_rate * localError
            #globalError += localError
        print k, "error", errorCounter
        if errorCounter == 0.0:
            break
        k += 1

    return weights, bias


def dot_product(weight, r):
    sum = 0
    for i, j in zip(weight, r):
        sum += i * float(j)
    return sum


def perceptronPredict (testData, w, b):
    bias = b
    weights = w
    label = []
    correctCount = 0.0
    for row in testData[1:]:
        activation = dot_product(weights, row) + bias
        if activation > 0:
            label.append("1")
            if row[-1] == "1":
                correctCount += 1.0
        else:
            label.append("0")
            if row[-1] == "0":
                correctCount += 1.0
    accuracy = float(correctCount/(len(testData) - 1))
    return label, accuracy


def output(test, weights, bias, model):
    label, acc = perceptronPredict(test, weights, bias)
    print "The Accuracy is:", acc
    with open(model, 'wb') as csvfile:
        outputwriter = csv.writer(csvfile, delimiter=' ')
        outputwriter.writerow(["{0:.6f}".format(bias)])
        i = 0
        while i < len(test[0][:-1]):
            outputwriter.writerow([test[0][i], "{0:.6f}".format(weights[i])])
            i += 1
        outputwriter.writerow(['Acuracy:', "{0:.6f}".format(acc)])


def main():
    train = read_file(sys.argv[1])
    test = read_file(sys.argv[2])
    eta = float(sys.argv[3])
    #print "start training!"
    model = sys.argv[4]
    weights, bias = perceptronTrain(train, eta, iterate_n = 100)
    #print "training finished!"
    output(test, weights, bias, model)

main()