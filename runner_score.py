#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

#Input Format
#The first line contains n. The second line contains an array A[] of n integers each separated by a space.

n=2
arr=[0,5,2,5,4]
length = len(arr)
max_ele = max(arr)
for i in range(1,length):
	if max_ele-i in arr:
		 print(max_ele-i)
		 break
		 
print("New method")
arr.sort()
print(arr)
while(max(arr) == max_ele):
	#print(max(arr))
	arr.pop()
print(max(arr))

waterfall -- agile CR/ER 
agile-->sprints 
legacy code --> lot of dependencies in 
based on selective parameter query will be generated. query should be proper. 
inner join market - periods-- product-- fact 
composite layer - hit --> check if it is in cache -->   
fact --> S, perscrebt , business_layer business_value logic defining in --> composite 
csv encoding part --> 4 stored query which 
pristine--> netezza keywords won't be understand 
based on their business logic---> get the output 
2. why netezza --> million of records, individual normal database can't hold. 
1. netezza should understand 2. top of that pivoted nested  3. netezza readable format query. 1000 lines. 
new fact --> added --> challenges to add csv and 
jsql parser--> not string handling --> map --> retrivre--> string builder --> little bit spring --> step by step design pattern 
fact --> dollar -- sales value 

ditinct > in or exists

--------------------
command driven(design pateern of java) --> bean --> spring mvc dependency injection --> 
