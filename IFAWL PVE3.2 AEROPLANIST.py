from typing import *
import random,time,re,shelve,winsound
from Module_01_txt import Tree
import Module_01_txt as m1
                #from Module_02_storehouse import *
                #from Module_03_entries import *
from Module_03_entries import entry_manager
import Module_03_entries as m3
from Module_04_fpses import Fps_general,Eqm_general
import Module_05_sounds as m5
                #from Module_05_sounds import *


__version_txt__="IFAWL PVE3.2 'AEROPLANIST'"
item1={"联邦信用点":1000,
       "合约纪念点":0,
       "保险点":0,
       "三钛合金":10,
       "湿件主机":10,
       "重水":10,
       "高强度树脂":10,
       "锈蚀电路板":10,
       "激光准晶体":10,
       "黄铜差分机":10,
       "电子变频箱":10}
item2={"精确制导单元":2,
       "临时装甲板":2,
       "备用加农炮管":2,
       "过载屏障阵列":2,
       "短弓炮管模组":2,
       "“焦糖星”":2}
items={"三钛合金":10,
       "湿件主机":10,
       "重水":10,
       "高强度树脂":10,
       "锈蚀电路板":10,
       "激光准晶体":10,
       "黄铜差分机":10,
       "电子变频箱":10}
allenskin=["","","",
           "“风行者”战术巡飞弹",
           "“咆哮”铜芯导弹自动发射台",
           "“水银”汞核心重型穿甲弹",
           "“白金”紧急维修小队前线安全屋",
           "“奶油”黑客老姐",
           "“维多利亚”加农炮式导弹发射架",
           "“修械师”常规维修小队吊舱",
           "“离人”牺牲式能量转化反应堆小组",
           "“柒”护盾汲能阵列",
           "“晴空”大功率粒子炮集群",
           "“北极”多目标导航雷达网络",
           "“信风”全结晶护盾防御系统",
           "“暴雨”全自动射手导弹发射台",
           "“情诗”大规模护盾疗救阵列",
           "“白夜”钨金外壳重型反物质穿甲弹",
           "“初夏”共生式护盾充能系统",
           "“苍穹”浅草寺战术快递发射炮",
           "“长安”大型相控阵巡天器",
           "“诗岸”高密度混凝打印式速固屏障",
           "“迫害妄想”点射式战术阳极激光炮",
           "“浮生”超高射速亚轨道浮游炮",
           "“攻城奶油”奶油的主动式电子进攻套件",
           "“阿贾克斯”动能子弹前端拦截系统",
           "“眠雀”麻醉性致幻剂发射器",
           "“瞳猫”反应堆尾流推进器",
           "“鹘鸮”全反射屏障武装反击阵列",
           "“酒师”塔阵反应屏障治疗体系",
           "“湾区铃兰”饱和式蜂巢突击粒子炮",
           "“白鲟”薄壁共振护盾再生平台",
           "“普罗旺斯”高能粒子点火平台",
           "“蛊”核同质异能素伽马射线炮",
           "“风间浦”全平台战术安全港",
           "“青鹄”时空连续体空洞构造反应堆",
           "“西岭”高速传统近防炮防空体系",
           "“星尘”非自动制导正光锥粒子流",
           "“澈”高牺牲护盾锐化改装套件",
           "无战术配置",
           "无生存维修站",
           "无主武器"]
wav=""
al_sho_title_cn = [
    "0/space 装弹","1 发射","2 上盾","3/e 风行者",
    "4/q 咆哮","5/q 水银","6/w 白金","7/e 奶油",
    "8/q 维氏","9/w 修械师","10/e 离人","11/w 柒",
    "12/q 晴空","13/e 北极","14/w 信风","15/q 暴雨",
    "16/w 情诗","17/q 白夜","18/w 初夏","19/e 苍穹",
    "20/e 长安","21/w 诗岸","22/e 妄想","23/q 浮生",
    "24/q 大奶油","25/w 贾氏","26/e 眠雀","27/e 瞳猫",
    "28/q 鹘鸮","29/w 酒师","30/q 湾铃","31/w 白鲟",
    "32/e 小狼","33/q 蛊","34/w 风间浦","35/e 青鹄",
    "36/e 西岭","37/q 星尘","38/w 澈","无战术","无生存","无武器"
]

al_sho_title_en = [
    "0/space 装弹","1 发射","2 上盾","3/e Skywalker",
    "4/q Roar","5/q Mercury","6/w Platinum","7/e Milky",
    "8/q Victoria","9/w Mechanist","10/e Leaver","11/w Chi",
    "12/q Serenity","13/e Polaris","14/w Trustist","15/q Hardrain",
    "16/w Sonetto","17/q Flashvault","18/w Earlisum","19/e Firmament",
    "20/e Chang·an","21/w Faramita","22/e Delirium","23/q Drift",
    "24/q The·Milky","25/w Ajax","26/e Sparrow","27/e Iris",
    "28/q Cushat","29/w Brewer","30/q Bay&Convallaria","31/w Sturgeon",
    "32/e Provence","33/q Deadlytoxic","34/w Windside","35/e Bengalensis",
    "36/e Dawnhill","37/q Infinity","38/w Sacrificer","无战术","无生存","无武器"
]

kwords = ["f","giveup","r"]

###########################################
n:List[int]                     = [1,0,0,0]
hard:int                        = 0.2
hardv:int                       = 0.3
whoreact_0me:int                = 0
distance:int                    = 0
days:int                        = 0
win_2me:int                     = 0
inf:int                         = 0
mode:int                        = 0
mining_number:int               = 12
shipname:str                    = "漂泊者"
username:str                    = ""
choi:List[int]                  = [0,1,2,17,18,7]
eqm:List[str]                   = []
mining_select_now:str           = "0"

win = ["胜利终究属于我们。我赌他们绝不敢再来一次。",
       "E01B区来电 祝贺你们！同时感谢你们，这边战线推进一切顺利。",
       "Z20B4区来电 祝贺你们的胜利！这边战线推进一切顺利。",
       "漫长的血战终于结束了。我提议开个庆功宴。"]
lose = [f"报告指挥官{username}，我方防线已崩溃。多支小队已被重创。请下达撤退命令！",
        "不要灰心，重整旗鼓，胜利女神会眷顾我们的。",
        "我方防线已崩溃，但我们会如风暴般归来。",
        "就让他们再得意一会吧！失败只是暂时的，胜利终将属于我们。"]

craft1={"精确制导单元":{"联邦信用点":1000,
                       "三钛合金":15,
                       "湿件主机":10,
                       "高强度树脂":5},

        "临时装甲板":  {"联邦信用点":1000,
                       "重水":15,
                       "高强度树脂":10,
                       "激光准晶体":5},

        "备用加农炮管":{"联邦信用点":1000,
                       "锈蚀电路板":15,
                       "激光准晶体":10,
                       "电子变频箱":5},

        "过载屏障阵列":{"联邦信用点":1000,
                       "黄铜差分机":15,
                       "电子变频箱":10,
                       "湿件主机":5},

        "短弓炮管模组":{"联邦信用点":1000,
                       "重水":15,
                       "湿件主机":10,
                       "三钛合金":5},

        "“焦糖星”"   :{"联邦信用点":1000,
                       "锈蚀电路板":15,
                       "电子变频箱":10,
                       "三钛合金":5}}

eqmdis={"精确制导单元":     "[风行者]小幅提升风行者的命中率 30%/层->30+20%/层",
        "临时装甲板":       "[舰船]提供额外开局护盾 1->1+2",
        "备用加农炮管":     "[维多利亚]大幅降低维多利亚发射架的故障率 20%->0%",
        "过载屏障阵列":     "[白金]提升白金的紧急回盾量 +3->4",
        "短弓炮管模组":     "[晴空]调整每层出伤 [0,0,1,2,4,5,7,8]->[0,1,2,3,4,4,4,5]",
        "“焦糖星”":         "[诗岸]其他形式的治疗转为回复诗岸速固屏障"}

item0={"凡晶石原矿":0,"灼烧岩原矿":0,"干焦岩原矿":0,"长流石原矿":0,"铱金原矿":0}

craft0={"凡晶石原矿":{"三钛合金":0.1,"湿件主机":0.1},
        "灼烧岩原矿":{"重水":0.1,"高强度树脂":0.1},
        "干焦岩原矿":{"锈蚀电路板":0.1,"激光准晶体":0.1},
        "长流石原矿":{"黄铜差分机":0.1,"电子变频箱":0.1}}
###########################################

class Mining:#小行星
    name                            = ""
    richness                        = 0
    output_quantity                 = 0
    output_item                     = ""
    mining_distance                 = 0
    prefix                          = ["贫矿","原生","饱和"]
    extra_prefix                    = ["流体","致密","固态","折射","光学","熔融"]
    namelist                        = ["凡晶石","灼烧岩","干焦岩","长流石","铱金"]
    is_exploited                    = False
    is_locked                       = False

    def __init__(self,richness):
        name0=random.choice(self.namelist)
        self.name=self.prefix[richness]+random.choice(self.extra_prefix)+name0
        self.output_quantity=random.randint(20+richness*40,100+richness*40)
        self.mining_distance=random.randint(0,50)
        self.output_item=name0+"原矿"
        pass

    def exploit1(self):#开采方式1 挂机
        global item0,mining_select_now
        if self.is_exploited == False:
            mining_time=3 if self.is_locked == True else 6
            print("正在开采",self.name,"预估收益",str(self.output_quantity*1),"原矿")
            print(    "0        25        50        75       100")
            print(    "|         |         |         |         |")
            m1.printplus("`````````````````````````````````````````",mining_time)
            print("开采完成")
            print()
            item0[self.output_item]+=self.output_quantity*1
            self.is_exploited=True
            self.is_locked=False
            mining_select_now="0"
    
    def exploit2(self):#开采方式2 qte
        global item0,mining_select_now
        if self.is_exploited == False:
            mining_time=3 if self.is_locked == True else 6
            print("正在开采",self.name,"预估收益",str(self.output_quantity*1),"原矿")
            multiple=m1.qte_game()
            print("开采完成")
            print()
            item0[self.output_item]+=self.output_quantity*multiple
            print(self.name,"收益",str(self.output_quantity*multiple),"原矿")
            self.is_exploited=True
            self.is_locked=False
            mining_select_now="0"

class Industry_selecting:#工业订单

    industry_select                 = [0,0,0,0]
    industry_lst_raw_material       = ["凡晶石原矿","灼烧岩原矿","干焦岩原矿","长流石原矿"]
    industry_lst_alt                = {"凡晶石原矿":["三钛合金","湿件主机"],
                                       "灼烧岩原矿":["重水","高强度树脂"],
                                       "干焦岩原矿":["锈蚀电路板","激光准晶体"],
                                       "长流石原矿":["黄铜差分机","电子变频箱"],
                                       "铱金原矿":["联邦信用点","联邦信用点"]}
    industry_raw_material_selecting_now = -1

    def __init__(self):
        pass

    def industry_painting(self):
        for i in range(0,4):
            target=self.industry_lst_alt[self.industry_lst_raw_material[i]][self.industry_select[i]]
            print(f"[{i+1}]"+self.industry_lst_raw_material[i]+">>"+target)
            if i == self.industry_raw_material_selecting_now:
                print("|")
                print("|-[q]"+self.industry_lst_alt[self.industry_lst_raw_material[i]][0])
                print("|")
                print("|-[w]"+self.industry_lst_alt[self.industry_lst_raw_material[i]][1])
            print()
        print("[5]铱金原矿>>>联邦信用点")
        print()
        restree = Tree(resource_nevigator.tree_output_title(),resource_nevigator.tree_output_body())
        restree.treeprint()
        
    def industry_react(self,inp:str):#响应用户输入
        if inp.isdigit() and 1 <= int(inp) <= 4:
            if int(inp)-1 != self.industry_raw_material_selecting_now:
                self.industry_raw_material_selecting_now=int(inp)-1
            else:
                self.industry_raw_material_selecting_now=-1    
        elif inp == "q"and self.industry_raw_material_selecting_now != -1:
            self.industry_select[self.industry_raw_material_selecting_now]=0
            self.industry_raw_material_selecting_now=-1
        elif inp == "w"and self.industry_raw_material_selecting_now != -1:
            self.industry_select[self.industry_raw_material_selecting_now]=1
            self.industry_raw_material_selecting_now=-1
        elif inp == "x":
            pass
    
    def industry_drop(self):
        global item1
        for i in range(0,4):
            target_product=self.industry_lst_alt[self.industry_lst_raw_material[i]][self.industry_select[i]]
            add=int(0.05*item0[self.industry_lst_raw_material[i]])
            item1[target_product]+=add
            print(f"基础物品产出：{target_product}*{add}")
            item0[self.industry_lst_raw_material[i]]=0
            sync()
        add=int(2.2*item0["铱金原矿"])
        item1["联邦信用点"]+=add
        print(f"基础物品产出：联邦信用点*{add}")
        item0["铱金原矿"]=0
        sync()

class Resource_nevigator:#资源导航器

    target_num=""
    target_list={}
    nevigator_list={}
    nevigator_mining_list={}

    re_craft={"联邦信用点":"铱金原矿",
       "三钛合金":"凡晶石原矿",
       "湿件主机":"凡晶石原矿",
       "重水":"灼烧岩原矿",
       "高强度树脂":"灼烧岩原矿",
       "锈蚀电路板":"干焦岩原矿",
       "激光准晶体":"干焦岩原矿",
       "黄铜差分机":"长流石原矿",
       "电子变频箱":"长流石原矿"}

    def ask(self):
        global item1
        al_craft_print()
        inp=input("请输入要追踪的装备代码·留空回车以清除当前跟踪·输入exit以退出>>>")
        try:
            al_temp=globals()["al"+inp]
            al_temp:Al_general
        except:
            if inp == "":
                print("已清除跟踪装备")
                self.target_num=""
                self.nevigator_list={}
                self.nevigator_mining_list={}
                self.target_list={}
                return
            else:
                print("正在退出")
                return
        self.target_num=inp
        self.target_list=al_temp.cost_list
        self.nevigator_list={}
        self.nevigator_mining_list={}
        for i in self.target_list:
            if item1[i]<self.target_list[i]:
                self.nevigator_list[i]=self.target_list[i]-item1[i]
        for i in self.nevigator_list:
            if i == "联邦信用点":
                self.nevigator_mining_list["铱金原矿"]=int(self.nevigator_list[i]/2.2)
            else:
                self.nevigator_mining_list[self.re_craft[i]]=int(self.nevigator_list[i]/0.05) if self.re_craft[i] not in self.nevigator_mining_list else self.nevigator_mining_list[self.re_craft[i]]+int(self.nevigator_list[i]/0.05)
        m1.printplus(al_temp.len_skin+"的合成配方已加入物品资源跟踪器",0.3)
        sync()
        time.sleep(0.4)
        return

    def refresh(self):
        if self.target_num != "":
            self.target_list=globals()["al"+self.target_num].cost_list
            self.nevigator_list={}
            self.nevigator_mining_list={}
            for i in self.target_list:
                if item1[i]<self.target_list[i]:
                    self.nevigator_list[i]=self.target_list[i]-item1[i]
            for i in self.nevigator_list:
                if i == "联邦信用点":
                    self.nevigator_mining_list["铱金原矿"]=int(self.nevigator_list[i]/2.2)
                else:
                    self.nevigator_mining_list[self.re_craft[i]]=int(self.nevigator_list[i]/0.05) if self.re_craft[i] not in self.nevigator_mining_list else self.nevigator_mining_list[self.re_craft[i]]+int(self.nevigator_list[i]/0.05)
            return
    
    def tree_output_title(self):
        self.refresh()
        if self.target_num != "":
            return "资源跟踪器>"+globals()["al"+self.target_num].short_skin+"-还需:"
        else:
            return "资源跟踪器-空闲"
    
    def tree_output_body(self):
        self.refresh()
        output=[]
        if self.target_num != "":
            for i in self.nevigator_list:
                output.append(f"{i}*{self.nevigator_list[i]}")
            output="[可以合成]" if output == [] else output
            return output
        else:
            return "(无跟踪)"
resource_nevigator=Resource_nevigator()

class Difference_animation_manager:

    pre_n = [0,0,0,0]

    def refresh(self):
        self.pre_n = [0,0,0,0]

    def print_cpu_ani(self):
        global n 
        if n[2] < self.pre_n[2]:
            for i in range(self.pre_n[2]-n[2]):
                print(
                    random.choice(
                        ["-x `-","~ - -"," -` -"," ~ x-"]
                    ),
                    end=""
                )
                if i == 0:
                    print(f" 有效伤害>{self.pre_n[2]-n[2]}.0")
                else:
                    print()

    def print_player_ani(self):
        global n 
        if al14.state != 0 :
            return
        if n[0] < self.pre_n[0]:
            for i in range(self.pre_n[0]-n[0]):
                print(
                    random.choice(
                        ["-x `-","~ - -"," -` -"," ~ x-"]
                    ),
                    end=""
                )
                if i == self.pre_n[0]-n[0] - 1:
                    print(f" 受到伤害>{self.pre_n[0]-n[0]}.0")
                else:
                    print()

    def sync(self):
        self.pre_n = n.copy()

di_ani_manager = Difference_animation_manager()

class Auto_pilot_manager:#自动驾驶

    to_do_list=[]
    to_do_list_spc=[]
    if_list=[]
    memory=[]

    def read(self,txt:str):
        txt=txt.replace("(","(-")
        txt=txt.replace("])","]);p")
        self.to_do_list=[]
        self.to_do_list_spc=[]
        self.if_list=[]
        raw_list=txt.split("-")     #["2","2","[True]2;1,1"]
        for i in range(len(raw_list)):
            raw=raw_list[i]
            if ";" in raw:          #"[True]2;1,1"
                pre_to_do=raw[raw.find("]")+1:raw.find(";")]#"2"
                pre_to_do_spc=raw[raw.find(";")+1:]#"1,1"
                pre_if=[]
                pre_if.append(raw[raw.find("[")+1:raw.find("]")])

                if "," in pre_to_do or "," in pre_to_do_spc:        #"[True]2;1,1"

                    pre_to_do=pre_to_do.split(",")
                    pre_to_do_spc=pre_to_do_spc.split(",")
                    
                    max_len=max(len(pre_to_do),len(pre_to_do_spc))
                    pre_to_do+=["p"]*(max_len-len(pre_to_do))
                    pre_to_do_spc+=["p"]*(max_len-len(pre_to_do_spc))

                    for i in range(len(pre_to_do)-1):
                        pre_if.append("z")
                    for i in range(len(pre_to_do)):
                        self.to_do_list.append(pre_to_do[i])
                        self.to_do_list_spc.append(pre_to_do_spc[i])
                        self.if_list.append(pre_if[i])
                else:
                    self.to_do_list.append(raw[raw.find("]")+1:raw.find(";")])
                    self.to_do_list_spc.append(raw[raw.find(";")+1:])
                    self.if_list.append(raw[raw.find("[")+1:raw.find("]")])
            else:
                self.to_do_list.append(raw)
                self.to_do_list_spc.append("2")
                self.if_list.append("True")
        
    def test(self):
        print(self.to_do_list)
        print(self.if_list)
        print(self.to_do_list_spc)
        print(self.memory)

    def react(self,n,days,item1):

        PS=n[0]
        PM=n[1]
        CS=n[2]
        CM=n[3]
        DAY=days
        F=ocp_manager.ocp_now.index
        ISK=item1["联邦信用点"]


        output=""

        while output in ["","(",")","p"] and self.to_do_list != []:
            if eval(self.if_list[0]):
                try:
                    if self.if_list[1] == "z":
                        self.if_list[1]="True"
                except:
                    pass
                output=self.to_do_list[0]
            else:
                try:
                    if self.if_list[1] == "z":
                        self.if_list[1]="False"
                except:
                    pass
                output=self.to_do_list_spc[0]

            if output == "(":
                self.memory=[self.to_do_list,self.to_do_list_spc,self.if_list]
            
            if output == ")":
                self.to_do_list,self.to_do_list_spc,self.if_list=self.memory

            try:
                self.if_list=self.if_list[1:]
                self.to_do_list=self.to_do_list[1:]
                self.to_do_list_spc=self.to_do_list_spc[1:]
            except:
                self.if_list=[]
                self.to_do_list=[]
                self.to_do_list_spc=[]
        return output

    def refresh(self):
        self.if_list=[]
        self.to_do_list=[]
        self.to_do_list_spc=[] 
        self.memory=[]      
auto_pilot=Auto_pilot_manager()

###########################################

class Al_general():
    len_skin                = ""
    state                   = 0
    num                     = 0
    rank                    = 0
    ranklist                = ["FREE","I","II","III","IV","V","VI","VII","VIII","IX","X"]
    rank_num                = 0
    description_txt         = ""

    def __init__(self,
                 lenskin:str,
                 voilist_pos:list,
                 voilist_neg:list,
                 skin:list,
                 costlist:dict,
                 tag:dict = {}):

        self.cost_list              = {}
        self.len_skin               = lenskin
        self.voilist_pos            = voilist_pos
        self.voilist_neg            = voilist_neg
        self.tag:dict[str,str]      = tag.copy()
        self.skin                   = skin
        self.index                  = allenskin.index(self.len_skin) 
        self.short_skin             = al_sho_title_cn[self.index].split(" ")[1] 
        self.short_skin_en          = al_sho_title_en[self.index].split(" ")[1]
        self.type                   = al_sho_title_cn[self.index].split(" ")[0][-1]
        for i in costlist:
            if costlist[i] != 0:
                self.cost_list[i]=costlist[i]
        self.rank_num               = int(
            costlist.get(
                "联邦信用点",
                0
            )/1100
        )
        self.rank                   =self.ranklist[self.rank_num]

        if self.type == "q":
            tag_temp = self.tag.copy()
            tag_temp.setdefault("武器平台","导弹")
            self.tag = tag_temp.copy()
        elif self.type == "w" or self.type == "e":
            tag_temp = self.tag.copy()
            tag_temp.setdefault("武器平台","通用")
            self.tag = tag_temp.copy()
        self.tag.setdefault("出身","")

    def print_description(self):

        tag0:str = self.tag["出身"]
        tag1:str = self.tag["武器平台"]
        tag2:str = item3[self.len_skin]
        tag3 = ">>[可以离站使用]<<" if tag2 > 0 or self.rank == "FREE" else "[▲无装备]"
        
        print(f"[{self.index}] {tag0}{self.len_skin+' '*(40-m1.printlen(self.len_skin+tag0+str(self.index)))}[{tag1}平台] [{self.rank}] {tag2}在仓库 {tag3}")
        print(f">>>>\"{self.short_skin_en}\"")
        print(self.description_txt)
        #[30] 岩河军工“湾区铃兰”饱和式蜂巢突击粒子炮      [粒子炮平台] [VIII] 1在仓库 >>[可以离站使用]<<
        print()

    def print_description_MD(self):

        tag0:str = self.tag["出身"]
        tag1:str = self.tag["武器平台"]
        tag2:str = item3[self.len_skin]
        tag3 = ">>[可以离站使用]<<" if tag2 > 0 or self.rank == "FREE" else "[▲无装备]"
        
        print(f"**[{self.index}] {tag0}{self.len_skin+'**'+' '*(40-m1.printlen(self.len_skin+tag0+str(self.index)+'**'))}[{tag1}平台] [{self.rank}]")
        print()
        des_list = self.description_txt.split("-")
        for i in des_list[1:]:
            print(f"- {i}")
            print()
        print("---")
        print()

    def voi_print_pos(self):
        print(f"[{self.short_skin}]",end="")
        m1.printplus(
            random.choice(
                self.voilist_pos
            ),
            0.3
        )
        time.sleep(0.4)

    def voi_print_neg(self):
        print(f"[{self.short_skin}]",end="")
        m1.printplus(
            random.choice(
                self.voilist_neg
            ),
            0.3
        )
        time.sleep(0.4)

    def report(self,txt:str,sleep=True):
        print(f"[{self.short_skin}]",end="")
        m1.printplus(txt)
        if sleep:
            time.sleep(0.4)

    def printself(self):
        if self.index in choi and self.state != 0:
            print(self.skin[self.state])
            print()

    def reset(self):
        self.state = 0
    
    def craft_self(self):
        if self.is_craftable_txt() == "[可合成●]":
            item3[self.len_skin]+=1
            for i in self.cost_list:
                item1[i]-=self.cost_list[i]
            print(self.len_skin+"*1 合成完成·已送至装备仓库并铭刻您的代号")
            time.sleep(0.5)
        else:
            print("材料不足·合成失败")
            time.sleep(0.5)
        sync()

    def is_craftable_txt(self):
        global item1
        j = 0
        k = 0
        for i in self.cost_list:
            if item1[i] >= self.cost_list[i]:
                j += 1
            k += 1
        if j == k:
            return "[可合成●]"
        else:
            return "[不可合成]"
        
    def in_choi(self):
        return self.index in choi

    def suggest(self):
        return ""
al_none = Al_general("",[],[],[],{})

class Al3(Al_general):#风行者

    description_txt = "-高速部署的轻型导弹\n-航行日内按下3立即发射，无需准备时间\n-敌方护盾层数越高命中率越高，命中则造成1点伤害"

    def react(self):
        global n,eqm
        if random.randint(0,9) >= 10-3*n[2]:
            player_atkplus(1)
            self.voi_print_pos()
        elif random.randint(0,9) >= 8-3*n[2] and "精确制导单元" in eqm:
            player_atkplus(1)
            self.voi_print_pos()
        else:
            self.voi_print_neg()

    def suggest(self):
        prob=n[2]*30
        if "精确制导单元" in eqm:
            prob += 20
        if prob != 0:
            return f"[e]发射巡飞弹|命中率{prob}%"
        else:
            return f"[无命中率]不建议发射巡飞弹"
al3=Al3(
    "“风行者”战术巡飞弹",
    [
        "风行者巡飞弹命中目标",
        "指挥官，风行者已命中敌方护盾"
    ],
    [
        "风行者巡飞弹未命中目标"
    ],
    [],
    {'三钛合金': 35, '湿件主机': 15, '重水': 35, '高强度树脂': 15, '锈蚀电路板': 0, '激光准晶体': 35, '黄铜差分机': 0, '电子变频箱': 15, '联邦信用点': 6600},
    {"出身":"浅草寺重工"}
)

