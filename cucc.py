#!C:\Users\titi9\AppData\Local\Programs\Python\Python39\python.exe

#
import cgi, cgitb

# Create instance of FieldStorage 
form = cgi.FieldStorage()

#
print("Content-Type: text/html\r\n")


#define variable that will store passwords
text=""
temp=[]
passwords={}

#open file
f = open("database.txt","r", encoding="utf-8")

#skip the first two lines
f.readline()
f.readline()

#read all the rest and add to the text variable
for line in f:
    
    temp=line.split()
    text+=line
    passwords.update({temp[0]:temp[1]})
    
f.close()




#teszt

username = form.getvalue("username")
password = form.getvalue("password")


if (password != passwords.get(username)):
    print("Wrong password<br>")
else:
    print("Good password<br>")


print('<a href="index.py">Go back</a>')







#show passwords
print("<br><br><br><br><br><br><br>")
print(passwords)


