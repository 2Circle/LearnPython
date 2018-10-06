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