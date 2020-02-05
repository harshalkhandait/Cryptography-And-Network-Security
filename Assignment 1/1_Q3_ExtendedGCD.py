#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Python program to demonstrate working of extended
# Euclidean Algorithm
# function for extended Euclidean Algorithm
def gcdExtended(a,b,s1,s2,t1,t2):
    if b==0:
        return a
    else:
        r= a%b
        q=(a-r)/b
        return gcdExtended(b,r,s2,s1-q*s2,t2,t1-q*t2)
print('Enter First Number')
a = int(input())
print('Enter Second Number')
b = int(input())
if a>b:
	s1=1
	s2=0
	t1=0
	t2=1
	print('GCD of '+str(a)+' and '+str(b)+' using Extended Euclidean Algorithm = '+str(gcdExtended(a, b, s1, s2, t1, t2)))
else:
	s1=0
	s2=1
	t1=1
	t2=0
	print('GCD of '+str(a)+' and '+str(b)+' using Extended Euclidean Algorithm = '+str(gcdExtended(b, a, s1, s2, t1, t2)))
