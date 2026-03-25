# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())

#     total = [0]*(k+1)
#     for _ in range(k):
#         b, c = map(int, input().split())
#         total[b] += c

#     total.sort(reverse=True)
#     print(sum(total[:n]))


class Solution:
	def nextSmallerEle(self, arr):
		n = len(arr)
		stack = []
		stack [0] = arr[0]
		result = [-1]*n   #[-1 -1 -1 -1 -1]
		for i in range(n-1, -1, -1):
			while stack and stack[-1] >= arr[i]:
				stack.pop()#25
				
			if stack:
				result[i] = stack[-1]#25
				
			stack.append(arr[i])#[2]
		
sol = Solution()
print(sol.nextSmallerEle([4, 8, 5, 2, 25]))