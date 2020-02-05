#Written by Harshal Khandait
#Enrollment Number BT17CSE074
#This python program performs statistical attack on given input string
def getMaximumOccuringCharacter(inputData):
    # Create array to keep the count of individual characters
    # Initialize the count array to zero
    count = [0] * 256 #ASCII SIZE
    # Utility variables
    maximum = -1
    # Traversing through the string and maintaining the count of each character
    for i in inputData:
        count[ord(i)]+=1;
    for i in inputData:
        if maximum < count[ord(i)]:
            maximum = count[ord(i)]
            c = i
    return c,maximum
# Although this program can be written in atmost 3 lines in Python
# the above program has been written for a better understanding of
# the reader

# Shorter version of the program
# import collections
# str = "sample string"
# print "Max occurring character is " +
#        collections.Counter(str).most_common(1)[0][0]
# This code has been contributed by Bhavya Jain on Geeks For Geeks

def reversingAdditiveCipherTechnique(inputData,key):
    result=''
    for i in range(len(inputData)):
        char = inputData[i]
        if char.isupper():
            result += chr((ord(char) - (key+65)) % 26 + 65)
        else:
            result += chr((ord(char) - (key+97)) % 26 + 97)
    return result
inputData = input('Enter Character :')
maximumAppearingCharacter , frequency = getMaximumOccuringCharacter(inputData)
print(maximumAppearingCharacter)
print(frequency)
#for i in range(0,26,1):
#    key = (int(ord(maximumAppearingCharacter) - (i+97)))%26
#    print('For value of '+ str(key) + ' is decoded in ' + reversingAdditiveCipherTechnique(inputData, key))
key = (int(ord(maximumAppearingCharacter) - ord('t')))%26
print('For value of '+ str(key) + ' is decoded in ' + reversingAdditiveCipherTechnique(inputData, key))
