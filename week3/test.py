# Create an empty list ( l = [] )
# Create an infinite loop
# Inside of the infinite loop, 
# ask the user what item from the store they’d like
# CHALLENGE
# check if the input is orange OR apple
# print "i dont have that"
# return



# Add that item to the list
# print the list


l = []
while True:
    amongus = input("What item do you want from the store ")

    if (amongus == "apple") or (amongus == "orange"):
        print('I dont have that :<')
        break
    l.append(amongus)
    print(l)
