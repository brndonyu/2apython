def sort_dictionary(myDict):
    nameList = []                               #save keys and values into three separate arrays
    phoneList = []
    ageList = []
    for n in myDict:
        nameList.append(n)
        phoneList.append(myDict[n][0])
        ageList.append(myDict[n][1])

    for i in range(len(ageList)-1):             #bubble sort
        for j in range(len(ageList)-1):
            if ageList[j] > ageList[j+1]:       #sorts according to age and swaps corresponding indexes
                temp = ageList[j]
                ageList[j] = ageList[j+1]
                ageList[j+1] = temp

                temp = nameList[j]
                nameList[j] = nameList[j+1]
                nameList[j+1] = temp

                temp = phoneList[j]
                phoneList[j] = phoneList[j+1]
                phoneList[j+1] = temp

    tupList = []                                #save sorted corresponding indexes for name and number as tuples
    for i in range(len(ageList)):
        tup = (nameList[i],phoneList[i])
        tupList.append(tup)
    
    return tupList