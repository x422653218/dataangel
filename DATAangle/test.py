engine='python'
import pandas
import datetime

def before(t,p):
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta<=0:return True
    else: return False

def after(t,p):
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta>=0:return True
    else: return False

if __name__ == '__main__':
    before('2016-07-01','2017-02-02')


# print("输入txt的分隔符，如|,空格输入\\t")
# s = input()
# try:
#     # df = pandas.read_table("data/sourcedata.txt", sep='|', encoding='ANSI')
#     df = pandas.read_table("data/test2.txt", sep=s, encoding='ANSI')
# except:
#     print("ERROR：数据源文件未放好")
# print(df)
