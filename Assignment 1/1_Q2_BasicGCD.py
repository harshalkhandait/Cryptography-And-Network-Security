#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Python program to demonstrate Basic Euclidean Algorithm
# Function to return gcd of a and b
def gcd(a, b):
	if a == 0 :
		return b
	return gcd(b%a, a)
print('Enter First Number')
a = int(input())
print('Enter Second Number')
b = int(input())
if a>b:
	print('GCD of '+str(a)+' and '+str(b)+' using Basic Euclidean Algorithm = '+str(gcd(a,b)))
else:
	print('GCD of '+str(a)+' and '+str(b)+' using Basic Euclidean Algorithm = '+str(gcd(b,a)))
