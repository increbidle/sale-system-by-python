"""ver1.3.0.1"""

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
def car_input():
    global products
    car_add_id=int(input("请输入商品编号以加入购物车"))
    while car_add_id not in [int(i[0]) for i in products]:#建立一个以products第一列为元素的数组
        car_add_id=input("输入错误，请重新输入")
    count=int(input("请输入购买数量"))

    while count > int(products[car_add_id-1][3]):
        count=int(input("输入数量大于库存，请重新输入"))
    if products_car!=[]:
        if products[car_add_id] in products_car:
            for h in range(len(products_car)):
                if products_car[h] in products_car:
                    products_car[h][1]=int(products_car[h][1])+1
                else:
                    products_car.append([products[int(car_add_id)-1][1],int(count)])#加入购物车
        else:
            products_car.append([products[int(car_add_id) - 1][1], int(count)])
    else:
        products_car.append([products[int(car_add_id) - 1][1], int(count)])
    print("添加完成")
    products[car_add_id-1][3]=str(int(products[int(car_add_id-1)][3])-count)
    return products
def car_view():
    print("您的购物车：")
    print("{:*<40s}".format(""))
    print("{:<12s}{:<10s}".format("商品","数量"))
    for h in range(len(products_car)):
        print("%-10s" %products_car[h][0],"%-6d" %products_car[h][1])
    print("{:*<40s}".format(""))
"""好像def内部的变量不能全局使用，我要哭了！"""#可以改！我又不哭了。
def pay():
    totle=0
    global sum
    for h in range(len(products)):
        for h1 in range(len(products_car)):
            if products_car[h1][0] in products[h][1]:
                sum=products_car[h1][1]*float(products[h][2])
                totle=totle+sum
    print("需要支付: {:.2f}".format(totle))
def option():
    global forced_out
    forced_out=0
    option_input=int(input("请输入指令以进行操作：1：查看商品 2：将商品加入购物车 3：查看购物车 4：结算 5:退出"))
    while option_input not in range (6):
        option_input=int(input("指令有误，请重新输入"))
    while option_input in range(5):
        if option_input==1:
            print_product()
        elif option_input==2:
            car_input()
        elif option_input==3:
            car_view()
        elif option_input==4:
            pay()
            forced_out=1
        if forced_out==1:
            break
        option_input = int(input("请输入指令以进行操作：1：查看商品 2：将商品加入购物车 3：查看购物车 4：结算 5:退出"))
    print("谢谢光临")
option()
