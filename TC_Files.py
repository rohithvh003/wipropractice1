# Read operation from file

file = open("f1.txt","r")
content = file.read()
content1 = file.readline()
content2 = file.readlines()
print(content)
print(content1)
print(content2)


file = open("f1.txt","a")
file.write("New line added\n")



file=open("f1.txt","w")
file.write("hello python\n")
file.write("this is my write example")
file.close()