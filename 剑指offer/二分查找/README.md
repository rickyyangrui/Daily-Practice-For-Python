## 二分查找
二分查找又叫折半查找，二分查找应该属于减治技术的成功应用。所谓减治法，就是将原问题分解成若干个子问题后，利用了规模为n的原问题的解与较小规模（通常是n/2）的子问题的解之间的关系。

二分查找利用了记录按关键码有序的特点，其基本思想为：在有序表中，取中间记录作为比较对象，若给定值与中间记录的关键码相等，则查找成功；若给定值小于中间记录的关键码，则在中间记录的左半边继续查找；若给定值大于中间记录的关键码，则在中间记录右半边区继续查找。不断重复上述过程，直到查找成功，或所查找的区域无记录，查找失败。

二分查找的时间复杂度是O(log(n))，最坏情况下的时间复杂度是O(n)。

* 优点是比较次数少，查找速度快，平均性能好，占用系统内存较少；
* 缺点是要求待查表为有序表，且插入删除困难。因此，折半查找方法适用于不经常变动而查找频繁的有序列表。

**算法要求：**
* 必须采用顺序存储结构。
* 必须按关键字大小有序排列。

下图是二分查找的减治思想：


![查找](https://github.com/rickyyangrui/Daily-Practice-For-Python/blob/master/%E5%89%91%E6%8C%87offer/%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE/%E5%87%8F%E6%B2%BB.png)

如果k< rmid查找这边 如果k> rmid查找这边

* 举个栗子：
在有序列表list1中[1, 3, 8, 12, 23, 31, 37, 42, 48, 58]中查找值为8的记录的。

### 思路：
```
1.low = 0; high = len(list1]-1 #设置初识查找区间
2.测试查找区间[low, high]是否存在，若不存在，则查找失败；否则
3.取中间mid=(low + high)/2；比较k与list1[mid]，有以下三种情况：
  3.1 若k<r[mid]，则high=mid-1；查找在左半区进行，转2；
  3.2 若k>r[mid]，则low=mid+1；查找在右半边区进行，转2；
  3.3 若k=r[mid]，则查找成功，返回记录在表中位置mid；
```

### 代码实现
* 方法一
```
#!/usr/bin/python
#coding=utf-8

#自定义函数，实现二分查找，并返回查找结果
def binary_search(find, list1) :
  low = 0
  high = len(list1)
  while low <= high :
    mid = (low + high) / 2
    if list1[mid] == find :
      return mid
    #左半边
    elif list1[mid] > find :
      high = mid -1
    #右半边
    else :
      low = mid + 1
  #未找到返回-1
  return -1

list1 = [1,2,3,7,8,9,10,5]
#进行二分查找算法前必须保证要查找的序列时有序的，这里假设是升序列表
list1.sort()

print "原有序列表为:",list1
try :
  find = int(raw_input("请输入要查找的数："))
except :
  print "请输入正整数！"
  exit()

result = binary_search(find, list1)
if result != -1 :
  print "要找的元素%d的序号为：%d" %(find,result)
else :
  print "未找到！"
```

* 方法二
python标准库中还有一个灰常给力的模块，那就是bisect。这个库接受有序的序列，内部实现就是二分。
```
    import bisect

    def binarySearch3(lst,x):
        i = bisect.bisect_left(lst,x)
        if i != len(lst) and lst[i] == x:
            return i
        raise ValueError

    if __name__ == '__main__':
        lst = sorted([2,5,1,7,3])
        print binarySearch3(lst,5)
```
