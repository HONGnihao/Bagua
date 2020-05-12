#Bagua_class
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
    def gua_zhanbu(n):
        for j in bgs:
            if n==j.name:
                print("+—————————————————————————————————————————————+")
                print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.name,chr(12288)))
                print("|{0}\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.pic,chr(12288)))
                print("|{0:{1}<45}|\n|{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}{1}|".format(j.guaci(),chr(12288)))
                j.yaoci()
                print("+—————————————————————————————————————————————+")
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
