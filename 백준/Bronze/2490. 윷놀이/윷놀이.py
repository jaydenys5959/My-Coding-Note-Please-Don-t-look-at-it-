for i in range(3):
	A,B,C,D = map(int,input().split())
	Q = A+B+C+D
	if Q == 3:
		print("A")
	if Q == 2:
		print("B")
	if Q == 1:
		print("C")
	if Q == 0:
		print("D")	
	if Q == 4:
		print("E")
