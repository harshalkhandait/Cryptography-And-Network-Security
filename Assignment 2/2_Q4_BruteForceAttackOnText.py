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
def reversingMultiplicatveCipherTechnique(inputData,key):
    result=''
    if checkMultiplicativeInverseExists(key)==-1:
        return result
    for i in range(len(inputData)):
        char = inputData[i]
        if char.isupper():
            result += chr(int(ord(char) * checkMultiplicativeInverseExists(key)) % 26 + 65)
        else:
            result += chr(int(ord(char) * checkMultiplicativeInverseExists(key)) % 26 + 97)
    return result
#check the above function
#Take string as input
inputData = input('Enter Character :')
#key = int(input('Enter value of key :'))
for i in range(0,26,1):
    temp = checkMultiplicativeInverseExists(i)
    if temp==-1:
        print ('Inverse of key '+str(i)+' does not exists. Hence it cannot be decrypted')
    else:
        print (inputData +' is decoded into '+ reversingMultiplicatveCipherTechnique(inputData,i) + ' for key value = ' + str(i))
