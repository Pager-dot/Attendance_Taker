
def sortAllwords(given_string):
    words_list = given_string.split()
    words_list.sort()

    print(" Sorted string words are: ")

    for word in words_list:
        print(word," ")
        
user_string = input("Enter input string : ")
sortAllwords(user_string)


