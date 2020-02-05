#Written by Harshal Khandait
#Enrollment Number BT17CSE074
def checkMultiplicativeInverseExists(key) :
    for i in range(26):
        if ((i * key) % 26 == 1) :
            return i # Returns value of the multiplicative inverser of the given key
    return -1;# Returns -1 if there are no matches found
#We are supposed to write a code to reverse the function in hit and trial method
# Function Returns a null string if inverse of the key does not exists
# If it exists it returns the value of the result
def reversingAffineCipherTechnique(inputData,key1,key2):
    result=''
    if checkMultiplicativeInverseExists(key1)==-1:
        return result
    for i in range(len(inputData)):
        char = inputData[i]
        if char.isupper():
            result += chr(int((ord(char)-(key2-65)) * checkMultiplicativeInverseExists(key1)) % 26 + 65)
        else:
            result += chr(int((ord(char)-(key2-97)) * checkMultiplicativeInverseExists(key1)) % 26 + 97)
    return result
def solveForKeys(alphabet1,alphabet2,cipher1,cipher2):
    return key1,key2
#check the above function
print('The program takes 4 alphabets as its input in format')
print('Alphabet -> Cipher')
alphabet1 = input()
cipher1 = input('->')
alphabet2 = input()
cipher2 = input('->')
print(str(ord(alphabet1)-65)+' * key1 + key2 = ' + str(ord(cipher1)-65)+'(mod 26)')
print(str(ord(alphabet2)-65)+' * key1 + key2 = ' + str(ord(cipher2)-65)+'(mod 26)')
#Getting values of two keys that were used for encrypting by solving two equations
#key1,key2 = solveForKeys(alphabet1,alphabet2,cipher1,cipher2)
#Take string as input
inputData = input('Enter Character :')
#XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS
print('Using Hit and Trial Method We have these combinations')
for key1 in range(0,27,1):
    for key2 in range(0,27,1):
        if checkMultiplicativeInverseExists(key1)!=-1:
            print (inputData +' is decoded into '+ reversingAffineCipherTechnique(inputData,key1,key2) + ' for key value = ' + str(key1) + ' and ' +str(key2))
