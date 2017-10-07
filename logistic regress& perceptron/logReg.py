__author__ = 'Peipei Wei'

from read_file import *
import math
import sys

#trainData =  read_file("test.csv")
def logRegression(trainData, learn_rate, sigma, iterate_n):
    lam = float(1.0/(sigma ** 2))
    weights = []
    p = 0
    while p < len(trainData[0][:-1]) :## initialize wights for every attribut to be 0
        weights.append(0.0)
        p += 1
     #initialize w0 to 0
    classLabel = []
    for row in trainData[1:]:
        classLabel.append(row[-1])

    k = 0
    w0 = 0.0

    while k <  iterate_n:
        ga_magnitude = 0.0
        weight_vector = 0.0
        gradient0 = 0.0
        q = 0
        gradient = []

        while q < len(trainData[0][:-1]):
            gradient.append(0.0)
            q += 1

        j = -1
        while j < len(gradient):
            for label, row in zip(classLabel, trainData[1:]):
                WX = dot_product (weights, row)
                #print oddsToProb( w0 + WX)
                if (j == -1):
                    gradient0 += (float(label) - oddsToProb( w0 + WX))
                    #print (float(label) - set_label(oddsToProb( w0 + WX)))
                else:
                    gradient[j] += (float(row [j])* ( float(label) - oddsToProb( w0 + WX)))
            j += 1
        i = -1
        while i < len(weights):
            if (i == -1):
                #print grad_ascent_0
                weight_vector += (w0**2)
                gradient0 -= lam * w0
                w0 += (learn_rate * gradient0)
                ga_magnitude += (gradient0 ** 2)
            else:
                weight_vector += (weights[i]**2)
                gradient[i]-= lam*weights[i]
                weights[i] += (learn_rate * gradient[i])
                #ga_magnitude += ( gradient[i]** 2)
                ga_magnitude += ( gradient[i]) ** 2
            i += 1
        #ga_magnitude = gradient0*gradient0
        #for g in gradient:
            #ga_magnitude += g**2
        #convergence = math.sqrt(convergence)

        #print weights
        #print gradient

        #ga_magnitude += grad_ascent_0 ** 2
        #weight_vector += w0**2
        ##w0 += learn_rate * (-1 * lam * w0 +  ( float(label) - set_label(math.exp( w0 + WX)/(1 + math.exp( w0 + WX)))))
        print k, math.sqrt(ga_magnitude), math.sqrt(weight_vector)
        if math.sqrt(ga_magnitude) < 0.00001:
            break
        k += 1

    return weights, w0

def oddsToProb(odds):
    return float(math.exp(odds)/(1+ math.exp(odds)))


def dot_product(weight, r):
    sum = 0.0
    for i, j in zip(weight, r):
        sum += i * float(j)
    return sum


def logRegPredict (testData, w0, w):
    weights = w
    label = []
    correctCount = 0.0
    for row in testData[1:]:
        WX = dot_product (weights, row)
        #odds = math.exp( w0 + WX)/(1 + math.exp( w0 + WX) )
        prob = oddsToProb(w0 + WX)
        if prob > 0.5:
            label.append("1")
            if row[-1] == "1":
                correctCount += 1.0
        else:
            label.append("0")
            if row[-1] == "0":
                correctCount += 1.0
    accuracy = float(correctCount/(len(testData) - 1))
    return label, accuracy

def output(test, weights, w0, model):
    label, acc = logRegPredict(test, w0, weights)
    print "The accuracy is", acc
    with open(model, 'wb') as csvfile:
        outputwriter = csv.writer(csvfile, delimiter=' ')
        outputwriter.writerow(["{0:.6f}".format(w0)])
        i = 0
        while i < len(test[0][:-1]):
            outputwriter.writerow([test[0][i], "{0:.6f}".format(weights[i])])
            i += 1
        outputwriter.writerow(['Acuracy:', "{0:.6f}".format(acc)])


def main():
    train = read_file(sys.argv[1])
    test = read_file(sys.argv[2])
    eta = float(sys.argv[3])
    sigma = float(sys.argv[4])
    #print "start training!"
    model = sys.argv[5]
    weights, w0 = logRegression(train, eta, sigma, iterate_n = 100)
    #print "training finished!"
    output(test, weights, w0, model)

main()





