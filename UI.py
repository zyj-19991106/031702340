from tkinter import *
from tkinter import ttk
class menu_interface():
    def __init__(self, master):
        self.root = master
        self.root.title("菜单界面")
        self.root.geometry("405x720")
        global photo1
        photo1 = PhotoImage(file=".\\ui附带图\\2.gif")#福州最受欢迎商圈
        Button(self.root,command=self.click1 ,relief="flat",image=photo1).place(x=32,y=20, width=145,height=196)
        global photo2
        photo2 = PhotoImage(file=".\\ui附带图\\3.gif")#福州性价最高餐厅
        Button(self.root,command=self.click2 , relief="flat",image=photo2).place(x=231,y=266,width=135, height=180)
        global photo3
        photo3 = PhotoImage(file=".\\ui附带图\\4.gif")#福州最佳美食聚集地
        Button(self.root, command=self.click3 ,relief="flat",image=photo3).place(x=202, y=16, width=181, height=217)
        global photo4
        photo4 = PhotoImage(file=".\\ui附带图\\5.gif")#福州最高评分商圈
        Button(self.root,command=self.click4 ,relief="flat",image=photo4).place(x=28, y=243, width=164, height=224)
    def click1(self):
        t1 = Toplevel()
        t1.title("福州最受欢迎商圈")
        t1.geometry('475x286')
        global photo11
        photo11 = PhotoImage(file=".\\ui附带图\\12.gif")
        Label(t1, image=photo11).place(x=0, y=0, width=475, height=286)  # 把图片整合到标签类中
    def click2(self):
        self.root.destroy()
        root = Tk()
        photo5 = PhotoImage(file=".\\ui附带图\\6.gif")
        Label(root, image=photo5).place(x=0, y=0, width=405, height=720)  # 把图片整合到标签类中
        food_interface(root)
    def click3(self):
        t1 = Toplevel()
        t1.title("福州最佳美食聚集地")
        t1.geometry('554x386')
        global photo12
        photo12 = PhotoImage(file=".\\ui附带图\\14.gif")
        Label(t1, image=photo12).place(x=0, y=0, width=347, height=154)  # 把图片整合到标签类中
        global photo13
        photo13 = PhotoImage(file=".\\ui附带图\\13.gif")
        Label(t1, image=photo13).place(x=0, y=154, width=554, height=232)  # 把图片整合到标签类中
    def click4(self):
        t1=Toplevel()
        t1.title("福州服饰最高评分商圈")
        t1.geometry('615x386')
        global photo14
        photo14 = PhotoImage(file=".\\ui附带图\\15.gif")
        Label(t1, image=photo14).place(x=0, y=0, width=615, height=386)  # 把图片整合到标签类中
