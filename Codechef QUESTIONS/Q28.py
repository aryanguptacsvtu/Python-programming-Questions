T = int(input())

for i in range(T):
    X,Y = map(int,input().split())
    
    if(X>Y):
        print("CAR")
        
    elif(X<Y):
        print("BIKE")
        
    else:
        print("SAME")


'''  "Car or Bike":-

Chef wants to reach home as soon as possible. He has two options:
Travel with his BIKE which takes X minutes.
Travel with his CAR which takes Y minutes.
Which of the two options is faster or do they both take same time?

"Output Format":-
For each test case, print CAR if travelling with Car is faster, BIKE if travelling with Bike is faster, SAME if they both take the same time.You may print each character of CAR, BIKE and SAME in uppercase or lowercase (for example, CAR, Car, cAr will be considered identical).'''