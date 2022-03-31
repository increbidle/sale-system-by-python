"""ver1.3.0"""

#欢迎系统
print("欢迎使用购物系统")
products=[["0001","伊雷娜的帽子","9999.00","2"],
          ["0002","麻衣学姐的兔耳朵","9999.01","1"],
          ["0003","后辈的踢屁股权","200.00","99"],
          ["0004","奇怪的石头面具","10.00","1"],
          ["0005","有拉链的黑色面罩","5.00","1"],
          ["0006","模你穷的头盔","35.00","114514"]]

products_car=[]#建立购物车
def print_product():
    # 打印商品列表
    # 2022/3/31留：以我目前的水平做不到中英混合字符串对齐，之后学会了优化
    print("{:*<50s}".format(""))
    print("{0:10s} {1:10s} {2:10s} {3:10s}".format("编号", "名称", "价格", "库存"))
    for h in range(len(products)):
        for l in range(len(products[h])):
            print("{:10s}".format(products[h][l]), end="")
        print("")
    return(1)
print_product()
def car_input():
    car_add_id=int(input("请输入商品编号以加入购物车"))
    while car_add_id not in [int(i[0]) for i in products]:#建立一个以products第一列为元素的数组
        car_add_id=input("输入错误，请重新输入")
    count=int(input("请输入购买数量"))
    while count > int(products[car_add_id-1][3]):
        count=int(input("输入数量大于库存，请重新输入"))
    products_car.append([products[int(car_add_id)-1][int(count)]])#加入购物车
    print("添加完成")
car_input()