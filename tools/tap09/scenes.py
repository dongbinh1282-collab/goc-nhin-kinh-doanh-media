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
def cal2(x,y,num,k=1.0):
    return [P(R(x,y,200*k,200*k,16),'#ffffff',5),P(R(x,y,200*k,56*k,16),RD,5),T(x+100*k,y+42*k,'NGÀY',34,'#ffffff'),T(x+100*k,y+160*k,num,84,INK)]
# 0 hook: 13 tuần tới, tuần nào thiếu tiền
def weeks(y,mark=10,q=True,tet=9,h=90):
    e=[]; x0=76
    e+=pre([P(R(x0+i*72,y,64,h,8),'#ffffff',4) for i in range(13)])
    e+=tag(x0+tet*72-38,y-80,140,'TẾT',YL,38)
    e+=[P(R(x0+mark*72,y,64,h,8),'#fbe3e0',6,RD)]
    if q: e+=[T(x0+mark*72+32,y+h/2+22,'?',64,RD)]
    return e
s=[T(540,80,'BA THÁNG TỚI',62,RD)]
s+=weeks(250,h=150)
s+=[T(540,490,'13 tuần tới',56,'#2c5aa0'),T(540,570,'Tuần nào thiếu tiền nhất?',50,INK)]
S.append(s)
# 1 chi tăng, thu chậm
s=[T(540,80,'CHI TĂNG, THU CHẬM',56,RD)]
s+=pre([P(R(50,170,420,360,22),'#fbe3e0',6,RD),P(R(610,170,420,360,22),'#e4f5e8',6,'#1f7a3e')])
s+=[T(260,250,'CHI',80,RD)]+coin(170,380,52)+coin(270,380,52)+coin(220,312,52)+[T(260,490,'tăng trước Tết',42,RD)]
s+=[T(820,250,'THU',80,'#1f7a3e')]+coin(820,370,52)+[T(820,490,'chậm sau Tết',42,'#1f7a3e')]
s+=arrow(480,350,600,350,INK,10)
s+=[T(540,600,'Không dùng số liệu tháng thường',46,INK)]
S.append(s)
# 2 chi dồn trước Tết + ví dụ
s=[T(540,80,'CHI DỒN TRƯỚC TẾT',56,RD)]
s+=tag(20,160,380,'Lương tháng 13',OR,40)+tag(420,160,300,'Tiền thưởng',OR,40)+tag(740,160,290,'Hàng, thuế',OR,40)
s+=arrow(230,235,280,350,RD,8)+arrow(555,235,340,370,RD,8)+arrow(860,235,380,400,RD,8)
s+=coin(300,450,80)
s+=pre([P(L((500,560),(1010,560)),None,6,INK)])
s+=[P(R(560,440,140,120,8),BL,5),T(630,425,'200 tr',44,'#2c5aa0'),T(630,610,'Tháng thường',40,INK)]
s+=[P(R(840,320,140,240,8),RD,5),T(910,305,'400 tr',44,RD),T(910,610,'Trước Tết',40,INK)]
S.append(s)
# 3 thu muộn sau Tết
s=[T(540,80,'TIỀN THU VỀ MUỘN',56,RD)]
s+=pre([P(R(30,170,330,210,20),'#e6f0fb',6,'#2c5aa0'),P(R(720,170,330,210,20),'#e4f5e8',6,'#1f7a3e')])
s+=[T(195,245,'Hẹn thu',46,'#2c5aa0'),T(195,325,'sát Tết',54,INK)]
s+=arrow(375,300,705,300,RD,9)+[T(540,265,'+2–3 tuần',44,RD)]
s+=[T(885,245,'Thực thu',46,'#1f7a3e'),T(885,325,'sau Tết',54,INK)]
s+=pre([P(R(60,440,960,120,18),'#fbe3e0',5,RD)])+[T(540,515,'Nghỉ Tết: gần như không có tiền vào',42,RD)]
S.append(s)
# 4 tuần đáy
s=[T(540,80,'TUẦN ĐÁY',62,RD)]
s+=pre([P(L((120,200),(120,560),(980,560)),None,8,INK)])
s+=[P(L((470,170),(470,560)),None,4,GY)]+tag(400,130,140,'TẾT',YL,38)
s+=[P(L((150,260),(300,300),(420,380),(470,430),(570,520),(690,450),(830,320),(950,270)),None,12,RD)]
s+=[P(C(570,520,24),None,8,RD),T(570,610,'Đáy: ngay sau Tết',44,RD)]
s+=[T(930,610,'tuần',40,INK)]
S.append(s)
# 5 chuẩn bị sớm
s=[T(540,80,'CHUẨN BỊ SỚM',62,RD)]
s+=person(270,250,1.4,'happy','point',BL,tie=True,legs=False)
s+=tag(540,190,460,'Ngân hàng',BL,46)+tag(540,300,460,'Nhà cung cấp',OR,46)
s+=[check(500,230,0.9),check(500,340,0.9)]
s+=[T(770,470,'Làm ngay từ bây giờ',50,'#1f7a3e')]
S.append(s)
# 6 kết
s=[T(540,110,'KHÔNG PHẢI VÌ TẾT',62,RD)]
s+=[T(540,200,'mà vì không thấy trước',50,INK),T(540,270,'tuần khó nhất',58,RD)]
s+=weeks(430,10,False,9,80)
S.append(s)
# 7 teaser
s=pre([P(R(140,90,800,330,28),'#fff3d6',6)])+[T(540,180,'PHẦN SAU',60,RD),T(540,280,'Hạn mức vay',58,INK),T(540,360,'trước khi cần',54,'#2c5aa0')]
s+=[P(Z((400,500),(540,445),(680,500)),'#e6f0fb',5)]+[P(R(420+i*70,505,34,80,4),'#ffffff',4) for i in range(4)]+[P(R(390,585,300,24,4),'#e6f0fb',5)]
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
