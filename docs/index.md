 # Pickling and Exception Handling
 **Dev:** *CEverett*  
 **Date:** *2/25/2022* 
 **Foundations of Programming: Python**  
 **Assignment 07**
 
 ## Introudction
 In this document I will go over the steps I took to learn both Pickling and File Exceptions from outside sources. I will discuss what I did to test these features in my code, and also why I choose each source. 
 
 ## Exception Handling
 I started with file exceptions as I thought it would be best to show errors first in the code before trying to do pickling. Based on the examples I saw in the lecture videos, I wanted to try something different with the exception handling errors and tried both a try except without an exception variable and one with. But first I started to research python exception handling on the internet. 
I found this source from a website called The Python Guru (ThePythonGuru, https://thepythonguru.com/python-exception-handling/ , 2022) that showed many different examples of exception handling. Reading through this blog I found it to be similar to the exception handling examples in the course though with a different take. Therefore I thought this to be a good site to try a couple of exception handling errors. 
Seeing the first example in Figure 1, I thought I could incorporate the file exception error into my code right away to show an example of not finding the right text file. 

![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%201.png "tooltip text")
 #### Figure 1: ThePythonGuru File Exception Example
 Taking this example as a starting point, I created my own first test of making a text file that wasn’t listed in my project folder. Figure 2 shows my file execption error trying to open a file not there. 
![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%202.png "tooltip text")
 #### Figure 2: File Not Found Exception
Going from here, I wanted to try another type of exception handling, something different than the divisional error that was shown often. Reading further down I came across this example going over value errors of putting in the string text of ‘one’ instead of the value ‘1’ into the code. I could see how this might be a mistake some users make if they input an alphanumeric name instead of the number value. Figure 3 shows the example from ThePythonGuru webpage.  
![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%203.png "tooltip text")
#### Figure 3: Name Error Exception
I noticed the writer used the function eval() to test the value to make sure the number was a value instead of the written word. I enjoyed how different this was and wanted to test out this exception on my own. Figure 4 shows the code I wrote in order to test this with putting in constants to test out the exceptions. 
```
#Showing how name value error works
strName = 'Sue'
intAge = 'Forty'

try:
    #testing age values
    eval(intAge)
    print(strName, "is ", intAge)
except Exception as e:
    print("Error Occurred. Expected integer value.")
    print(e)
    print(type(e))
    print(e.__doc__)

#Testing again with string integer value
intAge = '40'
try:
    # testing age values
    eval(intAge)
    print(strName, "is ", intAge)
except Exception as e:
    print("Error Occurred. Expected integer value.")
    print(e)
    print(type(e))
    print(e.__doc__)
```
#### Figure 4: Name Exception

 Above shows that I pass both strName and intAge to the print function, but the eval function first tests the variable intAge. In this case the eval() function is being used to test for integer values and not just a string statement to cause the error. Therefore on line 21 I put intAge = ‘Forty’ to make it cause the exception and pass the code into the various exceptions messages that could occur. Lower down though I have the same code but I test again by changing intAge to ‘40’ on line 34. This allows the print function to work as intended in this simple example. Figure 5 shows the full exceptions list working in PyCharm.
![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%205.png "tooltip text")
#### Figure 5: Excetpion Handling Output
 ## Pickling
 Moving onto pickling, I searched the internet webpages for a example of how to read, write, and save a binary file. Finding this GeekforGeeks webpage, (GeekforGeeks, https://www.geeksforgeeks.org/understanding-python-pickling-example/, 2022) I read through the example and thought this would be a good example to try. Based on how they write about the example, the code given, and that my test code worked, I figured this was a good source to test pickling functionality. Figure 6 shows the example on the webpage. 
![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%206.png "tooltip text")
 ### Figure 6: Pickling Example
 Through this example, seeing how they used dictionary variables and how we have used them in the class before, I decided to test out similar code for this assignment. Figure 7 represents my code for working as an example of pickling. 
 ```
 try:
    #testing again but get the else clause to run the pickling code
    objFile = open("AgeList.dat","ab")
except IOError:
    print("File not found.")
else:
    print("The file opened successfully.")

import pickle

#Initializing Data
dicSue = {"Name" : 'Sue' ,"Age": '40'}
dicJoe = {"Name": 'Joe', "Age": '50'}
dicMary = {"Name": "Mary" , "Age" :'25' }

#data base
db = {}
db['Sue'] = dicSue
db['Joe'] = dicJoe
db['Mary'] = dicMary

#load dating into file
pickle.dump(db,objFile)
objFile.close()

#testing reading file from binary
readFile = open('AgeList.dat',"rb")
db2 = pickle.load(readFile)
for keys in db2:
    print (keys, "is", db2[keys])
readFile.close()

print("File Complete.")
 ```
 #### Figure 7: Pickling Code
 I started with the same code as the File Exception example earlier on to show that the try except clause does work when I create a correct text file as shown on lines 47. I open the file in binary append mode to get it ready to load data into it. I first list out dictionary constants that I plan on passing into  the file before putting it into a table variable. Once db is ready I go ahead and use the pickle.dump() function to load my data into the objFile and then close the file. I did this to test reading the file once more after closing it to make sure that it read correctly. Therefore I have a new variable that opens the file AgeList.dat and a new variable to put the dictionary rows into called db2. Then I use a for loop on line 73 to read off the file contents before closing the file again. From all of this I was able to run the file in command prompt showing both examples of exception handling and pickling. Figure 8 shows these results. 
![alt text](https://github.com/ceverettx20/IntroToProg-Python-Mod07/blob/IntroToProg-Python/Figures/Figure%208.png "tooltip text")
#### Figure 8: Command Prompt
 
 ## Summary
 With these examples I was able to learn how both exception handling worked and how pickling worked. Exception handling is definitely something that I liked and have seen used in SQL within my job, and will definitely use it in the future. Pickling is interesting and I like the idea of how it can be used to obscure data. Finally I also experienced how to research different articles to find answers to given problems, which is something I have experienced a lot of in my job writing SQL code and Tableau dashboards. 
