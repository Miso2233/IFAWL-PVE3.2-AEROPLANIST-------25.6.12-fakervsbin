from Module_01_txt import Tree
import Module_01_txt as m1

class Fps_general:

    title                   = ""

    def __init__(self,
                 title:str,
                 description:str,
                 cost_list:dict = {"联邦信用点":1100},
                 ):
        self.cost_list      = cost_list.copy()
        self.description    = description
        self.title          = title
        self.index          = int(self.__class__.__qualname__[3:])

    def react(self):
        pass

    def is_craftable(self,item1,num = 1) -> bool:
        for i in self.cost_list:
            if self.cost_list[i]*num>item1[i]:
                return False
        return True
    
    def max_craft_num(self,item1) -> int :
        lst = []
        for i in self.cost_list:
            lst.append(item1[i]//self.cost_list[i])
        return min(lst)
    
    def print_description(self,item5):
        """
        [编号]标题 0在仓库

        |-描述文本
        """
        Tree(f"[{self.index}]{self.title} {item5[self.title]}在仓库",self.description).treeprint()

    def print_formula(self,item5):
        """
        [编号]标题 0在仓库

        |-描述文本

        |-联邦信用点*1
        """
        Tree(f"[{self.index}]{self.title} {item5[self.title]}在仓库",self.description,self.cost_list).treeprint()

    def print_calling(self,item5):
        """
        --- NOTE 

        #只在仓库里有该快递时显示

        [编号]标题 0在仓库

        |-描述文本
        """
        if item5[self.title]>0:
            Tree(f"[{self.index}]{self.title} {item5[self.title]}在仓库",self.description).treeprint()
        else:
            print(f"[{self.index}]{self.title} 无物品|不能发射",end = "\n\n")

    def craft_self(self,item1,item5):
        if self.is_craftable(item1):
            for i in item1:
                item1[i] -= self.cost_list.get(i,0)
            item5[self.title] += 1
            m1.printplus(f"{self.title}*1 合成成功")
        else:
            m1.printplus("材料不足，合成失败")

    def report(self):
        m1.printplus(f"[浅草寺]收到，{self.title}正在升空")


class Eqm_general:

    title                   = ""

    def __init__(self,
                 title:str,
                 description:str,
                 cost_list:dict = {"联邦信用点":1100},
                 ):
        self.cost_list      = cost_list.copy()
        self.description    = description
        self.title          = title




