import json, math
SK='#F6D2B4'; BL='#7DB3E8'; RD='#E8574A'; YL='#F5C842'; GR='#6CC27A'; INK='#1f2533'; GY='#cfd3da'
def C(cx,cy,r): return f"M{cx+r},{cy} A{r},{r} 0 1 1 {cx-r},{cy} A{r},{r} 0 1 1 {cx+r},{cy}"
def L(*p): return 'M'+' L'.join(f'{x},{y}' for x,y in p)
def Z(*p): return L(*p)+' Z'
def R(x,y,w,h,r=0):
    if r==0: return Z((x,y),(x+w,y),(x+w,y+h),(x,y+h))
    return f"M{x+r},{y} L{x+w-r},{y} Q{x+w},{y} {x+w},{y+r} L{x+w},{y+h-r} Q{x+w},{y+h} {x+w-r},{y+h} L{x+r},{y+h} Q{x},{y+h} {x},{y+h-r} L{x},{y+r} Q{x},{y} {x+r},{y} Z"
def A(cx,cy,r,a0,a1):
    x0=cx+r*math.cos(math.radians(a0)); y0=cy+r*math.sin(math.radians(a0)); x1=cx+r*math.cos(math.radians(a1)); y1=cy+r*math.sin(math.radians(a1))
    large=1 if (a1-a0)%360>180 else 0
    return f"M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f}"
def P(d,fill=None,sw=5,col=INK): return dict(k='p',d=d,fill=fill,sw=sw,col=col)
def T(x,y,txt,size=34,col=INK,anchor='middle',w=800): return dict(k='t',x=x,y=y,txt=txt,size=size,col=col,anchor=anchor,w=w)
BR='#c98a4b'
NV='#34405a'; SH='#2a2a2a'
def person(cx,cy,s=1.0,mood='ok',arms='down',shirt=BL,hair=INK,legs=True,tie=False,glasses=False):
    e=[]; hr=40*s; by=cy+hr+6*s; bh=115*s; bw=46*s
    if legs:
        e+=[P(R(cx-bw*0.75,by+bh-6,bw*0.68,70*s,6),NV,4),P(R(cx+bw*0.07,by+bh-6,bw*0.68,70*s,6),NV,4),
            P(R(cx-bw*0.95,by+bh+60*s,bw*0.9,16*s,7),SH,4),P(R(cx+bw*0.05,by+bh+60*s,bw*0.9,16*s,7),SH,4)]
    e.append(P(R(cx-8*s,cy+hr-6*s,16*s,16*s,3),SK,4))
    body=f"M{cx-bw*0.55},{by} Q{cx},{by-10*s} {cx+bw*0.55},{by} Q{cx+bw*1.05},{by+8*s} {cx+bw*0.95},{by+bh} L{cx-bw*0.95},{by+bh} Q{cx-bw*1.05},{by+8*s} {cx-bw*0.55},{by} Z"
    e.append(P(body,shirt,5))
    if tie: e.append(P(Z((cx,by+2),(cx+8*s,by+20*s),(cx,by+70*s),(cx-8*s,by+20*s)),RD,3))
    else: e.append(P(L((cx-12*s,by+2),(cx,by+16*s),(cx+12*s,by+2)),None,4))
    def arm(x0,y0,x1,y1,x2,y2):
        return [P(f"M{x0},{y0} Q{x1},{y1} {x2},{y2}",None,15*s,INK),P(f"M{x0},{y0} Q{x1},{y1} {x2},{y2}",None,9*s,shirt),P(C(x2,y2,9*s),SK,4)]
    L0=(cx-bw*0.8,by+14*s); R0=(cx+bw*0.8,by+14*s)
    A={'down':((cx-bw*1.2,by+50*s,cx-bw*1.15,by+bh*0.9),(cx+bw*1.2,by+50*s,cx+bw*1.15,by+bh*0.9)),
       'point':((cx-bw*1.2,by+50*s,cx-bw*1.15,by+bh*0.9),(cx+bw*1.6,by+10*s,cx+bw*2.6,by-5*s)),
       'up':((cx-bw*1.6,by-10*s,cx-bw*1.9,by-70*s),(cx+bw*1.6,by-10*s,cx+bw*1.9,by-70*s)),
       'head':((cx-bw*1.7,by-5*s,cx-hr*0.95,cy-hr*0.3),(cx+bw*1.7,by-5*s,cx+hr*0.95,cy-hr*0.3)),
       'phone':((cx-bw*1.2,by+50*s,cx-bw*1.15,by+bh*0.9),(cx+bw*1.5,by+30*s,cx+hr*0.9,cy+hr*0.2)),
       'relax':((cx-bw*1.7,by-5*s,cx-hr*0.6,cy-hr*0.9),(cx+bw*1.7,by-5*s,cx+hr*0.6,cy-hr*0.9))}[arms]
    e+=arm(L0[0],L0[1],*A[0])+arm(R0[0],R0[1],*A[1])
    e+=[P(C(cx-hr*0.98,cy+4*s,9*s),SK,4),P(C(cx+hr*0.98,cy+4*s,9*s),SK,4)]
    e.append(P(C(cx,cy,hr),SK,5))
    e.append(P(f"M{cx-hr*1.02},{cy-hr*0.05} Q{cx-hr*1.1},{cy-hr*1.25} {cx},{cy-hr*1.18} Q{cx+hr*1.1},{cy-hr*1.25} {cx+hr*1.02},{cy-hr*0.05} Q{cx+hr*0.6},{cy-hr*0.75} {cx-hr*0.1},{cy-hr*0.55} Q{cx-hr*0.6},{cy-hr*0.5} {cx-hr*1.02},{cy-hr*0.05} Z",hair,4))
    e+=[P(C(cx-hr*0.36,cy+hr*0.05,4.5*s),INK,3),P(C(cx+hr*0.36,cy+hr*0.05,4.5*s),INK,3)]
    if glasses: e+=[P(C(cx-hr*0.36,cy+hr*0.05,12*s),None,3),P(C(cx+hr*0.36,cy+hr*0.05,12*s),None,3),P(L((cx-hr*0.24,cy+hr*0.05),(cx+hr*0.24,cy+hr*0.05)),None,3)]
    if mood in('ok','happy'): e.append(P(A_(cx,cy+hr*0.2,hr*0.38,25,155),'#ffffff' if mood=='happy' else None,4))
    else: e.append(P(A_(cx,cy+hr*0.85,hr*0.32,215,325),None,4))
    if mood=='stress': e+=[P(f"M{cx+hr*1.2},{cy-hr*0.7} Q{cx+hr*1.4},{cy-hr*0.2} {cx+hr*1.2},{cy-hr*0.05} Q{cx+hr*1.0},{cy-hr*0.2} {cx+hr*1.2},{cy-hr*0.7}",'#9fd3ff',3)]
    return e
