#Written by Harshal Khandait
#Enrollment Number BT17CSE074
#A python function to illustrate Affine Cipher Technique
def affineCipherTechnique(inputData,key1,key2):
	result = ""
	# traverse inputData character wise
	for i in range(len(inputData)):
		char = inputData[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr(((ord(char) * key1) + key2) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr(((ord(char) * key1) + key2) % 26 + 97)
	return result
#check the above function
#Take string as input
inputData = input('Enter Character :')
key1 = int(input('Enter value of key(K1) :'))
key2 = int(input('Enter value of key(K2) :'))
print (inputData +' is encode into '+ affineCipherTechnique(inputData,key1,key2))
