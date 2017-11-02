# 创建字典的方法：

# 1.直接创建
```
dict = {'name':'earth', 'post':'80'}
```

# 2.工厂方法
```
items = [('name','earth'),('port','80')]
dict2 = dict(items)
dict1 = dict((['name','earth'],['port','80']))
```

# 3.formkeys()方法
```
dict1 = {}.formkeys(('x','y'),-1)
dict = {'x':-1,'y':-1}
dict2 = {}.formkeys(('x','y'))
dict2 = {'x':None, 'y':None}
```