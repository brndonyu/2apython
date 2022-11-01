import math
def swap_list(inputList):
    mid = len(inputList) // 2           #finds midpoint and highest number
    if (len(inputList) % 2) == 0:
        mid -= 1
    max = len(inputList) - 1            

    temp = inputList[mid]
    inputList[mid] = inputList[max]
    inputList[max] = temp
    
    return inputList