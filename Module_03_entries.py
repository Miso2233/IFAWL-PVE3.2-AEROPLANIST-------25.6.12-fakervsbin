from Module_01_txt import Tree
import Module_01_txt as m1
import random,shelve

def probability(pro)->bool:#概率为真
    if random.random()<pro:
        return True
    else:
        return False

mode_list=[1,2,5,6]


class Entry_general:
    title=""
    description=""
    rank_list=["NO","I","II","III","IV"]
    rank_description=[]
    rank=0
    points_list=[]

    def __init__(self,title:str,description:str,rank_description:list,points_list:list=[]):
        self.title=title
        self.description=description
        self.rank_description=rank_description
        self.points_list=points_list

    def react_print(self):
        m1.printplus(f"警告·[{self.title}]词条被触发")

    def refresh(self):
        self.rank=0

    def print_description(self):
        title = f"[{self.__class__.__qualname__[5:]}]“{self.title}”：{self.description}"
        body = []
        for j in range(1,len(self.rank_description)):
            if_chosen="[●已选中]" if j == self.rank else ""
            body.append((f"[{self.rank_list[j]}]{self.rank_description[j]}[{self.points_list[j]}分]{if_chosen}"))

        Tree(title,body).treeprint()

    def description_tree(self):
        title = f"[{self.__class__.__qualname__[5:]}]“{self.title}”：{self.description}"
        body = []
        for j in range(1,len(self.rank_description)):
            if_chosen="[●已选中]" if j == self.rank else ""
            body.append((f"[{self.rank_list[j]}]{self.rank_description[j]}[{self.points_list[j]}分]{if_chosen}"))

        return Tree(title,body)


class Entry1(Entry_general):#烈风 已整理好
    
    def react(self,atk,mode)->int:
        if (mode in mode_list) and probability(self.rank*0.2):
            self.react_print()
            return atk+1
        else:
            return atk
entry1=Entry1("烈风",
              "概率提升敌方攻击的伤害",
              ["","使敌方所有伤害有20%概率+1","使敌方所有伤害有40%概率+1","使敌方所有伤害有60%概率+1"],
              [0,40,60,80])

class Entry2(Entry_general):#战场迷雾 已整理好
    pass
entry2=Entry2("战场迷雾",
              "部分战场信息将不可见",
              ["","敌方导弹数量不可见","敌方导弹与我方护盾不可见"],
              [0,20,40])

class Entry3(Entry_general):#虚弱 已整理好
    
    def react(self,atk,mode)->int:

        if (mode in mode_list):
            if self.rank == 1 and atk>1 and probability(0.3):
                self.react_print()
                return atk-1
            elif self.rank == 2 and probability(0.3):
                self.react_print()  
                return atk-1
            else:
                return atk
        else:
            return atk  
entry3=Entry3("虚弱",
             "概率削弱我方攻击的伤害",
             ["","对于大于1的我方伤害，有30%概率使其-1","对于所有我方伤害，有30%概率使其-1"],
             [0,60,70])

class Entry4(Entry_general):#绝望 已整理好
    def react(self,mode,atk):#仅宏峰
        if self.rank != 0 and (mode in mode_list):        
            entry4.react_print()
            return atk+1
        return atk
entry4=Entry4("绝望",
              "增加宏峰导弹和殷红狂怒的伤害",
              ["","宏峰伤害+1","宏峰/殷红伤害+1"],
              [0,40,70])

class Entry5(Entry_general):#最终防线 已整理好
    
    def check_if_die(self,mode,hp):
        if (mode in mode_list) and self.rank == 1:
            if hp == 0:
                entry5.react_print()
                return True

        return False
entry5=Entry5("最终防线",
              "护盾被清空则失败",
              ["","护盾被清空则失败"],
              [0,50])

class Entry6(Entry_general):#灯塔已灭 已整理好
    
    def react(self,mode,cure):

        if (mode in mode_list) and probability(self.rank*0.2):
            self.react_print()
            return cure-1
        else:
            return cure
entry6=Entry6("灯塔已灭",
              "阻遏我方的上盾",
              ["","我方任何护盾回充均有20%概率-1","我方任何护盾回充均有40%概率-1"],
              [0,30,50])

class Entry7(Entry_general):#铁城 已整理好

    def react(self,mode):
        if mode in mode_list:
            if self.rank == 1:
                self.react_print()
                return 3
            elif self.rank == 2:
                self.react_print()
                return 6
        return 0
entry7=Entry7("铁城",
              "增加敌方初始护盾量",
              ["","敌方初始护盾+3","敌方初始护盾+6"],
              [0,60,100])

class Entry8(Entry_general):#滋生 已整理好
    def react(self,mode):
        if (mode in mode_list) and probability(entry8.rank*0.2):  
            self.react_print()
            return 1
        return 0 
