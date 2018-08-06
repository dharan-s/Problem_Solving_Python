#Robo.py

tel = {'jack': 4098, 'sape': 4139}
movement = {'L' :[-1,0], 'R':[1,0], 'U':[0,1], 'D':[0,-1]}

moves ="UUDDLULDULRDRRRULLLRRUDUURUULLDLLLRDLDLLRDRLDRRRDDRUDUDLRDLDRRUDLRLUDDRULLRRDLRLRLRULULDDDLUULDLLURR"
#moves = "LLLL"
print(moves)
dir = [0,0]

for s in moves:
	temp = movement[s]
	dir[0] += temp[0]
	dir[1] += temp[1]
#dir[0] %= 4
#dir[1] %= 4
print(dir)
if(dir[0] % 4 == 0 and dir[1] == 0):
	print("True")
else:
	print("False")
	
if(moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')):
	output True