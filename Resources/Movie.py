#Find the number of movies released between 1950 and 1960.

def first():
    cnt=0
    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            if (word[2]>= '1950' and word[2]<='1960') :
                cnt=cnt+1
    
        print(cnt)

#2. Find the number of movies having rating more than 4.
def second():
    cnt=0
    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            if (word[3]>= '4') :
                cnt=cnt+1
    
        print(cnt)

#3. Find the movies whose rating are between 3 and 4.
def third():
    cnt=0
    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            if (word[3]>= '3' and word[2]<='4') :
                cnt=cnt+1
    print(cnt)


#4. Find the number of movies with duration more than 2 hours (7200 second).
def four():
    cnt=0
    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            if (word[4]>= '7200') :
                cnt=cnt+1 
        print(cnt)


#5. Find the list of years and number of movies released each year.
def five():
    index=0  
    arr=set()
    count=[]


    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            word = line.split(',')
            year=word[2]
            arr.add(year)
        
    for i in arr:
        cnt=0
        with open('movie.txt', 'r') as file:
            data2 = file.readlines()
        for line in data:
            word = line.split(',')
            year=word[2]
            if(i == year):
                cnt=cnt+1
        count.append(cnt)

    list1=list(arr)   

    for i in range(len(list1)):
        print("Year {} having  {} no of movies".format(list1[i] ,count[i]))
 
    """sum=0
    for i in count:
        sum=sum+i
        print(sum)"""

    
    
#6. Find total number of movies in dataset
def six():
    cnt=0
    with open('movie.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            cnt=cnt+1
        print(cnt)



while True:
    print("-------------------------------------------------------------------------------------------------------------------------------------")
    print("\n\n\n**Which operation you want?**")
    print("\n1.Find the number of movies released between 1950 and 1960")
    print("2.Find the number of movies having rating more than 4.")
    print("3.Find the movies whose rating are between 3 and 4")
    print("4. Find the number of movies with duration more than 2 hours (7200 second)")
    print("5.Find the list of years and number of movies released each year")
    print("6.Find total number of movies in dataset")
    print("7.Exit")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    ch=input("Enter choice:")
    if ch=='1':
        first()
    elif ch=='2':
        second()
    elif ch=='3':
        third()
    elif ch=='4':
        four()
    elif ch=='5':
        five()
    elif ch=='6':
        six()
    elif ch=='7':
        break
    else:
        print("Wrong Choice")