entry8=Entry8("滋生",
              "在我方上盾时，概率使敌方护盾增加",
              ["","我方回盾时有20%概率使敌方护盾+1","我方回盾时有40%概率使敌方护盾+1"],
              [0,30,50])

class Entry9(Entry_general):#极限爆发 已整理好
    pass
entry9=Entry9("极限爆发",
              "敌方最后一层护盾被攻破时，对我方造成伤害",
              ["","敌方最后一层护盾被攻破时，对我方造成1伤害","敌方最后一层护盾被攻破时，对我方造成2伤害"],
              [0,30,60])

class Entry10(Entry_general):#烛燃 已整理好
    def react(self,mode):
        if (mode in mode_list) and probability(entry10.rank*0.3):
            self.react_print()
            return 1
        return 0
entry10=Entry10("烛燃",
              "敌方上弹时有概率额外装填一枚",
              ["","敌方上弹时有30%概率额外装填一枚","敌方上弹时有60%概率额外装填一枚"],
              [0,40,80])

class Entry11(Entry_general):#反冲锋 已整理好
    pass
entry11=Entry11("反冲锋",
                "使敌方行动概率增加",
                ["","使敌方行动概率增加10%","使敌方行动概率增加20%"],
                [0,30,60])

class Entry12(Entry_general):#海啸 已整理好

    def react(self,mode,miss):
        if (mode in mode_list) and probability(self.rank*0.2) and miss>0:
            self.react_print()
            return miss-1
        return miss
entry12=Entry12("海啸",
                "敌方攻击将拆除我方导弹",
                ["","大于一的敌方攻击有20%拆除我方导弹","大于一的敌方攻击有40%拆除我方导弹"],
                [0,30,60])

class Entry13(Entry_general):#压境 已整理好

    def react(self,mode,days)->int:
        if (mode in mode_list) and self.rank != 0 and days>100-20*self.rank:
            self.react_print()
            return 1
        return 0
entry13=Entry13("压境",
                "战斗将拥有时间限制",
                ["","天数大于80时每天造成1伤害","天数大于60时每天造成1伤害"],
                [0,40,70])

class Entry14(Entry_general):#狂怒 已整理好
    
    def react(self,mode,miss):
        if (mode in mode_list) and self.rank != 0:
            if miss>3 and self.rank == 1 or miss>2 and self.rank == 2:
                self.react_print()
                return 2
        return 1

entry14=Entry14("狂怒",
                "敌方导弹充足时可以连续发射导弹",
                ["","敌方导弹大于3时连续发射两枚导弹","敌方导弹大于2时连续发射两枚导弹"],
                [0,40,70])

class Entry15(Entry_general):#衰退 已整理好
    
    def react(self,t,mode):
        if mode in mode_list:
            if self.rank == 1 and t == 0 or self.rank == 2 and t != 2:
                self.react_print()
                return 1
        return 2

entry15=Entry15("衰退",
                "迷途旅人提供的护盾减少",
                ["","在第3天接迷途旅人提供的护盾减少一点","在第2，3天接迷途旅人提供的护盾减少一点"],
                [0,20,40])

class Entry16(Entry_general):#掣肘 已整理好
    choilist=[]
    def preset(self,choi,mode,skin_list:list[int]):
        if mode in mode_list and self.rank != 0:
            self.choilist:list[int]=random.sample(choi,5-self.rank)
            choilist_for_print = []
            for i in self.choilist:
                if mode == 6 and i not in [0,1,2]:
                    choilist_for_print.append(skin_list[i].replace(skin_list[i][skin_list[i].find("/")+1],["0","1","2","q","w","e"][choi.index(i)]))
                else: 
                    choilist_for_print.append(skin_list[i])
            print(f"本次可选项：{choilist_for_print+['f']}")

    def react(self,i):
        if self.choilist!=[] and i not in self.choilist + [str(j) for j in self.choilist]:
            self.react_print()
            self.choilist=[]
            return True
        self.choilist=[]
        return False

entry16=Entry16("掣肘",
                "限制航行日行动类型",
                ["","每我方航行日给出四个可选项，选择可选项之外的行动受到一伤害","航行日可选项减少至三个"],
                [0,40,70])

class Entry17(Entry_general):#涅槃 
    reborn=0
    def preset(self,mode):
        if mode in mode_list and self.rank != 0:
            self.reborn=1
            return 1
        return 0
    
    def react(self,cs):
        if self.reborn==1 and cs<0:
            self.reborn=0
            self.react_print()
            return 3
        return cs
    
entry17=Entry17("涅槃",
                "敌方可以复活",
                ["","敌方开局护盾减少1，但第一次死亡后以3护盾复活"],
                [0,80])

