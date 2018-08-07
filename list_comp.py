#You are given three integers x,y,z and  representing the dimensions of a cuboid along with an integer N . You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal to N. Here 0<=i<=x;0<=j<=y;0<=k<=z, 

#Input Format
#Four integers  and  each on four separate lines, respectively.

#Constraints
#Print the list in lexicographic increasing order.


x = 2
y = 2
z = 2
n = 2

#---------Simple plain-------#
result=[]
for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if(i+j+k != n):
				a=[i,j,k]
				result.append(a)
			
		
print(result)

#-----Using List comprehension---#

print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])