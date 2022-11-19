#Largest prime factor
# Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
n=600851475143
primfactor=7
for i in range(7,n):
     if prim(i):
          if n%i==0:
               primfactor=i
print(primfactor) 


