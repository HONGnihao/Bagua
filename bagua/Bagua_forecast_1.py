#易经蓍草占卜+（铜钱占卜）

__author__="Qiyang Hong"
#Wechat:chinaimhqy    Email:qyhong_1997@qq.com
#（这个做的不太好，没有过程的体现，没有参与感）
import random
from Bagua_class import Bagua
#得到第一爻
class Zhanbu:
    def get_yao():
        left_hand=random.randint(1,48) #大衍之数五十，用之四十有九。分而为二以象两，挂一以象三
        right_hand=49-left_hand   #49根分为左右两堆。
        #print(left_hand,right_hand)
        if (left_hand-1)%4==0:
            left_remainder=4
        else:
            left_remainder=(left_hand-1)%4  #挂一象三，从左手堆取出一根后四根一组，最后得到一个余数
        if right_hand%4==0:
            right_remainder=4
        else:            
            right_remainder=right_hand%4
        total_r
        emainder_1=left_remainder+right_remainder+1 #得到第一变。
        #print(total_remainder_1)
        left_hand=random.randint(1,48-total_remainder_1)#五岁再闰。再求一变
        right_hand=49-total_remainder_1-left_hand
        #print(left_hand,right_hand)
        if (left_hand-1)%4==0:
            left_remainder=4
        else:
            left_remainder=(left_hand-1)%4
        if right_hand%4==0:
            right_remainder=4
        else:
            right_remainder=right_hand%4
        total_remainder_2=left_remainder+right_remainder+1
        #print(total_remainder_2)
        left_hand=random.randint(1,48-total_remainder_1-total_remainder_2) #再求一变
        right_hand=49-total_remainder_1-total_remainder_2-left_hand
        #print(left_hand,right_hand)
        if (left_hand-1)%4==0:
            left_remainder=4
        else:
            left_remainder=(left_hand-1)%4
        if right_hand%4==0:
            right_remainder=4
        else:
            right_remainder=right_hand%4
        total_remainder_3=left_remainder+right_remainder+1
        #print(total_remainder_3)
        yao_1=(49-total_remainder_1-total_remainder_2-total_remainder_3)/4
        return yao_1
    def get_gua():   #三变为一爻，十有八变而成卦。
        a,b,c,d,e,f=0,0,0,0,0,0
        yao_1=int(Zhanbu.get_yao())
        if yao_1==6:
            print("初爻为老阴--")
        elif yao_1==7:
            a=1
            print("初爻为少阳—")
        elif yao_1==8:
            print("初爻为少阴--")        
        elif yao_1==9:
            a=1
            print("初爻为老阳—")
        yao_2=int(Zhanbu.get_yao())
        if yao_2==6:
            print("二爻为老阴--")
        elif yao_2==7:
            b=1
            print("二爻为少阳—")
        elif yao_2==8:
            print("二爻为少阴--")        
        elif yao_2==9:
            b=1
            print("二爻为老阳—")
        yao_3=int(Zhanbu.get_yao())
        if yao_3==6:
            print("三爻为老阴--")
        elif yao_3==7:
            c=1
            print("三爻为少阳—")
        elif yao_3==8:
            print("三爻为少阴--")        
        elif yao_3==9:
            c=1
            print("三爻为老阳—")
        yao_4=int(Zhanbu.get_yao())
        if yao_4==6:
            print("四爻为老阴--")
        elif yao_4==7:
            d=1
            print("四爻为少阳—")
        elif yao_4==8:
            print("四爻为少阴--")        
        elif yao_4==9:
            d=1
            print("四爻为老阳—")
        yao_5=int(Zhanbu.get_yao())
        if yao_5==6:
            print("五爻为老阴--")
        elif yao_5==7:
            e=1
            print("五爻为少阳—")
        elif yao_5==8:
            print("五爻为少阴--")        
        elif yao_5==9:
            e=1
            print("五爻为老阳—")
        yao_6=int(Zhanbu.get_yao())
        if yao_6==6:
            print("上爻为老阴--")
        elif yao_6==7:
            f=1
            print("上爻为少阳—")
        elif yao_6==8:
            print("上爻为少阴--")        
        elif yao_6==9:
            f=1
            print("上爻为老阳—")
        return a,b,c,d,e,f
    def get_gua_name():
        a,b,c,d,e,f=Zhanbu.get_gua()
        for i in yaos_code:
            if eval(i[0])==a:
                if eval(i[1])==b:
                    if eval(i[2])==c:
                        if eval(i[3])==d:
                            if eval(i[4])==e:
                                if eval(i[5])==f:
                                    print("您的卦象为{}\n下面为该卦象对应的卦爻辞".format(i[6]))
                                    return i[6]
                                    
#概率验证: 无论如何变动分而为二这一过程的范围，最终结果都相似。
#老阴概率为5%左右，少阳概率为30%左右，少阴概率为45%左右，老阳概率为20%左右。
'''
a,b,c,d=0,0,0,0   #abcd分别代表老阴，少阳，少阴和老阳。
e=eval(input())
for i in range(e):
    f=int(Zhanbu.get_yao())
    if f==6:
        a+=1
    elif f==7:
        b+=1
    elif f==8:
        c+=1
    elif f==9:
        d+=1        
print(a/e,b/e,c/e,d/e)
'''

#阴为0，阳为1。手动输入文档bagua_6yao.txt,再导入对应的卦名
names=[]
with open("bagua_name.txt","r") as f1:
    for line in f1:
        names.append(line.replace("\n","")[3:])
#print(names)
yaos_code=[]
with open("bagua_6yao.txt","r") as f2:
    for line in f2:
        yaos_code.append((",".join(line.replace("\n",""))).split(","))
#print(yaos_code)
count=0
for i in yaos_code:
    i.append(names[count])
    count+=1
#print(yaos_code)

#备份一下
'''
with open("bagua_6yao_code.txt","w+") as f3:
    for i in yaos_code:
        for j in i:
            f3.write(j)
            f3.write(",")
        f3.write("\n")
'''
#运行部分
Bagua.gua_zhanbu(Zhanbu.get_gua_name())
