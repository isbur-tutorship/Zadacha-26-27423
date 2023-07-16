f = open("26-2.txt")
# S, N = [int(x) for x in f.readline().split()]
S, N = f.readline().split()
S = int(S)
N = int(N)
# A = [int(x) for x in f.readlines()]
A = f.readlines()
for i in range(len(A)):
    A[i] = int(A[i])
f.close()

# print(A[:100])

A.sort()

#  print(A[:100])

cur_sum = 0
i = 0
while cur_sum + A[i] < S:
    cur_sum += A[i]
    i += 1

i -= 1
# print(A[i], i, cur_sum)
r = A[i]
for j in range(i+1, N):
    if cur_sum - r + A[j] <= S:
        cur_sum = cur_sum - r + A[j]
        r = A[j]
        # print(cur_sum, r)
print(i + 1, r)