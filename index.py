#!C:\Users\titi9\AppData\Local\Programs\Python\Python39\python.exe
# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
form = cgi.FieldStorage()



print("Content-Type: text/html\r\n")
print ("""\


<head></head>





<body>

<form action="/cucc.py" method = "post">
  <label for="fname">Username:</label>
  <input type="text" id="username" name="username"><br><br>
  <label for="lname">Password:</label>
  <input type="text" id="password" name="password"><br><br>
  <input type="submit" value="login">
</form>



</body>





""")
