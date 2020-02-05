#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Assuming condition of Addtive Cipher
#We are supposed to write a code to reverse the function in hit and trial method
def reversingAdditiveCipherTechnique(inputData,key):
    result=''
    for i in range(len(inputData)):
        char = inputData[i]
        if char.isupper():
            result += chr((ord(char) - (key+65)) % 26 + 65)
        else:
            result += chr((ord(char) - (key+97)) % 26 + 97)
    return result
#check the above function
#Take string as input
inputData = input('Enter Character :')
#key = int(input('Enter value of key :'))
for i in range(0,26,1):
    print (inputData +' is decoded into '+ reversingAdditiveCipherTechnique(inputData,i) + ' for key value = ' + str(i))
