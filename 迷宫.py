
import pygame #引入pygame模块
'''这两行是打开游戏窗口'''
pygame.init()
pygame.mixer.init()#引入pygame中的音乐模块
chang=pygame.mixer.Sound('field.wav')#进入游戏后播放主界面音乐
chang.play(-1)

window=pygame.display.set_mode((760,560))  #设置游戏窗口大小
pygame.display.set_caption('关于勇者在迷宫里捡宝物还要躲着魔物这档事')
window.fill((255,255,255))#将界面设置为白色
pygame.display .update()  #刷新窗口，下同

image1=pygame.image.load('界面2.jpg')
#blit是渲染打开的图片，使其能加载到窗口里
window.blit(image1,(0,0))
pygame.display.flip()

font =pygame .font .Font('简体.TTF',30)

#确定按钮
bx1,by1,bw,bh=325,300,150,50#按钮的位置及大小
pygame .draw.rect(window,(255,0,0),(bx1,by1,bw,bh))
text1=font.render('任意处开始',True,(255,255,255) )#设置开始按钮的内容
tw1,th1=text1.get_size()#获取方框大小
tx1=bx1+bw/2-tw1/2#计算将文字放在矩形框中间
ty1=by1+bh/2-th1/2
window.blit(text1,(tx1,ty1))
pygame.display.update()