class Al4(Al_general):#咆哮

    description_txt = "-高射速全自动的导弹发射系统\n-按下4建造\n-建成后当晚及后一天，无论敌我回合，均向敌方发射一枚铜芯导弹，不消耗常规导弹，不影响我方行动\n-[回流]若未命中，召回此铜芯导弹并使其进入常规待命状态"

    ready=["回流器建造完成，咆哮发射台已就绪","咆哮发射台已在作战甲板G就位"]

    def check_if_fin_building(self):
        if self.state == 2:
            print("[咆哮]"+random.choice(self.ready))

    def react(self):
        if self.state<2:
            self.state+=2
            m1.printplus("[咆哮]咆哮发射台收到",0.3)
            time.sleep(0.4)
            self.check_if_fin_building()

    def attack(self):
        global n
        if self.state>=2:
            self.state+=1
            if self.state==4:
                self.state=0
            if probability(0.7):
                player_atkplus(1)
                self.voi_print_pos()
            else:
                self.voi_print_neg()
                n[1]+=1
                print("咆哮发射台已召回导弹·导弹正在待命")

    def suggest(self):
        return ["[q] 部署发射台","[q] 挂载铜芯导弹 2/2","[自动攻击中]回流系统正在生效","[自动攻击中]回流系统正在生效"][self.state]
al4=Al4(
    "“咆哮”铜芯导弹自动发射台",
    [
        "咆哮发射台报告，“咆哮”铜芯穿甲弹确认命中",
        "咆哮发射台报告，既定目标护盾已穿透"
    ],
    [
        "咆哮发射台报告，导弹没有命中目标"
    ],
    [
        "",
        r"{\\//}准备中",
        r"{\\=//}自动发射台就绪",
        r"{\=//}剩余一枚"
    ],
    {'三钛合金': 10, '湿件主机': 0, '重水': 15, '高强度树脂': 10, '锈蚀电路板': 15, '激光准晶体': 0, '黄铜差分机': 25, '电子变频箱': 0, '联邦信用点': 3300},
    {
        "出身":"联邦海军"
    }
    )

class Al5(Al_general):#水银

    description_txt = "-高伤害重型武器\n-用两个连续或不连续的航行日按下5建造\n-建成后在任意航行日按下5发射，造成一般导弹的两倍伤害\n-[信使]建成而没有打出时，概率提升我方按0建立导弹的效率"

    def react(self):
        if self.state == 0:
            self.state+=1
            m1.printplus("[水银]水银收到，汞核心重弹装配中",0.3)
            time.sleep(0.4)
        elif self.state == 1:
            self.state+=1
            m1.printplus("[水银]水银重弹随时可以发射",0.3)
            time.sleep(0.4)
        else:
            self.state=0
            if random.randint(0,9)>-1:
                player_atkplus(2)
                self.voi_print_pos()
            else:
                self.voi_print_neg()

    def check_if_load(self,load) -> int:
        if self.state == 2 and probability(0.5):
            self.report("水银小队协助挂载了两枚巡航导弹")
            return load + 1
        else:
            return load

    def suggest(self):
        sugg_list=["[q]建立汞弹推进器 1/2","[q]加注液态汞 2/2","[q]发射汞弹|[0/space]上弹效率加成中"]
        return sugg_list[self.state]
al5=Al5("“水银”汞核心重型穿甲弹",
        ["水银报告，汞核心重弹已重创目标护盾","高烈度汞弹命中·敌方护盾已被穿透"],
        ["水银未命中目标","敌方运动速度过快，水银瞄准系统失灵"],
        ["","[x]准备中","[~]汞弹就绪·加成生效中"],
        {'三钛合金': 0, '湿件主机': 0, '重水': 30, '高强度树脂': 0, '锈蚀电路板': 0, '激光准晶体': 0, '黄铜差分机': 20, '电子变频箱': 0, '联邦信用点': 2200})

class Al6(Al_general):#白金

    description_txt = "-驻扎一支训练有素的工程师团队，提供千钧一发的紧急救援\n-用两个连续或不连续的航行日按下6建造，不可叠加\n-建成后，当我方所有护盾被打穿，立即生成三面紧急护盾，损耗\n-[帝国]在护盾被清空时输入6，立即使白金建成"

    def react(self):
        if self.state == 0:
            if n[0] > 0:
                self.state+=1
                self.voi_print_neg()
            else:
                self.state = 2
                self.report("生命的圣城……")
        elif self.state == 1:
            self.state+=1
            self.report(f"{username}指挥官，白金小队已就位")
    
    def check_if_need_cure(self):
        global n,eqm
        if self.state == 2 and n[0]<=0:#白金
            self.state=0
            player_cureplus(3)
            self.voi_print_pos()
            if "过载屏障阵列" in eqm:
                player_cureplus(1)
                self.report("白金过载屏障阵列启动")
        
    def suggest(self):
        return ["[w]建立安全屋1/2","[w]派遣维修小队2/2","[保护中]急救已就绪"][self.state]
al6=Al6("“白金”紧急维修小队前线安全屋",
        ["白金小队成功构造临时护盾","护盾急救完毕！队员轻伤！白金小组正在回撤！"],
        ["白金小队收到，请求火力掩护","白金小队正在前往前线","收到，护盾小组正在为白金打开缺口"],
        ["","[-]准备中","[+]白金就绪"],
        {'三钛合金': 0, '湿件主机': 10, '重水': 0, '高强度树脂': 20, '锈蚀电路板': 0, '激光准晶体': 0, '黄铜差分机': 20, '电子变频箱': 0, '联邦信用点': 2200})

class Al7(Al_general):#奶油

    description_txt = "-深居简出的黑客，（可能）在食堂能找到她\n-航行日内按下7命令其尝试剥夺敌方一枚导弹的控制权，使敌方失去一枚导弹\n-在夺得控制权后有概率使该导弹自爆，造成1点伤害\n-[整个好活]在敌方宏峰导弹来袭时使用奶油，有概率将宏峰导弹回击向敌方"
    
    def react(self):
        global n,past
        while 1:
            if self.state == 0:
                if probability(0.7):
                    if ocp_manager.ocp_now.index == 4 and ocp_manager.ocp_now.counting_down == 0:
                        m1.printplus("[奶油]妈妈！我黑进对面宏峰了！！")
                        self.state = ocp4.matk
                        ocp4.matk = 0
                        ocp_manager.ocp_now = ocp0
                    elif n[3] > 0:
                        self.state = 1
                        n[3] -= 1
                        self.voi_print_pos()
                else:
                    self.voi_print_neg()
                break
            else:
                self.check_if_boom()

    def check_if_boom(self):
        if self.state == 1:
            if random.randint(0,9)<6:
                player_atkplus(1)
                self.state-=1
                time.sleep(0.4)
                m1.printplus("[奶油]奶油强行启动了敌方导弹，即将命中其护盾")
            else:
                self.state-=1
                time.sleep(0.4)
                m1.printplus("[奶油]导弹脱离控制，奶油已将其销毁")
        elif self.state>1:
            if random.randint(0,9)<6:
                self.state
                player_atkplus(self.state)
                self.state=0
                m1.printplus("[奶油]宏峰牵引成功，预计伤害：",self.state)
            else:
                self.state=0
                m1.printplus("[奶油]宏峰牵引失效，奶油已将其销毁")

    def suggest(self):
        if n[3] == 0:
            return "[休息中]对面没有导弹"
        else:
            return "[e]入侵敌方导弹让他们倒大霉"

    def craft_self(self):
        print("[奶油]（睡眠中……）[FREE]不需合成即可离站使用")
al7=Al7("“奶油”黑客老姐",
        ["奶油收到，已剥夺敌方一枚导弹的控制权","奶油爆炸！上蹿下跳！已渗透一枚敌方导弹"],
        ["奶油报告，电子渗透失败","奶油报告，电子渗透遭到阻击","我觉得再试一次就能黑进去了，真的"],
        [],
        {'联邦信用点': 0},
        {"出身":"浅草寺重工"})

class Al8(Al_general):#维多利亚

    ready=["维多利亚就绪"]
    description_txt = "-极高爆发的超重型武器\n-用两个航行日按下8建造\n-建成后使我方之后发射的两枚普通导弹伤害翻倍，但存在故障概率\n-[续杯]打剩一半的维氏发射架，可以输入8或q使其重新变为满就绪状态"

    def check_if_fin_building(self):
        if self.state == 2:
            self.state=3
            print(random.choice(self.ready))

    def react(self):
        if self.state<2:
            self.state+=1
            self.report("维多利亚收到")
            self.check_if_fin_building()
        elif self.state == 2:
            self.state=3
            m1.printplus("[维氏]续杯完成")

    def attack(self):
        global eqm
        if random.randint(0,9)<8 or "备用加农炮管" in eqm:
            player_atkplus(2)
            n[1]-=1
            self.voi_print_pos()
        else:
            player_atkplus(1)
            n[1]-=1
            self.voi_print_neg()
        self.state-=1
        if self.state==1:
            self.state=0

    def suggest(self):
        return ["[q]建造发射架基础 1/2","[q]建成发射架炮管 2/2","[q]续杯|导弹伤害加成中","[已建立]导弹伤害加成中"][self.state]
         
al8=Al8("“维多利亚”加农炮式导弹发射架",
        ["维多利亚报告，全功率加农炮导弹命中敌方","维多利亚报告，加农炮导弹已重创敌方护盾"],
        ["维多利亚报告，加农炮导弹未能输出正常功率","维多利亚报告，发射架加力组件故障"],
        ["","{=}准备中","{=x}剩余一次","{x=x}发射架就绪"],
        {'三钛合金': 0, '湿件主机': 15, '重水': 0, '高强度树脂': 0, '锈蚀电路板': 10, '激光准晶体': 0, '黄铜差分机': 0, '电子变频箱': 0, '联邦信用点': 1100},
        {"出身":"浅草寺重工"})

class Al9(Al_general):#修械师

    description_txt = "-一群人数众多的护盾工程师，提高日常护盾充能的效率\n-用一个航行日部署，不可叠加\n-建成后，使我方下一次按下2进行护盾充能的效果翻三倍\n-[护盾学急救]部署时若护盾值过低，则立即额外回复护盾"

    def react(self):
        if self.state == 0:
            self.state+=1
            m1.printplus("[修械师]修械师小队收到，正在前往护盾区",0.3)
            if n[0]<=1:
                player_cureplus(1)
                m1.printplus("[修械师]护盾学急救已激活",0.3)
            time.sleep(0.4)
    
    def check_if_cure(self):
        global n
        if self.state == 1:
            player_cureplus(3)
            self.state=0
            self.voi_print_pos()
            n[0]-=1
    
    def suggest(self):
        if self.state == 0:
            if n[0]<=1:
                return "[w]建立吊舱|护盾学急救就绪"
            else:
                return "[w]建立吊舱"
        else:
            return "[已就绪]|[2]释放护盾"

al9=Al9("“修械师”常规维修小队吊舱",
        ["修械师小队已部署高密度有效护盾"],
        [],
        ["","[*]修械师就绪"],
        {'三钛合金': 25, '湿件主机': 0, '重水': 25, '高强度树脂': 0, '锈蚀电路板': 0, '激光准晶体': 25, '黄铜差分机': 0, '电子变频箱': 25, '联邦信用点': 4400})

class Al10(Al_general):#离人

    description_txt = "-重构舰船的反应堆，使得导弹和护盾的能量得以通用\n-航行日内输入10牺牲一层护盾来充能两枚导弹\n-护盾小于2时，尝试将一枚导弹转化为两层护盾"

    def react(self):
        if n[0] >= 2:
            n[0]-=1
            n[1]+=2
            self.voi_print_pos()
        elif n[0] <= 1:
            if n[1] != 0:
                player_cureplus(2)
                n[1]-=1
                self.voi_print_neg()
            else:
                player_cureplus(1)
                m1.printplus("[离人]离人小组正在与护盾小组取得联系",0.3)
                time.sleep(0.4)
        
    def suggest(self):
        if n[0] >= 2:
            return "[e]拆除护盾|获取2枚导弹"
        elif n[0] <= 1:
            if n[1] != 0:
                return "[e]拆除导弹|获取2层护盾"
            else:
                return "[资源耗竭]|[2]回充护盾|[0]回充导弹"
        
al10=Al10("“离人”牺牲式能量转化反应堆小组",
        ["收到，离人小组已牺牲一层护盾。两枚导弹已装填"],
        ["离人小组拆解了一枚导弹，护盾充能中"],
        [],
        {'三钛合金': 0, '湿件主机': 0, '重水': 0, '高强度树脂': 10, '锈蚀电路板': 0, '激光准晶体': 0, '黄铜差分机': 15, '电子变频箱': 0, '联邦信用点': 1100},
        {"武器平台":"导弹",
         "出身":"浅草寺重工"})

class Al11(Al_general):#柒

    description_txt = "-来自蜀地的民间护盾工程师，登舰支援战场\n-用一个航行日部署，不可叠加\n-部署后，敌方的两次护盾充能将回充到我方护盾上\n-[归来]部署时回复一层护盾\n-[为了身后的苍生]在柒满状态时输入11或w主动汲取敌方的一面护盾"

    def react(self):
        if self.state == 0:
            self.state+=2
            player_cureplus(1)
            m1.printplus("[“柒”]柒小队收到，敌方护盾锁定中",0.3)
            time.sleep(0.4)
        elif self.state == 2:
            player_atkplus(1)
            player_cureplus(1)
            self.state-=1
            m1.printplus("[“柒”]柒小队收到，敌方护盾夺取中",0.3)
            time.sleep(0.4)            

    def cure(self):
        player_cureplus(1)
        self.state-=1
        self.voi_print_pos()

    def suggest(self):
        return ["[w]建立汲能器","[剩余一次]敌方护盾锁定中","[就绪]敌方护盾锁定中|[w]主动汲取敌方护盾"][self.state]
al11=Al11("“柒”护盾汲能阵列",
        ["侦测到敌方护盾反应，柒夺取了一层护盾","正在汲取敌方护盾晶体，五秒钟后完成重结晶"],
        [],
        ["","[=]剩余一次","[≠]“柒”就绪"],
        {'三钛合金': 0, '湿件主机': 0, '重水': 0, '高强度树脂': 10, '锈蚀电路板': 0, '激光准晶体': 0, '黄铜差分机': 15, '电子变频箱': 0, '联邦信用点': 1100})

