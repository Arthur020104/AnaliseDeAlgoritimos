
array = []

def main():
    given_file = open("File.txt", "r")

    lines = str(given_file.readlines())
    lines = lines.split(",")
    
    for line in lines:
        try:
            addToArr(int(line))
        except ValueError:
            continue
   

    given_file.close()
    #while True: 
     #   try:
      #      vlr = int(input("Digite um numero: "))
            
      #  except ValueError:
         #   break  
       # addToArr(vlr)
    
    

def searchInArr(n):
    for i in range(len(array)):
        if array[i] > n:
            return False, i
        elif array[i] == n:
            return True, -1
    return False, len(array)

def addNOnI(n, index):
    newArray = []
    if array == []:
        newArray.append(n)
        return newArray
    for i in range(len(array)):
        if index == i:
            newArray.append(n)
        newArray.append(array[i])
    
    return newArray
    
def addToArr(n):
    boolean, index = searchInArr(n)
    if not boolean:
        new_array = addNOnI(n, index)
        array.clear()
        array.extend(new_array) 
    else:
        return

if __name__ == "__main__":
    main()
    print(array)
