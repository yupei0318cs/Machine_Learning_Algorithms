__author__ = 'Peipei Wei'

from IG import *
import sys

class Node:
    def __init__(self, attribute):
        self.attr = attribute
        self.leftChild = None
        self.rightChild = None
class Leaf:
    def __init__(self, val):
        self.value = val

class DecisionTree():


    def printTree(self, model, dataTrain):
        self.tree_model = open(model, "w+")
        current_node = self.growTree(dataTrain)
        self.printTree_helper(current_node, 0, flag = True)

    def printTree_helper(self, node, depth, flag = False):
        current_node = node
        #print "this is attribute"
        #print current_node

        if (isinstance(current_node, Leaf)) :
            self.tree_model.write(current_node.value)
            #print "no leaf"
            return
        elif (current_node == None):
            return
        elif (current_node.attr == ""):
            #print "current node"+current_node
            #self.tree_model.write(current_node.leftChild.value)
            if (current_node.leftChild !=None):
                self.tree_model.write(current_node.leftChild.value)
            if (current_node.rightChild != None):
                self.tree_model.write(current_node.rightChild.value)
            return
        else:
            #if isinstance(current_node.leftChild):
                #print isinstance(current_node.leftChild)
            self.tree_depth_printer(depth, flag)
            flag = False
            #print current_node
            self.tree_model.write(current_node.attr + "=" + "0" + ":")
            self.printTree_helper(current_node.leftChild, depth+1, flag)

            self.tree_depth_printer(depth, flag)
            flag = False
            self.tree_model.write(current_node.attr + "=" + "1" + ":")
            self.printTree_helper(current_node.rightChild, depth+1, flag)
            return

    def tree_depth_printer(self, depth, flag):
        if not flag:
            self.tree_model.write("\n")
        if depth > 0:
            for i in range(0, depth):
                self.tree_model.write(" | ")

    def growTree(self, dataTrain):
        #dataTrain, dataColumn = read_file("training-set")
        #base case
        attrInfoGain, chiSquare = infoGain(dataTrain)
        bestAttr = bestAttribute(attrInfoGain)

        flag, classLabel = self.checker(dataTrain)
        if flag:
            #print "creating leaves"
            current_node = Node(bestAttr)

            if classLabel == "0":
                current_node.leftChild = Leaf("0")
            elif classLabel == "1":
                current_node.rightChild = Leaf("1")
            return current_node

        else:
            current_node = Node(bestAttr)
            chi = chiSquare[bestAttr]
            ind = index(bestAttr, dataTrain)
            if chi < 6.635:
                return
            else:

                i = 1
                dataTrain0 = []
                dataTrain0.append(dataTrain[0])
                dataTrain1 = []
                dataTrain1.append(dataTrain[0])
                while i < len(dataTrain)-1 :

                    if dataTrain[i][ind] == '0':
                        dataTrain0.append(dataTrain[i])

                #split the database into two subdatabase
                    if dataTrain[i][ind] == '1':
                        dataTrain1.append(dataTrain[i])
                    i += 1
                #print dataTrain0
                #print dataTrain1
                #tree_model = open(model, "w+")
                current_node.leftChild = self.growTree(dataTrain0)
                current_node.rightChild = self.growTree(dataTrain1)

        return current_node


    #check whether the list is fully classified
    def checker(self, data):
        if len(data)== 1:
            return 0, ''
        else:
            label = data[1][-1]
            i = 2
            while i < len(data)-1:
                if data[i][-1]!= label:
                    return 0, ''
                i += 1
            return 1, label



def main():
    train = read_file(sys.argv[1])
    test = read_file(sys.argv[2])
    model = sys.argv[3]
    dtree = DecisionTree()
    dtree.printTree(model,train)


main()



