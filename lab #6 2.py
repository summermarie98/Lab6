totalList=[]
print "How many numbers do you want to run?"
userInput=int(raw_input())
for x in range(userInput):
        
    print "Please, enter your number:"
    userInput2=int(raw_input())
    totalList.append(x)
    
print "Your final answer is:" + str(sum(totalList))