A_=A
def phone(x,y,s=1.0,ring=True):
    e=[P(R(x,y,64*s,118*s,12),'#3b3f4a',5),P(R(x+7*s,y+14*s,50*s,84*s,4),'#bfe3ff',3)]
    if ring:
        for k in range(2): e+=[P(A(x+32*s,y+58*s,(60+k*24)*s,-55,15),None,5,RD),P(A(x+32*s,y+58*s,(60+k*24)*s,165,235),None,5,RD)]
    return e
def bubble(x,y,w,h,txt,size=32,col='#ffffff'):
    return [P(R(x,y,w,h,20)+f" M{x+34},{y+h} L{x+22},{y+h+28} L{x+62},{y+h}",col,4),T(x+w/2,y+h/2+size*0.36,txt,size)]
def check(x,y,s=1.0,col=GR): return P(L((x,y),(x+18*s,y+20*s),(x+52*s,y-22*s)),None,9,col)
def doc(x,y,w,h,lines=4,ck=True):
    e=[P(R(x,y,w,h,10),'#ffffff')]
    for k in range(lines):
        yy=y+40+k*(h-60)/max(1,lines-1)
        if ck: e+=[P(R(x+20,yy-14,24,24,4),'#e6f6ea',3),check(x+22,yy-2,0.45)]
        e.append(P(L((x+60,yy),(x+w-25,yy)),None,6,GY))
    return e
def beach(x,y,s=1.0):
    return [P(L((x,y),(x+160*s,y-70*s)),None,8,BR if False else '#8b5a2b'),P(Z((x+20*s,y-10*s),(x+170*s,y-75*s),(x+190*s,y-40*s),(x+40*s,y+20*s)),'#ffd9a0',5),
            P(L((x+40*s,y+20*s),(x+30*s,y+70*s)),None,7),P(L((x+170*s,y-50*s),(x+185*s,y+70*s)),None,7)]
import math
def coin(x,y,r=26): return [P(C(x,y,r),YL,4),P(C(x,y,r*0.62),None,3,'#c99a10'),T(x,y+r*0.36,'$',r*0.95,'#a87a00')]
def box(x,y,s=1.0): return [P(R(x,y,90*s,70*s,4),'#e7b97d',4),P(L((x,y+18*s),(x+90*s,y+18*s)),None,3),P(R(x+35*s,y,20*s,18*s,0),'#f3d3a3',3)]
def arrow(x0,y0,x1,y1,col=INK,w=7):
    a=math.atan2(y1-y0,x1-x0);h=22
    return [P(L((x0,y0),(x1,y1)),None,w,col),P(L((x1-h*math.cos(a-0.5),y1-h*math.sin(a-0.5)),(x1,y1),(x1-h*math.cos(a+0.5),y1-h*math.sin(a+0.5))),None,w,col)]
def pre(lst):
    for e in lst: e['pre']=True
    return lst
def pre(lst):
    for e in lst: e['pre']=True
    return lst
S=[]
def stack(x,y,cols,rows,s=0.8):
    e=[]
    for r in range(rows):
        for c in range(cols): e+=box(x+c*76*s,y-r*58*s,s)
    return e
