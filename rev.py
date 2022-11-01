def reverse_list(inputList):                    #decrement from highest index to lowest and append to a new list
    myList = []
    for i in range(len(inputList)-1,-1,-1):     #for(int i = n; i > -1; i--)
        myList.append(inputList[i])
    return myList                               #return new list
