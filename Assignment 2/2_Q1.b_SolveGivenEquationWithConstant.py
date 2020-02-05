#Written by Harshal Khandait
#Enrollment Number BT17CSE074
# Python program to demonstrate Basic Euclidean Algorithm
# Function to return gcd of a and b
def gcd(a, b):
	if a == 0 :
		return b
	return gcd(b%a, a)
# Python program to demonstrate Basic Euclidean Algorithm
# Function to return Multiplicative Inverse of B over Zn
def multiplicativeInverse(B,N) :
    B = B % N
    for i in range(1,N) :
        if ((i * B) % N == 1) :
            return i
    return 1
#Function to check if solution exists for a given code or not
def checkSolutionExists(A,B,N):
    if (B%gcd(A,N)) == 0:
        return True
    else:
        return False
def solveEquationWithoutConstant(A,B,N):
	#Checking if solution exists
	check_solution_exists = checkSolutionExists(A,B,N)
	if check_solution_exists==True:
	    #Simplifying the Equation further
	    gcdOfABC = gcd(gcd(A,B),N)
	    A=int(A/gcdOfABC)
	    B=int(B/gcdOfABC)
	    N=int(N/gcdOfABC)
	    #Calculation Multiplicative Inverse of A over Zz
	    A_inverse=multiplicativeInverse(A,N)
	    print('Following are the Solutions:')
	    #Calculating First Solution
	    X0=(B*A_inverse)%N
	    print('X0 =' + str(X0))
	    #Calculating Remaining Solution
	    for i in range(1,gcdOfABC):
	        print('X'+str(i)+'='+str(X0+(i)*(N)))
	else:
	    print('There exists no solution for '+str(A)+'x'+' = '+str(B)+ "(mod"+ str(N) +")")

# Assuming the input is
# Ax+C=B(mod N)
#Taking Input
A=int(input('Enter Value of A (Co-Efficient of X) :'))
B=int(input('Enter Value of B :'))
C=int(input('Enter Value of C :'))
N=int(input('Enter Value of N :'))
#Driver program
#Removing Constant and calling the function
solveEquationWithoutConstant(A,(B-C),N)
