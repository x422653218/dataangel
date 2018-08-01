import pandas as pd
import datetime

#判断时间
def before(t: object, p: object) -> object:
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta<=0:return True
    else: return False

#判断时间
def after(t,p):
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta>=0:return True
    else: return False
    
#键盘输入需求
def ip(list):
    flag="0"
    while flag=="0":
        print("请输入需要筛选的完整列名（一列）：")
        colname=input()
        if colname.lower()=="end":
            return "end"
        opr=""
        while (opr!="1") & (opr!="2") & (opr != "3") & (opr != "4") & (opr != "5") & (opr != "6") :
            print("请输入筛选操作序号:\n1.等于  2.不等于  3.大于  4.小于")#5.之前（日期比较）  6.之后（日期比较）
            opr=input()
        print("请输入筛选条件，如：是、否、25.2等（暂不支持百分数）")
        con=input()
        if opr == '1':
            opr = "等于"
        elif opr=='2':
            opr = "不等于"
        elif opr=='3':
            opr = "大于"
        elif opr=='4':
            opr = "小于"
        elif opr=='5':
            opr = "之前"
        elif opr=='6':
            opr = "之后"
        print("你输入的筛选是：",colname,opr,con,"；确认请按1，重新输入请按0： ")
        flag = input()
    list[0]=colname
    list[1]=opr
    list[2]=con
    return

#主函数
if __name__ == '__main__':
    print("欢迎使用DATA小公举！目前实现了筛选功能，请按提示输入：")
    print("默认读取data/sourcedata.txt。请输入txt的分隔符，如|,空格输入\\t")
    s=input()
    try:
        df = pd.read_table("data/sourcedata2.txt", sep=s, encoding='ANSI')
    except:
        print("ERROR：数据源文件未放好")

    while 1==1:
        print("输入end结束并输出结果，输入其他值继续:")
        if input().lower()=="end": break
        list=["","",""]
        ip(list)
        #print(list)
        colname2=list[0]
        con2=list[2]
        #输入一个筛选后即对数据进行筛选，list[1]=opr=1.等于  2.不等于  3.大于  4.小于
        try:
            if list[1]=="等于":
                df = df[(df[colname2] == con2)]
            elif list[1]=="不等于":
                df = df[(df[colname2] != con2)]
            elif list[1]=="大于":
                df = df[(df[colname2] > float(con2))]
            elif list[1]=="小于":
                df = df[(df[colname2] < float(con2))]
            # elif list[1]=="之前":
            #     df = df[(before(df[colname2],con2)]
            print("该条筛选已执行，请继续输入")
        except:
            print("该条筛选执行出错，请检查并再次输入")
    #输入完毕，输出结果
    df.to_csv("data/resultdata.csv", index=False, header=True, encoding='ANSI')
    print("你的筛选结果已输出到data文件夹的resultdata.csv中")