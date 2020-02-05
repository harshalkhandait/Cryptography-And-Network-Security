#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Python program to additive inverse using Extended Euclidean Algo
def gcd(a,b,t1,t2):
    #Termination Condition
    if b==0:
        return t1
    else:
        r= a%b
        q=(a-r)/b
        return gcd(b,r,t2,t1-q*t2)
#driver program
n=int(input("Enter value of n:"))
b=int(input("Enter the number whose Inverse is to be calculated: "))
t=gcd(n,b,0,1)
#print("\nMultiplicative inverse of ",b," = ",int(t%n),"\n")
print('Multiplicative Inverse of '+str(b)+' = '+str(int(t%n)))
