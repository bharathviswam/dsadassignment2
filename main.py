count =0 
def subset_sum(numbers, target, partial=[]):
    try:
        global count
        s = sum(partial)

        # check if the partial sum is equals to target
        if s == target: 
            print("sum(%s)=%s" % (partial, target))
            count += 1
            print(count)
        if s >= target:
            return  # if we reach the number we can stop

        for i in range(len(numbers)):
            n = numbers[i]
            subset_sum(numbers, target, partial + [n])
    except:
        print("Something went wrong while finding combinations")
        exit()

def printOutput():
    try:
        global count
        writeOutput = open("outputPS11.txt", "w")   #w will create file if it does not exist
        possCombination = "Possible Combinations: "+ str(count)
        writeOutput.write(possCombination)
        writeOutput.close()
    except:
        print("Something went wrong while writing output")
        exit()


def readInputData():
    try:
        try:
            f = open('inputPS11.txt','r')
        except:
            print("File inputPS11.txt doesnot exist")
        dictOfInput = {}
        for line in f:
            line = line.strip()
            rowSplit = line.split(':')
            rowSplitValue = rowSplit[1].strip().split(' ')
            if len(list(rowSplitValue))>1:
                rowSplitValue = [int(i) for i in list(rowSplitValue)] 
            else:
                rowSplitValue = int(rowSplitValue[0])
            dictOfInput[rowSplit[0].strip()] = rowSplitValue
        subset_sum(dictOfInput['Denominations'],dictOfInput['Purchase'])
        printOutput()
    except:
        print("Something went wrong while reading inputs")
        exit()


readInputData()
