#!/usr/bin/env python

import numpy as np

def padList(inputList):
    '''Pads a list so every sub list (assume 2d) 
    is of the same length
    '''
    maxLen = np.max([len(x) for x in inputList])
    for i,row in enumerate(inputList):
        while len(row) < maxLen:
            row.append('')
            inputList[i] = row
    return inputList

def readInput(fname):
    with open(fname,'r') as f:
        #lines = [y for x in f.readlines() for y in x.strip('#').strip('\n').split(' ') if y != '']
        lines = [x.strip('#').strip('\n').replace('\t',' ').strip(' ') for x in f.readlines()]
    toReturn = []
    for i,row in enumerate(lines):
        if row != '':
            toReturn.append([y for y in row.split(' ') if y != ''])
    return padList(toReturn)

def withinRange(it,schema='0-1'):
    '''
    @input it Integer or float of value to compare against
    @input schema is the range at which the `it` is compared to
    This returns a boolean if it is between (inclusive)
    '''
    try:
        start,end = schema.split('-')
        if float(start) <= it <= float(end):
            return True
        else:
            return False
    except:
        if it == float(schema):
            return True
        else:
            return False

def matchFormat(inVal,schema='str'):
    if (inVal.strip(' ') != '') or (inVal != None):
        if schema == 'str':
            return str(inVal)
        elif schema == 'tuple':
            return tuple(inVal)
        elif schema == 'list':
            return list(inVal)
        elif schema == 'float':
            return float(inVal)
        elif schema == 'int':
            return int(inVal)
    else:
        return None

def formatList(inputList,schema=(('0-2','str'),('3','str'),('4','str'),('5','str'))):
    '''Outputs a 2d list following the schema defined
    This schema follows a 2d tuple of linenumbers(inclusive),format
    '''
    toReturn = []
    temp = []
    tempRow = []
    schemaIter = 0
    rI = 0
    rV = ''
    for i,row in enumerate(inputList):
        while rI < len(row):
            rV = row[rI].strip(' ')
            #print(rI,rV)
            if withinRange(rI,schema[schemaIter][0]):
                temp.append(matchFormat(rV,schema[schemaIter][1]))
                if (rI == (len(row)-1)):
                    tempRow.append(' '.join(temp).strip(' '))
                rI += 1
            else:
                tempRow.append(' '.join(temp).strip(' '))
                temp = []
                schemaIter += 1
        toReturn.append(tempRow)
        schemaIter = 0
        rI = 0
        temp = []
        tempRow = []
    return toReturn

def compileCost(inputList,nameRow=3,costRow=5):
    toReturn = []
    temp = {}
    for i,row in enumerate(inputList):
        print(row)
        try:
            temp[row[nameRow]] += float(row[costRow])
        except KeyError:
            temp[row[nameRow]] = float(row[costRow])
    for x in temp:
        toReturn.append([x,'$'+str(round(temp[x],2))])
    return toReturn


if __name__ == '__main__':
    
    fname = input('Input the filename to read: ')
    inputsF = readInput(fname)
    ''' input
    # 14 April 2018 Kellen Chipotle 47.47
    # 21 April 2018 Jess   Chipotle 45.50
    '''
    print(compileCost(formatList(inputsF),1,3))

