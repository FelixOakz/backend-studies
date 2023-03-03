from random import sample
nums = tuple(sample(range(1, 10), 5))
print(f'os valores sorteados foram: {nums}.')
print(f'o maior valor sorteado foi {max(nums)} e o minimo: {min(nums)}.')
