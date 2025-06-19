import time,random
from typing import Literal

def printlen(txt):#求字符串在Shell中的显示长度
    """求字符串在Shell中的显示长度"""
    len1=r"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz<>/|-+\[]= :!@#%^&*()\{\}_.,;~"
    l=0
    for i in txt:
        if i in len1:
            l+=1
        else:
            l+=2
    return l

def adjustplus(txt:str,di:int=50,mode:Literal["left","right"]="left"):
    
    return {
        "left":txt + " "*(di - printlen(txt)),
        "right":" "*(di - printlen(txt)) + txt
    }.get(mode,"IFAWL_typing_error")

def shell_center(txt:str,target_len:int,m_txt:str)->str:
    """IFAWL笑传之词称变"""
    output=""
    total_need_to_be_fill_in=target_len-printlen(txt)
    right=int(total_need_to_be_fill_in/2)
    left=total_need_to_be_fill_in-right
    output=m_txt*left+txt+m_txt*right
    return output

def two_columnprint(left,right,di=50):#双栏打印
    if len(left)<len(right):
        for i in range(len(left),len(right)):
            left.append("")
    elif len(left)>len(right):
        for i in range(len(right),len(left)):
            right.append("")
    for i in range(0,len(left)):
        print(left[i]+" "*(di-printlen(left[i]))+right[i])

def three_columnprint(left,mid,right,di=50,dii=50):#三栏打印
    maxlen=max(len(left),len(right),len(mid))
    for i in range(len(left),maxlen):
        left.append("")
    for i in range(len(mid),maxlen):
        mid.append("")
    for i in range(len(right),maxlen):
        right.append("")
    for i in range(0,len(left)):
        print(left[i]+" "*(di-printlen(left[i]))+mid[i]+" "*(dii-printlen(mid[i]))+right[i])

def n_columnprint(columns:list[list[str]],di_list:tuple[int]=()):
    """
    IFAWL N栏打印引擎
    columns: 二维列表。将要打印的一栏制成行切片（参考Tree.lienlist() ），作为该列表的一项
    di_list: 栏左端间距列表。上过小学四年级的都学过植树问题，都知道长度要比columns少1
    """

    

    len_list = [len(i) for i in columns]
    maxlen=max(len_list)

    if di_list == ():
        di_list = [50 for i in range(len(columns) - 1)]
    elif type(di_list) == int:
        di = di_list
        di_list = [di for i in range(len(columns) - 1)]

    for i in range(len(columns)):
        for p in range(len(columns[i]),maxlen):
            columns[i].append("")

    for i in range(0,len(columns[0])):
        stri = ""
        k = 0
        for j in columns[:-1]:
            stri += adjustplus(j[i],di_list[k])
            k += 1
        stri += columns[-1][i]
        print(stri)

 

def printplus(txt:str,sec:float=0.3):#增强视觉print函数
    '''增强视觉print函数'''
    i=len(txt)
    if i<10:
        sec-=0.1
    if sec != 0:
        for j in txt:
            print(j,end="")
            time.sleep(sec/len(txt))
        print("")
        time.sleep(0.2)
    else:
        print(txt)

def inputplus(txt:str,sec:float=0.3):#增强视觉input函数
    i=len(txt)
    for j in txt:
        print(j,end="")
        time.sleep(sec/len(txt))
    if not txt.endswith(">>>"):
        print(">>>",end="")
    return input("")

def qte_game(run_delta_t:float=0.03):

    target = random.randint(33,66)

    try:
        inputplus("[矿业体系]确认后使用[ctrl+C]（请勿多次敲击或长按）锁定目标|[enter]确认>>>")
    except:
        print("谁叫你在这里按了？？")
        time.sleep(1)

    print(" "*(target-2) + "[ + ]")

    pos=-1
    for i in range(100):
        try:
            pos+=1
            print("|",end="")
            time.sleep(run_delta_t)
        except KeyboardInterrupt:
            break

    if target-4  <= pos <= target+4 :
        print("")
        if  target-2  <= pos <= target+2:
            #print(" "*(target-10)+r"\\\\  Exact!  ////")
            print(adjustplus(r"\\\\  Exact!  ////",di=target+10,mode="right"))
            #print(" "*(target-10)+r"   \\\\全命中////")
            print(adjustplus(r"   \\\\全命中////",di=target+8,mode="right"))
            return 2
        else:
            print(" "*(target-7)+r"\\ 部分命中 //")
            return 1
    else:
        print("锁定失败")
        return 0

