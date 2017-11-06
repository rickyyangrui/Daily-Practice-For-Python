a = 36
b = 21

## 最大公约数，最小公倍数
```
def maxCommon(a, b):
	while b: a,b = b, a%b
	return a 

def minCommon(a, b):
	c = a * b
	while b:a, b=b, a%b
	return c // a 
	
if __name__ == '__main__':
	print(maxCommon(a, b))
	print(minCommon(a, b))
```

## 获取中位数
```
def median(data):
	data.sort()
	half = len(data) // 2
	return (data[half] + data[~half])/2
	
l = [1, 3, 4, 53, 2, 46, 8, 42, 82]

if __name__ == '__main__':
	print(median(l))
```