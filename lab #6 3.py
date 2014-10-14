total=1

print "What number do you want to take the factorial of?"
userInput=int(raw_input())

for number in range(1,(userInput+1),1):
    total=total * number  
print total  
    