class Tree:#打印用tree对象

    topic=""
    body=[]

    def __init__(self,topic,*ag):
        self.topic=topic
        self.body=[]
        for i in ag:
            if type(i) == str or type(i) == int:
                self.body.append(i)
            elif type(i) == list:
                for j in i:
                    self.body.append(j)
            elif type(i) == dict:
                for j in i:
                    self.body.append(j+" "*(10-printlen(j))+f" *{i[j]}")
            elif type(i) == Tree:
                i:Tree
                self.body.append(i.topic)
                for j in i.body:
                    self.body.append(f" -{j}")

    def treeprint(self,is_foldable=False):
        print(self.topic)
        if is_foldable and len(self.body) > 3:
            for i in self.body[0:3]:
                print("|")
                print("|-"+str(i))
            print("|")
            print("|>>[已折叠]")
            print("")
        else:
            for i in self.body:
                print("|")
                print("|-"+str(i))
            print("")

    def linelist(self,is_foldable=False):
        """
        行切片生成函数
        """
        printlist=[]
        printlist.append(self.topic)
        if is_foldable and len(self.body) > 3:
            for i in self.body[0:3]:
                printlist.append("|")
                printlist.append("|-"+str(i))
            printlist.append("|")
            printlist.append("|>>[已折叠]")
            printlist.append("")
        else:
            for i in self.body:
                printlist.append("|")
                printlist.append("|-"+i)
            printlist.append("")
        return printlist



def dict_give_and_get_print(father:dict,get:dict,give:dict):
    
    def print_main(zoom):
        print(i,end=" "*(12-printlen(i)))
        if i in get:
            print("-"*(father[i]//zoom),end="")
            print(">"*(get[i]//zoom),end="")
            print(f"  {father[i]}+{get[i]}")
        elif i in give:
            print("-"*((father[i]-give[i])//zoom),end="")
            print("<"*(give[i]//zoom),end="")
            print(f"  {father[i]}-{give[i]}")
        else:
            print("-"*(father[i]//zoom),end="")
            print(f"  {father[i]}")

    for i in father:
        if i not in "联邦信用点合约纪念点保险点":
            print_main(5)
        elif i == "联邦信用点":
            print_main(400)
        elif i == "保险点":
            print_main(1)
    print()

def dict_diff_print(old:dict,new:dict):
    get={}
    give={}
    for i in old:
        if old[i]<new[i]:
            get[i]=new[i]-old[i]
        elif new[i]<old[i]:
            give[i]=old[i]-new[i]
    dict_give_and_get_print(old,get,give)

def plot_print(*line,fast_mode=False):
    print("[ctrl+C] 跳过（请勿多次敲击或长按）",end="\n\n")
    try:
        if fast_mode:
            time=0
        else:
            time=0.3
        for i in line:
            if type(i) == str:
                printplus(f"-{i}",time)
            elif type(i) == list:
                for j in i:
                    inputplus(f"[enter]{j}>>>",time)
            print()
    except:
        for i in line:
            print(i);print()

def ask_plus(txt:str,kword:list):
    kword_str = kword.copy()
    kword_str = [str(j) for j in kword]
    while 1:
        inp=inputplus(txt)
        if inp in kword_str:
            break
        else:
            print("请在可选范围内输入")
    return  inp

def max_index_finder(raw_tuple:tuple,
                     target:str,
                     add1=True):

    target_list = []
    for i in raw_tuple:
        if i.startswith(target):
            try:
                target_list.append(
                    int(
                        i[len(target):]
                    )
                )
            except:
                pass
    output = max(target_list) + 1 if add1 else max(target_list)
    return output

if __name__ == '__main__':
    printplus("本文件是IFAWL文本处理模块")