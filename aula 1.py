import random
M = [[random.randint(-99,99) for i in range(3)],[random.randint(-99,99) for i in range(3)],[random.randint(-99,99) for i in range(3)]]
N = [[4*x for i in (range(len(M)//3)) for x in M[i]],[4*x for i in range(1,len(M)*2//3) for x in M[i]],[4*x for i in (range(2,len(M))) for x in M[i]]]
O = [[0]*i+[1]+[0]*(len(N)-i-1) for i in range(len(N))]