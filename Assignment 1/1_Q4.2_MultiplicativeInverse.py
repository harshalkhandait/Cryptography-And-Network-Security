#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Python program to calculate pairs of multiplicative inverse in Zn
# Function to print pairs
def multiplicativeInverse(z) :
    for i in range(z):
        for j in range(i, z) :
            if ((i * j) % z == 1) :
                print('Multiplicative Inverse of '+str(i)+' is '+str(j))
# Driver Program
print('Enter the Size of Z')
z = int(input())
multiplicativeInverse(z)
