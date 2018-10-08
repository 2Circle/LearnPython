#列表的使用范例
GameCompanys = ["nintendo","sony","microSoft"]
print(GameCompanys)
#用数字下标访问
print(GameCompanys[0])
#使用-1可以直接访问最后一个
print(GameCompanys[-1])
#for循环遍历列表元素
for gamecompany in GameCompanys:
    print(gamecompany.title())
#用append增加元素
GameCompanys.append("sega")
print(GameCompanys)
#用insert插入元素
GameCompanys.insert(0,"tencent")
print(GameCompanys)

#使用del删除元素
del GameCompanys[0]
print(GameCompanys)

#使用pop删除元素
GameCompanys.pop(-1)
print(GameCompanys)
#使用remove删除元素
GameCompanys.remove("sony")
print(GameCompanys)

#使用range生成数字
ManyNumbers = range(1,101)#错误的写法
for value in range(1,101):
    print(value)

#列表解析写法
squares = [value**2 for value in range(1,11)]
print(squares)

#列表切片
print(GameCompanys[0:1]) 

for cm in GameCompanys:
    if cm == "nintendo":
        print(cm.upper())
    else:
        print(cm.title())