#让创建的窗口能够检测鼠标按键
while True:
    for event in pygame.event.get():
        '''检测窗口被关闭'''
        if event.type== pygame.QUIT:
            exit()
        if event.type== pygame .MOUSEBUTTONDOWN : #这里检测鼠标按键按下
            mx,my=event.pos
            if bx1<=mx<=bx1+bw and by1<=my<=by1+bh:  #检测鼠标按下的坐标范围
                pygame .draw .rect(window,(200,200,200),(bx1,by1,bw,bh) )
                window.blit(text1,(tx1,ty1))
                pygame .display .update()
        if event.type==pygame .MOUSEBUTTONUP :  #这里检测鼠标按键抬起
            mx, my = event.pos
            if bx1 <= mx <= bx1 + bw and by1 <= my <= by1 + bh:   #检测鼠标按键抬起的范围
                pygame .draw.rect(window,(255,0,0),(bx1,by1,bw,bh))
                window.blit(text1 ,(tx1,ty1))
                pygame .display .update()

            '''现在进入游戏主体'''
            import turtle as k
            import random
            import pygame
            pygame.mixer.init()  #同样引入pygame中的音乐模块
            win=pygame.mixer.Sound('win.wav')    #定义播放关卡胜利音乐的变量
            lose=pygame.mixer.Sound('lose.wav')  #定义播放关卡失败音乐的变量
            get=pygame.mixer.Sound('get.wav')    #定义播放捡到宝箱音乐的变量
            chang=pygame.mixer.Sound('field.wav')#定义播放背景音乐的变量

            mg = k.Screen() #创建窗口
            mg.setup(820, 820) #窗口大小

            mg.bgcolor('black')
            mg.title('关于勇者在迷宫里捡宝物还要躲着魔物这档事')
            # 这里用函数改变画笔的形状，改变成图片文件以满足游戏显示的需要
            mg.register_shape('rock.gif')  #用来画墙壁
            mg.register_shape('player.gif')  #用来画玩家，下面是画玩家不同状态时的画面
            mg.register_shape('playerR.gif')
            mg.register_shape('playerL.gif')
            mg.register_shape('playerB.gif')
            mg.register_shape('gui.gif')     #用来画敌人
            mg.register_shape('bao.gif')     #用来画宝箱
            mg.tracer(0)#让迷宫等元素立马画出来

            #这里开始画每个关卡，用“X”表示墙壁，用“P”表示玩家，用“B”表示宝箱，用“G”表示敌人
            levels = []   #定义一个关卡的数组
            level_1 =[    #第一关
            'XXXXXXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXXXXB      XXXXXXXXXXX',
            'XXXXXXXXX P    XXXXXXXXXXX',
            'XXXXXXXXX      XXXXXXXXXXX',
            'XXXXXXXXX      XXXXXXXXXXX',
            'XXXXXXXXX     BXXXXXXXXXXX',
            'XXXXXXXXXXX  XXXXXXXXXXXXX',
            'XXXXXXXX     XXXXXXXXXXXXX',
            'XXXXXXXXXX    XXXXXXXXXXXX',
            'XXXXXXXXXXX    GXXXXXXXXXX',
            'XXXXXXXXXXXX         XXXXX',
            'XXXXXXXXXXXX         XXXXX',
            'XXXXXXXXXXXG         XXXXX',
            'XXXXXXXXXXX          XXXXX',
            'XXXXXXXXBXXXXXXXXX   XXXXX',
            'XXXXXX    XXXXXXXX   XXXXX',
            'XXXXXXX              GXXXX',
            'XXXX             BXXXXXXXX',
            'XXXXXX   XXXXXXXXXXXXXXXXX',
            'XXXXXX   GXXXXXXXXXXXXXXXX',
            'XXXXXXX   XXXXXXXXXXXXXXXX',
            'XXXXXXX   XXXXXXXXXXXXXXXX',
            'XXXXXXXX         XXXXXXXXX',
            'XXXXXXXXXXXXXX   XXXXXXXXX',
            'XXXXXXXXXXXXXXX BXXXXXXXXX',
            'XXXXXXXXXXXXXXXXXXXXXXXXXX'
            ]
            level_2 =[    #第二关
            'XXXXXXXXXXXXXXXXXXXXXXXXXX',
            'XXXP        XXXXXXXXXXXXXX',
            'XXXXXXXX           XXXXXXX',
            'XXXXXXX    XX         XXXX',
            'XXXXXX     XXXXXX       XX',
            'XXB      XXXXXXXXX      XX',
            'XXXXXXXXXXXXX         XXXX',
            'XXXXXXXXXXXXXXXXX     GXXX',
            'XXXXXXXXXX           BXXXX',
            'XXXXXXXXX      XXXXXXXXXXX',
            'XXXXXXXXXXXX   XXXXXXXXXXX',
            'XXXXXXXXXXXX          XXXX',
            'XXX            XXXXX  XXXX',
            'XXX   GXXXXX   XXXGX  XXXX',
            'XXXX   XXXXX   XXXXX  XXXX',
            'XXXX   XXXXX    XXX    XXX',
            'XXXXX   XXXX    XXX    XXX',
            'XXXXXB   XXX    XXXB   XXX',
            'XXXXXXXXXXX     XXXXXXXXXX',
            'XXXXXXXX       XXXXXXGXXXX',
            'XXXXXX     XXXXXXXX  XXXXX',
            'XXXXXXX              GXXXX',
            'XXXXXXXX    BXXXX   XXXXXX',
            'XXXXXXXXXXXXXXXXXB   XXXXX',
            'XXXXXXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXXXXXXXXXXXXXXXXXXXXXX'
            ]
            level_3 =[    #第三关
            'XXXXXXXXXXXXXXXXXXXXXXXXXX',
            'XXX   XXXXXXXXXXXXXXXXXXXX',
            'XXP   XXXXXXXB     XXXXXXX',
            'XXX  XXXXXXXXXXXX  XXXXXXX',
            'XX   XXXXXXXXXXXX  XXGXXXX',
            'XX  XXXXXXXXXXXX   XXXXXXX',
            'XX                  XXXXXX',
            'XXXXX   XXXXXXXXX  XXXXXXX',
            'XXXXXX  XXXXXXXX     GXXXX',
            'XXXX    XXXXXXX  XXXXXXXXX',
            'XXXX    XXXXXXX  XXXXXXXXX',
            'XXXX    XX             XXX',
            'XXXXXX  XXXXXXXX   XXXXXXX',
            'XXB       BXXGXXX  XXXXXXX',
            'XXXX   XXXXXXXXXX  XXXXXXX',
            'XXXXX  XXXXXX          XXX',
            'XXXXXXXXXXXXXXXXX  XX  XXX',
            'XX         XXXXXX  XXX   X',
            'XXXX  XXX     XXX  XXB  XX',
            'X     XXX   XXXXX  XXX  XX',
            'XXXX  XXXB  BXXXX  XX  XXX',
            'XXG   XXXX  XXXXX  X    XX',
            'XXX   XXXXXXXXGXX  XX  XXX',
            'XX                    XXXX',
            'XXXXXXB XXXXXXXXX GXXXXXXX',
            'XXXXXXXXXXXXXXXXXXXXXXXXXX'
            ]
            levels . append(level_1 ) #用append将关卡放到定义的数组里面了
            levels . append(level_2 )
            levels . append(level_3 )

            score=0
            life=1
            '''定义一个专门写分数和命数的pen，'''
            pen6 =k.Turtle()
            pen6.ht()
            pen6.speed(0)
            pen6.penup()
            pen6.goto(-750, 360)  #显示分数的位置
            font = ('Arial', 20, 'bold')  #分数的字体
            pen6.color('red')
            pen6.write('当前分数：{}  生命：{}'.format(score, life), align='left', font=font)  #在游戏左上角来显示分数


            class Ghost(k.Turtle):  #这里定义敌人的类
                def __init__(self):
                    super().__init__()  #使用super()函数进行多重继承，避免代码重复造成冗余
                    self.ht()
                    self.shape('gui.gif')  #敌人的形状
                    self.speed(0)
                    self.penup()
                    self.st()

                def move(self):    #定义敌人移动的函数
                    self.turn()
                    if self.ds =='U':     #向上移动
                        run_x = self.xcor()
                        run_y = self.ycor() +30#每次移动30个像素，下面的都是向对应方向移动30像素
                    elif self.ds =='D':   #向下移动
                        run_x = self.xcor()
                        run_y = self.ycor() -30
                    elif self.ds =='L':   #向左移动
                        run_x = self.xcor() -30
                        run_y = self.ycor()
                    elif self.ds =='R':   #向右移动
                        run_x = self.xcor()+30
                        run_y = self.ycor()
                    self.goto(run_x ,run_y )
                    k.ontimer(self.move,random.randint(100,400))  #这里用随机数来控制敌人每次移动的间隔时间

                def turn(self):#这里定义鬼来跟随玩家
                    if self.distance(player) <90:   #当敌人与玩家间隔的距离小于90像素的时候敌人就会向玩家靠近
                        if self.xcor() < player.xcor():
                            self.ds ='R'  #当敌人横坐标距离小于玩家时，说明敌人在玩家左边，则敌人会向右移动来靠近玩家(下同)
                        elif self.xcor() > player.xcor():
                            self.ds ='L'
                        elif self.ycor() < player.ycor():
                            self.ds ='U'
                        elif self.ycor() > player.ycor():
                            self.ds ='D'
                    else:
                        self.ds = random.choice(['U', 'D', 'L', 'R'])  #若敌人与玩家距离大于90像素的时候就会随机移动

                    # global life
                    # life=1
                    # if self.distance(player)<30:
                    #     life-=1
                    #     print(life )
                    # if life==0:
                    #     breakpoint()
                    '''这里虽然定义了玩家会死亡，但发现有多余的代码，并且会导致程序崩溃'''
                    '''在下面用循环结构来实现玩家死亡'''


            class Bao(k.Turtle):   #定义宝箱类
                def __init__(self):
                    super().__init__()  #super()函数实现多重继承
                    #下面是画宝箱的各种操作
                    self.ht()
                    self.shape('bao.gif')
                    self.speed(0)
                    self.penup()
                    self.st()

            class Player(k.Turtle):  #定义玩家类
                def __init__(self):
                    super().__init__()
                    self.ht()
                    self.shape('player.gif')
                    self.speed(0)
                    self.penup()
                    self.st()
                def go_right(self):       #定义玩家向右移动的函数
                    run_x=self.xcor()+30  #每次移动距离也是30像素（下同）
                    run_y=self.ycor()
                    self.shape('playerR.gif' )#移动的方向不一样，画出来的玩家的状态也不一样（下同）
                    self.move(run_x,run_y)
                def go_left(self):        #定义玩家向左移动的函数
                    run_x = self.xcor()-30
                    run_y = self.ycor()
                    self.shape('playerL.gif')
                    self.move(run_x, run_y)
                def go_up(self):          #定义玩家向上移动的函数
                    run_x = self.xcor()
                    run_y = self.ycor()+30
                    self.shape('playerB.gif')
                    self.move(run_x, run_y)
                def go_down(self):        #定义玩家向下移动的函数
                    run_x = self.xcor()
                    run_y = self.ycor()-30
                    self.shape('player.gif')
                    self.move(run_x, run_y)

                def move(self,run_x,run_y):  #储存玩家移动坐标的函数
                    if (run_x, run_y) not in rocks:
                        self.goto(run_x, run_y)
                        self.look_for_bao(run_x, run_y)

                def look_for_bao(self,run_x,run_y):
                    global score#全局变量，用来改变分数
                    for b in baowu:
                        if b.distance(player)==0:
                            score+=1
                            pen6.clear()
                            pen6.write('当前分数：{}  生命：{}'.format(score, life), align='left', font=font)
                            b.ht() #讲个小插曲，敲这段代码的时候这两行没有缩进
                            baowu .remove(b)#导致人物一旦移动宝物就会消失
                            get.play()
                    if not baowu :
                        success()



            class Pen(k.Turtle):  #创建画笔类，令它继承k.Turtle
                def __init__(self):
                    super().__init__()  #调用它自己的初始化方法
                    self.ht()
                    self.shape('rock.gif')
                    self.speed(0)
                    self.penup()
                    self.st()

                def draw_migong(self):  #定义画迷宫各部分的函数
                    level = levels[now_level-1]#变量提取
                    for i in range(len(level)):
                        row = level [i]
                        for j in range(len(row)):
                            zhou_x = -380 + 30 * j  #计算墙体要用的坐标数
                            zhou_y = 380 - 30 * i   #计算墙体要用的坐标数
                            if row[j]=='X':  #画墙体
                                self.goto(zhou_x,zhou_y )
                                self.stamp()#盖一个章，将墙体固定住
                                rocks.append((zhou_x ,zhou_y)) #用元组将迷宫的所有坐标储存起来
                            elif row[j]=='P':  #画玩家
                                player.goto(zhou_x,zhou_y)
                                player.st()
                            elif row[j]=='B':  #画宝箱
                                gold  = Bao()
                                baowu.append(gold)
                                gold.goto(zhou_x,zhou_y)
                                gold.st()
                            elif row[j]=='G':  #画敌人
                                gui = Ghost()#解析引用的gui的时候，=不能用俩
                                ghosts.append(gui)
                                gui.goto(zhou_x,zhou_y)
                                gui.st()

            '''进入下一关的操作'''
            now_level= 1
            def success():
                if (now_level ==len(levels ) ):  #通过判断之前定义存放关卡的列表长度来判断是否全通关
                    xianshi_success('太厉害了！','全通关！！！')
                    win.play()
                else:
                    xianshi_success('恭喜过关！','按回车键进入下一关')
                    win.play()

            success_pen = k.Turtle()
            def xianshi_success(title, msg):  #显示成功过关的信息
                success_pen.ht()
                success_pen.speed(0)
                success_pen.penup()
                success_pen.goto(-100, -100)
                success_pen.fillcolor('yellow')  # 设置填充色
                success_pen.begin_fill()  # 开始填充
                for i in range(4):
                    success_pen.fd(300)
                    success_pen.left(90)#这是转向的角度
                success_pen.end_fill()  # 结束填充
                success_pen.goto(-80, 100)
                success_pen.color('red')
                success_pen.write(title, align='left', font=('Arial', 20, 'bold'))
                success_pen.goto(-80, -30)
                success_pen.write(msg, align='left', font=('Arial', 20, 'bold'))

            def goon():
                global now_level #定义一个全局变量解析引用的 now_level
                if(now_level == len(levels)):
                    now_level = 1
                else:
                    now_level =now_level +1
                success_pen.clear()

                for g in ghosts :
                    g.ht()
                ghosts.clear() #清空鬼

                pen.clear()#清空画笔
                rocks.clear()#清空砖墙

                pen.draw_migong() #重新画墙
                for g in ghosts:
                    k.ontimer(g.move, random.randint(100, 400))


            '''调用你定义的类'''

            pen=Pen()
            player= Player()#player和迷宫的调用顺序不能反，顺序反了之后就会报错
            ghosts = []#将所有的鬼储存起来
            rocks = []#将所有墙坐标储存起来
            baowu = []#将所有的宝物坐标储存
            pen.draw_migong()  #进行画迷宫的操作


            mg.listen()  #让这个迷宫听你的
            mg.onkey(player.go_right,'Right')  #获取键盘的指令，控制玩家移动（下同）
            mg.onkey(player.go_left, 'Left')
            mg.onkey(player.go_up, 'Up')
            mg.onkey(player.go_down, 'Down')
            mg.onkey(goon, 'Return')
            
            for g in ghosts:
                k.ontimer(g.move,random.randint(100,400) )
            '''给鬼设置一个闹钟，让他们在规定的时间到了之后移动'''

            game_over= False  #从这里开始定义游戏结束
            while True:
                if game_over :  #当游戏结束时就退出程序
                    break
                mg.update()#使界面可以一直刷新
                for g in ghosts:
                    if g.distance(player)<30:  #当敌人与玩家距离小于30时，即敌人碰到了玩家
                        life-=1    #上面172行定义了初始生命值为1，这里让生命-1
                        pen6.clear()
                        pen6.write('当前分数：{}  生命：{}'.format(score, life), align='left', font=font)
                    if life == 0:  #当生命值为0的时候
                        lose.play()  #这里的lose是播放失败时候的音乐
                        game_over = True
                        pen1 = k.Turtle()  #使用画笔画出失败的信息
                        pen1.ht()
                        pen1.speed(0)
                        pen1.penup()
                        pen1.goto(-190, 0)
                        font = ('Arial', 20, 'bold')
                        pen1.color('red')
                        pen1.write('死了啦，都你害的啦，拜托！', align='left', font=font)    #显示失败信息
            mg.mainloop()  #允许程序循环执行，并进入等待和处理事件。当程序中的组件发生变化时可以实时更新窗口，这也是这个程序能运行起来的关键