import pandas as pd
import datetime

#判断时间 t是否在p之前
def before(t, p):
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta<=0:return True
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
            #print("请输入筛选操作序号:\n1.等于  2.不等于  3.大于  4.小于 5.之前（日期比较）  6.之后（日期比较")
            print("请输入筛选操作序号:\n1.等于  2.不等于  3.大于  4.小于")
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
    print("欢迎使用DATA小公举！目前实现了筛选、排序功能，请将源数据放入data文件夹，然后输入文件名（data.txt/data.csv)")
    d: str=input()
    d='data/'+d
    try:
        if ('.txt' in d):
            print("请输入txt的分隔符，如|,空格输入\\t")
            s = input()
            df = pd.read_table(filepath_or_buffer=d, sep=s, encoding='ANSI')
        elif ('.csv' in d): df = pd.read_csv(filepath_or_buffer=d, sep=',', encoding='ANSI')
    except Exception as e:
        print(e)
        print("error:读取文件出错，请退出重来，文件名必须包括.txt/.csv")

    while 1==1:
        print("请输入菜单对应序号：1.筛选   2.分组排序    3.求值(平均数)   0.结束输出")
        i=input()
        if i=='0': break
        elif i=='1': #筛选
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
                #     df.loc[before(df[colname2],con2)]
                #elif list[1] == "之后":
                print("该条筛选已执行，请继续输入")
            except Exception as e:
                print(e)
                print("该条筛选执行出错，请检查并再次输入")
        elif i=='2':#排序
            try:
                print("如：对于A列值相同的，取B列值最大/最小的N（10/15)行，请按顺序输入A列名、B列名、N")
                groupby: str=input()
                sortby: str=input()
                N=input()
                print("取最大输入0，取最小输入1")
                ascending=input()#升序降序
                if ascending=='0':ascending = False #从大到小要降序,false降序
                elif ascending=='1': ascending = True
                else:print("输错了，退出程序重新输入")
                df.sort_values(by=sortby, ascending=ascending,inplace=True)#先排序
                df=df.groupby(groupby).head(int(N)).sort_values(by=[groupby,sortby],ascending=ascending)#后分组取TOP N的值，再按分组和大小排序
                print("成功排序")
            except Exception as e:
                print(e)
        elif i=='3':#求值（平均数）
            print("如：对于A列值相同的，取B列值的平均值，请按顺序输入A列名、B列名")
            groupby: str = input()
            sortby: str = input()
            df = df.groupby([groupby], as_index=False)[sortby].mean()  # 按分组求均值
            print("该次操作完毕")
    #输入完毕，输出结果
    df.to_csv("data/resultdata.csv", index=False, header=True, encoding='ANSI')
    print("你的处理结果已输出到data文件夹的resultdata.csv中")