class food_interface():
    def __init__(self, master):
        self.root = master
        self.root.title("美食餐厅排行榜")
        self.root.geometry("405x720")
        #Button(self.root, text="返回", font=("华文行楷", 30),command=self.click1, relief="flat", bg="#e5e5e5").place(x=37, y=25, width=173, height=62)
        global photo6
        photo6 = PhotoImage(file=".\\ui附带图\\7.gif")  # 福州最受欢迎商圈
        Button(self.root, command=self.click1, relief="flat", image=photo6).place(x=41, y=63, width=140, height=148)
        global photo7
        photo7 = PhotoImage(file=".\\ui附带图\\8.gif")  # 福州性价最高餐厅
        Button(self.root, command=self.click2, relief="flat", image=photo7).place(x=228, y=178, width=140, height=147)
        global photo8
        photo8 = PhotoImage(file=".\\ui附带图\\9.gif")  # 福州最佳美食聚集地
        Button(self.root, command=self.click3, relief="flat", image=photo8).place(x=34, y=320, width=151, height=149)
        global photo9
        photo9 = PhotoImage(file=".\\ui附带图\\10.gif")  # 福州最高评分商圈
        Button(self.root, command=self.click4, relief="flat", image=photo9).place(x=225, y=427, width=150 ,height=158)
        global photo10
        photo10 = PhotoImage(file=".\\ui附带图\\11.gif")  # 福州最高评分商圈
        Button(self.root, command=self.click5, relief="flat", image=photo10).place(x=279, y=641, width=83, height=46)
        self.root.mainloop()
    def click5(self):
        self.root.destroy()
        root = Tk()
        photo = PhotoImage(file=".\\ui附带图\\1.gif")
        Label(root, image=photo).place(x=0, y=0, width=405, height=720)  # 把图片整合到标签类中
        menu_interface(root)
        root.mainloop()
    def click1(self):
        w = Tk()
        
        scrollBar = Scrollbar(w)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = ttk.Treeview(w, yscrollcommand=scrollBar.set, show="headings")
        scrollBar.config(command=tree.yview)

        def treeviewClick(event):
            tree.bind('<Button-1>', treeviewClick)

        tree.bind('<Button-1>', treeviewClick)
        tree["columns"] = ("店名","地址", "星级", "点评数", "人均", "口味", "环境","服务")
        tree.column("店名", width=100, anchor='center')  # 表示列,不显示
        tree.column("地址", width=250, anchor='center')
        tree.column("星级", width=50, anchor='center')
        tree.column("点评数", width=50, anchor='center')
        tree.column("人均", width=50, anchor='center')
        tree.column("口味", width=50, anchor='center')
        tree.column("环境", width=50, anchor='center')
        tree.column("服务", width=50, anchor='center')
        tree.heading("店名", text="店名")  # 显示表头
        tree.heading("地址", text="地址")
        tree.heading("星级", text="星级")
        tree.heading("点评数", text="点评数")
        tree.heading("人均", text="人均")
        tree.heading("口味", text="口味")
        tree.heading("环境", text="环境")
        tree.heading("服务", text="服务")
        tree.insert("", "1", values=("学姐的店","博仕后","国宾大道233号","五星","166","7","9.3","9.2","9.3"))
        tree.insert("", "1", values=("巢南之（福大店）","博仕后","学府北路","五星","70","16","9.2","9.2","9.2"))
        tree.insert("", "1", values=("一谷茉莉鲜果茶(三坊七巷店)"	,"东街口吉庇巷87-10"	,"五星"	,"206",	"14","9.2","9.1","9.2"))
        tree.insert("", "1", values=("韩一点","闽侯县 10国道闽江学院东门","五星","206","23","9.1","9.1","9.1"))
        tree.insert("", "1", values=("唐沫茶兮（仓山万达店","仓山万达广场 浦上大道272号万达广场金街","五星","527","16","9.2","9.2","9.2"))
        tree.pack()
    def click2(self):
        w = Tk()
       
        scrollBar = Scrollbar(w)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = ttk.Treeview(w, yscrollcommand=scrollBar.set, show="headings")
        scrollBar.config(command=tree.yview)

        def treeviewClick(event):
            tree.bind('<Button-1>', treeviewClick)

        tree.bind('<Button-1>', treeviewClick)
        tree["columns"] = ("店名", "地址", "星级", "点评数", "人均", "口味", "环境", "服务")
        tree.column("店名", width=100, anchor='center')  # 表示列,不显示
        tree.column("地址", width=250, anchor='center')
        tree.column("星级", width=50, anchor='center')
        tree.column("点评数", width=50, anchor='center')
        tree.column("人均", width=50, anchor='center')
        tree.column("口味", width=50, anchor='center')
        tree.column("环境", width=50, anchor='center')
        tree.column("服务", width=50, anchor='center')
        tree.heading("店名", text="店名")  # 显示表头
        tree.heading("地址", text="地址")
        tree.heading("星级", text="星级")
        tree.heading("点评数", text="点评数")
        tree.heading("人均", text="人均")
        tree.heading("口味", text="口味")
        tree.heading("环境", text="环境")
        tree.heading("服务", text="服务")
        tree.insert("", "1", values=("胜好寿司(仓山万达店)",	"仓山万达 广场浦上大道亭头路253-29号",	"五星",	"93",	"67",	"9.2"	,"9.1",	"9.1"))
        tree.insert("", "1", values=("骨之味(世欧王庄店)",	"王庄 长乐中路世欧王庄广场南区4楼"	,"五星"	"359",	"90",	"9.1"	,"9.2",	"9.3"))
        tree.insert("", "1", values=("宫创意寿司"	,"正祥中心 水部街道高桥巷华翔新村C#12号店面",	"五星"	,"305",	"60",	"9.1",	"8.9"	,"9.1"))
        tree.insert("", "1", values=("抖渝","博仕后上街镇邱阳东路8号书香领寓4号楼1层07-09号店面",	"五星",	"343",	"53"	,"9.2"	,"9.2",	"9.3"))
        tree.insert("", "1", values=("潮粥荟(世欧店)",	"王庄 长河路世欧广场南区四楼108",	"五星"	,"1354",	"79","9.1","9.1","9.1"))
        tree.pack()
    def click3(self):

        w = Tk()
       
        scrollBar = Scrollbar(w)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = ttk.Treeview(w, yscrollcommand=scrollBar.set, show="headings")
        scrollBar.config(command=tree.yview)

        def treeviewClick(event):
            tree.bind('<Button-1>', treeviewClick)

        tree.bind('<Button-1>', treeviewClick)
        tree["columns"] = ("店名", "地址", "星级", "点评数", "人均", "口味", "环境", "服务")
        tree.column("店名", width=150, anchor='center')  # 表示列,不显示
        tree.column("地址", width=250, anchor='center')
        tree.column("星级", width=50, anchor='center')
        tree.column("点评数", width=50, anchor='center')
        tree.column("人均", width=50, anchor='center')
        tree.column("口味", width=50, anchor='center')
        tree.column("环境", width=50, anchor='center')
        tree.column("服务", width=50, anchor='center')
        tree.heading("店名", text="店名")  # 显示表头
        tree.heading("地址", text="地址")
        tree.heading("星级", text="星级")
        tree.heading("点评数", text="点评数")
        tree.heading("人均", text="人均")
        tree.heading("口味", text="口味")
        tree.heading("环境", text="环境")
        tree.heading("服务", text="服务")
        tree.insert("", "1", values=("肉倉焼肉バー",	"东街口 勺园里4座101",	"五星",	"158",	"121",	"9.2"	,"9.2",	"9.2"))
        tree.insert("", "1", values=("肉祭烧肉一番(万象生活城店)	","宝龙万象"	,"五星",	"1993"	,"126"	,"9.2",	"9.1"	,"9.2"))
        tree.insert("", "1", values=("海底捞火锅(东方百货店)"	,"东街口 杨桥东路8号东方百货7层",	"五星"	,"1359",	"117"	,"9.2",	"9.2",	"9.2"))
        tree.insert("", "1", values=("海底捞火锅(工业路苏宁广场店)",	"苏宁广场 工业路233号苏宁广场5楼501"	,"五星"	,"1736",	"123",	"9.2"	,"9.2",	"9.3"))
        tree.insert("", "1", values=("左稻(融侨中心店)"	,"宝龙万象 江滨西大道100号融侨中心ARTMALL4楼",	"五星",	"1364",	"181",	"9.1",	"9.3"	,"9.1"))
        tree.pack()
    def click4(self):
        w = Tk()
      
        scrollBar = Scrollbar(w)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = ttk.Treeview(w, yscrollcommand=scrollBar.set, show="headings")
        scrollBar.config(command=tree.yview)
        def treeviewClick(event):
            tree.bind('<Button-1>', treeviewClick)
        tree.bind('<Button-1>', treeviewClick)
        tree["columns"] = ("店名", "地址", "星级", "点评数", "人均", "口味", "环境", "服务")
        tree.column("店名", width=100, anchor='center')  # 表示列,不显示
        tree.column("地址", width=250, anchor='center')
        tree.column("星级", width=50, anchor='center')
        tree.column("点评数", width=50, anchor='center')
        tree.column("人均", width=50, anchor='center')
        tree.column("口味", width=50, anchor='center')
        tree.column("环境", width=50, anchor='center')
        tree.column("服务", width=50, anchor='center')
        tree.heading("店名", text="店名")  # 显示表头
        tree.heading("地址", text="地址")
        tree.heading("星级", text="星级")
        tree.heading("点评数", text="点评数")
        tree.heading("人均", text="人均")
        tree.heading("口味", text="口味")
        tree.heading("环境", text="环境")
        tree.heading("服务", text="服务")
        tree.insert("", "1", values=("宣和苑"	,"左海/西湖公园 西二环路华侨新村内32号",	"五星",	"599"	,"368",	"9.2"	,"9.3"	,"9.2"))
        tree.insert("", "1", values=("禧悦楼"	,"鼓屏路/屏山公园 福飞南路156号璞璟酒店3楼"	,"五星"	,"483",	"380",	"9.2"	,"9.3",	"9.2"))
        tree.insert("", "1", values=("松月自慢料理",	"五四路商务区 北二环中路21号"	"五星"	,"1028",	"359"	,"9.2"	,"9.3",	"9.1"))
        tree.insert("", "1", values=("渡鲑亭"	,"东二环泰禾 连江北路东二环泰禾广场新天地13号楼2楼229",	"五星"	,"342",	"273"	,"9.2",	"9.1",	"9.4"))
        tree.insert("", "1", values=("埖绛法式日料花园餐厅","	左海/西湖公园 西二环北路236号华侨新村28座内"	,"五星"	,"192"	,"263",	"9.0"	,"9.3"	,"9.2"))
        tree.pack()
class foodflock_inerface():
    def __init__(self, master):
        self.root = master
        self.root.title("最佳美食聚集地")
        self.root.geometry("934x960")
        Button(self.root, text="返回", font=("华文行楷", 30),command=self.click1, relief="flat", bg="#fff5ee").place(x=43, y=320, width=131,
                                                                                           height=90)
        Label(self.root, text="", font=("华文行楷", 15), bg="#fff5ee").place(x=258, y=130, width=568, height=706)
        self.root.mainloop()
    def click1(self):
        self.root.destroy()
        root = Tk()
        menu_interface(root)
        root.mainloop()

if __name__ == '__main__':
    root = Tk()
    photo = PhotoImage(file=".\\ui附带图\\1.gif")
    Label(root, image=photo).place(x=0, y=0, width=405, height=720)  # 把图片整合到标签类中
    menu_interface(root)
    root.mainloop()
