list = [1, 5, 98, 32, 61, 22, 7, 13, 20] #unordered, uneven list

n = len(list) 

print("\nOriginal List is: ")
for i in range(n):
    print(list[i])

def mergeLists(list, startindex, center, endindex):
    #define the last index of each separate placeholder list
    n1, n2 = (center - startindex + 1), (endindex - center)
    
    #instantiate placeholder lists for the temporary lists, use last indexes from above to create "empty" lists of approriate length
    L1 = [0] * n1
    L2 = [0] * n2
    
    #place the values in L1 and L2 lists
    for i in range(0, n1):
        L1[i] = list[startindex + i]
    
    for j in range(0, n2):
        L2[j] = list[center + 1 + j]

    i, j = 0, 0 #iterators for L1 and L2 index locations
    k = startindex #establish the starting index within the final list in order to iterate

    #Start sorting values via GTE comparison and place into final list. Keep running as long as we haven't reached out of index.
    while i < n1 and j < n2: 
        if L1[i] <= L2[j]: 
            list[k]=L1[i]
            i += 1
        else:
            list[k] = L2[j]
            j += 1
        k += 1 #iterator for final list index
    
    #handle remainders for uneven list lengths
    while i < n1:
        list[k] = L1[i]
        i += 1
        k += 1
    while j < n2:
        list[k] = L2[j]
        j += 1
        k += 1

#confirm valid indices, find middlepoint, repeat with center value as endindex to break the values out to atomic values, pass values to mergeLists function for value comparison and sorting
def mergeSorter(list, startindex, endindex):
    if startindex < endindex:
        center = startindex + (endindex-startindex) // 2 # separate the given list into two
        mergeSorter(list, startindex, center) # pass first list half
        mergeSorter(list, center + 1, endindex) # pass second list half
        mergeLists(list, startindex, center, endindex) # combine and value compare lists/values

mergeSorter(list, 0, n-1) #start the mergesort process using list, index 0 and last index determined by length of list - 1

print("\nAfter MergeSort, list is:")
for i in range(n):
    print(list[i])