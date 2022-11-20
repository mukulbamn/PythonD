c=1
while(c<6 and c>0):
    print("*"*50)
    print("\t\t List functions")
    print("*"*50)
    print("\t     1.If all Numbers")
    print("\t     2.Count Odd if Numeric")
    print("\t     3.Largest String")
    print("\t     4.Reverse List")
    print("\t     5.Find a specified element")
    print("\t     6.Exit")
    print("*"*50)
    c=int(input(" Enter your choice: "))
    print("*"*50)
    
    if c==1:
        arr=list(input("Enter the list:").split())
        print("The list contains all numbers: ",ifNumber(arr))
    elif c==2:
        arr=list(input("Enter the list:").split())
        print("Number of Odd numbers in Numeric List:",countOdd(arr))
    elif c==3:
        arr=list(input("Enter the list:").split())
        print("Largest String in the string List:",largestString(arr))
    elif c==4:
        arr=list(input("Enter the list:").split())
        print("Reverse form of list:",reverseList(arr))
    elif c==5:
        arr=list(input("Enter the list:").split())
        key=int(input("Enter element to search:"))
        print("Key found at:",findEle(key,arr))
    else:
        exit