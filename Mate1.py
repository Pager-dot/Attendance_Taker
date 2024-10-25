fopener = open("Demo.txt")
roll=input("Enter full roll no: ")
for line in fopener :
    if line.startswith(roll) == True:
        print(line)
        print("This student was present")
        print("Thank you")
        break
else:
    print('This student was absent or you enter wrong input')