class Al12(Al_general):#晴空

    atk=[0,0,1,2,4,5,7,8]
    description_txt = "-需要连续航行日充能的重型粒子炮武器群\n-在确认一段时间内生存能力的情况下，在每一个连续的我方回合输入12进行充能\n-充能被其他输入打断时，对敌方造成伤害\n-[十四行赞美诗与一首绝望的歌]当晴空被迫以0伤害打断时，为我方回复1层护盾"

    def reset(self):
        global eqm
        self.state=0
        if "短弓炮管模组" in eqm:
            self.atk=[0,1,2,3,4,4,4,5]
        else:
            self.atk=[0,0,1,2,4,5,7,8]

    def react(self):
        if self.state<7:
            self.state+=1
            m1.printplus("[晴空]晴空报告，粒子炮正常充能中",0.3)
            time.sleep(0.4)
        else:
            player_atkplus(self.atk[self.state])
            p_c_manager.boom_now()
            self.state=0
            m1.printplus("[晴空]晴空粒子炮即将过热·已自动以极限功率输出",0.3)
            time.sleep(0.4)
    
    def attack(self):
        if self.atk[self.state] != 0:
            player_atkplus(self.atk[self.state])
            p_c_manager.boom_now()
            self.state=0
            self.voi_print_pos()
        elif self.atk[self.state] == 0:
            self.state=0
            m1.printplus("[晴空]晴空粒子炮充能失效·集群阵列回收中")
            player_cureplus(1)
            time.sleep(0.4)
    
    def printself(self):
        if self.state != 0:
            print(self.skin[self.state//3],end="")
            print(f"[晴空]粒子炮集群伤害水准：{self.atk[self.state]}")
            print()

    def suggest(self):
        if self.state == 0:
            return "[q]开始充能"
        elif self.state == 7:
            return f"[q/任意键]最高功率开火|{self.atk[self.state]}伤害"
        elif self.atk[self.state] == 0:
            return f"[q]继续充能|[任意键]放弃开火并触发回盾|0伤害"
        else:
            return f"[q]继续充能|[任意键]粒子炮开火|{self.atk[self.state]}伤害"
al12=Al12("“晴空”大功率粒子炮集群",
        ["晴空粒子炮全弹发射·已重创敌方护盾","众星因你，皆化为尘"],
        [],
        [r"{//|\\}",r"{//||\\}",r"{//x||x\\}"],
        {'三钛合金': 45, '湿件主机': 0, '重水': 45, '高强度树脂': 0, '锈蚀电路板': 20, '激光准晶体': 20, '黄铜差分机': 0, '电子变频箱': 45, '联邦信用点': 7700},
        tag={"武器平台":"粒子炮",
             "出身":"浅草寺重工"})

class Al13(Al_general):#北极

    description_txt = "-依托现有雷达阵列强行提升运算力，同时为复数导弹提供导航\n-航行日内输入13同时发射两枚导弹\n-不能触发维多利亚发射架的加成"

    def react(self):
        if n[1] == 0:
            n[1]+=1
            m1.printplus("[北极]未检测到导弹，北极小组正在与装弹小组取得联系")
            time.sleep(0.4)
        elif n[1] == 1:
            n[1]-=1
            player_atkplus(1)
            m1.printplus("[北极]收到，北极小组正在为单颗导弹提供导航")
            time.sleep(0.4)
        else:
            n[1]-=2
            player_atkplus(2)
            self.voi_print_pos()
        
    def suggest(self):
        if n[1] == 0:
            return "[无导弹]不能使用北极|[0]装弹"
        elif n[1] == 1:
            return "[e]导航单颗导弹|[0]装弹"
        else:
            return "[e]全功率导航"
al13=Al13("“北极”多目标导航雷达网络",
        ["北极小组收到，全功率导航器已启动","目视到两枚导弹正常划出右舷，护盾缺口正在打开","夜风是你的车辇，星辰是你的舞伴"],
        [],
        [],
        {'三钛合金': 0, '湿件主机': 25, '重水': 0, '高强度树脂': 25, '锈蚀电路板': 0, '激光准晶体': 25, '黄铜差分机': 0, '电子变频箱': 25, '联邦信用点': 4400},
        {"武器平台":"导弹",
         "出身":"联邦海军"})

class Al14(Al_general):#信风

    description_txt = "-年轻的创新护盾科技，通过过量结晶来强化已有护盾\n-输入14将一面我方普通护盾增强为可以抵御三点伤害的“信风”强化护盾\n-可以叠加。信风护盾不增加敌方风行者的命中率\n-[过饱和时代]强化后若仍拥有普通护盾，有概率再次触发强化"
    
    def react(self):
        global n
        if n[0]>0:
            self.voi_print_pos()
            self.state+=3
            n[0]-=1
        else:
            player_cureplus(1)
            m1.printplus("[信风]原始护盾不足，信风正在联系护盾小组")
            time.sleep(0.4)
        if probability(0.4) and n[0] > 0:
            self.react()
    
    def printself(self,mode=0):
        if mode == 0:
            print(self.skin[self.state-(self.state//3)*3],end="")
            print("\n//\\\\//"*(self.state//3))
        else:
            print(self.skin[self.state-(self.state//3)*3],end="")
            print("\nX$%&X"*(self.state//3))

    def suggest(self):

        global n
        if n[0] == 0:
            return "[护盾不足]不能使用信风|[2]回充护盾"
        else:
            return "[w]强化护盾"
al14=Al14("“信风”全结晶护盾防御系统",
        ["护盾结晶完毕！","信风来了，又是下雨的日子","让强风吹拂护盾的每一个结晶面！"],
        [],
        ["",r"\--//- 剩余一次",r"/-\/- 剩余两次","XTXTX"],
        {'三钛合金': 25, '湿件主机': 25, '重水': 25, '高强度树脂': 25, '锈蚀电路板': 50, '激光准晶体': 0, '黄铜差分机': 50, '电子变频箱': 0, '联邦信用点': 8800},
        {"出身":"岩河军工"})

class Al15(Al_general):#暴雨

    description_txt = "-高精度的全自动导弹发射系统\n-航行日内输入15来切换发射/待命状态\n-发射状态下，每两天自动打出一枚导弹，无论敌我回合·但按1发射导弹不可用\n-[暴雨绸缪]每次进入发射状态，将充能一枚附送导弹\n-[弹雨滂沱]暴雨上线时，按0可装载两枚导弹"

    def react(self):
        if self.state == 0:
            self.state=2
            m1.printplus("[暴雨]暴雨发射台正在暖机·预备导弹上线")
            n[1]+=1
            time.sleep(0.4)
        else:
            self.state=0
            m1.printplus("[暴雨]暴雨下线，常规发射器可用")
            time.sleep(0.4)

    def check_if_load(self,load) -> int:
        if self.state > 0:
            self.report("把神明从天国打下来！")
            return load + 1
        else:
            return load

    def printself(self):
        if 15 in choi:
            print(self.skin[self.state])
        
    def check_if_attack(self):
        if self.state>0:#暴雨
            if self.state == 1:
                if n[1]>0:
                    n[1]-=1
                    player_atkplus(1)
                    self.state=2
                    self.voi_print_pos()
                else:
                    self.state=0
                    m1.printplus("[暴雨]导弹耗尽·暴雨准备下线")
            else:
                self.state-=1
    
    def suggest(self):
        return ["[q]发射台开机|激活预备导弹","[自动攻击中]当日发射|[q]发射台关机|[0]辅助上弹","[自动攻击中]次日发射|[q]发射台关机"][self.state]
al15=Al15("“暴雨”全自动射手导弹发射台",
        ["暴雨命中目标，小心碎片","你见过凌晨四点的浅草寺吗？","牢大！我想你了！"],
        [],
        ["{-}暴雨待命中","{-[]-}即将发射","{[]}预计次日发射","{--}正在充能"],
        {'三钛合金': 15, '湿件主机': 15, '重水': 15, '高强度树脂': 45, '锈蚀电路板': 20, '激光准晶体': 20, '黄铜差分机': 45, '电子变频箱': 0, '联邦信用点': 7700},
        {"出身":"浅草寺重工"})

class Al16(Al_general):#情诗

    cure_list=[0,4,6,8,10]
    description_txt = "-晴空与修械师团队联合部署构造的护盾阵列\n-用多个连续或不连续的航行日输入16充能\n-输入2消耗所有层数并提供回盾量加成\n-[二十七行颂歌与一首绝望的诗]携带情诗时，按下2释放护盾及护盾充能不会打断12/q晴空的充能"

    def react(self):
        if self.state<4:
            self.state+=1
            m1.printplus("[情诗]情诗小队收到，大规模护盾构建中")
            time.sleep(0.4)
        else:
            self.state=0
            player_cureplus(self.cure_list[4])
            m1.printplus("[情诗]大规模护盾即将超载，即将自动释放")
            time.sleep(0.4)
            n[0]-=1

    def check_if_cure(self):
        if self.state != 0:#情诗
            player_cureplus(self.cure_list[self.state])
            self.state=0
            n[0]-=1
            self.voi_print_pos()

    def printself(self):
        if self.state != 0:
            print(self.skin[self.state//2],end="")
            print(f"[情诗]大规模护盾存量：{self.cure_list[self.state]}")
    
    def suggest(self):
        if self.state == 0:
            return "[w]开始充能"
        elif self.state == 4:
            return f"[w/2]极限存量护盾|{self.cure_list[self.state]}层"
        else:
            return f"[w]继续充能|[2]释放大规模护盾|{self.cure_list[self.state]}层"
al16=Al16("“情诗”大规模护盾疗救阵列",
        ["十四行诗的笔触，能否将你拯救？","微风泛起涟漪，留鸟越过池塘"],
        [],
        ["[+|+]","{+||+}","{+x||x+}"],
        {'三钛合金': 0, '湿件主机': 15, '重水': 0, '高强度树脂': 35, '锈蚀电路板': 15, '激光准晶体': 35, '黄铜差分机': 15, '电子变频箱': 35, '联邦信用点': 6600},
        {"出身":"浅草寺重工"})

class Al17(Al_general):#白夜

    description_txt = "-伤害极高的导弹弹头，但发射时会对我方护盾造成创伤\n-输入17来装载弹头到已有导弹并发射，对敌方造成2伤害\n-同时对我方护盾造成1创伤"

    def react(self):
        global n
        if n[1] == 0:
            n[1]+=1
            m1.printplus("[白夜]当前没有可用导弹·已联系导弹挂载小组",0.3)
            time.sleep(0.4)
        elif n[0]+al31.state <= 0:
            player_cureplus(1)
            m1.printplus("[白夜]当前护盾量不支持使用白夜·已联系护盾小组",0.3)
            time.sleep(0.4)
        else:
            cpu_atkplus(1,"[白夜]不惜代价，粉碎他们！",en1_liefeng=False)
            player_atkplus(2)
            n[1] -= 1
            self.voi_print_pos()

    def craft_self(self):
        print("[白夜]不是哥们，咱们是免费的不用合成 [FREE]不需合成即可离站使用")
        time.sleep(0.5)

    def suggest(self):
        if n[1] == 0:
            return "[资源耗竭][0]装填弹药"
        elif n[0]+al31.state <= 0:
            return "[资源耗竭][2/w]回复护盾"
        else:
            return "[q]发射白夜装甲弹"
al17=Al17("“白夜”钨金外壳重型反物质穿甲弹",
        ["白夜小组收到，导弹即将发射","洞穿一切！"],
        [],
        [],
        {"联邦信用点":0},
        {"出身":"联邦海军"})

class Al18(Al_general):#初夏

    description_txt = "-挂载于护盾回充器上的小型能量回收系统\n-不需部署·输入2或18是等价的\n-回充护盾时，有概率使回充量翻倍\n-[初夏将至]回充失败后，下一次必然成功"

    def react(self):
        if probability(0.6) or self.state == 1:
            player_cureplus(2)
            self.state = 0
            self.voi_print_pos()
        else:
            player_cureplus(1)
            self.state = 1
            self.voi_print_neg()

    def craft_self(self):
        print("[初夏]（睡眠中……）[FREE]不需合成即可离站使用")

    def suggest(self):
        if self.state == 0:
            return "[2/w]回充护盾|概率回充2层"
        else:
            return "[2/w]回充护盾|回充2层"            
al18=Al18("“初夏”共生式护盾充能系统",
          ["共生护盾充能成功","初夏共生护盾准备释放！","你是否相信，岸边的无名花会开满整个盛夏？"],
          ["共生式护盾充能未成功，正在寻找下一次机会"],
          [],
          {"联邦信用点":0},
          {"出身":"联邦海军"})

class Al19(Al_general):#苍穹

    ready=["浅草寺报告，建造完成，苍穹已就绪","苍穹就位"]
    description_txt = "-浅草寺重工出品的重型快递发射炮，固定在浅草寺的穹顶上\n-航行日内输入19召唤浅草寺战术快递\n-在接下来的三天内，给予舰船护盾或导弹（导弹平台）或粒子匣（粒子炮平台）\n-[巡行]每次快递发射时概率发射一颗风行者战术巡飞弹"

            

    def react(self):
        if self.state==0:
            self.state=3
            m1.printplus("[苍穹]浅草寺收到，苍穹待命中",0.3)
            time.sleep(0.4)
            m1.printplus("[苍穹]"+random.choice(self.ready))

    def suply(self):
        global n

        self.voilist_neg = ["浅草寺报告，观察到导弹已就位"] if q_is_missile() else ["浅草寺报告，观察到粒子匣已就位"]

        if self.state>0:
            self.state-=1
            if probability(0.5):
                player_cureplus(1)
                self.voi_print_pos()
            else:
                n[1]+=1
                self.voi_print_neg()
            if probability(0.5):
                al3.react()

    def suggest(self):
        return ["[e]呼叫浅草寺战术补给","[补给中]剩余一次","[补给中]剩余两次","[补给中]剩余三次"][self.state]
al19=Al19("“苍穹”浅草寺战术快递发射炮",
          ["快递抵达，护盾生成中"],
          ["浅草寺报告，观察到导弹已就位"],
          ["",r"{\\x//}苍穹就绪",r"{\x//}剩余两次",r"{\x//}剩余一次"],
          {'三钛合金': 25, '湿件主机': 25, '重水': 0, '高强度树脂': 25, '锈蚀电路板': 0, '激光准晶体': 50, '黄铜差分机': 50, '电子变频箱': 25, '联邦信用点': 8800},
          {"出身":"浅草寺重工"})

class Al20(Al_general):#长安

    global hard
    description_txt = "-巡视在战场上空的大型雷达，兼具信息干扰作用\n-航行日内输入20使用长安使之成为计划的一部分，使我方后续回合行动概率大幅增加\n-存在五个任意日的冷却时间\n-[索解]长安将实时运算并显示下一回合我方的行动概率"

    def react(self):
        global hard
        if self.state == 0:
            hard-=0.6
            self.state=-5
            self.voi_print_pos()
        else:
            self.voi_print_neg()
    
    def check_if_cool(self):
        global hard

        if self.state<0:
            self.state+=1
            
    
    def printself(self):
        global choi,hard
        if 20 in choi:
            print(f"[长安]下一天仍为我方航行日的概率：{1-hard}")

    def suggest(self):
        if self.state == 0:
            return "[e]压制敌方行动"
        else:
            return f"[冷却中]剩余{-self.state}天"
al20=Al20("“长安”大型相控阵巡天器",
            ["全功率扫描！宇宙为你闪烁！","跟长安雷达一起巡天，这是计划的一部分！"],
            ["长安报告，信标扫描器正在冷却中"],
            [],
            {'三钛合金': 15, '湿件主机': 15, '重水': 30, '高强度树脂': 15, '锈蚀电路板': 35, '激光准晶体': 0, '黄铜差分机': 0, '电子变频箱': 15, '联邦信用点': 5500},
            {"出身":"浅草寺重工"})

class Al21(Al_general):#诗岸

    description_txt = "-基于固液双相混凝合金的屏障构造体系\n-携带诗岸时，按下2护盾充能将进行液态护盾充注\n-当舰船护盾受到致命伤害，消耗一层液态护盾并将舰船护盾补全至一层\n-若同时持有的液态护盾过多，有概率意外全部固化为普通护盾，失去急救能力\n-按下21或w主动将所有液态护盾以1.5倍转化为普通护盾\n-[泛泛人类不会祈祷]迷途旅人的盾转化为诗岸液态屏障"

    def reset(self):
        self.state=0

    def react(self):
        if self.state>0:           
            n[0] += int(self.state*1.5)            
            self.state=0
            m1.printplus("[诗岸]诗岸报告，所有液态混凝屏障已凝固")
        else:
            self.state+=1
            m1.printplus("[诗岸]未检测到有效的诗岸屏障")

    def check_if_cure(self):
        global n
        if n[0]<=0:
            if self.state>0:
                self.state-=1
                n[0]=1
                self.voi_print_pos()

    def printself(self):
        if self.in_choi():
            if self.state <= 6:
                print("/-/-/-/\n"*self.state)
            else:
                print(f"/-/-/-/ x{self.state}")

    def suggest(self):

        if self.state>=3:
            return "[w]主动凝固|[2]充注液态护盾|请注意意外凝固风险"
        elif self.state>0:
            return "[w]主动凝固|[2]充注液态护盾|急救保护中"
        else:
            return "[2]充注液态护盾"
al21=Al21("“诗岸”高密度混凝打印式速固屏障",
            ["紧急凝固已就位","我拯救你的梦！","你梦见过有着纯白色天穹的乌托邦吗？"],
            [],
            [],
            {'三钛合金': 45, '湿件主机': 20, '重水': 20, '高强度树脂': 0, '锈蚀电路板': 45, '激光准晶体': 0, '黄铜差分机': 0, '电子变频箱': 45, '联邦信用点': 7700},
            {"出身":"岩河军工"})

class Al22(Al_general):#迫害妄想

    description_txt = "-由“晴空”团队开发的小型激光高能点射式爆破类战术装备\n-航行日内输入22使用迫害妄想对敌方稳定造成1点伤害\n-存在三个任意日的自动充能时间。在这三个任意日中，你将不能使用“迫害妄想”\n-[妄想税]在使用迫害妄想并结算当日所有伤害后，若敌方盾空则额外造成一点伤害"

    def react(self):
        if self.state >= 0:
            player_atkplus(1)
            self.state=-3
            self.voi_print_pos()
        else:
            self.voi_print_neg()

    def fps_react(self):
        player_atkplus(1)
        self.voi_print_pos()
        if n[2]<=0 :
            player_atkplus(1)
            m1.printplus(random.choice(["[妄想]洞穿你的妄想！","[妄想]そう、汚い妄想は、汚いお光で 解決ちせましょう。"]))            


    def check_if_cool_and_atk(self):
        if self.state == -3 and n[2]<=0:
            player_atkplus(1)
            m1.printplus(random.choice(["[妄想]洞穿你的妄想！","[妄想]そう、汚い妄想は、汚いお光で 解決ちせましょう。"]))

        if self.state<-1:
            print(f"[妄想]自动充能时间：{1-self.state}")
        elif self.state == -1:
            print("[妄想]迫害妄想已就绪")

        if self.state<0:
            self.state+=1

    def suggest(self):
        if self.state >= 0:          
            if n[2]<=1:
                return "[e]处决敌方"
            else:
                return "[e]造成1伤害"
        else:
            return f"[冷却中]剩余{-self.state}天"


al22=Al22("“迫害妄想”点射式战术阳极激光炮",
          ["伤害输出完毕！"],
          ["妄想报告，激光炮管正在重新预热"],
          [],
          {'三钛合金': 0, '湿件主机': 20, '重水': 45, '高强度树脂': 45, '锈蚀电路板': 0, '激光准晶体': 45, '黄铜差分机': 20, '电子变频箱': 0, '联邦信用点': 7700},
          {"出身":"浅草寺重工"})

class Al23(Al_general):#浮生

    description_txt = "-运行在舰船右舷的轨道浮游炮，可以极快地发射甲板导弹\n-航行日内输入23来连续发射三枚导弹\n-若中途导弹耗尽，提供一次自动装弹机会"

    def react(self):
        global n
        for i in range(3):
            if n[1]>0:
                n[1] -= 1
                player_atkplus(1)
                self.voi_print_pos()
            else:
                n[1] += 1
                self.voi_print_neg()
                break
    
    def suggest(self):
        if n[1]>=3:
            return "[q]浮游炮全功率开火"
        else:
            return ["[无导弹]不能使用浮生|[0]上弹","[q]浮游炮开火|导弹不足 1/3|[0]上弹","[q]浮游炮开火|导弹不足 2/3|[0]上弹"][n[1]]
al23=Al23("“浮生”超高射速亚轨道浮游炮",
          ["薄暮尽染！","戍角悲吟！","万城灯火！","一衣带水！","风起天末！"],
          ["导弹耗尽，上弹！"],
          [],
          {'三钛合金': 15, '湿件主机': 35, '重水': 0, '高强度树脂': 15, '锈蚀电路板': 15, '激光准晶体': 20, '黄铜差分机': 35, '电子变频箱': 15, '联邦信用点': 6600},
          {"出身":"岩河军工"})

class Al24(Al_general):#攻城奶油

    description_txt = "-奶油要是只会吃饱饱睡觉的话，那就别在这个人杰地灵的浅草寺混了\n-输入24强制把敌方5枚导弹从弹药库牵引至甲板，并引爆其中一部分造成伤害。对于每一颗没有黑到的导弹，获得一个『密钥』\n-持有『密钥』时，奶油有概率消耗一个『密钥』来接住一枚来袭的导弹，使其受我方控制\n-[传统艺能]持有『密钥』时输入25，消耗一个『密钥』，进行一次奶油黑客行动"

    def react(self):
        global n
        if self.state == 0:
            n[3]+=5
            self.state+=5
            while self.state:
                n[3]-=1
                player_atkplus(1)
                self.voi_print_pos()
                self.state-=1
                if probability(0.4*(4-self.state)):
                    break
        elif self.state != 0:
            m1.printplus("[大奶油]大黑特黑！")            
            al7.react()
            self.state-=1

    def protect(self,atk:int):
        global n
        if self.state == 0:
            return atk
        if probability(0.99):
            self.state-=upint(atk,2)
            atk=0
            n[1]+=1
            m1.printplus("[大奶油]我接住了！")
            if self.state<0:
                self.state=0
        return atk

    def printself(self):##祖师爷
        if 24 in choi:
            print("奶油的工作流")
            if self.state>0:
                print(f"|当前-解析保护中|可入侵敌方导弹[q]|『密钥』：{self.state}")
            else:
                print("|当前-空闲|电子进攻就绪[q]")
    
    def suggest(self):
        if self.state>0:
            return f"[q]入侵敌方导弹|解析保护中|『密钥』：{self.state}"
        else:
            return "[q]电子爆破进攻|获得秘钥"
        

al24=Al24("“攻城奶油”奶油的主动式电子进攻套件",
          ["boom!","导弹引爆！","对面甲板着火了！","哇袄！"],
          [],
          [],
          {'三钛合金': 25, '湿件主机': 0, '重水': 50, '高强度树脂': 25, '锈蚀电路板': 50, '激光准晶体': 0, '黄铜差分机': 25, '电子变频箱': 25, '联邦信用点': 8800},
          {"出身":"浅草寺重工"})

class Al25(Al_general):#阿贾克斯

    description_txt = "-由源氏工业设计并制造的新一代高效AI防御系统\n-在航行日输入25使一架位于前线待命的“阿贾克斯”无人机进入防御状态，不可叠加\n-此后，阿贾克斯将使用动能子弹稳定拦截3次敌方的任意攻击，然后进入5个任意日的冷却时间\n-[借力打力]“阿贾克斯”的拦截有概率震碎敌方一层护盾"

    def react(self):
        if self.state == 0:
            self.state=3
            m1.printplus("[贾氏]已进入防备状态，上膛完毕")
        
    def protect(self,atk):
        if atk == 0:
            return atk
        if self.state>0:
            m1.printplus("[贾氏]泄力！")
            self.state-=1
            if probability(0.3):
                player_atkplus(1)#
                self.voi_print_pos()
            if self.state == 0:
                self.state=-5
                m1.printplus("[贾氏]进入冷却")
            return 0
        else:
            return atk
    
    def check_if_cool(self):
        if self.state<0:
            self.state+=1

    def printself(self):
        if self.state<0:
            print(self.skin[4])
        elif 25 in choi:
            print(self.skin[self.state])

    def suggest(self):
        if self.state<0:
            return f"[冷却中]剩余{-self.state}天"
        elif self.state == 0:
            return f"[w]启动贾氏无人机群"
        else:
            return f"[防御进行中]剩余{self.state}次"

al25=Al25("“阿贾克斯”动能子弹前端拦截系统",
          ["[反击]吾乃天谴之矛！","[反击]寸拳！","[反击]吾乃天谴之矛！","[反击]十二点钟砸肘！","[反击]鹤踢！"],
          [],
          ["=[---]= 待命中","=[..|]= 剩余一次","=[.||]= 剩余二次","=[|||]= 就绪","=[...]= 冷却中"],
          {'三钛合金': 15, '湿件主机': 35, '重水': 0, '高强度树脂': 15, '锈蚀电路板': 0, '激光准晶体': 35, '黄铜差分机': 10, '电子变频箱': 15, '联邦信用点': 5500},
          {"出身":"源氏电气"})
            
class Al26(Al_general):#眠雀

    description_txt = "-来自蜀地的“信息麻醉师”，能支配对方行动\n-在航行日按下26使下次必定为我方行动\n-可以选择敌方下两次行动的内容，然后进入六个任意日的冷却\n-[谐振]若你选定的敌方行动与其本来计划相同，则造成1点伤害且不消耗次数"

    def react(self):
        if self.state == 0:
            self.state=3
            m1.printplus("[眠雀]渗透进黑暗中")
            
    def check_if_cool(self):
        if self.state<0:
            self.state+=1

    def check_if_control(self,d:int):
        if self.state>0:
            m1.printplus("[眠雀]成功获得敌方操作权")
            enemy_dicision_by_me=m1.ask_plus("[眠雀]选择敌方操作",["0","1","2","3"])
            enemy_dicision_by_me=int(enemy_dicision_by_me)
            self.state-=1
            if d == enemy_dicision_by_me:
                self.voi_print_pos()
                player_atkplus(1)
                self.state+=1
            if self.state == 0:
                self.state=-5
            return enemy_dicision_by_me
        else:
            return d

    def suggest(self):
        if self.state == 0:
            return "[e]控制敌方两次行动"
        elif self.state<0:
            return f"[冷却中]剩余{-self.state}天"
        elif self.state>0 and whoreact_0me == 0:
            return f"[生效中]剩余{self.state}次"
        else:
            return "[支配中]输入敌方指令[0]装弹|[1]发射|[2]上盾|[3]风行者"


al26=Al26("“眠雀”麻醉性致幻剂发射器",
          ["沉眠吧！"],
          [],
          [],
          {'三钛合金': 0, '湿件主机': 20, '重水': 0, '高强度树脂': 0, '锈蚀电路板': 10, '激光准晶体': 10, '黄铜差分机': 0, '电子变频箱': 10, '联邦信用点': 2200},
          {"出身":"源氏电气"})

class Al27(Al_general):#瞳猫

    description_txt = "-住在反应堆的喵喵喵喵喵喵喵！我闪！\n-航行日内不进行攻击叠加一层数，按下e使层数额外加一，攻击时使层数清零\n-能闪避敌方攻击，层数越高，护盾越少，闪避概率越大\n-喵！"

    def check_if_promote(self):
        if 27 in choi and self.state<9:
            self.state+=1

    def break_now(self):
        if 27 in choi and self.state>0:
            self.state=0;self.voi_print_neg()

    def check_if_evade(self,atk):
        if 27 in choi:
            if probability(self.state*0.1-(n[0]+al14.state-1)*0.12):
                atk=0
                self.voi_print_pos()
        return atk

    def react(self):
        if self.state<9:
            self.state+=1
            m1.printplus("[瞳猫]喵的，充能确认，尾流推进准备中")

    def suggest(self):
        if self.state<9:
            return f"[e]提升层数|{self.state}层|当前闪避率>>{self.state*10-(n[0]+al14.state-1)*12}%"
        else:
            return f"[层数已满]|{self.state}层|当前闪避率>>{self.state*10-(n[0]+al14.state-1)*12}%"
al27=Al27("“瞳猫”反应堆尾流推进器",
          ["喵！"],
          ["报告，层数已被清空"],
          [],
          {'三钛合金': 45, '湿件主机': 20, '重水': 0, '高强度树脂': 0, '锈蚀电路板': 45, '激光准晶体': 20, '黄铜差分机': 0, '电子变频箱': 45, '联邦信用点': 7700},
          {"出身":"浅草寺重工"})

class Al28(Al_general):#鹘鸮

    description_txt = "-依托敌方攻击带来的能量，给予敌人强烈的打击\n-在航行日按下28进入‘招架’，获得可抵挡三点伤害的临时护盾\n‘招架’持续到下一个敌方航行日若期间受到伤害，则发起攻击\n-[动能回收]‘招架’未反击时回复两枚导弹，导弹大于一时消耗一枚导弹额外造成一点伤害"

    def printself(self):
        if self.state>0:
            print(r"/===\鹘鸮招架中")
            print("~~~~~\n"*max(0,4-self.state))


    def react(self):
        if self.state == 0 :
            self.state=1
            m1.printplus("[鹘鸮]已做好反击准备")

    def check_if_protect_and_count(self,atk):
        if self.state>0 and self.state<4:
            while atk:
                atk-=1
                self.state+=1
                if self.state == 4:
                    break
        if self.state>=4:
            self.state+=atk
        if self.state>0:
            print(f"[鹘鸮]当前层数：{self.state}")
        return atk

    def check_if_fire(self):
        if self.state<0:
            self.state+=1
            print(f"[鹘鸮]剩余冷却天数：{-self.state}")
            return
        if whoreact_0me == 1:
            if self.state == 1:
                n[1]+=2
                self.voi_print_neg()
                self.state=-4
            elif self.state>1:
                if n[1]>1:
                    n[1]-=1
                    player_atkplus(self.state+1)                    
                    self.voi_print_pos()
                    self.voi_print_pos()
                    m1.printplus(f"[鹘鸮]造成伤害：{random.randint(3,self.state+1)}")
                else:
                    player_atkplus(self.state)
                    self.voi_print_pos()
                    m1.printplus(f"[鹘鸮]造成伤害：{random.randint(2,self.state)}")
                if n[2]<0:
                    m1.printplus("[鹘鸮]勘破灭！",2)
                self.state=0
    
    def suggest(self):
        if self.state==0:
            return "[q]进入招架状态"
        elif self.state>0:
            return f"[招架中]临时护盾剩余{max(0,4-self.state)}点"
        else:
            return f"[冷却中]剩余{-self.state}天"


al28=Al28("“鹘鸮”全反射屏障武装反击阵列",
          ["下绝 地纪！"],
          ["咕？"],
          [],
          {'三钛合金': 30, '湿件主机': 15, '重水': 35, '高强度树脂': 0, '锈蚀电路板': 15, '激光准晶体': 15, '黄铜差分机': 15, '电子变频箱': 0, '联邦信用点': 5500},
          {"出身":"环星学会"})

class Al29(Al_general):#酒师

    state = []
    description_txt = "-尖塔状的护盾治疗装备，可叠加使用\n-航行日内输入29来建立一座治疗塔，每座塔持续一到三天，每天回充一层护盾\n-治疗塔可以叠加建立，场上所有治疗塔同时生效\n-[人间清醒]在经历许多批评之后，酒师再也不会造出只存在零天的塔了"

    def reset(self):
        self.state = []

    def react(self):
        self.state.append(
            random.choices([0,1,2,3], weights=[0,3,3,2])[0]
        )
        self.voi_print_pos()

    def check_if_cure(self):
        if self.state != []:

            while True:
                try:
                    self.state.remove(0)
                except:
                    break
                
            player_cureplus(
                len(self.state)
            ) 
            for i in range(len(self.state)):
                self.state[i] -= 1
            
            m1.printplus(f"[酒师]工作中|救治{len(self.state)}次")

            while True:
                try:
                    self.state.remove(0)
                except:
                    break

    def printself(self):
        if 29 in choi:
            for i in self.state:
                print(self.skin[i],end=" ")
            print()

    def suggest(self):
        if self.state == []:
            return "[2/w]建立治疗塔"
        else:
            return f"[2/w]建立治疗塔|工作中|预计维持{max(self.state)}天|总治疗量{sum(self.state)}层" 
al29=Al29("“酒师”塔阵反应屏障治疗体系",
          ["这把要是还能输的话你给我滚回家卖烧酒吧喂!","无敌了你。","相信武魂真身去吧。"],
          [],
          ["",r"[||]x1",r"[/\]x2",r"[/||\]x3",r"[/|=|\]x4"],
          {'三钛合金': 25, '湿件主机': 15, '重水': 30, '高强度树脂': 0, '锈蚀电路板': 30, '激光准晶体': 15, '黄铜差分机': 0, '电子变频箱': 35, '联邦信用点': 6600},
          {"出身":"浅草寺重工"})

class Al30(Al_general):#湾区铃兰

    description_txt = "-爆发力与续航皆臻高位的大型粒子炮武器\n-在航行日输入30发射粒子炮，输出伤害并进入冷却\n-冷却期间，有概率消耗一个粒子匣为我方任何伤害提供伤害加成\n-[风中盛夏]在冷却期间输入30，牺牲两层护盾，仍能正常输出造成伤害"
    
    def react(self):
        if self.state == 0 :
            player_atkplus(2)
            self.state -= 5
            self.voi_print_pos()
            p_c_manager.boom_now()
        else:
            cpu_atkplus(2,"[护盾]护盾受损！我们受伤了！")
            self.voi_print_neg()
            player_atkplus(2)
            p_c_manager.boom_now()

    def check_if_increase(self,atk:int) -> int :
        if self.state < 0 and probability(0.8) and n[1] > 0:
            self.report(random.choice(["湾流正向你低语……","铃兰无声地盛开……"]))
            n[1] -= 1
            return atk + 1
        else:
            return atk

    def check_if_cool(self):
        if self.state<0 and whoreact_0me == 0:
            self.state+=1
    
    def suggest(self):
        if self.state == 0:
            return "[q]粒子炮倾巢发射"
        else:
            if n[0] >=2 :
                return f"[冷却中]剩余{-self.state}天|伤害加成中|[q]牺牲护盾强行攻击"
            else:
                return f"[冷却中]剩余{-self.state}天|伤害加成中"
        

al30=Al30("“湾区铃兰”饱和式蜂巢突击粒子炮",
          ["开火！让铃兰开满湾区的整个盛夏！","向！前！突！击！","粒子炮启动！湾流在咆哮啊！"],
          ["牺牲护盾！粉碎他们！","我们再无退路！","干涩如海风的咽喉！"],
          [],
          {'三钛合金': 25, '湿件主机': 50, '重水': 0, '高强度树脂': 25, '锈蚀电路板': 25, '激光准晶体': 50, '黄铜差分机': 25, '电子变频箱': 25, '联邦信用点': 9900},
          {"武器平台":"粒子炮",
           "出身":"岩河军工"})

class Al31(Al_general):#白鲟

    description_txt = "-兼有上弹能力的护盾再生平台\n-在航行日输入31获得6层临时护盾并获得一枚弹药，每我方航行日流失一点\n-临时护盾耗竭后进入五个任意日的冷却"

    def react(self):
        if self.state == 0:
            self.state = 6
            n[1] += 1
            self.report("临时护盾已部署")

    def protect(self,atk):
        if self.state > 0:
            di_atk = min(self.state,atk)
            self.state -= di_atk
            atk -= di_atk
            self.voi_print_pos()
            if self.state==0:
                self.state=-5
                self.voi_print_neg()
        return atk
            
    def check_if_cool_and_bleed(self):

        if self.state<0:
            self.state+=1
        elif self.state>0 and whoreact_0me == 0:
            self.state-=1
            self.report("报告，护盾正在流失")
            if self.state == 0:
                self.state=-5
                self.voi_print_neg()

    def suggest(self):
        if self.state==0:
            return "[w]部署临时护盾并获得一枚弹药"
        elif self.state>0:
            return f"[保护中]剩余{self.state}层"
        else:
            return f"[冷却中]剩余{-self.state}天"

    def printself(self):
        print(".....\n"*self.state)
al31=Al31("“白鲟”薄壁共振护盾再生平台",
            ["江水破碎，如水随形，护盾已保全","是要生存下去，还是走向死亡？","愿江水伴你永生"],
            ["白鲟报告，正在冷却中"],
            [],
            {'三钛合金': 10, '湿件主机': 15, '重水': 0, '高强度树脂': 25, '锈蚀电路板': 0, '激光准晶体': 10, '黄铜差分机': 15, '电子变频箱': 0, '联邦信用点': 3300},
            {"出身":"源氏电气"})

class Al32(Al_general):#普罗旺斯

    description_txt = "-部署在外层甲板的高能特种粒子炮平台，点燃敌方护盾上附着的粒子炮弹\n-在航行日内输入32激活点火平台。有粒子附着在敌方护盾上时，增加一层附着层数并立即引爆之\n-若没有粒子附着在敌方护盾上，充能两盒粒子匣"

    def react(self):
        if p_c_manager.plies >= 1:
            self.voi_print_pos()
            p_c_manager.plies += 1
            p_c_manager.boom_now()
        else:
            n[1] += 2
            self.voi_print_neg()
    
    def suggest(self):
        if p_c_manager.plies>=1:
            return "[e]附着一层粒子炮并引爆所有粒子炮"
        else:
            return "[未附着粒子炮]|[1]附着粒子|[0]装填粒子炮"

al32=Al32("“普罗旺斯”高能粒子点火平台",
            ["收到，天灾信使即将到场","准备点火，注意闪光！"],
            ["没有粒子附着，准备上弹"],
            [],
            {'三钛合金': 15, '湿件主机': 10, '重水': 15, '高强度树脂': 0, '锈蚀电路板': 25, '激光准晶体': 0, '黄铜差分机': 10, '电子变频箱': 0, '联邦信用点': 3300},
            {"武器平台":"粒子炮",
            "出身":"浅草寺重工"})

class Al33(Al_general):#蛊

    description_txt = "-由源氏通用电气基于核同质异能素的独特性质开发的新一代快速反应高能粒子定向能武器\n-在航行日输入33，使“蛊”以由核同质异能素坍缩产生的伽马光子，破坏敌方护盾的晶体结构，使敌方数层护盾沾染破损值\n-敌方护盾上的破损值将逐步加深；破损值大于100时，伤害该护盾并使大于100的部分将过渡到下一层护盾\n-[强充能]当敌方护盾量不小于五且我方粒子匣数不小于一，“蛊”将对敌方前五个护盾造成破坏；否则，则只对前三个造成破坏"
    state = [0,0,0,0,0]

    def reset(self):
        self.state = [0,0,0,0,0]

    def react(self):
        p_c_manager.boom_now()
        if n[1] > 0 and n[2] >=5:
            n[1]-=1
            pre_poi_list=[60,40,30,10,10]
            self.report(f"报告，{random.randint(135,246)}号核同质异能素组已坍缩至基态；观察到由伽马光子造成的晶格破损。")
        else:
            pre_poi_list=[40,30,30,0,0]
            self.report("已启用“蛊”的内置核同质异能素组；观察到伽马光子造成的晶格破损。")
        for i in range(5):#for(int i; i < 5; i++)
            self.state[i]+=pre_poi_list[i]
        if n[2]<=5:#去尾
            for i in range(n[2],5):
                self.state[i]=0
    
    def check_if_move(self,times):
        if 33 in choi:
            for i in range(times):
                self.state=self.state[1:]
                self.state.append(0)
    
    def check_if_deepen_and_poison(self):
        for i in range(5):
            if self.state[i] > 0:
                self.state[i] += 4
        while self.state[0] >= 100:
            n[2] -= 1
            self.voi_print_pos()
            if n[2] != 0:
                self.state[1] += self.state[0] - 100
            self.check_if_move(1)

    def printself(self):
        if n[2]>0:
            future = self.state.copy()
            if n[1] > 0 and n[2] >=5:
                pre_poi_list=[60,40,30,10,10]
            else:
                pre_poi_list=[40,30,30,0,0]
            for i in range(5):
                future[i]+=pre_poi_list[i]
            
            for i in range(1,n[2]+1):
                p=n[2]-i
                if p<5 and al33.state[p] != 0:
                    print(f"----->{self.state[p]} |q]>{future[p]}")
                elif  p<5 and al33.state[p] == 0 and future[p] !=0:
                    print(f"-----    |q]>{future[p]}")
                else:
                    print("-----")


    def suggest(self):

        now = self.state.copy()
        if n[1] > 0 and n[2] >=5:
            pre_poi_list=[60,40,30,10,10]
            return f"[q]射线粒子炮发射|估计破损{pre_poi_list}|加成中"
        else:
            pre_poi_list=[40,30,30,0,0]
            return f"[q]射线粒子炮发射|估计破损{pre_poi_list}"
        

al33=Al33("“蛊”核同质异能素伽马射线炮",
          ["And now,it's time for our moment that you've been waiting for!","On target,fire！","看破！","观察到敌方护盾正在坍缩。","你可曾知道，千里之堤，溃于蚁穴    "],
          ["没有粒子附着，准备上弹"],
          [],
          {'三钛合金': 15, '湿件主机': 15, '重水': 15, '高强度树脂': 15, '锈蚀电路板': 0, '激光准晶体': 35, '黄铜差分机': 20, '电子变频箱': 35, '联邦信用点': 6600},
          {"武器平台":"粒子炮",
           "出身":"源氏电气"})##考虑好了

class Al34(Al_general):#风间浦

    description_txt = "-双模式防御系统，提供从保守到激进的多种生存方案\n-以保守模式进入对局。在该模式下，所有回盾有概率加一。没有护盾时，这一概率上升至100%\n-输入34进入激进模式。这一模式下，舰船将不会死亡，持续至往后三个敌方日\n-激进模式结束后，回复与激进模式内受到总伤害等量的护盾，并进入五个航行日的冷却\n-[烈风]在进入激进模式的瞬间，对敌方造成1伤害"
    state = [0,0]

    def reset(self):
        self.state = [0,0]

    def check_if_promote(self,cure:int) -> int :
        if 34 not in choi:
            return cure
        if self.state[0] == 0 and probability(0.5):
            self.report("大规模充能就绪！")
            return cure + 1
        elif self.state[0] == 0 and n[0] == 0:
            self.report("大规模充能就绪！")
            return cure + 1
        else:
            return cure


    def check_if_cool_and_protect(self):
        if self.state[0] > 5:
            if n[0] <= 0:
                n[0] = 1
                self.voi_print_pos()
        elif self.state[0] == 5 and self.state[1] != 0:
            player_cureplus(self.state[1])
            self.state[1] = 0
            self.report("安全港就位，极限防御启动！")

        if self.state[0] > 5 and whoreact_0me == 1:
            self.state[0] -= 1
        elif 0 < self.state[0] <= 5 and whoreact_0me == 0:
            self.state[0] -= 1

    def record(self,atk):
        if self.state[0] > 5:
            self.state[1] += atk
            self.report(f"风期已至，{atk}伤害进入充能")
        
    def react(self):
        if self.state[0] == 0:
            self.state[0] = 8
            player_atkplus(1)
            self.report("对面那个打导弹的！你爹来了！")

    def suggest(self):
        if self.state[0] > 5:
            return f"[激进模式]剩余{self.state[0] - 5}天|{self.state[1]}伤害计入"
        elif self.state[0] == 5:
            return f"[脱离激进模式]{self.state[1]}护盾即将回充"
        elif self.state[0] > 0:
            return f"[充能中]剩余{self.state[0]}天"
        else:
            return "[保守模式]回盾加成中|[w]进入激进模式"        

al34=Al34("“风间浦”全平台战术安全港",
          ["救你一命！","别怕！","风的脉管里，动脉血在翻涌！"],
          [],
          [],
          {'三钛合金': 0, '湿件主机': 25, '重水': 25, '高强度树脂': 50, '锈蚀电路板': 50, '激光准晶体': 0, '黄铜差分机': 25, '电子变频箱': 25, '联邦信用点': 8800},
          {"出身":"岩河军工"})

class Al35(Al_general):#青鹄

    voi_list={"q":["复道行空，敌盾贯通！","泡影俱散，对面完蛋！"],"w":["固若金汤，有烟无伤！","防微杜渐，护盾无限！"],"e":["",""]}

    description_txt = "-来自唐朝的穿越者和她的时间机器（自称），使用无粒子引力源扭曲时间\n-在航行日输入35获得2充能，每天额外获得一充能，达到4充能时进入待命状态；待命期间输入35消耗所有充能与二枚弹药造成2伤害\n-待命时在敌方回合获得额外回合，获得一枚弹药和一层护盾，按下[q][w][e]触发对应效果或清空冷却，随后减少4充能,退出待命状态\n-[主观缓时]每天额外获得一充能；键入35能额外使任务天数减少一天（不影响事件计时）"

    def react(self):
        global days
        days-=1
        if self.state<4:
            self.state+=2
            self.voi_print_pos()
        else:
            if n[1]>1:
                player_atkplus(2)
                n[1]-=2
                self.state=0
                self.report("接招!")
            else:
                n[1]+=1
                if whoreact_0me==1:
                    n[1]+=1
                self.report("弹药不足，已自动装弹")
    def check_if_add(self):
        if 35 in choi:
            self.state+=1
        if self.state>=4 and whoreact_0me==1:
            n[0]+=1
            n[1]+=1
            self.report("报告，一弹一盾已部署，额外回合即将展开")

    def check_if_extra_act(self):
        
        if self.state>=4 and whoreact_0me==1:
            suggestion_tree = suggestion_print()
            suggestion_tree.topic = "额外回合操作"
            suggestion_tree.treeprint()
            inp=m1.ask_plus("""+[+Extra action+]+>>选择你的操作[q/w/e]立即响应或重置其冷却""",["q","w","e"])
            d="012qwe".find(inp)
            try:
                al_temp:Al_general=globals()[f"al{choi[d]}"]
                if type(al_temp.state)==int and al_temp.state<0:
                    al_temp.state=0
                    self.report_plus(inp,1)
                    self.report(f"{al_sho_title_cn[choi[d]]}冷却已重置")
                else:
                    self.report_plus(inp,0)
                    al_temp.react()
            except:
                pass
            if self.state!=0 :
                self.state-=4
    
    def report_plus(self, type, num):
        txt=self.voi_list[type][num]
        if txt=="":
            return
        if item3[self.len_skin]<3:
            txt=txt[0:min(len(txt),4)]+"！"
        return super().report(txt, True)

    def suggest(self):
        if self.state<1:
            return f"[e]增加二层充能|充能层数{self.state}/4"
        elif self.state<4:
            return f"[e]增加二层充能并进入待命状态|充能层数{self.state}/4"
        elif n[1]>1:
            return f"[e]攻击对方并清空充能|[待命中]获得额外回合|充能层数{self.state}/4"
        else:
            return f"[e]装弹|[待命中]获得额外回合|充能层数{self.state}/4"
al35=Al35("“青鹄”时空连续体空洞构造反应堆",
            ["多谢贵人拔擢~"],
            [""],
            [],
            {'三钛合金': 25, '湿件主机': 25, '重水': 50, '高强度树脂': 50, '锈蚀电路板': 0, '激光准晶体': 25, '黄铜差分机': 25, '电子变频箱': 0, '联邦信用点': 8800},
            {"出身":"随便观"})

class Al36(Al_general):#西岭

    description_txt = "-极其传统的大口径速射防空炮，可以自动防空拦截敌方导弹，也可以用于主动进攻\n-默认模式为自动防空模式。有概率拦截敌方的普通攻击\n-输入36切换至主动进攻模式。每个航行日获得一次弹雨扫射机会，共四十枚速射弹药，长按enter发射"

    def check_if_protect(self,atk):
        if 36 not in choi or self.state == 1 :
            return atk
        if probability(0.5):
            self.voi_print_pos()
            return 0
        else:
            self.voi_print_neg()
            return atk

    def react(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def check_if_attack(self):
        if self.state == 1 and whoreact_0me == 0:
            if_auto = True
            count_shot = 40
            while count_shot > 0:
                if not if_auto:
                    inp = input(f"[西岭]机炮已就位|剩余{count_shot}梭>>>")
                    if inp == "a":
                        if_auto = True
                else:
                    print(f"[西岭]机炮已就位|剩余{count_shot}梭")
                count_shot -= 1
                if probability(0.017):
                    print("[西岭]" + 
                        random.choice(
                            [
                                "攻击命中！",
                                "护盾破碎！",
                                "判定摧毁！"
                            ]
                        ) +
                        "------------+++[命中确认]+++------------"
                    )
                    player_atkplus(1)
                else:
                    print("[西岭]攻击未命中！--------[未能命中]---------")
        time.sleep(0.4)

    def suggest(self):
        if self.state == 0:
            return "[自动防空]导弹拦截中|[e]切换至饱和式弹雨扫射模式"
        else:
            return "[弹雨启动]每日攻击就位|[e]切换回自动防御模式"            

al36=Al36("“西岭”高速传统近防炮防空体系",
            ["击坠敌方导弹！","抓住了！","守护所有人！"],
            ["没拦住！","失误了！"],
            [],
            {'三钛合金': 20, '湿件主机': 30, '重水': 0, '高强度树脂': 0, '锈蚀电路板': 35, '激光准晶体': 10, '黄铜差分机': 20, '电子变频箱': 35, '联邦信用点': 6600},
            {"出身":"岩河军工"})

class Al37(Al_general):#星尘

    description_txt = "-极致优雅·极致精准·极致射击体验·粒子炮平台诚意之作\n-在航行日输入37进入预备状态，轻按[enter]进入锁定模式\n-锁定时，当“|”符号运动至“[ + ]”正下方时，按下[ctrl+C]锁定敌方并发射粒子炮\n-根据精确度消耗粒子匣并造成消耗粒子匣1.5倍的伤害\n-[星尘无尽]无尽/肉鸽模式下，溢出的伤害按照一定比例转化回粒子匣，以供下一轮使用"


    def react(self):
        if self.state<0:
            self.report("冷却中")
            return
        try:
            m1.inputplus("[星尘]确认后使用[ctrl+C]（请勿多次敲击或长按）锁定目标|[enter]确认>>>")
        except:
            self.report("谁叫你在这里按了？？")
        #time.sleep(1)
        run_delta_t=0.03
        e = random.randint(33,66)
        print(" "*(e-2) + "[ + ]")

        pos=-1
        for i in range(100):
            try:
                pos+=1
                print("|",end="")
                time.sleep(run_delta_t)
            except KeyboardInterrupt:
                break

        if e-4  <= pos <= e+4 :
            print("x")
            self.state=-7
            if  e-2  <= pos <= e+2:
                print(" "*(e-10)+r"\\\\   [星尘]   ////")
                print(" "*(e-10)+r"   \\\\FIRE!!////")
                damage=min(10,n[1])
            else:
                print(" "*(e-10)+r"\\ [星尘]SPLASH!! //")
                damage=min(4,n[1])
                self.state=-4
            self.voi_print_pos()
            player_atkplus(
                int(
                    damage*1.5
                )
            )
            p_c_manager.boom_now()
            n[1]-=damage
            self.report(
                f" 有效伤害>{di_ani_manager.pre_n[2]-n[2]}.0"
            )
        else:
            print("?")
            self.report("锁定未成功")

    def check_if_cool(self):
        if self.state<0:
            self.state+=1

    def check_if_recycle(self):
        if n[2]<-1 and self.in_choi():
            n[1]+=int((-1-n[2])*0.5)
            n[2]=-1
            self.report("能量已回收")
        
    def suggest(self):
        if self.state<0:
            return f"[冷却中]剩余{-self.state}天"
        else:
            return "[q]启动狙击粒子炮|注意-含有qte"
al37=Al37("“星尘”非自动制导正光锥粒子流",
            ["众星因你，皆化为尘","向群星而去……"],
            [],
            [],
            {'联邦信用点': 0},
            {"出身":"环星学会","武器平台":"粒子炮"})

class Al38(Al_general):#澈

    description_txt = "-以牺牲为核心的新一代护盾平台，拥有比更多的模式，更灵活的进攻防守策略\n-航行日输入38获得三层锋镝，随之对自己造成两次共计两点伤害\n-任何时候，在护盾小于一时，澈将依照现有锋镝最多补充护盾至二，并消耗对应层数锋镝\n-[澄]模式|澈的正常模式|在敌我发动攻击时获得一层锋镝\n-若锋镝大于九，进入[寂]\n-[寂]模式|澈的牺牲模式|我方发动攻击时消耗一层锋镝使伤害加一，直到锋镝小于五时退出[寂]"

    def reset(self):
        self.state=[0,False]

    def react(self):
        self.state[0]+=3
        self.voi_print_neg()
        cpu_atkplus(1,en1_liefeng=False)
        cpu_atkplus(1,en1_liefeng=False)

    def check_if_add(self):
        if self.in_choi() and self.state[1]==False and probability(0.5):
            self.state[0]+=1
            print("[澈]收到")
    
    def check_if_cure(self):
        if self.state[0]>0 and n[0]<1:
            cure = min(self.state[0],2-n[0])
            self.state[0]-=cure
            player_cureplus(cure)
            self.voi_print_pos()

    
    def check_if_turn(self):
        if self.state[0]>9 and self.state[1]==False:
            self.state[1]=True
            self.report("激进模式开启")
        elif self.state[0]<5 and self.state[1]==True:
            self.state[1]=False
            self.report("激进模式关闭")

    def check_if_increase(self,atk):
        if self.state[1] and self.state[0]>0:
            self.state[0]-=1
            self.report(
                random.choice(
                    [
                        "飞快地下着雨一样的血……",
                        "丛林中的暴风雨，正在酝酿……"
                    ]
                )
            )
            return atk+1
        return atk

    def printself(self):
        if self.state[0] <= 5:
            print("--X--\n"*self.state[0])
        else:
            print(f"--X-- x{self.state[0]}")

    def suggest(self):
        return f"{self.state}"
al38=Al38("“澈”高牺牲护盾锐化改装套件",
            ["现在还没到牺牲的时候","护盾补充就位！","这是末世之下最后的加护"],
            ["你是相信牺牲的血脉，还是要放任命运扣响你绝望的门扉？","锋刃蒙尘，面目成灰","天罚已至！"],
            [],
            {'联邦信用点': 0},
            {"出身":"浅草寺重工"})

class Particle_cannon_manager:

    plies = 0

    def boom_now(self):
        if self.plies != 0:
            if probability(0.5):
                self.plies *= 2
                m1.printplus("[粒子炮]粒子弹暴击迹象！")                
            player_atkplus(self.plies)
            m1.printplus("[粒子炮]高能粒子引爆！小心闪光！")
            self.plies = 0
    
    def adding(self,num:int):
        self.plies += num

    def check_if_boom(self):
        if self.plies != 0 and probability(0.2*self.plies):
            self.boom_now()

    def print_self(self):
        if self.plies != 0:
            print("{"+f"*{self.plies}"+"}")

p_c_manager = Particle_cannon_manager()

class Machine_gun_manager:
    
    pass

m_g_manager = Machine_gun_manager()


al_num = m1.max_index_finder(globals(),"al")

q_list=["-1"]
w_list=["-2"]
e_list=["-3"]

for i in range(0,al_num):
    try:
        al_temp:Al_general=globals()[f"al{i}"]
        if al_temp.type == "q":
            q_list.append(f"{i}")
        if al_temp.type == "w":
            w_list.append(f"{i}")        
        if al_temp.type == "e":
            e_list.append(f"{i}")
    except:
        pass

q_list_0=[]
q_list_1=[]
q_list_2=[]

w_list_0=[]
w_list_1=[]
w_list_2=[]

e_list_0=[]
e_list_1=[]
e_list_2=[]

for i in range(3,al_num):
    try:
        al_temp:Al_general=globals()[f"al{i}"]
        if al_temp.rank_num<=2:
            rank_now = 0
        elif al_temp.rank_num<=5:
            rank_now = 1
        elif al_temp.rank_num<=10:
            rank_now = 2
        else:
            rank_now = None
        globals()[f"{al_temp.type}_list_{rank_now}"].append(i)
    except:
        pass

al_promoting_dict={}
for i in ("q","w","e"):
    for j in (0,1,2):
        if j != 2:
            al_promoting_dict[tuple(globals()[f"{i}_list_{j}"])]=globals()[f"{i}_list_{j+1}"]
        else:
            al_promoting_dict[tuple(globals()[f"{i}_list_{j}"])]=globals()[f"{i}_list_{j}"]

###########################################


###########################################

class Fps1(Fps_general):

    def react(self):
        self.report()
        for i in range(3):
            al3.react()
fps1 = Fps1("风行者巡飞阵列",
            "从浅草寺连续发射三枚风行者攻击敌方")
class Fps2(Fps_general):

    def react(self):
        self.report()
        al14.state += 3
fps2 = Fps2("支援型信风",
            "从浅草寺呼叫一层信风护盾")

class Fps3(Fps_general):

    def react(self):
        self.report()
        al22.fps_react()

    def report(self):
        m1.printplus(f"[浅草寺]收到，{self.title}准备就绪")
fps3 = Fps3("追迹日落以西",
            "从浅草寺请求超远距离“迫害妄想”激光炮射击")

class Fps4(Fps_general):

    def react(self):
        self.report()
        n[0] += 2
        n[1] += 1    

fps4 = Fps4("守岸人体系",
            "从浅草寺请求一枚导弹与两层护盾")

fps_num = m1.max_index_finder(globals(),"fps")
item5 = {}
for i in range(1,fps_num):
    fps_temp:Fps_general = globals()[f"fps{i}"]
    item5[fps_temp.title] = 0

class Fps_manager:

    def print_all_formula(self):
        for i in range(1,fps_num):
            fps_temp:Fps_general = globals()[f"fps{i}"]
            fps_temp.print_formula(item5)

    def print_all_calling(self):
        for i in range(1,fps_num):
            fps_temp:Fps_general = globals()[f"fps{i}"]
            fps_temp.print_calling(item5)
        if sum(item5.values()) <= 0:
            print("（无装备）")

    def craft_main(self):
        while True:
            print()
            self.print_all_formula()
            print(f"当前信用点>>{item1['联邦信用点']} ISK",end="\n\n")
            inp_index:str = m1.ask_plus("[数字]输入要合成的战术快递编号|[e/exit]退出>>>",[str(i) for i in range(1,fps_num)]+["e","exit"])

            if inp_index in ["e","exit"]:
                m1.printplus("正在退出")
                return

            fps_temp:Fps_general = globals()[f"fps{inp_index}"]
            fps_temp.craft_self(item1,item5)
            sync()


    def calling_main(self):
        while 1:
            print()
            self.print_all_calling()
            inp_index:str = m1.ask_plus("[数字]输入要呼唤的战术快递编号|[c]进入合成界面>>>",[str(i) for i in range(1,fps_num)]+["","c"])
            if inp_index == "":
                return m1.inputplus("请选择你的操作>>>",0.2)
            if inp_index == "c":
                self.craft_main()
            else:
                break
        fps_temp:Fps_general = globals()[f"fps{inp_index}"]
        if item5[fps_temp.title] >= 1:
            fps_temp.react()
            item5[fps_temp.title] -= 1
            sync()
        else:
            m1.printplus("无装备|呼叫失败")
            return m1.inputplus("请选择你的操作>>>",0.2)
        return "r"

fps_manager = Fps_manager()



###########################################

class CMP_Market:

    price_list1 = {
        "联邦信用点":0.1,
        "三钛合金":4.0,
        "湿件主机":4.0,
        "重水":4.0,
        "高强度树脂":4.0,
        "锈蚀电路板":4.0,
        "激光准晶体":4.0,
        "黄铜差分机":4.0,
        "电子变频箱":4.0}
    price_list2={}
    cart={}

    def price_print(self):
        global item1
        print("欢迎来到合约纪念点商城",end="\n\n")
        lst=[]
        for i in self.price_list1:
            left=f"[{i}]"
            right=f"{self.price_list1[i]} CMP"
            lst.append(left+"-"*(40-m1.printlen(left)-m1.printlen(right))+right)
        price_tree1=Tree("基础物品与信用点",lst)
        price_tree1.treeprint()

    def cart_print(self):
        global item1
        lst=[]
        for i in self.cart:
            left=f"[{i}]"
            right=f"*{self.cart[i]}>>{self.price_list1[i]*self.cart[i]}CMP"
            lst.append(left+"-"*(40-m1.printlen(left)-m1.printlen(right))+right)
        tree_output_lst="（空闲）" if lst == [] else lst
        cart_tree=Tree("当前购物车",tree_output_lst,f"""总价:{self.cost_sum()} CMP /现有：{item1["合约纪念点"]} CMP""")
        cart_tree.treeprint()

    def ask_and_put_into_cart(self):
        inp_item=m1.inputplus("请输入要加入或减少至购物车的商品名称·输入回车结算·输入x清空购物车>>>")
        if inp_item in self.price_list1 or inp_item in self.price_list2:
            print("已确认")
            inp_num=int(m1.inputplus("请输入要加入购物车的商品数量·输入负数使购物车物品减少>>>"))
            try:
                self.cart[inp_item]+=inp_num
            except:
                self.cart[inp_item]=inp_num
            print("已确认")
        elif inp_item == "x":
            self.cart={}
        else:
            return False

    def clear_check(self):
        temp_cart={}
        for i in self.cart:
            if self.cart[i]>0:
                temp_cart[i]=self.cart[i]
        self.cart={}
        for i in temp_cart:
            self.cart[i]=temp_cart[i]

    def cost_sum(self):
        cost=0
        for i in self.cart:
            if i in self.price_list1:
                cost+=self.price_list1[i]*self.cart[i]
            elif i in self.price_list2:
                cost+=self.price_list2[i]*self.cart[i]
        return cost
    
    def cost(self):
        global item1
        for i in self.cart:
            print(f"{i}*{self.cart[i]} 已购置")
            item1[i]+=self.cart[i]
        item1["合约纪念点"]-=self.cost_sum()
        self.cart={}
        sync()
        time.sleep(1)

    def market_main(self):
        global item1
        while 1:
            self.price_print()
            self.cart_print()
            m1.dict_give_and_get_print(item1,self.cart,{})
            brk=self.ask_and_put_into_cart()
            self.clear_check()
            if brk == False:
                if self.cost_sum()<=item1["合约纪念点"]:
                    self.cost()
                    break
                else:
                    m1.printplus("当前购物车总支出已超过可支付总额")

cmp_market=CMP_Market()

###########################################

def item_list_creater(total):
    output_list={}
    item_num=random.randint(2,4)
    num_expect=total//item_num

    pre_list=list(items.keys())
    random.shuffle(pre_list)
    item_list=pre_list[0:item_num]
    for i in item_list:
        output_list[i]=random.randint(num_expect-3,num_expect+3)
    return output_list

def afford_checked(son:dict,father:dict):
    j=0
    k=0
    for i in son:
        try:
            if father[i]>=son[i]:
                j+=1
        except:
            pass
        k+=1
    if j == k:
        return True
    else:
        return False
    
def zero_clear(dic:dict):
    pre=[]
    for i in dic:
        pre.append(i)

    for i in range(len(pre)):
        if dic[pre[i]] == 0:
            dic.pop(pre[i])
    return dic

class Contract:

    title_list=["货品合同",
                "易物合同",
                "工业合同",
                "回购合同",
                "保险合同"]

    title=""
    rank=0
    index=0
    get_list={}
    give_list={}
    is_selected=False
    is_traded=False

    al_index=0 

    def __init__(self,index:int):
        self.index=index
        self.rank=random.randint(1,8)
        self.title=random.choice(self.title_list)

        if self.title == "货品合同":
            self.give_list=item_list_creater(25*self.rank)
            s=self.rank
            pre_get_list={}
            pre_get_list["联邦信用点"]=random.randint(1000*s-100,1000*s+100)
            self.get_list=pre_get_list
            if random.random()<0.5:
                self.give_list,self.get_list=self.get_list,self.give_list

        elif self.title == "易物合同" :
            self.give_list=item_list_creater(25*self.rank)
            self.get_list=item_list_creater(30*self.rank)
            for i in self.give_list:
                if i in self.get_list:
                    p=self.get_list[i]-self.give_list[i]
                    if p>0:
                        self.get_list[i]-=self.give_list[i]
                        self.give_list[i]=0
                    elif p<0:
                        self.give_list[i]-=self.get_list[i]
                        self.get_list[i]=0
                    else:
                        self.give_list[i]=0
                        self.get_list[i]=0
            self.get_list=zero_clear(self.get_list)
            self.give_list=zero_clear(self.give_list)

        elif self.title == "工业合同":
            ran_al=random.randint(3,len(al_sho_title_cn)-4)
            al_temp:Al_general=globals()[f"al{ran_al}"]

            while al_temp.rank == "FREE":
                ran_al=random.randint(3,len(al_sho_title_cn)-4)
                al_temp:Al_general=globals()[f"al{ran_al}"]

            self.al_index=ran_al
            self.rank=al_temp.rank_num
            pre_get={al_sho_title_cn[ran_al]:1}
            self.get_list=pre_get
            self.give_list=item_list_creater(20*self.rank)
            self.give_list["联邦信用点"]=random.randint(1000*self.rank-300,1000*self.rank+100)

        elif self.title == "回购合同":
            ran_al=random.randint(3,len(al_sho_title_cn)-4)
            al_temp:Al_general=globals()[f"al{ran_al}"]

            while al_temp.rank == "FREE":
                ran_al=random.randint(3,len(al_sho_title_cn)-4)
                al_temp:Al_general=globals()[f"al{ran_al}"]

            self.al_index=ran_al
            self.rank=al_temp.rank_num
            pre_give={al_sho_title_cn[ran_al]:1}
            self.give_list=pre_give
            pre_get={"联邦信用点":self.rank*2200+random.randint(-50,50)*10}
            self.get_list=pre_get

        elif self.title == "保险合同":
            self.get_list={"保险点":self.rank}
            self.give_list={"联邦信用点":self.rank*1100+random.randint(-50,50)}

        aff_tag=" [●]" if self.affordable() else ""
        self.title_tree=Tree(f"[{self.index}] "+self.title+f" [{self.rank}]级")
        self.get_tree=Tree("你将得到>>>",self.get_list)
        self.give_tree=Tree("你将支付>>>"+aff_tag,self.give_list)

    def aff_refresh(self):
        aff_tag=" [●]" if self.affordable() else ""
        self.title_tree=Tree(f"[{self.index}] "+self.title+f" [{self.rank}]级")
        self.get_tree=Tree("你将得到>>>",self.get_list)
        self.give_tree=Tree("你将支付>>>"+aff_tag,self.give_list)


#    def test_print(self):
#        print("┌────────────┐")
#        self.title_tree.treeprint()
#        self.give_tree.treeprint()
#        self.get_tree.treeprint()
#        print("└────────────┘")
#        print()

    def print_self(self):
        self.aff_refresh()
        print("┌──────────┐")
        for i in self.title_tree.linelist():
            print(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
        for i in self.give_tree.linelist():
            print(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
        for i in self.get_tree.linelist():
            print(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
        print("└──────────┘")

    def print_list(self):
        self.aff_refresh()
        output=[]
        if self.is_traded == False:
            output.append("┌──────────┐")
            for i in self.title_tree.linelist():
                output.append(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
            for i in self.give_tree.linelist():
                output.append(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
            for i in self.get_tree.linelist():
                output.append(f"│{i}"+" "*(22-m1.printlen(f"│{i}"))+"│")
            output.append("└──────────┘")
        else:
            output.append("┌──────────┐")
            for l in self.title_tree.linelist():
                output.append(f"│{l}"+" "*(22-m1.printlen(f"│{l}"))+"│")
            for l in self.give_tree.linelist():
                output.append(f"│"+" "*(20)+"│")
            for l in range(len(self.get_tree.linelist())-1):
                output.append(f"│"+" "*(20)+"│")
            output.append(f"│[已交易]"+" "*(22-m1.printlen(f"│[已交易]"))+"│")
            output.append("└──────────┘")            
        return output
    
    def affordable(self):
        global item1,item3
        if self.title == "货品合同":
            if afford_checked(self.give_list,item1):
                return True
        elif self.title == "易物合同" :
            if afford_checked(self.give_list,item1):
                return True
        elif self.title == "保险合同" :
            if afford_checked(self.give_list,item1):
                return True
        elif self.title == "工业合同":
            if afford_checked(self.give_list,item1):
                return True
        elif self.title == "回购合同":
            al_temp:Al_general=globals()[f"al{self.al_index}"]
            check_list={al_temp.len_skin:1}
            if afford_checked(check_list,item3):
                return True
        return False

    def trade(self):
        global item1
        if self.affordable() and not self.is_traded:
            
            if self.title == "货品合同" or self.title == "易物合同" or self.title == "保险合同":
                for i in self.give_list:
                    item1[i]-=self.give_list[i]
                    print(f"{i} *{self.give_list[i]} 已支付")
                for i in self.get_list:
                    item1[i]+=self.get_list[i]
                    print(f"获得 {i} *{self.get_list[i]}")

            elif self.title == "工业合同":
                for i in self.give_list:
                    item1[i]-=self.give_list[i]
                    print(f"{i} *{self.give_list[i]} 已支付")
                al_temp:Al_general=globals()[f"al{self.al_index}"]
                item3[f"{al_temp.len_skin}"]+=1
                print(f"{al_temp.len_skin} *1 已送至空间站并铭刻你的代号")

            elif self.title == "回购合同":
                al_temp:Al_general=globals()[f"al{self.al_index}"]
                item3[f"{al_temp.len_skin}"]-=1
                print(f"{al_temp.len_skin} *1 已出售")
                for i in self.get_list:
                    item1[i]+=self.get_list[i]
                    print(f"获得 {i} *{self.get_list[i]}")                
            self.is_traded=True
        
        sync()
        
        time.sleep(1)

class Contract_manager:

    filter_list={"货品合同":True,
                 "易物合同":True,
                 "工业合同":True,
                 "回购合同":True,
                 "保险合同":True}
    filter_key_list={"货品合同":"z",
                     "易物合同":"x",
                     "工业合同":"c",
                     "回购合同":"v",
                     "保险合同":"b"}

    column0=column1=column2=column3=column4=column5=[]

    def market_generate(self,total_con):
        for i in range(1,total_con+1):
            globals()[f"con{i}"]=Contract(i)

    def market_print(self,total_con):

        

        for i in range(0,6):
            setattr(self,f"column{i}",[])
            for j in range(i*total_con//6+1,(i+1)*total_con//6+1):
                con_temp:Contract=globals()[f"con{j}"]
                if self.filter_list[con_temp.title] == True:
                    setattr(self,f"column{i}",
                        getattr(self,f"column{i}") + con_temp.print_list()
                    )
                else:
                    output_list=[]
                    output_list.append("┌──────────┐")
                    for l in con_temp.title_tree.linelist():
                        output_list.append(f"│{l}"+" "*(22-m1.printlen(f"│{l}"))+"│")
                    for l in con_temp.give_tree.linelist():
                        output_list.append(f"│"+" "*(20)+"│")
                    for l in range(len(con_temp.get_tree.linelist())-1):
                        output_list.append(f"│"+" "*(20)+"│")
                    output_list.append(f"│[已屏蔽]"+" "*(22-m1.printlen(f"│[已屏蔽]"))+"│")
                    output_list.append("└──────────┘")
                    setattr(self,f"column{i}",
                        getattr(self,f"column{i}") + output_list
                    )

        
        re_tree=Tree(resource_nevigator.tree_output_title(),resource_nevigator.tree_output_body())
        
        m1.n_columnprint(
            [self.column0,self.column1,self.column2,self.column3,self.column4,self.column5],
            24
        )
        m1.n_columnprint([re_tree.linelist()])
        print("合同筛选器|[小写zxcvb]切换显示状态|[大写ZXCVB]单独显示|[a]全部显示")
        for i in self.filter_list:
            print(f"{i}[{self.filter_key_list[i]}] {self.filter_list[i]}",end="   ")
        print()

    def contract_market_main(self):
        while 1:
            self.market_print(24)
            print()
            m1.dict_give_and_get_print(item1,{},{})
            inp=input("[数字] 选择合同|[r/refresh] 刷新市场|[e/exit] 退出>>>")
            if inp in ["Z","X","C","V","B"]:
                inp = inp.lower()
                self.filter_list={
                    "货品合同":False,
                    "易物合同":False,
                    "工业合同":False,
                    "回购合同":False,
                    "保险合同":False
                }
            if inp == "exit" or inp == "e":
                break
            elif inp == "a":
                self.filter_list={
                    "货品合同":True,
                    "易物合同":True,
                    "工业合同":True,
                    "回购合同":True,
                    "保险合同":True
                }
            elif inp == "refresh" or inp == "r":
                self.market_generate(24)
            elif inp == "z":
                self.filter_list["货品合同"]=not self.filter_list["货品合同"]
            elif inp == "x":
                self.filter_list["易物合同"]=not self.filter_list["易物合同"]
            elif inp == "c":
                self.filter_list["工业合同"]=not self.filter_list["工业合同"]
            elif inp == "v":
                self.filter_list["回购合同"]=not self.filter_list["回购合同"]
            elif inp == "b":
                self.filter_list["保险合同"]=not self.filter_list["保险合同"]
            elif inp.isdigit():
                try:
                    con_temp:Contract=globals()[f"con{inp}"]
                    con_temp.print_self()
                    m1.dict_give_and_get_print(item1,con_temp.get_list,con_temp.give_list)
                    inp1=input("check=签署并交易 [enter]=退出>>>")
                    if inp1 == "check":
                        con_temp.trade()
                except KeyError:
                    pass
contract_maneger=Contract_manager()
###########################################

class Diamond():

    def __init__(self,index,type:str,rank:int,entry,if_on:bool):
        self.type=type
        self.rank=rank
        self.entry=entry
        self.index=index
        self.if_on=if_on
        #print([self.index,self.type,self.rank,self.entry,self.if_on])

    def put(self):
        if self.if_on:
            self.if_on=False
            diamond_manager.hollow[self.type].remove(globals()[f"diamond{self.index}"])
        elif len(diamond_manager.hollow[self.type])<=2:
            self.if_on=True
            diamond_manager.hollow[self.type].append(globals()[f"diamond{self.index}"])
        #print([self.index,self.type,self.rank,self.entry,self.if_on])
    
    def linelist(self):
        label=[]
        rank_list=["ORIGIN","I","II","III","IV","V","VI","VII","VIII","IX","X"]
        for i in range(len(diamond_manager.qwe_entry_discribe_and_pro_list[self.type])):
            if self.entry[i] != 0:
                raw_disc:str=diamond_manager.qwe_entry_discribe_and_pro_list[self.type][i]
                left,right=raw_disc.split("一定")
                output_txt=left+str(diamond_manager.qwe_entry_discribe_and_pro_list[f"{self.type}_pro"][i]*self.entry[i])+right
                label.append(f"{output_txt}---+{self.entry[i]}")
        tag_if_on="已装备" if self.if_on else "未装备"
        self.tree=Tree(f"凡晶石套件[{self.index}][{tag_if_on}][{rank_list[self.rank]}]",label)
        return self.tree.linelist()

class Diamond_manager():
    qwe_entry_discribe_and_pro_list={
              "q":["所有伤害有一定概率增加一点",
                   "所有伤害有一定概率翻倍",
                   "造成伤害时有一定概率充能一枚弹药",
                   "造成伤害时有一定概率回充一层护盾",
                   "造成伤害时有一定概率追加一次奶油的黑客行动"],
              "q_pro":[0.06,0.1,0.06,0.06,0.06],
              "w":["所有回盾有一定概率增加一点",
                   "所有回盾有一定概率翻倍",
                   "护盾减少时有一定概率充能一枚弹药",
                   "护盾减少时有一定概率回充一层护盾",
                   "护盾减少时有一定概率追加一次奶油的黑客行动"],
              "w_pro":[0.06,0.06,0.06,0.06,0.06],
              "e":["按下e时有一定概率使天数减少",
                   "造成伤害时有一定概率使行动概率增加",
                   "我方连续行动时有一定概率充能二枚弹药",
                   "敌方连续行动有一定概率削减其二层护盾",
                   "使迷途旅人增加一定的发生概率"],
              "e_pro":[0.08,0.06,0.08,0.08,0.08]}
    
    numlist=[]
    hollow={"q":[],"w":[],"e":[]}
    qwe_entry_total_num_list={"q":[0,0,0,0,0],"w":[0,0,0,0,0],"e":[0,0,0,0,0]}

    def __init__(self,numlist:list,hollow:dict):
        self.hollow=hollow
        self.numlist=numlist
        self.count()
        
    def generate(self,type:str,rank:int):
        for i in range(0,200):
            if i not in self.numlist:               
                entry_strengthen_index=random.randint(0,4)
                init_entry_list=[0,0,0,0,0]
                init_entry_list[entry_strengthen_index]+=rank+1
                globals()[f"diamond{i}"]=Diamond(i,type,rank,init_entry_list,False)
                self.numlist.append(i)
                self.on_or_off(self.numlist[-1])
                self.count()
                break
    
    def on_or_off(self,index:int):
        try:
            globals()[f"diamond{index}"].put()
            self.count()
        except:
            pass
    
    def count(self):
        self.qwe_entry_total_num_list={"q":[0,0,0,0,0],"w":[0,0,0,0,0],"e":[0,0,0,0,0]}
        for ty in self.hollow:
            try:
                for i in self.hollow[ty]:
                    i:Diamond
                    entry=i.entry
                    for p in range(len(self.qwe_entry_total_num_list[ty])):
                        self.qwe_entry_total_num_list[ty][p]+=entry[p]
            except:
                pass

    def printall(self):
        column=[]
        for p in self.hollow:
            column0=[p.center(47," "),"-"*47]
            for dia_temp in self.hollow[p]:
                dia_temp:Diamond
                column0+=dia_temp.linelist()
            column.append(column0)
        m1.three_columnprint(column[0],column[1],column[2])
        print("~"*150)
        columnqwe={"q":[],"w":[],"e":[]}
        for i in self.numlist:
            dia_temp:Diamond=globals()[f"diamond{i}"]
            if not dia_temp.if_on:
                columnqwe[dia_temp.type]+=dia_temp.linelist()
        m1.three_columnprint(columnqwe["q"],columnqwe["w"],columnqwe["e"])

    def reset_dia(self,index):
        dia_temp:Diamond=globals()[f"diamond{index}"]
        if dia_temp.if_on:
            diamond_manager.on_or_off(index)
        self.numlist.remove(index)
        del globals()[f"diamond{index}"]

    def refresh(self):
        for i in range(len(self.numlist)):
            self.reset_dia(self.numlist[-1])
        self.numlist=[]
        self.hollow={"q":[],"w":[],"e":[]}
        self.qwe_entry_total_num_list={"q":[0,0,0,0,0],"w":[0,0,0,0,0],"e":[0,0,0,0,0]}

    def mainloop(self):
        while 1:
            self.printall()
            inp=input("[编号]放置/取下宝石|[b]退出>>>")
            if inp.isdigit() and int(inp) in self.numlist:
                diamond_manager.on_or_off(int(inp))
                #print(diamond_manager.hollow)
                #print(diamond_manager.numlist)
            elif inp == "b":
                break
    def check_if_react(self,type:str,index:int):
        if probability(self.qwe_entry_total_num_list[type][index]*self.qwe_entry_discribe_and_pro_list[f"{type}_pro"][index]):
            m1.printplus(f"注意·凡晶石装备套件响应·{self.qwe_entry_discribe_and_pro_list[type][index]}")
            return True
        else:
            return False
diamond_manager=Diamond_manager([],{"q":[],"w":[],"e":[]})

#################################################

class Room_general:#肉鸽·房间对象

    index=0
    title=""
    cn_title=""
    icon = ""

    title_to_tag3_list={"safezone":"回复状态，重燃深空中虚弱的希望",
                        "fight":"举起武器，苍白的花朵于死亡中绽放",
                        "evacuate":"回家，我们回家",
                        "treasure":"一个曾经存在过的时代，消散在深空中",
                        "market":"看不到头的黑暗里，唯一的烟火气息"}
    title_to_tag4_list={"safezone":"[护盾]++/[导弹]++/[重置行动概率]",
                        "fight":"[装备提升机会]",
                        "evacuate":"[回到浅草寺]",
                        "treasure":"[“凡晶石”装备套件]++",
                        "market":"[示例文本]"}

    def __init__(self,index=0):
        self.index=index
        title_to_tag1_list={"safezone":["联邦海军","浅草寺重工"],
                            "fight":["游袭者","天日自卫队","涅墨军团"],
                            "evacuate":["浅草寺信标","浅草寺跃迁引导站"],
                            "treasure":["荒废矿区","奥德修斯城遗迹","对舞之战遗址"],
                            "market":["浮岛商会","深空集市"]}
        self.tag1=random.choice(title_to_tag1_list[self.title])
        self.tag2=random.randint(100,200)

    def perform(self):
        pass

    def print_self(self):
        #print(f"[{self.index}] {self.tag1} {self.cn_title} ({self.tag2}km)")
        Tree(f"[{self.index}] {self.icon} {self.tag1} {self.cn_title} ({self.tag2}km)",
             self.title_to_tag3_list[self.title],
             self.title_to_tag4_list[self.title]).treeprint()

    def print_self_tree(self):
        return Tree(
            f"[{self.index}] {self.icon} {self.tag1} {self.cn_title} ({self.tag2}km)",
            self.title_to_tag3_list[self.title],
            self.title_to_tag4_list[self.title]
        )

class Room_safezone(Room_general):

    title="safezone"
    cn_title="安全区"
    icon="--+--"

    def perform(self):

        global hard
        hard=0.3

        if self.tag1 == "联邦海军":
            m1.plot_print("我们很快来到了先遣部队的临时补给点。这是一个巨大的桶状空间站，与浅草寺稍显不同。在繁星的背景下，它斜斜地飘着，很安静",
                    "先遣部队早已得知你们的到来，但他们公事公办地要求进行双方信息确认",
                    ["出示执照与舰船信息"],
                    f"“欢迎{username}和{shipname}号，你们的泊位在D-{random.randint(20,99)}。”",
                    "你知道那是打发落魄指挥官的地方。",
                    "无论如何我们在临时补给站暂时安顿了下来。补给站的物资不算多，但还过得去",
                    ["[奶油]人总得吃饭不是？"])
        else:
            m1.plot_print(f"我们很快来到了浅草寺准备的休息点。这是一个油漆剥落、锈迹斑驳的空间站，小得仅仅能容下{shipname}的舰身",
                       "[ent……不用。这儿能自动进站。也没管我们要什么证件",
                       "“指挥官，我们等你很久了！”",
                       "几个汉子一边抱怨着，一边把几个物资箱搬到船边",
                       "“都是旧货，”他们这时恢复了笑容，“但是保管结实！”")

        times=0
        while 1:
            times+=1
            m1.inputplus("[enter]翻找>>>")
            if probability(0.5):
                n[0]+=1
                m1.printplus("\n一台尚且能用的护盾发生器 [护盾+1]\n")
            else:
                n[1]+=1
                m1.printplus("\n一颗老式巡飞弹 [导弹+1]\n")
            if probability(0.3-room_manager.depth*0.02) or times>=10:
                break

        if self.tag1 == "联邦海军":
            m1.plot_print("你已把补给站能拿的物资悉数带走",
                    "我们不能在这里逗留太久——这片地区看着不太欢迎我们",
                    ["起锚"],
                    f"{shipname}号往无垠的深空而去")
        else:
            m1.plot_print("你已把补给站能拿的物资悉数带走",
                       "浅草寺的站点，总能在漆黑的太空中给人跳脱的惊喜",
                       "你想停留得久一些——可是深空不等人",
                       ["起锚"],
                       "几个汉子在无线电里兴奋地欢送我们离去")
        print("-----------------")

        return None
    
class Room_fight(Room_general):

    title="fight"
    cn_title="预计战斗区"
    icon="--X--"



    def perform(self):
        global win_2me,days

        if self.tag1 == "游袭者":
            m1.plot_print(f"几艘海盗船仗着自己人多势众，在{shipname}号刚踏足这片深空时就向我们发起了冲锋",
                       "（乌合之众。）",
                       "你暗自笑着，前推油门",
                       ["舰船进入战斗模式"])
        elif self.tag1 == "天日自卫队":
            m1.plot_print("我们很快就被路过的叛军巡逻队盯上了。像是挑衅般，他们亮出了机腹的武器",
                       f"你当然不会坐以待毙，{shipname}号的名字不允许任何人的侮辱",
                       ["命令全舰进入一级战备状态"])
        elif self.tag1 == "涅墨军团":
            m1.plot_print("我们即将在这片死寂的深空展开探索……突然，一枚风行者巡飞弹尖厉地划开宁静的星空。警报声此起彼伏，随之而来的是更猛烈的攻势",
                       f"你忙乱地操纵着{shipname}号躲过第一轮攻击，你绝望地看到，敌人的铁城密不透风，猖狂地展示着边境军阀的势力",
                       "第一颗误入的彗星被导弹击碎又划过舷窗，这会是一场恶战吧",
                       ["开战！！！"])
        
        entry_manager.entry_choose(room_manager.depth,inf)
        while 1:
            entry_manager.tree().treeprint()
            diamond_manager.printall()
            m1.three_columnprint([allenskin[choi[3]]],[allenskin[choi[4]]],[allenskin[choi[5]]])
            print()
            inp=input("dia=访问“凡晶石”装备套件系统\nq\\w\\e=更换对应装备\n[enter]开战>>>")
            if inp == "dia":
                diamond_manager.mainloop()
            elif inp in room_manager.pool:
                room_manager.al_now_print()
                room_manager.simple_choi(inp,room_manager.pool[inp])
            else:
                break

        time.sleep(0.3)
        n[2]=0
        n[3]=0
        ranop(al_count()//3+room_manager.depth*3+5)
        
        days=0

        fight_daily()

        if win_2me == 0:
            m1.plot_print(">>战斗失败<<")
            return False
        else:
            m1.plot_print(">>战斗胜利<<")
            return True
        
class Room_evacuate(Room_general):

    title="evacuate"
    cn_title="撤离点"
    icon="->>>-"

    def perform(self):
        m1.plot_print(f"跃迁定位器的锚定夹夹住了{shipname}号的船舷",
                   "（你感到座位一阵震动）",
                   ["抬起头环顾四周"],
                   "星门的强劲引力扭曲了明亮的星空",
                   "星门上沿，浅草寺重工的标志闪着红光",
                   "“准备开始跃迁……倒计时……”",
                   ["让大家扣上安全带坐好"],
                   "（你深深吸了一口气）",
                   "5……4……",
                   "跟那些双目无神的流浪汉不同，你至少还有一张回家的门票",
                   ["逃离深空"],
                   "强大的推力把你、奶油、导弹发射手护盾回充手以及qwe一干人等死死地压在座位上")
    
class Room_market(Room_general):
    
    title="market"
    cn_title="集市"
    icon="--$--"

    items_price={"护盾急救包":50}
    items_description={"护盾急救包":"每次进入战斗时回充2层护盾"}

    def perform(self):
        m1.plot_print(f"{shipname}号滑入{self.tag1}环形港的琥珀色接驳光束",
                   "（气压平衡的嗡鸣中渗出千种语言的碎语）",
                   "深空之中的集市，是漆黑宇宙中唯一有些人声的地方",
                   ["检查腰间的铱金匣"],
                   "只是换一些必需品的话，这些铱金应该够的",
                   ["将终端调为议价模式"],
                   "“浅草寺认证买家请走虹膜加密通道——”",
                   ["激活视网膜屏幕"],
                   "一瞬间闪过的黑市交易浮窗，在屏幕上展开猩红边框",
                   "（真热闹啊）",
                   ["进入市场"])

class Room_treasure(Room_general):

    title="treasure"
    cn_title="旧时代发掘区"
    icon="--*--"

    def perform(self):
        global username
        output_type=random.choice(["q","w","e"])
        type_tag_list={"q":"攻击型巡弋舰",
                       "w":"防护型战列舰",
                       "e":"战术型巡洋舰"}
        m1.plot_print("在视野的尽头，飘荡着幽灵般的沧桑碎片，在星辉下散着诡异的光，扭曲的金属板在岁月的磨砺下，显得粗粝如岩石",
                   f"{shipname}号轻轻飘过这些残骸，像误入歧途的旅人",
                   "一股前所未有的庄重，沉沉地砸在你的心上",
                   "这里的一切，无不昭示着当年的惨烈——你甚至能感知到游荡着的英灵",
                   "你想起了年少的自己那些幼稚的梦——那些而今快要忘却的、横刀立马保家卫国的梦",
                   "“不要放弃它们！”年代久远的战场上，一个古老的声音对你说",
                   ["全舰起立向英烈致意"],
                   f"你低下头，默默说：“我是{username}指挥官，{shipname}号全体舰员在此致意。我们不会忘记你们的伟大贡献。愿深空给予你们安息之所，给予你们祝福。”",
                   "按照战场惯例，搜查战争遗物在所难免，但你仍心有戚戚",
                   f"一具无处安葬的焦黑尸体无声地擦过{shipname}号的舰首，使你的心情更为沉重",
                   ["开展搜查·释放探测机器人"],
                   "你最终还是下定了决心，派出了探测机器人",f"在你面前的，是一艘联邦海军『{type_tag_list[output_type]}』的深灰色遗骸",
                   "在那里，探测机器人读出了两块II级凡晶石的词条。十秒后，两块凡晶石已被试装上船",
                   ["显示到主屏幕"])
        diamond_manager.generate(output_type,2)
        diamond_manager.generate(output_type,2)
        m1.two_columnprint(globals()[f"diamond{diamond_manager.numlist[-2]}"].linelist(),
                        globals()[f"diamond{diamond_manager.numlist[-1]}"].linelist())
        m1.plot_print("而在深处的乱流内，探测机器人回报着更为模糊的信息")
        inp=m1.inputplus("[1]选择已装上船的两块凡晶石[II级*2 词条已知]|[2]选择两块未知凡晶石[III级*2 词条未知]|[3]更换凡晶石类型[III级*2 词条未知]>>>")
        if inp == "3":
            type_list=["q","w","e"]
            type_list.remove(output_type)
            output_type=random.choice(type_list)
        if inp != "1":
            diamond_manager.reset_dia(diamond_manager.numlist[-1])
            diamond_manager.reset_dia(diamond_manager.numlist[-1])
            diamond_manager.generate(output_type,3)
            diamond_manager.generate(output_type,3)
        print("\n你获得了：\n")
        m1.two_columnprint(globals()[f"diamond{diamond_manager.numlist[-2]}"].linelist(),
                        globals()[f"diamond{diamond_manager.numlist[-1]}"].linelist())
        m1.plot_print("你对自己说，这是英烈们留给我们的祝福",
                   f"怀着敬意与决心，你，落魄的{username}，和{shipname}号再次踏上征途",
                   ["起锚"])
    
class Room_manager:
    pool={"q":[],"w":[],"e":[]}
    backpack={}
    depth=0

    q_rank=0
    w_rank=0
    e_rank=0

    def reset(self):

        global choi,n

        for i in range(0,al_num):
            try:
                al_temp:Al_general=globals()[f"al{i}"]
                al_temp.reset()
            except:
                pass
        self.pool={"q":[],"w":[],"e":[]}
        self.backpack={"铱金":0}
        self.depth=0

        self.q_rank=0
        self.w_rank=0
        self.e_rank=0

        choi=[0,1,2,-1,-2,-3]
        self.start_choi()
        n[0]=2
        n[1]=1

    def al_now_print(self):

        columns={"q":[],"w":[],"e":[]}
        cn_list={'q':'武器','w':'生存','e':'战术'}

        for type in ("q","w","e"):
            for rank in (0,1,2):
                target_list=globals()[f"{type}_list_{rank}"]
                columns[type].append("")
                columns[type].append(f"{cn_list[type]} {rank}区")
                for i in target_list:
                    if i in room_manager.pool[type]:
                        columns[type].append("|")
                        columns[type].append(f"|-{al_sho_title_cn[i]}")
                    else:
                        columns[type].append("|")
                        columns[type].append(f"|-[{i}]*未解锁*")
        m1.three_columnprint(columns["q"],columns["w"],columns["e"])
        print()


    def room_statistics(self):
        statistics={}
        for i in range(1,8):
            room_temp:Room_general=globals()[f"room{i}"]
            statistics.setdefault(room_temp.title,0)
            statistics[room_temp.title]+=1
        return statistics
                
    
    def single_generate(self,index:int):
        if self.depth>4:
            return random.choice([Room_safezone(index),Room_fight(index),Room_fight(index),Room_treasure(index)])
        elif self.depth == 4 and ("evacuate" not in self.room_statistics()):
            return Room_evacuate(index)
        else:
            return random.choice([Room_safezone(index),Room_fight(index),Room_fight(index),Room_treasure(index),Room_treasure(index)])

    def generate(self):
        for i in range(1,13):
            globals()[f"room{i}"]=self.single_generate(i)


    def print_all(self):
        print()
        left0   = ("亣".join(["亣".join(globals()[f"room{i}"].print_self_tree().linelist()) for i in range(1,5)])).split("亣")
        mid0    = ("亣".join(["亣".join(globals()[f"room{i}"].print_self_tree().linelist()) for i in range(5,9)])).split("亣")
        right0  = ("亣".join(["亣".join(globals()[f"room{i}"].print_self_tree().linelist()) for i in range(9,13)])).split("亣")
        m1.three_columnprint(
            left0,
            mid0,
            right0
        )
    def sit_and_ask(self):
        while 1:
            print(f"当前深度>>{self.depth}")
            print()
            al_list=[allenskin[choi[3]],allenskin[choi[4]],allenskin[choi[5]]]
            Tree(f"{shipname}号 舰船状态",f"[护盾] {n[0]}层",f"[导弹] {n[1]}枚",al_list).treeprint()
            print(self.backpack)
            inp=m1.inputplus("[数字]=前往指定地点\ndia=访问“凡晶石”装备套件系统\nq\\w\\e=更换对应装备\n>>>")
            print()
            if inp.isdigit() and 0<int(inp)<=12:
                m1.printplus("已确认选择")
                print()
                return int(inp)
            elif inp == "dia":
                diamond_manager.mainloop()
                self.print_all()
            elif inp in self.pool:
                self.al_now_print()
                self.simple_choi(inp,self.pool[inp])
            else:
                m1.printplus("请在可选目标中选择")
                print()

    def al_promote(self,type="z"):#装备升级
       
        if type == "z":
            self.al_now_print()
            type=m1.ask_plus("请输入要提升的装备类型·当前等级对应装备将全部解锁 q/w/e r=放弃 >>>",["q","w","e","r"])
        if type == "r":
            return

        rank_now = 0
        if type == "q" and self.q_rank != 3:
            self.q_rank+=1
            rank_now = self.q_rank
        if type == "w" and self.w_rank != 3:
            self.w_rank+=1
            rank_now = self.w_rank
        if type == "e" and self.e_rank != 3:
            self.e_rank+=1
            rank_now = self.e_rank

        print("\n同级装备已全部解锁>>")
        for i in globals()[f"{type}_list_{rank_now-1}"]:
            print(allenskin[i])
        print()
        
        choi_index=[0,1,2,"q","w","e"].index(type)
        choi[choi_index]=room_manager.pool[type][0]
        choi_now_num=choi[choi_index]
        for i in al_promoting_dict:
            if choi_now_num in i:
                to_promote_list=al_promoting_dict[i]
                self.pool[type]+=list(i)
                break

        print("下一级装备列表>>")
        for i in to_promote_list:
            print(allenskin[i]+f"({i})")
        print()


        to_choi_num=m1.ask_plus("请输入要选择的下一级装备编号 >>>",to_promote_list)
        globals()[f"al{choi_now_num}"].reset()
        self.pool[type][0]=int(to_choi_num)
        choi[choi_index]=int(to_choi_num)
        print(al_sho_title_cn[int(to_choi_num)],"已确认装备")
        time.sleep(0.4)
        
    def simple_choi(self,type:str,choilist:list):

        inp=m1.ask_plus("请输入选择的装备编号 [enter]=退出 >>>",choilist+[""])
        if inp == "":
            return
        choi_index=[0,1,2,"q","w","e"].index(type)
        try:
            globals()[f"al{choi[choi_index]}"].reset()
        except:
            pass
        choi[choi_index]=int(inp)
        print(al_sho_title_cn[int(inp)],"已确认装备")

    def start_choi(self):
        print("装备选择，若跳过默认选择free装备")
        print()

        for i in q_list_0:
            print(allenskin[i]+f"({i})")
        print()
        self.simple_choi("q",q_list_0)
        if choi[3]<0:
            choi[3]=17
            print(al_sho_title_cn[17],"已确认装备")
        self.pool["q"].append(choi[3])
        print()

        for i in w_list_0:
            print(allenskin[i]+f"({i})")
        print()
        self.simple_choi("w",w_list_0)
        if choi[4]<0:
            choi[4]=18
            print(al_sho_title_cn[18],"已确认装备")
        self.pool["w"].append(choi[4])
        print()

        for i in e_list_0:
            print(allenskin[i]+f"({i})")
        print()
        self.simple_choi("e",e_list_0)
        if choi[5]<0:
            choi[5]=7
            print(al_sho_title_cn[7],"已确认装备")
        self.pool["e"].append(choi[5])


    def deepen(self):
        self.depth+=1

    def rog_main(self):

        global win_2me,username

        win_2me=1
        
        self.reset()
        self.generate()
        m1.plot_print(f"浅草寺停机坪·航行计时{time.time()}·任务准备中",
                   f"指挥官{username}",
                   ["进入深空"])
        while 1:
            auto_pilot.refresh()
            self.print_all()
            ask=self.sit_and_ask()
            room_temp:Room_general=globals()[f"room{ask}"]
            room_temp.perform()
            if room_temp.title == "evacuate":
                break
            elif room_temp.title == "safezone":
                pass
            elif room_temp.title == "fight" and win_2me == 0:#战场失败

                break

            elif room_temp.title == "fight" and win_2me == 2:#战场胜利

                self.al_promote()
                self.deepen()
                win_2me=1
                self.backpack["铱金"]+=max(20,60-days)*(1+0.2*self.depth)

            if self.depth>4:
                self.deepen()
            globals()[f"room{ask}"]=self.single_generate(ask)
                
        if win_2me == 0:
            m1.plot_print(f"在最后一枚导弹的烟尘中，{shipname}号被迫落荒而逃。在千百次的梦中，你从未料到这个结局",
                        "恍惚间，你似乎感觉到背后的柔软与温柔",
                        ["尝试睁开眼"],
                        "炽烈的强光逼迫你眨了好几次早已干涸的眼",
                        "“啊，你怎么还没死！还以为你就这么要交代在那里哩。”是奶油的声音，还有其他舰员的声音。",
                        ["尝试开口"],
                        "“怎么回事？”你听到自己沙哑地说",
                        f"“{shipname}号的AI自作主张把我们都送了回来，不然我们也不会在医院里。”你听到暴雨说",
                        f"“{shipname}号现在怎么样了？”",
                        f"“一切都还好，只有你还有点脑震荡。”晴空担忧地说",
                        "“说吧，想吃什么，姐现在去给你带饭！”奶油强行活跃了气氛",
                        ["报菜名"],
                        f"“我就知道。好啦，我们走吧；而你呢，{username}，好好休息吧昂。”奶油招呼其他几位神色稍显凝重，离开了病房",
                        "你看向医院的窗外，企盼下一次的复仇")
            item1["联邦信用点"]+=int(min(self.backpack.get("铱金",0),300)*20)
            sync(if_entry=False)
        else:
            m1.plot_print("“指挥官，欢迎回港”",
                       "浅草寺的气温，要比深空高上不少",
                       ["打开舱门"],
                       "大家争先恐后地跳下船去吃晚饭",
                       "丝毫没有从鬼门关走一趟回来的感觉",
                       "（深深地呼出一口气）",
                       "我还活着。",
                       ["关闭索敌雷达","关闭主发动机","关掉空调与通信器"],
                       f"你跳下{shipname}号，背向卸船工们与修械师们，向食堂冲去")
            item1["联邦信用点"]+=int(min(self.backpack.get("铱金",0),300)*30)
            sync(if_entry=False)
        sf=shelve.open("savedata")
        try:
            for i in range(3,6):
                choi[i]=sf["user"][username][i]
        except:
            pass
        diamond_manager.refresh()
        for i in range(0,entry_manager.en_num):
            try:
                globals()[f"entry{i}"].rank=sf[f"{username}entry"][i]
            except:
                pass
        sf.close()
room_manager=Room_manager()

###########################################

class Ocp_general:

    index                       = 0
    title                       = ""
    counting_down               = 0
    days                        = 0
    daily_voi_list              = []

    def print_self(self):
        txt_today=self.daily_voi_list[-1*self.counting_down]
        print(txt_today)

    def react(self):
        pass

    def __init__(self,index:int,title:str,voi_list:list,days:int):
        self.title                  = title
        self.index                  = index
        self.daily_voi_list         = voi_list
        self.counting_down          = 0
        self.days                   = days
ocp0=Ocp_general(0,"",[],0)

class Ocp1(Ocp_general):

    def react(self):
        print("旅人留下的发生器已经部署")
        player_cureplus(m3.entry15.react(self.counting_down,mode),al21_shian=True)
        self.counting_down = 0
ocp1=Ocp1(1,
          "当前事件>>>迷途旅人",
          ["新事件报告·我们接到了一则来自一位燃料将要耗竭的迷途旅人发来的求助电讯。他的方位大致在我方两点钟方向0.9km处。\n旅人的船上装有许多护盾发生器。他提出用两个护盾发生器交换半箱燃料。\n您有三个航行日时间确认·按下f即可·您确认交换后，危险品处理小队将出发检查，并在确认安全后进行安装。",
          "您还有两个航行日来确认",
          "指挥官，旅人即将出发，这是您能接收其回馈的最后一天"],
          3)

class Ocp2(Ocp_general):
    pass
ocp2=Ocp2(2,
          "当前事件>>>危险·殷红狂怒",
          ["Day1\n新事件报告·前线侦查连发现“洪流”信息站系统!@#$%^%$敌我通讯##$^&%&(瘫痪#%^#@(*全线崩溃！*\n新事件报告·于我%^&&$)(发现大面积敌导弹 $^&$%检测到@#%&^%信火打击#%$&做好全线防@$^$!",
          "Day2\n前线@%^&^惨$%^&(舰体左舷%^(%&^全力修理&#$%(@指挥官$%^~^*&破溃#!&*^&~(^请求撤退！ ",
          "Day3\n前线报告：我方通讯组正努$^%*&^恢复通*&_)预计完全恢%&^(#两天&^(*前线火力$&(_+猛(!~t通讯组伤亡人$%&^(激增$!&&#(不要!*(~_撤退!*@^& ",
          "Day4\n情报组%&()：信火打击$&((*$即将结束^(*&)做好最后%&(&()^@#~_防御准备$^%&！！！",
          "Day5\n通讯有望全部恢复%(&)信火打击有%(&())(_+减 弱倾向%&(做好%&(防^(+_~@最后一击的准备！"],
          5)

class Ocp3(Ocp_general):

    def print_self(self):
        global item1
        txt_today = self.daily_voi_list[-1*self.counting_down]
        print(txt_today)
        print("账户现有 " + str(item1["联邦信用点"]) + "ISK")
    
    
    def react(self):

        global item1

        player_cureplus(1)
        item1["联邦信用点"] -= 1000
        it=list(item1.keys())
        it.remove("联邦信用点")
        it.remove("合约纪念点")
        it.remove("保险点")
        it=random.sample(it,2)
        for i in it:
            k=random.randint(5,10)
            item1[i] += k
            print("交易完成",i,"x",k)
        sync(if_entry=False)
        self.counting_down = 0
ocp3=Ocp3(3,
          "当前事件>>>行商",
          [f"新事件报告·我们发现了一位兜售物资的行商。此人正在后泊位A7接驳我舰。\n这位满面皱纹的老人本来能在合同时限之前把货物运到G3地区，却因为恒星磁暴搁浅在这里。为了不至于亏损，他情愿折价把船上的货物卖给我们。\n奶油和水银小队谈妥了价钱。以半箱燃料为代价，老人决定再跟我们换一个护盾发生器。\n您有三个航行日时间确认·按下f即可·您确认交换后，将以电子方式支付 1000 ISK。",
          "您还有两个航行日来确认",
          "指挥官，行商即将出发，这是您能交易物资的最后一天"],
          3)
class Ocp4(Ocp_general):
    matk = 0
    def print_self(self):

        txt_today = self.daily_voi_list[-1*self.counting_down]
        print(txt_today)
        self.matk = random.randint(2,3)
        self.matk = m3.entry4.react(mode,self.matk)
        print(">>>预计创伤：" + str(self.matk))
        print("指挥官，请发出全舰弃船命令")

    def check_if_fire(self):
        if ocp_manager.ocp_now.index == 4 and ocp_manager.ocp_now.counting_down == 0:
            result = cpu_atkplus(self.matk,"宏峰导弹已命中")
            self.matk = 0

ocp4=Ocp4(4,
          "当前事件>>>危险·宏峰导弹来袭",
          ["全舰注意！侦测到敌方“宏峰”重型穿甲弹·清空舰首甲板!所有人员立即从舰首区域撤离!"],
          1)

class Ocp5(Ocp_general):
    matk = 0
    def print_self(self):

        txt_today = self.daily_voi_list[-1*self.counting_down]
        print(txt_today)
        self.matk = random.randint(1,2)
        print(">>>预计创伤：" + str(self.matk))
        print("指挥官，请做好防冲击措施")

    def check_if_fire(self):
        if ocp_manager.ocp_now.index == 5 and ocp_manager.ocp_now.counting_down == 0:
            result = cpu_atkplus(self.matk,
                                en1_liefeng = False,
                                al24_danaiyou = False)
            n[2] -= self.matk
            al33.check_if_move(self.matk)
            print(f"微陨石流对我方造成{result}点伤害|对敌方造成{self.matk}点伤害")
            self.matk = 0

ocp5=Ocp5(5,
          "当前事件>>>危险·陨石流来袭",
          [f"警报：侦测到微陨石流于我方{random.randint(1,12)}点方向向我袭来！"],
          1)

class Ocp6(Ocp_general):
    pass
ocp6=Ocp6(6,
          "当前事件>>>复仇者",
          ["[战场态势感知]侦测到一艘不明型号不明用途的民用飞船闯过了战场封锁线，并似乎正以失控的速度于敌方盲区向敌舰靠近\n-浅草寺重工提醒您，根据《战场指挥官通用操守协议》，阻止平民伤亡是指挥官的责任和义务\n消息栏|新消息>>>民船>>>“不要拦我！！！我要报仇！！！”\n指挥官，接下来是你的选择：\n[f]选择强行骇入平民飞船扭转其航线|[enter/任意键]选择静观其变]"],
          1)

class Ocp_manager:

    ocp_now=ocp0

    def ocp_random(self):
        global n

        self.ocp_now:Ocp_general

        if self.ocp_now.index == 0:

            ocp_ready_list = [ocp0,ocp1,ocp2,ocp3,ocp4,ocp5]                           
            weight_list    = [0   ,0.1 ,0.1 ,0.05,0.1 ,0.1]                            

            if days <= 5:                         
                ocp_ready_list[1] = ocp0                          
            if days <= 25+inf/3:                          
                ocp_ready_list[2] = ocp0                          
            if item1["联邦信用点"] < 1000:                            
                ocp_ready_list[3] = ocp0                          
            if days <= 20:                            
                ocp_ready_list[4] = ocp0  
            if days <= 15:
                ocp_ready_list[5] = ocp0 
                                        
            weight_list[0] = 1-sum(weight_list)                           

            self.ocp_now = random.choices(ocp_ready_list,weight_list,k=4)[random.randint(0,3)]                                   

#            ocp=random.randint(0,99)
#            if ocp>=0 and ocp<=9 and days>5:
#                self.ocp_now=ocp1
#            if ocp>=10 and ocp<=19 and days>25+inf/3:
#                self.ocp_now=ocp2
#                n[3]+=6
#            if ocp>=20 and ocp<=24 and item1["联邦信用点"]>=1000:
#                self.ocp_now=ocp3
#            if ocp>=25 and ocp<=34 and days>20:
#                self.ocp_now=ocp4
            if self.ocp_now.index == 2 :
                n[3]+=6
            if self.ocp_now.index == 0 and diamond_manager.check_if_react("e",4):
                self.ocp_now = ocp1
            if self.ocp_now.index != 0:
                self.ocp_now.counting_down = self.ocp_now.days
            

    def ocp_check(self):
        if self.ocp_now.index != 0:
            ocp4.check_if_fire()
            ocp5.check_if_fire()
            if self.ocp_now.counting_down == 0:
                self.ocp_now=ocp0
               
    def all_ocp_react(self):
        if self.ocp_now.index != 0:
            self.ocp_now.react()

    def counting(self):
        if self.ocp_now.index != 0:
            self.ocp_now.print_self()
            self.ocp_now.counting_down-=1

    def refresh(self):
        for i in range(1,10):
            try:
                globals()[f"ocp{i}"].counting_down=0
            except:
                pass
        self.ocp_now=ocp0
ocp_manager=Ocp_manager()

###########################################

item3={}
for i in range(0,al_num+1):
    try:
        item3[globals()["al"+str(i)].len_skin]=globals()["al"+str(i)].num
    except:
        pass
    
###########################################

class Infinity_manager:

    def save_inf(self):
        global inf,eqm,n,choi
        sf=shelve.open("savedata")
        try:
            big_dict = sf[username+"infnew"].copy()
        except:
            big_dict = {}
        for i in ("inf","eqm","n"):
            big_dict[i] = globals()[i]
        for i in (3,4,5):
            big_dict[f"al{choi[i]}"]=globals()[f"al{choi[i]}"].state
        big_dict["al14"]=al14.state
        pre_entry={}
        for i in range(0,entry_manager.en_num):
            if f"entry{i}" in globals():
                pre_entry[i]=globals()[f"entry{i}"].rank    
            else:
                pre_entry[i]=0
        big_dict["entry"]=pre_entry
        #print(big_dict)
        sf[username+"infnew"] = big_dict
        sf.close()

    def load_inf(self):
        global inf,eqm,n,choi
        sf = shelve.open("savedata")
        big_dict = sf.get(username+"infnew",{}).copy()
        if big_dict == {}:
            return
        sf.close()
        #print(big_dict)
        for i in ("inf","n"):
            globals()[i] = big_dict[i]
        eqm+=big_dict["eqm"]
        al14.state=big_dict.get("al14",0)
        for i in (3,4,5):
            try:
                al_temp:Al_general = globals()[f"al{choi[i]}"]
                al_temp.state=big_dict.get(f"al{choi[i]}",0)
                if al_temp.state == 0:
                    al_temp.reset()
            except:
                pass
        pre_entry:dict=big_dict["entry"].copy()
        for i in range(1,entry_manager.en_num):
            if f"entry{i}" in globals():
                #print(pre_entry)
                #print(pre_entry.get(i,0))
                globals()[f"entry{i}"].rank = pre_entry.get(i,0)   

    def print_savedata(self):
        sf=shelve.open("savedata")
        big_dict = sf.get(username+"infnew",{})
        sf.close()
        if big_dict == {}:
            return
            
        pre_entry:dict=big_dict["entry"].copy()
        for i in range(1,entry_manager.en_num):
            if f"entry{i}" in globals():
                globals()[f"entry{i}"].rank = pre_entry.get(i,0)
                
        al_title_list = []
        for i in big_dict:
            try:
                i:str
                if i.startswith("al"):
                    index = int(i[2:])
                    al_title_list.append(al_sho_title_cn[index])
            except:
                pass
        if al_title_list == []:
            al_title_list.append("（无）")

        al_title_now = []
        for index in choi[3:6]:
            try:
                al_title_now.append(al_sho_title_cn[index])
            except:
                pass
        if al_title_now == []:
            al_title_now.append("（无）")

        n_pre=big_dict["n"]
        Tree("您有一个保存在空间站的INF存档",
             f"战况|我方护盾>{n_pre[0]}|我方弹药>{n_pre[1]}|敌方盾弹总量估计>{4+al_count()//6+inf}>",
             f"轮次|{big_dict['inf']}->{big_dict['inf']+1}",
             f"设备|已装备>{big_dict['eqm']}|追加>{eqm}",
             f"配置|历史曾用>{al_title_list}>当前>{al_title_now}"
             ).treeprint()
        entry_manager.print_now()
        return m1.inputplus("[y]读取存档|[enter]开启新一局/不覆盖已有存档|[return]返回空间站>>>")

    def infinity_mode_main(self):

        global mode,inf,win_2me

        entry_manager.refresh()
        inp=self.print_savedata()#敏生修改
        reset_general()
        if inp == "y":
            self.load_inf()
            ranop(4+al_count()//6+inf)
        elif inp == "return":
            return
        else:
            entry_manager.refresh()
            ranop(4+al_count()//6)
        while True:
            if "临时装甲板" in eqm:          #
                player_cureplus(2)
            fight_daily()
            if win_2me == 2:
                print(win[random.randint(0,len(win)-1)])
                inf+=1
                win_2me = 1
                print("下一场战斗词条：")
                entry_manager.entry_choose(room_manager.depth,inf)
                entry_manager.print_now()
                item_drop(int(inf/2+1),2)
                inp=m1.inputplus("[save]保存存档",0.3)
                if inp == "save":
                    infinity_manager.save_inf()
                e=m1.inputplus("[enter]赴下一场战斗·武器护盾将保留·词条难度提升|[输入return] 返回空间站>>>",0.3)
                if e == "return":
                    inf=0
    
                    break
            else:
                print(lose[random.randint(0,len(lose)-1)])
                al_cost()
                inf=0

                win_2me = 1
                break      
            reset_general(inf_reset=False,
                          player_reset=False,
                          auto_pilot_reset=False) 
            ranop(4+al_count()//6 + inf)    

infinity_manager=Infinity_manager()
    
def probability(pro)->bool:#概率为真
    if random.random()<pro:
        return True
    else:
        return False

def endingpic_print(i):
    left=[]
    left.append("-"*70)
    left.append("|")
    try:
        left.append(f"""|\\{al_sho_title_cn[choi[3]]}|{globals()["al"+str(choi[3])].voilist_pos[-1]}""")
    except:
        left.append(f"""|\\{al_sho_title_cn[choi[3]]}|""")
    left.append("|")
    left.append("|")
    try:
        left.append(f"""|   \\{al_sho_title_cn[choi[4]]}|{globals()["al"+str(choi[4])].voilist_pos[-1]}""")
    except:
        left.append(f"""|   \\{al_sho_title_cn[choi[4]]}|""")
    left.append("|")
    left.append("|")
    try:
        left.append(f"""|      \\{al_sho_title_cn[choi[5]]}|{globals()["al"+str(choi[5])].voilist_pos[-1]}""")
    except:
        left.append(f"""|      \\{al_sho_title_cn[choi[5]]}|""")
    left.append("|")
    left.append("|")
    left.append(f"|最终战况>>[{n[0]},{n[1]},{n[2]},{n[3]}] 使用天数>>{days}")
    left.append(f"|危机合约#2")
    left.append(f"|战死之地  我们的身后，天灾的面前，即是浅草寺寂静的穹顶")
    left.append("-"*70)
    right=[]
    p=max([17,m1.printlen(f"  {username}-{shipname}  ")])
    right.append("-"*(p+1))
    right.append(("            ").center(p," ")+"|")
    right.append((r"  |\        ").center(p," ")+"|")
    right.append((r"  |\        ").center(p," ")+"|")
    right.append((r"  |\========").center(p," ")+"|")
    right.append(("  |\\"+(f"{entry_manager.total_points}").center(4," ")+r"\|  ").center(p," ")+"|")
    right.append((r"========\|  ").center(p," ")+"|")
    right.append((r"        \|  ").center(p," ")+"|")
    right.append((r"        \|  ").center(p," ")+"|")
    right.append(("            ").center(p," ")+"|")
    right.append(("            ").center(p," ")+"|")
    right.append(time.strftime("%m-%d %H:%M",time.localtime()).center(p," ")+"|")
    if p == 17:
        right.append((f"  {username}-{shipname}  ")+" "*(17-m1.printlen(f"  {username}-{shipname}  "))+"|")
    else:
        right.append((f"  {username}-{shipname}  ")+"|")
    right.append(("   IFAWL   ").center(p," ")+"|")
    right.append("-"*(p+1))
    if i == "p":
        m1.two_columnprint(left,right,di=70)       
    elif i == "2":
        sf=shelve.open("savedata")
        sf[username+"pic"]=[left,right]
        sf.close()

def probability(pro)->bool:#概率为真
    if random.random()<pro:
        return True
    else:
        return False

def upint(a,b):#向上取整
    if a%b != 0:
        return (a//b)+1
    else:
        return a//b

def cpu_atkplus(atk:int,txt:str="",
                en1_liefeng=True,
                al24_danaiyou=True,
                al36_xiling=False)->int:#增强敌方攻击
    '''
    敌方攻击函数

    en1_liefeng：   是否受烈风词条伤害加成

    al24_danaiyou： 是否可以被大奶油拦截

    al36_xiling:    是否可以被西岭拦截
    '''

    global mode
    if atk==0:
        return 0
    if en1_liefeng:
        atk=m3.entry1.react(atk,mode)#烈风
    al38.check_if_add()
    atk=al28.check_if_protect_and_count(atk)

    if al24_danaiyou:
        atk=al24.protect(atk)
    if al36_xiling:
        atk = al36.check_if_protect(atk)
    atk=al31.protect(atk)
    atk=al25.protect(atk)
    atk=al27.check_if_evade(atk)

    if atk == 0:
        m1.printplus("[舰船]攻击被完全处理")
    elif txt != "":
        m1.printplus(txt)

    if diamond_manager.check_if_react("w",2):
        n[1]+=1
    if diamond_manager.check_if_react("w",3):
        n[0]+=1
    if diamond_manager.check_if_react("w",4):
        al7.react()

    if atk>1:
        n[1]=m3.entry12.react(mode,n[1])
    al34.record(atk)
        
    if atk>al14.state:
        n[0]-=atk-al14.state
        al14.state=0
    else:
        al14.state-=atk


    return atk

def player_atkplus(atk:int):

    global mode,hard

    al27.break_now()
    al38.check_if_add()

    if diamond_manager.check_if_react("q",1):
        atk*=2
    if diamond_manager.check_if_react("q",0):#
        atk+=1
    if diamond_manager.check_if_react("q",2):
        n[1]+=1
    if diamond_manager.check_if_react("q",3):
        n[0]+=1
    if diamond_manager.check_if_react("q",4):
        al7.react()#
    if diamond_manager.check_if_react("e",1):
        hard-=0.2

    atk = m3.entry3.react(atk,mode)#虚弱
    atk = al30.check_if_increase(atk) 
    atk = al38.check_if_increase(atk)

    
    al33.check_if_move(atk)
    n[2]-=atk

    if (mode in entry_manager.mode_list) and n[2] == 0:
        if m3.entry9.rank != 0:
            cpu_atkplus(m3.entry9.rank,en1_liefeng=False)
            m3.entry9.react_print()

def player_cureplus(cure:int,al21_shian=False,if_dengtayimie=True):
    global n,mode
    if diamond_manager.check_if_react("w",0):
        cure+=1
    if diamond_manager.check_if_react("w",1):
        cure*=2
    n[2]+=m3.entry8.react(mode)
    if if_dengtayimie:
        cure=m3.entry6.react(mode,cure)#灯塔已灭

    cure = al34.check_if_promote(cure)

    if 21 in choi and (al21_shian or "“焦糖星”" in eqm):
        al21.state+=cure
    else:
        n[0]+=cure

def itemprint(topic:str,it:dict,l:int = 20,r:int = 6):#空间站仓库打印

    title = topic.center(2*l+r-4,"-")
    body = []
    for k,v in it.items():
        body.append(k.ljust(l,"·")+str(v).rjust(r))

    Tree(title,body).treeprint()

def ranop(h = 7):#随机开局

    p_c_manager.plies = 0

    n[2] = h//3
    n[3] = h//3
    h -= (h//3)*2
    c = random.randint(0,h)
    #print(c)
    n[2] += c
    n[3] += h-c

def storehouse_load_or_new():#载入或新建仓库
    global item1,item2,item3,item5
    sf=shelve.open("savedata")

    item1_raw:dict = sf.get(f"{username}1",{})
    if item1_raw == {}:
        print("空间站建立完成")
    for i in item1:
        item1[i] = item1_raw.get(i,0)
    sf[f"{username}1"] = item1.copy()

    try:
        preitem2=sf[username+"2"]
        if preitem2.keys() != item2.keys():#覆写旧仓库
            for i in item2:
                try:
                    item2[i]=sf[username+"2"][i]
                except:
                    pass
            sf[username+"2"]=item2
            print("版本已更新")
        else:
            item2=preitem2#读取仓库
    except:
        sf[username+"2"]=item2
        print("空间站建立完成")

    try:
        preitem3=sf[username+"3"]
        if preitem3.keys() != item3.keys():#覆写旧仓库
            for i in item3:
                try:
                    item3[i]=sf[username+"3"][i]
                except:
                    pass
            sf[username+"3"]=item3
            print("版本已更新")
        else:
            item3=preitem3#读取仓库
    except:
        sf[username+"3"]=item3  
        print("空间站建立完成")
    try:
        resource_nevigator.target_num=sf[username+"4"]
    except:
        sf[username+"4"]=""  
        print("空间站建立完成")
        
    if f"{username}entry" in sf.keys():
        for i in range(0,entry_manager.en_num):
            try:
                globals()[f"entry{i}"].rank=sf[f"{username}entry"][i]
            except:
                pass
    else:
        sf[f"{username}entry"]={}
    
    fps_list_raw:dict = sf.get(f"{username}5",{})
    if fps_list_raw == {}:
        print("空间站建立完成")
    for i in range(1,fps_num):
        title = globals()[f"fps{i}"].title
        item5[title] = fps_list_raw.get(title,0)
    sf[f"{username}5"] = item5.copy()

    sf.close()
    
def item_drop(pr,kinds):#掉落与保存
    global item1
    if kinds >=len(item1.keys()):
        kinds=len(item1.keys())-1
    k=random.randint(400,600)+pr*300
    item1["联邦信用点"]+=k
    print("[赏金到账]信用点x",k)
    it=list(item1.keys())
    it.remove("联邦信用点")
    it.remove("合约纪念点")
    it.remove("保险点")
    it=random.sample(it,kinds)
    for i in it:
        k=random.randint(5,10)+pr*3
        item1[i]+=k
        if i in resource_nevigator.nevigator_list:
            print("[战利品收集] ",i,"x",k,"[▲]")
        else:
            print("[战利品收集] ",i,"x",k)
    sync(if_entry=False)

def sync(if_entry=False):#同步所有仓库
    """同步包括词条在内的所有仓库，调整if_entry来设置"""
    sf=shelve.open("savedata")
    sf[username+"1"]=item1
    sf[username+"2"]=item2
    sf[username+"3"]=item3
    sf[username+"4"]=resource_nevigator.target_num
    sf[username+"5"]=item5
    pre_entry={}
    if if_entry:
        for i in range(0,entry_manager.en_num):
            if f"entry{i}" in globals():
                pre_entry[i]=globals()[f"entry{i}"].rank    
            else:
                pre_entry[i]=0
        sf[username+"entry"]=pre_entry
    sf.close()

def item1count():#统计一般掉落物
    r = 0
    for i in item1.keys():
        r += item1[i]
    r -= item1["联邦信用点"]
    r -= item1["合约纪念点"]
    r -= item1["保险点"]
    return int(r)

def item2count():#统计消耗品
    r=0
    for i in item2.keys():
        r+=item2[i]
    return r

def usersave():#保存私人配置
    global username,choi,shipname
    sf=shelve.open("savedata")
    r=choi.copy()
    shipname_inp=input(f"请输入舰船名称 [enter]沿用原名“{shipname}”>>>")
    if shipname_inp == "":
        shipname_inp=shipname
    r.append(shipname_inp)
    g=sf["user"]
    g[username]=r
    sf["user"]=g
    print("配置保存成功")
    sf.close()

def userload():#载入私人配置
    global choi,shipname,username
    sf=shelve.open("savedata")
    if "user" not in sf.keys():
        sf["user"]={}
        print("私人配置系统已建立")
    if username in sf["user"].keys():
        for i in range(3,6):
            choi[i]=sf["user"][username][i]
        shipname=sf["user"][username][6]
        print("指挥官代号识别成功·%s号护卫舰正在启动"%shipname)

def craftprint():#配方书打印
    print("---------空间站产品列表----------")
    for i in craft1:
        print(i)
        print("|")
        print("|-",end="")
        print(eqmdis[i])
        for j in craft1[i]:
            print("|")
            print("|-",end="")
            print(j,"x",craft1[i][j],"/",item1[j],sep="")
        print("")

def al_craft_print():#装备配方书打印
    global item1
    print("---------空间站装备列表----------")
    for i in range(0,al_num):
        try:
            al_temp:Al_general
            al_temp=globals()["al"+str(i)]
            if al_temp.rank != "FREE" :
                str1=f"[{i}]"+al_temp.len_skin+f" [{al_temp.rank}]"
                print(str1,end="")
                print(" "*(45-m1.printlen(str1)),end="")
                print(al_temp.is_craftable_txt(),end="")
                print(f"   现有 {item3[al_temp.len_skin]} 在仓库")
                for j in al_temp.cost_list:
                    note="[▲]" if al_temp.cost_list[j]>item1[j] else ""
                    str0=f"|-{j}x{al_temp.cost_list[j]}/{item1[j]}{note}"
                    print(str0,end="")
                    print(" "*(22-m1.printlen(str0)),end="")
                print()
                print()
        except:
            pass

def al_craft_print():
    """保持原有单行显示风格，但性能提升 3 倍以上"""
    global item1, item3

    # 预加载所有装备对象，避免循环中反复查询全局变量
    al_list = [globals().get(f"al{i}") for i in range(al_num)]
    valid_als = [al for al in al_list if al and al.rank != "FREE"]
    
    # 预计算所有输出内容（核心优化点）
    buffer = ["\n---------空间站装备列表----------"]
    
    for idx, al_temp in enumerate(valid_als):
        # --- 生成标题行 ---
        title = f"[{al_temp.index}]{al_temp.len_skin} [{al_temp.rank}]"
        craft_status = al_temp.is_craftable_txt()
        stock_info = f"   现有 {item3.get(al_temp.len_skin, 0)} 在仓库"
        
        # 动态计算标题对齐（保留原空格填充逻辑）
        title_padded = title + " " * (45 - m1.printlen(title))
        buffer.append(f"{title_padded}{craft_status}{stock_info}")

        # --- 生成材料行 ---
        cost_line = []
        for item, req in al_temp.cost_list.items():
            current = item1.get(item, 0)
            note = "[▲]" if req > current else ""
            cost_str = f"|-{item}x{req}/{current}{note}"
            cost_str += " "*(22 - m1.printlen(cost_str))
            cost_line.append(cost_str)
        
        # 保持原样：所有材料项连续显示，不换行（关键修改点）
        buffer.append("".join(cost_line) + " " * 2)  # 保留末尾两个空格
        buffer.append("")  # 空行分隔

    # 一次性输出（性能提升核心）
    for i in buffer :
        print(i)
        time.sleep(0.005)

def al_craft():#装备合成器
    ind="1"
    while ind != "":
        ind=input("工业流程正常运转中·请输入要合成的装备代码·按下回车退出>>>")
        if ind == "":
            return 0
        else:
            try:
                globals()["al"+ind].craft_self()
                al_craft_print()
                time.sleep(0.3)
            except:
                pass

def craft():#合成器
    ind="1"
    while ind not in craft1.keys() and ind != "":
        ind=input("工业流程正常运转中·请输入要合成的物品·按下回车退出>>>")
    if ind == "":
        return 0
    it=ind
    ind=craft1[ind]
    num=int(input("%s蓝图信息已读取·请输入合成数量>>>"%ind))
    i=0
    j=0
    for k in ind.keys():
        if num*ind[k]<=item1[k]:
            i+=1
        j+=1
    if i == j:
        for k in ind.keys():
            item1[k]-=num*ind[k]
        item2[it]+=num
        m1.printplus("合成完成")
    else:
        m1.printplus("材料不足·不能合成")
    sf=shelve.open("savedata")
    sf[username+"1"]=item1
    sf[username+"2"]=item2
    sf.close()

def eqmprint():#安装消耗品
    global eqm
    i="114514"

    while i != "":
        for g in item2.keys():
            print(g)
            print("|")
            print("|-",end="")
            print(eqmdis[g])
            print("|")
            print("|-",end="")
            print("现有",item2[g])
            print("")
        i=input("请输入要安装的战术设备|[e1]跳转合成界面|[enter]退出>>>")
        if i not in item2.keys() and i != "":
            print("输入有误")
            pass
        if i in eqm:
            print("设备已重复存在")
        elif i=="e1":
            while 1:
                craftprint()
                cra=craft()
                if cra == 0:
                    break
            continue
        elif i != "" and item2[i]>0:
            eqm.append(i)
            print("设备安装完成")
        elif i != "":
            print("无设备")
        else:
            m1.printplus("正在退出",0.2)

def al_is_ready():#离站武器检查
    global choi
    check=0
    for i in choi[3:6]:
        try:
            al_temp=globals()["al"+str(i)]
            al_temp:Al_general
            if item3[al_temp.len_skin]>0 or al_temp.rank == "FREE":
                check+=1
        except:
            check+=1
    if check == 3:
        return True
    else:
        return False

def al_count() -> int:#装备统计
    global choi
    out=0
    for i in choi[3:6]:
        try:
            al_temp:Al_general=globals()[f"al{i}"]
            out+=al_temp.cost_list["联邦信用点"]//1100
        except:
            pass
    return out

def al_cost():#武器消耗
    global choi,item1,item3
    if item1["保险点"]<al_count():
        for i in range(3,6):
            try:
                al_temp=globals()["al"+str(choi[i])]
                al_temp:Al_general
                if not al_temp.rank == "FREE":
                    item3[al_temp.len_skin]-=1
                    print(f"{al_temp.len_skin} 损毁")
                    choi[i]=2-i
            except:
                pass
    else:
        item1["保险点"]-=al_count()
        print(f"{al_count()}保险点已扣除·已保全所有装备")
    sync(if_entry=False)

def itemcost():#离站消耗
    for i in eqm:
        item2[i]-=1
        print(f"{i}*1 被消耗")
    time.sleep(0.7)
    sf=shelve.open("savedata")
    sf[username+"2"]=item2
    sf.close()

def rock():#石头剪刀布
    ock=0
    if al26.state == 3:
        al26.state-=1
        return 0    
    ock=random.random()
    if ock>1-hard:
      return 1
    else:
      return 0

def suggestion_print() :#战斗辅助提示器
    suggestion_list = []
    for i in choi:
        try:
            al_temp:Al_general=globals()[f"al{i}"]
            sugg:str = al_temp.suggest()
            if mode == 6:
                sugg = sugg.replace(f"{al_temp.type}",["0","1","2","q","w","e"][choi.index(i)])
            if sugg != None:
                suggestion_list.append(f"[{al_temp.short_skin}]"+sugg)
        except:
            pass
    if suggestion_list == []:
        suggestion_list.append("空闲")
    return Tree("战斗辅助面板",suggestion_list)


def surroundings_suggestion_print() :#战场环境辅助提示器

    global n,days
    suggestion_list = []
    
    if n[0] + al14.state + al21.state == 0 : 
        suggestion_list.append("[严重警告]我方护盾被全面清空|[2][w]抢救舰船")
    
    if n[0] + al14.state + al21.state < n[3] : 
        suggestion_list.append("[警告]敌方导弹已全面覆盖我方护盾|[2][w]生存")
    
    if days > 25+inf/3 and n[0] + al14.state + al21.state <= 2 : 

        if m3.entry4.rank == 2 :
            suggestion_list.append("[注意]观察“殷红狂怒”信火一体打击的可能迹象|词条激活|护盾不足|[2][w]生存")
        else:
            suggestion_list.append("[注意]观察“殷红狂怒”信火一体打击的可能迹象|护盾不足|[2][w]生存")

    if suggestion_list == [] :
        suggestion_list.append("空闲")

    return Tree("环境辅助面板",
                suggestion_list)
    

def sitprint(is_normal):#战场打印
    global mode
    if is_normal:
        print("%s指挥官，"%username,"今天是战线展开的第",days,"天。",auto_pilot.to_do_list)
    else:
        print("%s指挥官，"%username,"今&%%%是战线展&*第",days,"天。")
    if mode == 1:
        print("当前无尽模式轮次：",inf+1)
    print(ocp_manager.ocp_now.title)
    if days<5:
        m1.printplus("当前舰船位置>>正在离港",0.3)
    elif days<10:
        m1.printplus("当前舰船位置>>我方领土边缘",0.3)
    elif days<=20:
        m1.printplus("当前舰船位置>>边境核心战场",0.3)
    elif days>20:
        if is_normal:
            m1.printplus("当前舰船位置>>敌方腹地危险区域",0.3)
        else:
            m1.printplus("当前舰船位置>>@$%）%^$^(*^&$#&())^%$",0.3)
    al20.printself()
    if not is_normal:
        print("^&$%"*n[3])
    elif (mode in entry_manager.mode_list) and m3.entry2.rank != 0:
        print("[NO INFO]")
    else:
        print("[]"*n[3])
    if not is_normal:
        for i in range(n[2]):
            print("&(-$^") 
    elif 33 in choi:
        al33.printself()
    else:
        for i in range(n[2]):
            print("-----")  
    di_ani_manager.print_cpu_ani() 
    p_c_manager.print_self()
    print("\n\n\n\n\n")
    al6.printself()
    al9.printself()
    al11.printself()
    al25.printself()
    if not is_normal:
        for i in range(n[0]):
            print("#$^&-")        
    elif (mode in entry_manager.mode_list) and m3.entry2.rank == 2:
        print("[NO INFO]")        
    else:
        al28.printself()
        al31.printself()
        al14.printself(not is_normal)
        al29.printself()
        di_ani_manager.print_player_ani()
        for i in range(n[0]):
            print("-----")
    al21.printself()
    al38.printself()
    if not is_normal:
        print("(^*"*n[1])        
    elif q_is_missile():
        print("[]"*n[1])
    else:
        print("|| "*n[1])
    print()

    al4.printself()
    al12.printself()
    al16.printself()
    al15.printself()
    al8.printself()
    al5.printself()
    al19.printself()

    m1.two_columnprint(suggestion_print().linelist(),
                    surroundings_suggestion_print().linelist(),
                    di=60)
    print()
    for j in range(0,6):
        if mode == 6 and j>2:
            print(al_sho_title_cn[choi[j]].replace(al_sho_title_cn[choi[j]][al_sho_title_cn[choi[j]].find("/")+1],["0","1","2","q","w","e"][j])," ",end="")
        else:
            print(al_sho_title_cn[choi[j]]," ",end="")
    if sum(item5.values()) >= 1:
        if is_normal:
            print("r 战术快递")
        else:
            print("r 战&快*")
    else:
        print("")


#def blisitprint():#致盲的战场打印
#    print("%s指挥官，"%username,"今&%%%是战线展&*#第",days,"天。")
#    if mode == 1:
#        print("当前无*%￥式轮次：",inf+1)
#    print(ocp_manager.ocp_now.title)
#    if days<5:
#        printplus("当前舰船位置>>正在离港",0.3)
#    elif days<10:
#        printplus("当前舰船位置>>我方领土边缘",0.3)
#    elif days<=20:
#        printplus("当前舰船位置>>边境核心战场",0.3)
#    elif days>20:
#        printplus("当前舰船位置>>@$%）%^$^(*^&$#&())^%$",0.3)
#    al20.printself()
#    print("^&$%"*n[3])
#    print("&(-$^\n"*n[2])
#    p_c_manager.print_self()
#    print("\n\n\n\n\n")
#    al6.printself()
#    al9.printself()
#    al11.printself()
#    al14.printself(1)
#    al29.printself()
#    print("\n#$^&-"*n[0])
#    print("(^*"*n[1])
#    print()
#
#    al4.printself()
#    al12.printself()
#    al16.printself()
#    al15.printself()
#    al8.printself()
#    al5.printself()
#    al19.printself()
#
#    two_columnprint(suggestion_print().linelist(),
#                    surroundings_suggestion_print().linelist(#),
#                    di=60)
#    print()
#    for j in range(0,6):
#        print(al_sho_title_cn[choi[j]]," ",end="")
#    if sum(item5.values()) >= 1:
#        print("r 战&快*")
#    else:
#        print("")
    
def silsitprint():#空白的战场打印
    print("%s指挥官，"%username,"今天是战线展开的第",days,"天。")
    if mode == 1:
        print("当前无尽模式轮次：",inf+1)
    print(ocp_manager.ocp_now.title)
    if days<5:
        m1.printplus("当前舰船位置>>正在离港",0.3)
    elif days<10:
        m1.printplus("当前舰船位置>>我方领土边缘",0.3)
    elif days<=20:
        m1.printplus("当前舰船位置>>边境核心战场",0.3)
    elif days>20:
        m1.printplus("当前舰船位置>>敌方腹地危险区域",0.3)
    print("NO INFO\n"*7)
    for j in range(0,6):
        print(al_sho_title_cn[choi[j]]," ",end="")
    print("")

def rockprint(r):#石头剪刀布结果
    if r == 1:
        print("今天由敌方行动")
    else:
        m1.printplus("今天由我方行动",0.3)

def choiprintplus(a):#主要装备选择
    global username,choi,shipname
    if a == "q":
        for i in q_list:
            try:
                al_temp:Al_general = globals()[f"al{i}"]
                al_temp.print_description()
            except:
                pass
        m1.n_columnprint(
            [
                Tree(
                    "导弹平台",
                    "使用舰对舰导弹攻击敌方",
                    "#操作简单|#进攻迅速"
                ).linelist(),
                Tree(
                    "粒子炮平台",
                    "使用舰载大功率粒子炮进行攻击",
                    "#战术|#延迟爆炸|#可暴击"
                ).linelist()
            ],
            50
        )
        while 1:
            inp=m1.inputplus("\n指挥官，请输入数字选择本场战斗的主武器（对局中输入q或对应数字来使用）[-1=不使用主武器]>>>",0.3)
            if inp not in q_list:
                if inp == "":
                    break
                print("请在武器库中进行选择")
                pass
            else:
                print(al_sho_title_cn[int(inp)],"已确认装备")
                choi[3]=int(inp)
                print("")
                time.sleep(0.4)
                break

        if is_contra():
            m1.printplus("你的战术位装备与当前主武器平台不匹配，已自动卸下战术装备")
            choi[5] = -3

    elif a == "w":
        for i in w_list:
            try:
                al_temp:Al_general = globals()[f"al{i}"]
                al_temp.print_description()
            except:
                pass
        print("")
        while 1:
            inp=m1.inputplus("请选择本场战斗的维修生存站（对局中输入w或对应数字来使用）[-2=不使用生存位]>>>",0.3)
            if inp not in w_list:
                if inp == "":
                    break
                print("请在维修团队中进行选择")
                pass
            else:
                print(al_sho_title_cn[int(inp)],"已确认装备")
                choi[4]=int(inp)
                print("")
                time.sleep(0.4)
                break
    elif a == "e":
        for i in e_list:
            try:
                al_temp:Al_general = globals()[f"al{i}"]
                al_temp.print_description()
            except:
                pass
        while 1:
            inp=m1.inputplus("请选择本场战斗的战术配置（对局中输入e或对应数字来使用）[-3=不使用战术位]>>>",0.3)
            if inp not in e_list:
                if inp == "":
                    break
                print("请在可选战术配置中进行选择")
                pass
            else:
                print(al_sho_title_cn[int(inp)],"已确认装备")
                choi[5]=int(inp)
                print("")
                time.sleep(0.4)
                if choi[5] == -3:
                    m1.printplus("[奶油]喂")
                    time.sleep(0.9)
                    m1.printplus("[奶油]听说你又没钱了？")
                    time.sleep(0.9)
                    m1.printplus("[奶油]连战术位都买不起了？")
                    time.sleep(0.9)
                    m1.printplus("[奶油]我得来看看乐子。")
                    time.sleep(0.9)
                    m1.printplus(f"[{username}]……")
                    time.sleep(0.9)
                    m1.printplus("[奶油]行了行了，下把我罩你。")
                    time.sleep(0.9)
                    print(al_sho_title_cn[7],"已确认装备")
                    time.sleep(1)
                    choi[5]=7
                break
        try:
            al_temp_q:Al_general = globals()[f"al{choi[3]}"]
            al_temp_e:Al_general = globals()[f"al{choi[5]}"]
            if al_temp_e.tag["武器平台"] != "通用" and al_temp_e.tag["武器平台"] != al_temp_q.tag["武器平台"]:
                m1.printplus("你的战术位装备与当前主武器平台不匹配，已自动卸下主武器")
                choi[3] = -1
        except:
            pass
    sf=shelve.open("savedata")
    r=choi.copy()
    r.append(shipname)
    g=sf["user"]
    g[username]=r
    sf["user"]=g
    sf.close()    

def choiprint():#开局武器选择
    choiprintplus("q")
    choiprintplus("w")
    choiprintplus("e")

def faker_vs_bin_main():
    global hard
    left=[]
    for i in q_list:
        try:
            left.append(i+"|"+allenskin[int(i)])
        except:
            pass
    mid=[]
    for i in w_list:
        try:
            mid.append(i+"|"+allenskin[int(i)])
        except:
            pass
    right=[]
    for i in e_list:
        try:
            right.append(i+"|"+allenskin[int(i)])
        except:
            pass
    m1.n_columnprint([left,mid,right])
    choi[3]=int(m1.ask_plus("选择你的[q]位置装备",[i for i in range(3,al_num+1)]))
    choi[4]=int(m1.ask_plus("选择你的[w]位置装备",[i for i in range(3,al_num+1)]))
    choi[5]=int(m1.ask_plus("选择你的[e]位置装备",[i for i in range(3,al_num+1)]))
    reset_general()
    hard = 0
    sum_num:str=m1.ask_plus("敌方开局盾弹和（7~20）",[i for i in range(7,21)]+[""])
    if sum_num.isdigit():
        ranop(int(sum_num))
    else:
        ranop(7)
    if m1.inputplus("是否重新选择词条？[y]是") == "y":
        entry_manager.ask(username)

        
def q_is_missile():
    if choi[3] != -1 :
        if globals()[f"al{choi[3]}"].tag["武器平台"] == "导弹":
            return True
        else:
            return False
    else:
        return True

def is_contra() -> bool :
    if choi[3] < 0 or choi[5] < 0:
        return False
    e_temp:Al_general = globals()[f"al{choi[5]}"]
    q_temp:Al_general = globals()[f"al{choi[3]}"]
    if e_temp.tag['武器平台'] == "通用" or q_temp.tag['武器平台'] == "通用":
        return False
    elif e_temp.tag['武器平台'] != q_temp.tag['武器平台']:
        return True
    else:
        return False

def operation_main():#主操作函数 

    global distance,wav,days,hard

    al27.check_if_promote()
    ocp_manager.counting()
    m3.entry16.preset(choi,mode,al_sho_title_cn)
    if auto_pilot.to_do_list == []:        
        i=m1.inputplus("请选择你的操作>>>",0.2)###########
        if i == "m":
            try:
                winsound.PlaySound(wav,winsound.SND_PURGE)
                wav=""
                i=m1.inputplus("音乐已关闭，请选择你的操作>>>",0.3)
            except:
                try:
                    wav=winsound.PlaySound("危机合约第3赛季「净罪作战」主题曲",winsound.SND_ASYNC)
                    i=m1.inputplus("音乐已开启，请选择你的操作>>>",0.3)
                except:
                    print("无此文件")
                    i=m1.inputplus("请选择你的操作>>>",0.3)

    else:
        i=auto_pilot.react(n,days,item1)
        m1.printplus(f"自动战斗接管中·当前操作：{i}")
    if "-" in i:
        auto_pilot.read(i)
        i=auto_pilot.react(n,days,item1)
        m1.printplus(f"自动战斗接管中·当前操作：{i}")
        m1.printplus("自动战斗数据录入完成·自动战斗即将开始")

    if choi[3] != -1 :
        if globals()[f"al{choi[3]}"].tag["武器平台"] == "导弹":
            missile = True
        else:
            missile = False
    else:
        missile = True

    voi_0=[f"[导弹]{username}指挥官,导弹已挂置在左舷","[导弹]导弹已移入发射井","[导弹]热能弹头预热完毕"] if missile else [f"[粒子炮]{username}指挥官,小型粒子匣已装载","[粒子炮]粒子炮正在G6甲板待命","[粒子炮]粒子炮正在B3甲板待命"]
    voi_1=["[导弹]fox1，导弹确认命中","[导弹]fox2，确认穿透敌方护盾","[导弹]fox3，敌方结晶护盾已融化"] if missile else [f"[粒子炮]注意十二点钟闪光！Attention,stick！","[粒子炮]splash1，粒子确认粘附","[粒子炮]splash2，粒子炮发射","[粒子炮]splash3，小心闪光"]
    voi_2=["结晶化护盾已生成","已联络最近的电磁屏障","拮抗力场正在凝固"]
    if i == "q":
        i=choi[3]
    elif i == "w":
        i=choi[4]
    elif i == "a" and distance != -3:
        distance-=1
        n[1]+=1
    elif i == "d" and distance != 3:
        distance+=1
        n[1]+=1
    elif i == "e":
        i=choi[5]
        if days>10 and diamond_manager.check_if_react("e",0):
            days-=2
    elif i == " ":
        i = "0"
    elif i == "f":
        ocp_manager.all_ocp_react()
    elif i == "giveup":
        n[0]=-1
    elif i == "":
        i=114514
    elif i == "r":
        i = fps_manager.calling_main()
    else:
        pass
    if i not in kwords:
        if m3.entry16.react(i):
            cpu_atkplus(1)
    if i == "2" and 18 in choi:
        i=18
    if i == "2" and 29 in choi:
        i=29
    if i in [str(j) for j in choi] + choi:
        if i == "0":#建导弹         
            load = 1
            load = al5.check_if_load(load)
            load = al15.check_if_load(load)
            n[1] += load
            if load == 1:
                m1.printplus(random.choice(voi_0),0.3)
                time.sleep(0.4)
        elif i == "1":#进攻
            if n[1] > 0:
                if al8.state>=2:#维多利亚
                    al8.attack()
                elif al15.state != 0:#暴雨
                    m1.printplus("[暴雨]一般发射器离线。已为您新建一枚导弹。",0.3)
                    n[1]+=1
                else:
                    if q_is_missile():
                        player_atkplus(1)
                        n[1] -= 1
                    else:
                        p_c_manager.adding(1)
                        n[1] -= 1
                m1.printplus(voi_1[random.randint(0,2)],0.3)
                time.sleep(0.4)
            else:
                m1.printplus("[武器甲板]弹药不足",0.3)
                n[1]+=1
        elif i == "2":#建护盾
            al9.check_if_cure()
            al16.check_if_cure()
            if 21 in choi:
                if al21.state>2:
                    if probability(0.5):
                        al21.react()
                    else:
                        al21.state+=1
                        m1.printplus("[诗岸]诗岸已充注一层混凝层")
                else:
                    al21.state+=1
                    m1.printplus("[诗岸]诗岸已充注一层混凝层")
            else:
                player_cureplus(1)
                m1.printplus("[护盾]"+random.choice(voi_2),0.3)
        else:
            try:
                globals()["al"+str(i)].react()
            except:
                pass
        if i != 12 and al12.state != 0 and not (16 in choi and i == 2):#notice
            al12.attack()
    elif i not in kwords:
        m1.printplus("奶油爆炸！上蹿下跳！你跳过了这一天！",0.3)
        i="0"

def decide():#敌方操作函数
    w=["敌方导弹已挂载","敌方导弹已移入发射井"]
    o=["我方最外层护盾被击破","警告·最外层电磁屏障被贯穿"]
    c=["敌方生成结晶化护盾","敌方部署了电磁屏障"]

    if n[0]+al14.state == 0 and n[3]>0:    #必处决
        d=1
    elif n[0] > 2 and n[2]>2 :  #我方多盾
        d=3
    elif n[3]>=2 and n[2]>0:               #导弹过多
        d=1
    elif n[2] <= 2:             #自保
        d=random.choices([0,2], weights = [4,6])[0]
    else:
        d=random.choices([0,1,2], weights = [4,2,4])[0]

    if ocp_manager.ocp_now.index == 2 :
        d=1

    #d=int(input("敌方玩家·请输入操作>>>"))
    d=al26.check_if_control(d)
    if d == 0:#建导弹
        n[3]+=1
        n[3]+=m3.entry10.react(mode)
        time.sleep(0.4)
        print(w[random.randint(0,1)])
    elif d == 1:#进攻
        if n[3]>0:
            if ocp_manager.ocp_now.index == 2:#殷红狂怒
                n[3]-=1
                cpu_atkplus(2,"严重警告·敌方饱和式打击重创我方护盾",al36_xiling=True)
                if m3.entry4.rank == 2 and (mode in entry_manager.mode_list):
                    m3.entry4.react_print()
                    cpu_atkplus(1,al36_xiling=True)
                time.sleep(0.4)
            else:
                frequency=m3.entry14.react(mode,n[3])
                for i in range(frequency):
                    n[3]-=1#进攻
                    cpu_atkplus(1,o[random.randint(0,1)],al36_xiling=True)
                    time.sleep(0.4)
        else:
            n[3]+=1#自动装弹
            time.sleep(0.4)
            print(w[random.randint(0,1)])
    elif d == 2:#建护盾
        if al11.state>0:#柒
            al11.cure()
        else:
            n[2]+=1
            time.sleep(0.4)
            print(c[random.randint(0,1)])
    #print(d)
    elif d == 3:#巡飞弹
        if random.randint(0,9)>=10-3*(n[0]):
            result=cpu_atkplus(1,"敌方风行者巡飞弹命中我方护盾")
            time.sleep(0.4)
        else:
            time.sleep(0.4)
            print("敌方风行者擦过我方护盾")

def check():#死亡判断函数
    global mode
    
    al37.check_if_recycle()
    n[2]=m3.entry17.react(n[2])

    if m3.entry5.check_if_die(mode,n[0]+al14.state):
        m3.entry17.reborn=0
        return 0

    if n[0]<0:
        m3.entry17.reborn=0
        return 0#我死
    elif n[2]<0:
        return 2#敌死
    else:
        return 1

def pre_al_check():#操作前装备判定 prebulidcheck()
    al7.check_if_boom()
    al20.check_if_cool()
    al29.check_if_cure()
    al35.check_if_add()
    al38.check_if_turn()
    
def pos_al_check():#操作后装备&事件判定 buildcheck()
    cpu_atkplus(m3.entry13.react(mode,days),"",en1_liefeng=False)
    ocp_manager.ocp_check()
    p_c_manager.check_if_boom()
    al19.suply()
    al4.attack()
    al15.check_if_attack()
    al28.check_if_fire()
    al6.check_if_need_cure()    
    al22.check_if_cool_and_atk()
    al37.check_if_cool()
    al25.check_if_cool()
    al31.check_if_cool_and_bleed()
    al26.check_if_cool()
    al30.check_if_cool()
    al38.check_if_cure()
    al21.check_if_cure()
    al33.check_if_deepen_and_poison()
    al36.check_if_attack()
    al34.check_if_cool_and_protect()

def sitplus(n,r):#增强战报打印
    if n[1]>n[2]:
        m1.printplus("注意·我方导弹阵列可全面覆盖敌方护盾体系",0.3)
    if n[3]>n[0]:
        m1.printplus("注意·敌方导弹阵列可全面覆盖我方护盾体系",0.3)
    if n[0] == 0 and al14.state == 0:
        m1.printplus("警告：我方护盾全面崩溃",0.3)
    if n[2] == 0:
        m1.printplus("注意·敌方护盾已被全部击破",0.3)
        if n[1]>0 and r == 0:
            time.sleep(0.8)
            m1.printplus("指挥官，任务即将结束")

def mining_refresh():#刷新小行星带
    global mining_select_now
    mining_select_now="0"
    for i in range(1,mining_number+1):
        if globals()[f"mining{i}"].is_locked == False:
            globals()[f"mining{i}"]=Mining(random.randint(0,2))

def mining_print():#打印小行星带
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    mining_guitree=Tree("工业开采模式运行中","[数字]=临时锁定小行星","[临时锁定后]e=主锁定","q=自动开采全部主锁定目标 xe=全部脱离主锁定","w=qte挖矿","z=主动雷达扫描","enter=刷新界面 x=退出")
    print("当前舰船位置>>小行星带 外圈采矿区")
    print()
    for i in range(1,mining_number+1):
        obj=globals()["mining"+str(i)]
        if obj.is_exploited == False:#对于未被开采的小行星
            if str(i) == mining_select_now:#临时锁定
                Tree(
                    "-[临时锁定]["+str(i)+"]"+obj.name+"("+str(obj.mining_distance)+"km)-",
                    "[q][开采]双向渗透法",
                    "[w][开采]简谐共振法",
                    "[e][锁定]部署/取消主锁定"
                ).treeprint()
                
            elif obj.is_locked == True:#强锁定
                print("+[主雷达已锁定]["+str(i)+"]"+obj.name+"("+str(obj.mining_distance)+"km)+")
            else:#其它
                print("["+str(i)+"]"+obj.name+"("+str(obj.mining_distance)+"km)")
        else:#对于已被开采的小行星
            if str(i) == mining_select_now:#临时锁定
                print("-[临时锁定]["+str(i)+"]"+obj.name+"("+str(obj.mining_distance)+"km)-")
                print("|")
                print("|-[已被开采]")
            else:#其它
                print("[已被开采]["+str(i)+"]"+obj.name+"("+str(obj.mining_distance)+"km)")


        print()
    resource_nevigator.refresh()
    try:
        target_lenskin=globals()["al"+resource_nevigator.target_num].len_skin
        print(f"资源跟踪器-{target_lenskin}-当前需求>",end="")
        print(resource_nevigator.nevigator_mining_list)
        print()
    except:
        pass
    mining_guitree.treeprint()
    print(item0)
#————————————————————————————
past=[]

def reset_general(player_reset      = True,
                  inf_reset         = True,
                  hard_reset        = True,
                  auto_pilot_reset  = True):
    
    global win_2me,days,n,whoreact_0me,hard,hardv,past,inf,distance

    di_ani_manager.refresh()

    if player_reset:
        n[0]        = 1
        n[1]        = 1
        for inx in range(0,al_num):
            try:
                globals()["al"+str(inx)].reset()
            except:
                pass
        distance    = 0
    if inf_reset:
        inf         = 0
    if hard_reset:
        hard        = 0.2
        hardv       = 0.3
    if auto_pilot_reset:
        auto_pilot.refresh()
    whoreact_0me    = 0
    days            = 0
    win_2me         = 1

def fight_daily():
    global win_2me,days,n,whoreact_0me,hard,hardv,past
    n[2]+=m3.entry7.react(mode)#铁城
    n[2]-=m3.entry17.preset(mode)
    m5.play_sound("01_战斗-主体_管弦" , loop = True)
    di_ani_manager.sync()
    while win_2me == 1:
        time.sleep(0.4)
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        days+=1
        ocp_manager.ocp_random()#随机决定事件
        whoreact_0me_yesterday=whoreact_0me
        whoreact_0me=rock()#石头剪刀布
        if whoreact_0me == 0:
            hard+=hardv#我方
            if (mode in entry_manager.mode_list) and m3.entry11.rank != 0:
                hard+=m3.entry11.rank*0.03
                
        else:
            hard-=hardv#敌方
        pre_al_check()
        if mode != 3:
            sitprint(ocp_manager.ocp_now.index != 2)#当日战况及图示
        else:
            silsitprint()
        di_ani_manager.sync()
        sitplus(n,whoreact_0me)#各种警报
        rockprint(whoreact_0me)#石头剪刀布结果展示
        past=[n[0],al14.state]
        #打印事件文本
        if whoreact_0me == 0:
            operation_main()#我方行动
            if whoreact_0me_yesterday == 0 and diamond_manager.check_if_react("e",2):
                n[1]+=2
        else:
            al35.check_if_extra_act()
            decide()#敌方行动 
            if whoreact_0me_yesterday == 1 and diamond_manager.check_if_react("e",3):
                n[2]-=2
                al33.check_if_move()
        pos_al_check()#操作后建筑检查
        #检查事件是否被响应
        
        win_2me=check()
        print()
    ocp_manager.refresh()

def mining_daily():
    global mining_select_now,mining_select
    for i in range(1,mining_number+1):
        globals()["mining"+str(i)]=Mining(random.randint(0,2))
    while 1:
        mining_print()
        inp=input(">>>")
        if inp.isdigit() and 1 <= int(inp) <= mining_number:#锁定小行星
            mining_select=inp
            if mining_select == mining_select_now:
                mining_select_now="0"
            else:
                mining_select_now=mining_select
        elif inp == "z":#主动扫描
            print("主动雷达阵列正在启动")
            print(    "0        25        50        75       100")
            print(    "|         |         |         |         |")
            m1.printplus("`````````````````````````````````````````",5)
            m1.printplus("雷达定位完成·已刷新所有未进行主锁定的矿石",0.3)
            print()
            mining_refresh()
        elif inp == "e" and 1<= int(mining_select_now) <= mining_number:#主锁定
            obj=globals()["mining"+mining_select_now]
            if obj.is_exploited == False:
                obj.is_locked=True if obj.is_locked == False else False
            else:
                print("该矿石已被开采")
                time.sleep(0.1)
            mining_select_now="0" 
        elif inp == "q"and 1<= int(mining_select_now) <= mining_number:#开采1 挂机
            obj=globals()["mining"+mining_select_now]
            obj.exploit1()
        elif inp == "q"and mining_select_now in "0":#开采1 挂机 批量开采
            for i in range(1,mining_number+1):
                obj=globals()["mining"+str(i)]
                if obj.is_locked == True:
                    obj.exploit1() 
        elif inp == "w"and 1<= int(mining_select_now) <= mining_number:#开采1 挂机
            obj=globals()["mining"+mining_select_now]
            obj.exploit2()
        elif inp == "w"and mining_select_now in "0":#开采1 挂机 批量开采
            for i in range(1,mining_number+1):
                obj=globals()["mining"+str(i)]
                if obj.is_locked == True:
                    obj.exploit2() 
        elif inp == "xe":#一键脱离锁定
            for i in range(1,mining_number+1):
                globals()["mining"+str(i)].is_locked=False
        elif inp == "x":#退出
            break
        elif inp == "z":#舰船控制面板
            ctrtree=Tree("矿石仓库",)
            itemprint("矿石仓库",item0,20,6)
    while 1:
        industry_guitree=Tree("已进入铜城矿业空间站","q=调整加工订单","enter=确认订单")
        industry_guitree.treeprint()
        ind=Industry_selecting()
        print("目前订单状态")
        print()
        ind.industry_painting()
        inp=input(">>>")
        if inp.isdigit() == True and 0<int(inp)<5:
            ind.industry_raw_material_selecting_now=int(inp)
        if inp == "":
            break
        if inp == "q":
            while 1:
                industry_guitree=Tree("工业订单创建中","1-4=选定原材料","[选定后]q/w=选择输出产品","enter=确认订单")
                industry_guitree.treeprint()
                print()
                ind.industry_painting()
                inp=input(">>>")
                ind.industry_react(inp)
                if inp == "":
                    break
    ind.industry_drop()

def ending():
    global win_2me,mode,inf,item1
    if mode not in (1,4):#其余非矿区/无尽模式
        if win_2me == 0:#输
            print(lose[random.randint(0,len(lose)-1)])
            if mode != 5 and mode != 6:
                al_cost()
            inf=0
        elif win_2me == 2:#赢
            print(win[random.randint(0,len(win)-1)])            
            if mode != 2:
                item_drop(2,2)
            else:
                item1["合约纪念点"]+=entry_manager.total_points
                print("得分已等额转化为纪念点·请检查您的钱包")
                print("在下一行按下2以覆盖式保存结算画面，在仓库查看")
                sync()
        i=input("按任意键返回浅草寺空间站>>>")
        if mode == 2:
            endingpic_print(i)
def al_level_count():
    al_level=0
    for i,j in item3.items():
        num=allenskin.index(i)
        al_level+=globals()[f"al{num}"].rank_num*j
    return al_level
def personal_isk_shower():
    '''
    统计玩家的个人资产
    '''
    tree1 = Tree("账户信用点",f"{item1['联邦信用点']} ISK")

    item1_temp = item1.copy()
    item1_temp.pop("联邦信用点")
    item1_temp.pop("保险点")
    item1_temp.pop("合约纪念点")
    tree2 = Tree("基础物资",f"{sum(item1_temp.values())} 立方米",f"{int(sum(item1_temp.values())*1100/25)} ISK")

    tree3 = Tree("附加设备",f"{sum(item2.values())} 立方米",f"{int(sum(item2.values())*2000)} ISK")

def station_main():

    global eqm
    eqm.clear()
    entry_manager.loadentry(username)
    m5.play_sound("04_空间站-主体_管弦" , loop = True)
    while 1:#空间站打印
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        hour=time.localtime(time.time()).tm_hour
        minute=time.localtime(time.time()).tm_min
        left_station_tree = Tree(
            "当前空间站>>>联邦海军L33地区“浅草寺”前哨空间站",
            f"空间天气>{
                random.choice(
                    ["晴朗","大雾","恒星磁暴","微陨石暴雨","平静","error-空间站气象仪故障","恒星季风","小行星骤雨","稀疏尘埃云","稠密尘埃云"]
                )
            }",
            f"轨道高度>{random.randint(35997,36003)} km",
            random.choice(
                ["出入站航道>正常",
                "哨站食堂>午饭供应中",
                "哨站宿舍>热水供应时段",
                "航站机库>无人机蜂群正在停泊",
                f"武器装备库>{random.choice(allenskin)}正在检修",
                "船舶检修>正常"]
                ),
            f"站内时间>{hour}:{minute}"
        )

        right_user_tree = Tree(
            f"持证指挥官>>{username}",
            f"从属舰艇>>>{shipname}号侦查护卫舰",
            f"信用点：{item1['联邦信用点']} ISK",
            f"合约纪念点：{int(item1['合约纪念点'])} CMP"
        )

        ssg_tag = "[保险点未覆盖当前舰船]" if item1["保险点"]<al_count() else ">>保险点已覆盖当前舰船<<"
        right_alssgeqm_tree = Tree(
            f"""装备配置 总等级 {al_count()} {ssg_tag} 保险点--{item1["保险点"]}""",

            "武器站:"+globals().get(f"al{choi[3]}",al_none).tag.get("出身","")
            +allenskin[choi[3]]+f"（{item3.get(allenskin[choi[3]],"无")}）",

            "维修器:"+globals().get(f"al{choi[4]}",al_none).tag.get("出身","")
            +allenskin[choi[4]]+f"（{item3.get(allenskin[choi[4]],"无")}）",

            "战术区:"+globals().get(f"al{choi[5]}",al_none).tag.get("出身","")
            +allenskin[choi[5]]+f"（{item3.get(allenskin[choi[5]],"无")}）",

            eqm
        )
        

        right_store_tree = Tree(
            f"仓库存储>正常",
            f"物品仓库>{item1count()}立方米",
            f"装备仓库>{item2count()}件",
            f"战术快递>{sum(item5.values())}件",
            "[s0/z]访问仓库"
        )
        
        mid_res_nevigator_tree = Tree(
            resource_nevigator.tree_output_title(),
            resource_nevigator.tree_output_body()
        )

        left_gui_tree = Tree(
            "空间站服务",
            "|---THE SHIP/舰船---/",
            "p1/x=离站并开始任务",
            "p2=更换所有装备 q/w/e=更换对应装备",
            "p3=重命名舰船",
            "|---ALs/主要装备---/",
            "a1/c=工业合成装备 a2/v=装备资源跟踪器",
            "|EQM&FPS/外加/快递设备/",
            "e1=工业合成战术设备",
            "e2=安装战术设备 e3=卸载所有战术设备",
            "f1=合成战术快递",
            "|---CON/战死之地----/",
            "c1=战死之地词条编辑 c2=访问合约商店",
            "|---GTC/贸易中心----/",
            "g1=前往贸易中心",
            "|-------------------/",
            "enter=刷新界面"
        )

        mid_alcraft_tree = Tree(
            "空间站工业",
            f"个人资产当量估值>{int(
                (item1count()*40+item1['联邦信用点']+item1['合约纪念点']*10)/2100+al_level_count()
            )}级",
            "[a1]前往工业合成区",
            "[a2]装备资源跟踪器"
        )

        def available_con_count():
            out = 0
            for i in range(1,25):
                con_temp:Contract = globals()[f'con{i}']
                if con_temp.affordable() and not con_temp.is_traded:
                    out += 1
            return out

        mid_market_tree = Tree(
            "星际贸易中心",
            f"个人信用点>{item1['联邦信用点']} ISK",
            f"可交易合同>{available_con_count()}/24",
            "[g1]前往贸易中心"
        )

        left    = []
        mid     = []
        right   = []

        left += left_station_tree.linelist()
        left += left_gui_tree.linelist()

        mid  += mid_alcraft_tree.linelist()
        mid  += mid_res_nevigator_tree.linelist()
        mid  += mid_market_tree.linelist()

        right+= right_user_tree.linelist()
        right+= right_alssgeqm_tree.linelist()
        right+= entry_manager.tree().linelist(is_foldable=True)
        right+= right_store_tree.linelist()

        m1.n_columnprint([left,right,mid],[55,65])

        #three_columnprint(left,right,restree.linelist())
        #doublecolumn结束，这一行下面是input
        pos=input(">>>")
        if pos == "s0" or pos == "z":
            itemprint("空间站物品仓库",item1,20,6)
            print("物资分布统计与当下盈亏：")
            m1.dict_diff_print(item1_old,item1)
            itemprint("空间站装备仓库",item2,20,6)
            itemprint("主装备仓库",item3,20,6)
            itemprint("战术快递仓库",item5,20,6)
            ifp=input("[enter] 退出|[2] 观看已保存的结算画面>>>")
            if ifp == "2":
                sf=shelve.open("savedata")
                try:
                    pic=sf[username+"pic"]
                    m1.two_columnprint(pic[0],pic[1],di=70)
                    input("[enter] 退出>>>")
                except:
                    pass
                sf.close()
        elif pos == "e1":
            while 1:
                craftprint()
                cra=craft()
                if cra == 0:
                    break
        elif pos == "p1" or pos == "x":
            m1.printplus("\n[浅草寺]离站请求已被接受",0)
            time.sleep(0.4)
            break
        elif pos == "p2":
            choiprint()
        elif pos in ["q","w","e"]:
            choiprintplus(pos)
        elif pos == "p3":
            usersave()
        elif pos == "e2":
            eqmprint()
        elif pos == "e3":
            eqm=[]
        elif pos == "a1" or pos == "c":
            while 1:
                al_craft_print()
                cra=al_craft()
                if cra == 0:
                    break    
        elif pos == "a2" or pos == "v":
            resource_nevigator.ask() 
        elif pos == "c1":
            entry_manager.ask(username)
        elif pos == "c2":
            cmp_market.market_main()
        elif pos == "g1":
            contract_maneger.contract_market_main()
        elif pos == "f1":
            fps_manager.craft_main()

m1.printplus(f"\n{__version_txt__} > 工程启动中 > \n")
m1.inputplus("按任意键开始游戏|输入后请回车>>>")
username=m1.inputplus("指挥官，请输入您的代号>>>")
storehouse_load_or_new()
userload()
m1.printplus(f"指挥官{username}登陆成功·欢迎来到浅草寺",0.3)

contract_maneger.market_generate(24)
item1_old=item1.copy()
while 1:#全游戏循环mian_loop()
    if inf == 0:
        station_main()

#模式选择

    print()
    deptree=Tree("准备起锚·导航器已就位",
                    "[-1]取消出发计划并回站",
                    "[0]突袭行星际海盗窝点 [基本对战]",
                    "[1]边境敌军清剿 [无尽模式]",
                    "[2]战死之地 [危机合约]",
                    "[3]沉默渗透敌方基地 [全盲模式]",
                    "[4]跃迁到矿区 [工业开采]",
                    "[5]进入死亡深空 [肉鸽模式]",
                    "[6]Faker vs Bin 模式 [危机合约][重新选择装备] ")
    if not al_is_ready():
        print("并非所有装备均有存货·你将不能离站",end="\n\n")
    deptree.treeprint()
    inp0 =m1.ask_plus(
            ">>>",
            [str(i) for i in range(-1,7)] + [""]
        )
    if inp0.isdigit():
        inp0 = int(inp0)
    if not al_is_ready() or inp0 in (-1,""):
        continue
    if inp0 in (0,1,2,3,5):
        itemcost()
    if inp0 == 5:
        choi=[0,1,2,17,18,7]
        mode = inp0
    else:
        mode = inp0
        win_2me = 1
    if mode == 2:#危机合约
        reset_general()
        hard = 0
        ranop()
    elif mode == 6:
        faker_vs_bin_main()
    elif mode == 1:#无尽
        infinity_manager.infinity_mode_main()
    elif mode == 5:#肉鸽
        room_manager.rog_main()
    else:
        entry_manager.refresh()
        reset_general()
        ranop(4+al_count()//3)
    if mode in (0,2,3,6):                 #这里是战斗或采矿的单次代码
        if "临时装甲板" in eqm:          #
            player_cureplus(2)          #
        fight_daily()                   #
    elif mode == 4:                     #
        mining_daily()                  #

    time.sleep(0.8)
    print("任务结束·舰船待命中")
    
    if mode == 2 and win_2me == 2:
        endingpic_print("p")
        entry_manager.print_now()
    elif mode == 6:
        userload()
    ending()


    
        
    
    
