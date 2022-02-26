'''
Title: Pickingling and Exception Handling
Dev: Chris Everett
Date: Feb 24th, 2022
Change Log: (Who, what, when):
CEverett: Created Initial File
'''


#Below codes test out the exception handling functionality of python

try:
    #test opening file to see if it's found
    objFile = open("nameAge.dat","rb")
except IOError:
    print("File not found.")
else:
    print("The file opened successfully.")
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



