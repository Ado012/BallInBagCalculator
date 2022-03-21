#Ball in Bag Calculator

# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count



#take three inputs

# balls in bag sequence
 
input_string = input("Welcome to Ball In Bag Calculator. For all your ball in bag drawing needs. Please Enter the balls in bag and their values ie 1 4 2: ")
ballSequenceString  = input_string.split()

ballSequence = [int(item) for item in ballSequenceString]

amountOfBalls = len(ballSequence)


print("Balls in the bag and their values:", ballSequence)


# sum goal
sumGoal = int(input("Enter the sum the 3 drawn balls must reach : "))


#group numbers into unique digits

# start a list for the distinct values in the bag
uniqueBallValues = []

# taking an counter
count = 0

# traversing ball sequence
for value in ballSequence:
	if value not in uniqueBallValues:
		count += 1
		uniqueBallValues.append(value)

# printing the number of unique ball values
print("No of unique items are:", count)

#counting the times the unique values appear
uniqueBallValuesCount = []

for ballValue in uniqueBallValues:
    ballValueCount = countX(ballSequence,ballValue)
    uniqueBallValuesCount.append(ballValueCount)




#find all possible draw combinations
ballDrawCombos = []

#find the number of unique ball values
uniqueBallValuesSize=len(uniqueBallValues)
ballDrawComboAmount=pow(uniqueBallValuesSize,3)
ballDrawComboAmountFixedFirstDigit=pow(uniqueBallValuesSize,2)

print(uniqueBallValues)
print(uniqueBallValuesCount)


#specify the digits for each combination one digit at a time

#first digit
#print unique digits square of ball draw combos times until you reach the end of the unique digits
for i in uniqueBallValues:
   #print(i)
   for j in range(ballDrawComboAmountFixedFirstDigit):
      #print(i)
      ballDrawCombos.append([i,0,0]) #might want to replace 0s with null values

#seconddigit
#append each unique digit by the amount of unique digits times. Go through all unique digits for each unique first digit
i = 0

while i < (ballDrawComboAmount):
   for digit in uniqueBallValues:
      print("range int uniqueballvaluesize",range(int(uniqueBallValuesSize)))
      for j in range(int(uniqueBallValuesSize)):
         print("second digit",digit)
         ballDrawCombos[i][1]=digit
         i = i + 1
         print("ballDrawCombo 2nd digit:", ballDrawCombos)

#thirddigit
i = 0
#loop through unique digits appending to the combo entries until you reach the end.
while i < (ballDrawComboAmount):
   for digit in uniqueBallValues:
         ballDrawCombos[i][2] = digit
         i = i + 1


print("ballDrawCombo Before:", ballDrawCombos)



#eliminate all duplicates
ballDrawCombosNoDups = list()
for sublist in ballDrawCombos:
    if sublist not in ballDrawCombosNoDups:
        ballDrawCombosNoDups.append(sublist)


ballDrawCombos = ballDrawCombosNoDups
#eliminate all perturbations with more digits of a group than in pool
badComboFlag = 0 

#print("i:", i)

print("ballDrawCombo:", ballDrawCombos)
#print("uniqueBallValues:", uniqueBallValues)
#print("uniqueBallValues 0:", uniqueBallValues[0])
#print("uniqueBallValues 1:", uniqueBallValues[1])
#print("uniqueBallValuesCount:", uniqueBallValuesCount)

ballDrawCombosNoExcess = []

for i in ballDrawCombos:
      comboStatusFlag = 0 
      comboStatusFlag2 = 0
      print("ballDrawCombo i",i)
      for j in i: #go through digits of draw combo
         comboStatusFlag = 0
         print("digit in ballDrawCombo j",j)
         count = countX(i, j) #count up the times a digit occurs
         
         for k in uniqueBallValues:    #go through unique values
            print("point1")    
            print("j",j)
            print("k",k)    
            if j == k: #if the digit in the combo and the unique value match  
               print("point1p5")
               comboStatusFlag = 1 #done sweeping through unique digits for digit in draw combo
               if count > uniqueBallValuesCount[uniqueBallValues.index(k)]: #if the times the digit occurs exceeds the times the unique value occurs in the ball sequence
                  print("point2")
                  #removalplaceholder = i #save place in queue
                  #ballDrawCombos.remove(i) #remove bad combo
                  #i = removalplaceholder
                  print ("i restored:",i)
                  print("ballDrawCombo:", ballDrawCombos)
                  comboStatusFlag2 = 1 #move on to next ball draw combo
                  break
               
            if comboStatusFlag == 1:
               break
         if comboStatusFlag2 == 1:
            break  
      if comboStatusFlag2 == 0:
         ballDrawCombosNoExcess.append(i)

ballDrawCombos = ballDrawCombosNoExcess

      

print("ballDrawCombo:", ballDrawCombos)

ballDrawCombosMeetGoal = []

#eliminate all perturbations which do not meet sumgoal
for i in ballDrawCombos:
   sumOfBallDrawCombo = sum(i)
   if sumOfBallDrawCombo >= sumGoal: 
      ballDrawCombosMeetGoal.append(i)

ballDrawCombos = ballDrawCombosMeetGoal

#calculate probability for each pertubation without replacement. 
uniqueBallValuesCountBag = uniqueBallValuesCount.copy() #regular assignment makes them literally the same

moreballsthaninbagflag = 0

perturbationProbabilityFractions = []
probabilityToMeetGoal=0

for i in ballDrawCombos:#for each remaining ball draw combo
   ballsDrawn = 0
   uniqueBallValuesCountBag = uniqueBallValuesCount.copy()
   perturbationProbabilityFractions = []
   #print("ballDrawCombos",i)
   #print("uniqueBallValuesCount",uniqueBallValuesCount)
   #print("uniqueBallValuesCountBag",uniqueBallValuesCountBag)
   for j in i: #go through each digit of the three draw 
     for k in uniqueBallValues: #look for digit in unique values
         #print("j",j) 
         #print("k",k)
         #print("k index",uniqueBallValues.index(k))
         #print("uniqueBallValuesCountBag",uniqueBallValuesCountBag)
         #print("uniqueBallValues",uniqueBallValues)
         if j == k: #if found
            amountofdigit = uniqueBallValuesCountBag[uniqueBallValues.index(k)] #retrieve the amount of the value in the ball sequence
            uniqueBallValuesCountBag[uniqueBallValues.index(k)] = uniqueBallValuesCountBag[uniqueBallValues.index(k)]-1 #subtract from amount based on the draw
            if uniqueBallValuesCountBag[uniqueBallValues.index(k)] < 0:
               moreballsthaninbagflag = 1
            break
     
     print("draw combo",i)
     print("numerator",amountofdigit)
     print("denominator",amountOfBalls-ballsDrawn)
     

     fractionalProbability = amountofdigit/(amountOfBalls-ballsDrawn) #construct fractional probability based on amount of value and total balls left
     perturbationProbabilityFractions.append(fractionalProbability) #append to probability group
     ballsDrawn = ballsDrawn + 1

   print("perProbFracs:",perturbationProbabilityFractions)
   perturbationProbability = perturbationProbabilityFractions[0] * perturbationProbabilityFractions[1] * perturbationProbabilityFractions[2] #calculate total probability for combo

   probabilityToMeetGoal=probabilityToMeetGoal+perturbationProbability #add to total probability

print("ballDrawCombos",ballDrawCombos) 
           

print("Probability to Meet Goal:",probabilityToMeetGoal)


if moreballsthaninbagflag == 1:
   print("falled to remove draws that had more balls than in bags")










