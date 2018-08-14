import pandas as pd
import numpy as np
import datetime


#
# ========
#小可需求：就是分组找出J列[小区名称]一样的，找出N列[系统内每相邻关系切换出请求次数]TOP10的，然后求平均值，输出（J列名字，N列名字，均值）
# try:
#     df = pd.read_csv("data/wuyou.csv",sep=',', encoding='ANSI')
# except:
#     print("ERROR：数据源文件未放好")
#print(df)
#
# groupby='小区名称'
# sortby='系统内每相邻关系切换出请求次数'
# ascending=False#从大到小要降序,false降序
# N=10
# # groupby=input()
# # sortby=input()
# # ascending=input()#升序降序
# # N=input()
#
# df.sort_values(by=sortby, ascending=ascending,inplace=True)#先排序
# df=df.groupby(groupby).head(N).sort_values(by=[groupby,sortby],ascending=ascending)#后分组取TOP N的值，再按分组和大小排序
# #m=df.groupby([groupby],as_index = False)[sortby].mean()#按分组求均值
# df.to_csv("data/测试输出2.csv", index=False, header=True, encoding='ANSI')
# # print(m)
# ==================

# =====测试时间
def before(t,p):
    d1 = datetime.datetime.strptime(t, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(p, '%Y-%m-%d')
    delta = (d1 - d2).days
    print(delta)#小于0就是d1在d2前，大于0就是d1在d2后
    if delta<=0:return True
    else: return False

if __name__ == '__main__':
    try:
        df = pd.read_table("data/sourcedata2.txt", sep='\t', encoding='ANSI')
        df.set_index('时间')
        df.loc[before(df['时间'],'2018/4/18')]
        df.to_csv("data/时间测试输出.csv", index=False, header=True, encoding='ANSI')
    except Exception as e:
        print(e)














