from random import randint


def draw(nums):
	for i in range(5):
		nums.append(randint(0, 100))


def evenSum(nums):
	even = 0
	for i in nums:
		if i % 2 == 0:
			even += i
	print(f'> Adding even numbers from the list {nums}, we have: {even}')


nums = []
draw(nums)
evenSum(nums)
