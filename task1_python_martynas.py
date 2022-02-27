import sys
import os


if __name__ == '__main__':
    filename = sys.argv[1]
    filesize = os.path.getsize(filename)
    print(filesize)
    if filesize == 0:
        print("file is empty")
        exit()
    else:    
        with open(filename, 'r') as logfile:
            totalRows = 0
            ipAddresses = []
            statusCodes = []
            byteSizes = []
            for line in logfile:
                totalRows += 1
                element = line.split(" ")
                ipAddresses.append(element[0])
                statusCodes.append(element[8])
                byteSizes.append(element[9])
        

def checkOne():
    decision1 = input ("submit [1] for IP addresses, [2] for status codes:")
    
    if decision1.strip().isdigit() and (int(decision1)==1 or int(decision1)==2):
        return int(decision1)
    else:
        print("Please enter a correct value!!!")
        checkOne();
       
def checkTwo():
    decision2 = input ("submit [1] to receive count, [2] to receive count percentage, [3] to receive total number of bytes :")
    
    if decision2.strip().isdigit() and (int(decision2)==1 or int(decision2)==2 or int(decision2)==3):
        return int(decision2)
    else:
        print("Please enter a correct value!!!")
        checkTwo();

def checkThree():
    decision3 = input ("How many rows do you want to be printed? Press enter if you want all the rows to be printed!")
    
    if decision3.strip().isdigit():
        return int(decision3)
    elif decision3 == "":
        decision3 = totalRows
        return decision3
    else:
        print("Please enter a correct value!!!")
        checkThree();

decision1 = checkOne();
decision2 = checkTwo();
decision3 = checkThree();

def dictionary_sorter(value):
    return {k: v for k, v in sorted(value.items(), key=lambda item: item[1],reverse=True)}

def countResult(dictChoise, someList):
    for index in dictChoise:
        dictChoise[index] = someList.count(index)
    return dictChoise

def countPercentage(dictChoise, someList):
    for index in dictChoise:
        dictChoise[index] = someList.count(index)/totalRows*100
    return dictChoise

def countByteSizes(dictChoise, someList):
    for index in dictChoise:
            i = 0
            for index2 in someList:
                if index == index2:
                    if byteSizes[i] != "-":
                        dictChoise[index] += int(byteSizes[i])
                i += 1
    
#ip adresses
if decision1 == 1:
    
    choiseOneDict = dict.fromkeys(set(ipAddresses), 0)

    if decision2 == 1:	
        
        countResult(choiseOneDict, ipAddresses)         
        choiseOneDictSorted = dictionary_sorter(choiseOneDict)
        temp = 0
        
        for index in choiseOneDictSorted:
            if temp < decision3:
                print("IP address:", index, " Count:", choiseOneDictSorted[index])
            temp += 1  
                                                        
    elif decision2 == 2:
        
        countPercentage(choiseOneDict, ipAddresses)
        choiseOneDictSorted = dictionary_sorter(choiseOneDict)
        temp = 0
        
        for index in choiseOneDictSorted:
            if temp < decision3:
                print("IP address:", index, " Count percentages:", choiseOneDictSorted[index],"%")
            temp += 1
                   
    else:
        countByteSizes(choiseOneDict, ipAddresses)
        choiseOneDictSorted = dictionary_sorter(choiseOneDict)
        temp = 0
        
        for index in choiseOneDictSorted:
            if temp < decision3:
                print("IP address:", index, " Total transferred bytes:", choiseOneDictSorted[index])
            temp += 1        
else:
#statusCodes  
    choiseTwoDict = dict.fromkeys(set(statusCodes), 0)
    if decision2 == 1:
        
        countResult(choiseTwoDict, statusCodes)
        choiseTwoDictSorted = dictionary_sorter(choiseTwoDict)
        temp = 0
        
        for index in choiseTwoDictSorted:
            if temp < decision3:
                print("Status codes:", index," Count:", choiseTwoDictSorted[index])
            temp += 1
            
    elif decision2 == 2:
        countPercentage(choiseTwoDict, statusCodes)
        choiseTwoDictSorted = dictionary_sorter(choiseTwoDict)
        temp = 0
        
        for index in choiseTwoDictSorted:
            if temp < decision3:
                print("Status codes:", index, " Count percentages:", choiseTwoDictSorted[index], "%")
            temp += 1
            
    else:
        countByteSizes(choiseTwoDict, statusCodes)
        choiseTwoDictSorted = dictionary_sorter(choiseTwoDict)
        temp = 0
        
        for index in choiseTwoDictSorted:
            if temp < decision3:
                print("Status codes:", index, " Total transferred bytes:", choiseTwoDictSorted[index])
            temp += 1