class Entry_manager:

    total_points=0
    mode_list=[1,2,5]
    def __init__(self):
        self.en_num=m1.max_index_finder(globals(),"entry")

    def entry_choose(self,depth,inf):
        self.refresh()
        goal=(depth*2+inf//5+1)*120
        box=[1,3,4,6,8,9,10,5,11,12,13,14,15,16,17]#删除了战场迷雾
        if depth>=1:
            box.append(7)
        while self.total_points<goal:
            entry=random.choice(box)
            box.remove(entry)
            entry_temp:Entry_general=globals()[f"entry{entry}"]
            for i in range(len(entry_temp.points_list)):
                entry_temp.rank=i
                entry_manager.points_count()
                if entry_manager.total_points>=goal:
                    break
            if box == []:
                break
    
    def sync_entry(self,username):
        sf=shelve.open("savedata")
        pre_entry={}
        for i in range(0,self.en_num):
            if f"entry{i}" in globals():
                pre_entry[i]=globals()[f"entry{i}"].rank    
            else:
                pre_entry[i]=0
        sf[username+"entry"]=pre_entry
        sf.close()

    def loadentry(self,username):
        sf=shelve.open("savedata")
        for i in range(0,self.en_num):
            try:
                globals()[f"entry{i}"].rank=sf[f"{username}entry"][i]
            except:
                pass
        sf.close()

    def points_count(self):
        self.total_points=0
        for i in range(1,self.en_num):
            try:
                entry_temp:Entry_general=globals()[f"entry{i}"]
                self.total_points+=entry_temp.points_list[entry_temp.rank]
            except:
                pass

    def print_all(self):


        left = []
        right = []

        for j in [globals()[f"entry{i}"].description_tree().linelist() for i in range(1,self.en_num,2)]:
            left += j
        for j in [globals()[f"entry{i}"].description_tree().linelist() for i in range(2,self.en_num,2)]:
            right += j

        m1.n_columnprint([left,right],70)

        

    def print_now(self):


        output_list=[]

        self.points_count()
        for i in range(1,self.en_num):
            try:
                entry_temp:Entry_general=globals()[f"entry{i}"]
                if entry_temp.rank != 0:
                    output_list.append(f"[{i}]{entry_temp.title}{entry_temp.rank_list[entry_temp.rank]}:{entry_temp.rank_description[entry_temp.rank]} [{entry_temp.points_list[entry_temp.rank]}分]")
            except:
                pass
        if output_list == []:
            entry_tree=Tree("当前词条","（无）")
        else:
            entry_tree=Tree(f"当前词条·总分{self.total_points}",output_list)
        entry_tree.treeprint()

    def tree(self):


        output_list=[]
        
        self.points_count()
        for i in range(1,self.en_num):
            try:
                entry_temp:Entry_general=globals()[f"entry{i}"]
                if entry_temp.rank != 0:
                    output_list.append(f"[{i}]{entry_temp.title}{entry_temp.rank_list[entry_temp.rank]}:{entry_temp.rank_description[entry_temp.rank]} [{entry_temp.points_list[entry_temp.rank]}分]")
            except:
                pass
        if output_list == []:
            entry_tree=Tree("战死之地>当前选择的词条","（无）")
        else:
            entry_tree=Tree(f"战死之地>当前选择的词条 [总分:{self.total_points}]",output_list)
        return entry_tree

    def refresh(self):
        for i in range(1,self.en_num):
            try:
                globals()[f"entry{i}"].rank=0
            except:
                pass
        self.total_points=0

    def ask(self,username):
        while 1:
            print()
            entry_manager.print_all()
            entry_manager.print_now()
            print()
            inp=m1.inputplus("请输入要修改或加入的词条·输入回车退出·输入0清空词条·输入all选择所有词条>>>")
            if inp == "0":
                for i in range(1,self.en_num):
                    try:
                        globals()[f"entry{i}"].rank=0
                    except:
                        pass
                m1.printplus("词条已清空")
                self.sync_entry(username)
                continue
            if inp == "all":
                for i in range(1,self.en_num):
                    try:
                        entry_tep:Entry_general=globals()[f"entry{i}"]
                        entry_tep.rank=len(entry_tep.points_list)-1
                    except:
                        pass
                m1.printplus("词条已选择")
                self.sync_entry(username)
                continue
            try:
                entry_temp:Entry_general=globals()[f"entry{inp}"]
                print()
                print(f"[{inp}]“{entry_temp.title}”：{entry_temp.description}")
                for j in range(1,len(entry_temp.rank_description)):
                    print("|")
                    print(f"|-[{entry_temp.rank_list[j]}] {entry_temp.rank_description[j]} [{entry_temp.points_list[j]}分]")
                print()
                globals()[f"entry{inp}"].rank=int(m1.inputplus("输入1，2，……来选定词条难度·输入0删除词条>>>"))
            except:
                m1.printplus("正在退出")
                self.sync_entry(username)
                break
entry_manager=Entry_manager()
        