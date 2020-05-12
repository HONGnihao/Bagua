


#易经六十四卦搜索器

__author__="Qiyang Hong"
#Wechat:chinaimhqy    Email:qyhong_1997@qq.com
from Bagua_class import Bagua

#import requests
#import re
#from bs4 import BeautifulSoup
#import time
#从网上获取卦名
'''
r=requests.get("https://www.buyiju.com/zhouyi/",headers={"user-agent":"Mozallia/5.0"},timeout=5)
r.encoding="utf-8"
gua=re.compile(r"<br/>.*</a></li>")
gualst=gua.findall(r.text)
for i in gualst:
    print(i[5:-9])
    with open("bagua_name.txt","a+") as f:
        f.writelines(i[5:-9])
        f.write("\n")
'''               
#从网上获取卦爻辞
'''
for i in range(64,65):
    try:
        url="https://www.buyiju.com/zhouyi/yijing/64gua-{}.html".format(i)
        rn=requests.get(url,headers={"user-agent":"Mozallia/5.0"},timeout=5)
        rn.encoding="utf-8"
        soup=BeautifulSoup(rn.text,"lxml")
        if len(str(soup.find_all("p")[4]))<=40:
            exp=str(soup.find_all("p")[3])
        else:
            exp=str(soup.find_all("p")[4])
        exp=exp.replace("<p>","")
        exp=exp.replace("</p>","")
        exp=exp.replace("<br/>","")
        exp=exp.replace("\n","")
        exp=exp.replace(" ","")
        exps.append(exp)
        print(i)
        print(exp)
        with open("bagua_exps.txt","a+") as f:
            f.writelines("{}.".format(i)+exp)
            f.write("\n")
        time.sleep(5)
    except:
        print("Error")
        continue
'''    
#运行部分
for i in range(64):
    gua=input("请输入要查询的卦名或相关关键词：\n")
    Bagua.Bagua_search(gua)
    





    
    



