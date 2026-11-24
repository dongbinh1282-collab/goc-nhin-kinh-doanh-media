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

def cal(x,y,lab,s=1.0):
    return [P(R(x,y,170*s,170*s,14),'#ffffff',5),P(R(x,y,170*s,48*s,14),RD,5),T(x+85*s,y+36*s,lab,int(28*s),'#ffffff'),T(x+85*s,y+132*s,'30',int(70*s),INK)]
def tag(x,y,w,lab,c,size=32):
    return [P(R(x,y,w,64,14),c,5),T(x+w/2,y+44,lab,size,INK)]
OR='#f08a3c'; PK='#f4a0a0'
def X(cx,cy,r=60,w=10): return [P(L((cx-r,cy-r),(cx+r,cy+r)),None,w,RD),P(L((cx+r,cy-r),(cx-r,cy+r)),None,w,RD)]
# 0 hook
s=pre([T(540,95,'LÃI TRÊN GIẤY',70,RD),P(L((200,135),(880,135)),None,6,RD)])
s+=pre(doc(120,230,300,330,4,False)+[T(270,600,'Báo cáo lãi',32,INK)])
s+=wallet(560,300)+[T(655,500,'Tiền: 0 đ',36,RD)]
s+=person(880,300,0.9,'stress','head',BL,tie=True,legs=False)
S.append(s)
# 1 definition
s=[T(540,80,'DOANH SỐ CÂN BẰNG',58,'#2c5aa0')]
s+=[P(R(300,170,480,120,20),'#fff3d6',6,'#e0a020'),T(540,250,'Lãi = 0',52,'#b36b00')]
s+=[P(R(100,380,380,140,18),'#ffe3e0',5,RD),T(290,455,'Dưới mức này: lỗ',36,RD)]
s+=[P(R(600,380,380,140,18),'#e6f6ea',5,GR),T(790,455,'Trên mức này: lãi',36,'#1f7a3e')]
S.append(s)
# 2 fixed vs variable
s=[T(540,80,'1. TÁCH CHI PHÍ',58,RD)]
s+=tag(100,170,280,'Tiền thuê',BL,32)+tag(410,170,320,'Lương quản lý',YL,32)
s+=[T(540,300,'Cố định: không đổi',36,'#2c5aa0')]
s+=tag(100,370,400,'Nguyên vật liệu',GR,32)+tag(530,370,330,'Hoa hồng',OR,32)
s+=[T(540,490,'Biến đổi: theo số lượng bán',36,'#1f7a3e')]
S.append(s)
# 3 ratio with counter
s=[T(540,80,'2. TỶ LỆ LÃI',58,RD)]
s+=[P(R(120,190,840,150,20),'#e6f0fb',5),T(540,270,'1 − chi phí biến đổi ÷ giá bán',44,INK)]
s+=[dict(k='c',x=540,y=460,size=110,**{'from':0},to=40,t0=0.5,t1=2.5,suf='%')]
s+=[P(R(230,520,620,80,16),'#e6f6ea',5,GR),T(540,575,'Mỗi đồng doanh thu còn lại',36,'#1f7a3e')]
S.append(s)
# 4 formula
s=[T(540,80,'3. DOANH SỐ CÂN BẰNG',58,RD)]
s+=[P(R(90,190,320,130,18),'#ffe3e0',5,RD),T(250,270,'Chi phí cố định',34,RD)]
s+=[T(470,270,'÷',80,INK)]
s+=[P(R(540,190,220,130,18),'#e6f0fb',5),T(650,270,'Tỷ lệ lợi nhuận',34,'#2c5aa0')]
s+=[T(820,270,'=',80,INK)]
s+=[P(R(870,190,170,130,18),'#e6f6ea',6,GR),T(955,265,'Đích',34,'#1f7a3e')]
s+=arrow(540,400,540,470,INK,7)+[T(540,540,'Doanh số cần đạt mỗi tháng',36,'#2c5aa0')]
S.append(s)
# 5 example with counter
s=[T(540,80,'VÍ DỤ',58,'#2c5aa0')]
s+=[P(R(100,150,400,120,18),'#ffe3e0',5,RD),T(300,205,'Chi phí cố định',30,INK),T(300,250,'60 triệu',40,RD)]
s+=[P(R(580,150,400,120,18),'#e6f0fb',5),T(780,205,'Tỷ lệ lợi nhuận',30,INK),T(780,250,'40%',40,'#2c5aa0')]
s+=[dict(k='c',x=540,y=430,size=96,**{'from':60},to=150,t0=1.0,t1=3.0,suf=' triệu')]
s+=[P(R(250,500,580,90,16),'#e6f6ea',5,GR),T(540,560,'Cần bán 150 triệu mỗi tháng',36,'#1f7a3e')]
S.append(s)
# 6 teaser
s=[P(R(140,110,800,360,28),'#fff3d6',6),T(540,200,'PHẦN SAU',60,RD),T(540,300,'Đọc dòng tiền',58,INK),T(540,385,'để tránh thiếu tiền',54,'#2c5aa0')]
s+=doc(470,490,140,130,3,False)
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
