#Written by Harshal Khandait
#Enrollment Number BT17CSE074
#A python program to illustrate Additive Cipher Technique
def additiveCipherTechnique(inputData,key):
	result = ""
	# traverse inputData character wise
	for i in range(len(inputData)):
		char = inputData[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + key-65) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + key - 97) % 26 + 97)
	return result
#check the above function
#Take string as input
inputData = input('Enter Character :')
key = int(input('Enter value of key :'))
print (inputData +' is encode into '+ additiveCipherTechnique(inputData,key))
