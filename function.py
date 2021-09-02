# f = open("test.txt")
# fileLine = f.readlines()
# for line in fileLine:
#     print(line)
# introString = "my name is shaan , i am 14 years old"
# words = introString.split(",")
# print(words)
# def greet(name):
#     print("hello, " + name)

# greet("shaan")

def countWordsFromFile():
    filename = input("enter the file name -")
    numberofwords = 0

    file = open(filename,"r")
    for line in file:
        words = line.split()
        numberofwords = numberofwords + len(words)
    print("numberofwords:")
    print(numberofwords)

countWordsFromFile()

