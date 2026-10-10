#important to call the range functions at time especially with the for loop
for number in range(3):
    print("Attempt", number +1, (number + 1) * ".")
#stating start and end point
for number in range(1,4):
    print("Attempt", number, (number) * ".")
#passing third parameter to the range function to specify the step
for number in range(1,10,2):
    print("Attempt", number, (number) * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempt failed")