def wallet(x,y):
    return [P(R(x,y,190,130,18),'#8b5a2b',5),P(R(x+110,y+40,90,50,12),'#a8743e',4),P(C(x+140,y+65,8),YL,3)]
# 0 hook
s=pre([T(540,95,'KHO ĐẦY HÀNG',76,RD),P(L((200,135),(880,135)),None,6,RD)])
s+=pre(stack(120,500,4,4,0.85))
s+=pre([P(R(580,200,400,110,20),'#fff3d6',6,'#e0a020'),T(780,272,'NHƯNG HẾT TIỀN?',46,'#b36b00')])
s+=wallet(640,360)+[T(735,560,'Tài khoản: 0 đ',36,RD)]
S.append(s)
# 1 holding cost
s=[T(540,80,'CHI PHÍ TỒN KHO MỖI NĂM',50,'#2c5aa0')]
for k,(lab,c) in enumerate([('Lưu kho',BL),('Hư hỏng','#f08a3c'),('Lỗi mốt',RD)]):
    s+=[P(R(110+k*200,170,170,120,16),c,5),T(195+k*200,245,lab,32,'#ffffff')]
s+=arrow(330,330,330,400,INK,7)+[P(R(110,410,570,150,24),'#fff3d6',6,'#e0a020'),T(395,510,'20–30%',90,RD)]
s+=[T(850,330,'giá trị',40,INK),T(850,380,'hàng tồn',40,INK)]+coin(850,470,55)
S.append(s)
# 2 key items 20/80
s=[T(540,80,'1. NHÓM HÀNG CHỦ LỰC',54,RD)]
s+=[T(280,150,'Mặt hàng',36,INK),P(R(140,180,280,380,10),'#eef1f6',4),P(R(140,484,280,76,10),GR,5),T(280,532,'20%',40,'#ffffff')]
s+=arrow(450,450,610,330,GR,9)
s+=[T(800,150,'Doanh thu',36,INK),P(R(660,180,280,380,10),'#eef1f6',4),P(R(660,256,280,304,10),GR,5),T(800,420,'80%',64,'#ffffff')]
S.append(s)
# 3 days of inventory formula
s=[T(540,80,'2. SỐ NGÀY TỒN KHO',56,RD)]
s+=[P(R(90,150,900,130,22),'#ffffff'),T(540,203,'Giá trị tồn kho',40,INK),P(L((200,225),(880,225)),None,5),T(540,265,'Giá vốn bán ra mỗi ngày',36,INK)]
s+=arrow(540,300,540,370,INK,7)+[P(R(250,385,580,140,22),'#e6f6ea',6,GR),T(540,470,'= Số ngày hàng nằm kho',42,'#1f7a3e')]
S.append(s)
# 4 slow stock
s=[T(540,80,'3. XỬ LÝ HÀNG CHẬM',56,RD)]+stack(90,330,2,3,0.8)+[P(R(80,370,190,70,14),'#ffe3e0',4,RD),T(175,418,'> 90 ngày',34,RD)]
for k,(lab,c) in enumerate([('Giảm giá',YL),('Bán kèm',BL),('Thanh lý','#f08a3c')]):
    y=170+k*120; s+=arrow(300,300,440,y+35,INK,6)+[P(R(450,y,260,72,16),c,5),T(580,y+48,lab,34,INK)]
s+=arrow(730,300,800,300,GR,8)+coin(880,260,48)+coin(920,350,48)+[T(895,450,'Thu hồi vốn',32,GR)]
S.append(s)
# 5 buy to demand
s=[T(540,80,'4. NHẬP THEO NHU CẦU',56,RD)]
s+=stack(110,470,3,5,0.75)+[P(L((90,150),(330,560)),None,10,RD),P(L((330,150),(90,560)),None,10,RD),T(215,600,'Nhập một lần thật nhiều',30,RD)]
for k in range(3): s+=stack(520+k*160,470,1,2,0.75)+[check(540+k*160,250,0.8)]
s+=[T(760,600,'Nhiều lần, vừa đủ',34,GR)]
S.append(s)
# 6 message
s=[P(R(70,130,940,190,24),'#ffffff'),T(540,205,'Hàng chỉ là tài sản',52,INK),T(540,275,'khi nó được bán ra',46,'#2c5aa0')]
s+=stack(150,500,2,2,0.8)+[T(225,612,'Nằm im',34,RD)]+arrow(400,470,620,470,INK,8)+coin(760,430,56)+coin(840,480,56)+[T(800,612,'Sinh lời',34,GR)]
S.append(s)
# 7 teaser
s=[P(R(140,110,800,360,28),'#fff3d6',6),T(540,200,'PHẦN SAU',60,RD),T(540,300,'Kế hoạch dòng tiền',56,INK),T(540,385,'13 tuần',60,'#2c5aa0')]
s+=[P(R(470,480,140,110,12),'#ffffff'),P(R(470,480,140,30,12),RD,4),T(540,568,'13',44,INK)]
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
