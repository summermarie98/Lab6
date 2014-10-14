print "How many times do you want to add together?"

userInput=int(raw_input())
total=0
for x in range(userInput):
    print "Please, enter your number"
    numberListed=int(raw_input())
    total=total+userInput
   
print "Your number is:"
print total