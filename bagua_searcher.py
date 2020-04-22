#易经六十四卦搜索器

__author__="Qiyang Hong"
#Wechat:chinaimhqy    Email:qyhong_1997@qq.com

class Bagua:
    def __init__(self,name,pic,explain):
        self.name=name
        self.pic=pic
        self.explain=explain
        
    def guaci(self):
        return self.explain[0]
    
    def yaoci(self):
        try:
            if self.name=="乾为天" or self.name=="坤为地":
                for i in range(7):
                    print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(self.explain[i+1],chr(12288)))
            else:
                for i in range(6):
                    print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(self.explain[i+1],chr(12288)))
        except:
            print("404")
    def Bagua_search(n):    #查询特定卦象或是关键词
        count=0
        for j in bgs:
            if n in j.name or n in j.explain[0] or n in j.explain[1] or n in j.explain[2] or n in j.explain[3] or n in j.explain[4] or n in j.explain[5] or n in j.explain[6] or n in "用九：见群龙无首，吉。用六：利永贞。":
                print("+—————————————————————————————————————————————+")
                print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.name,chr(12288)))
                print("|{0}\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.pic,chr(12288)))
                print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.guaci(),chr(12288)))
                j.yaoci()
                print("+—————————————————————————————————————————————+")
                count+=1
        print("匹配到相关卦象{}个".format(count))
        if count==0:
            print("输入卦名或关键字未能匹配，请重试")    
        
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
#从文档中读取卦名和卦爻辞
names=[]
with open("bagua_name.txt","r") as f:
    for line in f:
        names.append(line.replace("\n",""))
f.close()

exps=[]
with open("bagua_exps.txt","r") as f:
    for line in f:
        exps.append(line.replace("\n",""))
f.close()
exps_list=[]
for i in exps:
    i=i[3:].replace("。初六","。|初六")
    i=i.replace("。初九","。|初九")
    i=i.replace("。六","。|六")
    i=i.replace("。九","。|九")
    i=i.replace("。上六","。|上六")
    i=i.replace("。上九","。|上九")
    exps_list.append(i.split("|"))

#输入卦象,Unicode码 4DC0—4DFF为六十四卦卦象
pics=[]
for i in range(0X4DC0,0X4E00):
    pics.append(chr(i))
    
#创建实例
bgs=[]
for i in range(1,65):
    bgs_obj="bg{}".format(i)
    bgs_obj=Bagua(names[i-1][3:],pics[i-1],exps_list[i-1])
    bgs.append(bgs_obj)
    
#运行部分
for i in range(64):
    gua=input("请输入要查询的卦名或相关关键词：\n")
    Bagua.Bagua_search(gua)
    





    
    



