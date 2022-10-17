import sys


listOfItems = []
print("This is the name of the program:", sys.argv[0])
if len(sys.argv) >0:
    print("No arguments")
    listOfItems.append("cenv0")

if len(sys.argv) > 1:
    print("This is the first argument:", sys.argv[1])
if len(sys.argv) > 2:
    print("This is the second argument:", sys.argv[2])
    numberOfItems = sys.argv[2]
    for x in range(0, int(numberOfItems)):
        # print("Hello world")
        listOfItems.append(sys.argv[1]+str(x))
# if len(sys.argv) > 3:
#     print("This is the third argument:", sys.argv[3])
#     numberOfItems = sys.argv[3]
#     for x in range(0, int(numberOfItems)):
#         # print("Hello world")
#         listOfItems.append(sys.argv[2]+sys.argv[3])

print(listOfItems)

# sys.argv[3] is the third argument, assign a variable to it
# and print it out

#create a list of items which have cenv%listnumber

#loop through the list and print out the items


# print("Tese are the commands", sys.argv[1], sys.argv[2])
# print("Argument List:", str(sys.argv))