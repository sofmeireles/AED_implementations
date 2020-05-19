"""code adapted from the java version on https://www.quora.com/How-can-I-sort-strings-using-Radix-Sort (by Ore Asonibare).
Consulted on 19/05/2020."""

def countingSort(array, index, lower, upper):
    lower=ord(lower)
    upper=ord(upper)
    countArray =[]
    auxArray = []
    
    for idx in range((upper-lower)+2):
        countArray.append(0)

    for i in range(0,len(array)):
        if (len(array[i])-1)<index:
            charIndex=0
        else:
            charIndex=(ord(array[i][index])-lower)+1
        countArray[charIndex]+=1
        auxArray.append('')

    for i in range(1,len(countArray)):
        countArray[i] += countArray[i-1]

    
    for i in range(len(array)-1,-1,-1):
        if len(array[i])-1 < index:
            charIndex=0
        else:
            charIndex=ord(array[i][index])-lower+1
        auxArray[countArray[charIndex]-1]=array[i]
        countArray[charIndex]-=1

    for i in range(len(auxArray)):
        array[i]=auxArray[i]
    
  

def radixSort(array, lower, upper): 
    maxIndice=0
    for i in range(len(array)):
        if(len(array[i])-1) > maxIndice:
            maxIndice = len(array[i])-1
    
    for j in range(maxIndice,-1,-1):
        countingSort(array,j,lower,upper)
    


if __name__ == "__main__":
    array=["apple", "australia", "algorithm","sell", "olympic","jack","sleep"]
    radixSort(array,'a','z')
    print(array)