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
S=[]
# 0 hook - pre-drawn big text + stamp
s=pre([T(540,150,'DOANH THU x2',84,GR),P(L((150,190),(930,190)),None,6,GR)])
s+=pre([P(R(130,250,820,120,20),'#ffe8e5',6,RD),T(540,332,'VẪN ĐI VAY TRẢ LƯƠNG?',52,RD)])
s+=person(540,455,1.05,'stress','head',BL,tie=True,legs=False)
S.append(s)
# 1 book vs bank, big
s=[T(540,330,'≠',140,RD),P(R(60,120,380,380,18),'#ffffff'),T(250,100,'SỔ SÁCH',40,INK),T(250,280,'Lợi nhuận',46,INK),T(250,370,'+2 tỷ',72,GR)]
s+=[P(R(640,120,380,380,18),'#ffffff'),T(830,100,'TÀI KHOẢN',40,INK),T(830,280,'Tiền mặt',46,INK),T(830,370,'0 đ',72,RD)]
S.append(s)
# 2 receivables
s=[T(540,80,'1. CÔNG NỢ',60,RD),P(R(40,190,250,200,14),'#ffffff'),T(165,440,'Công ty',36,INK)]+box(115,240,1.2)
s+=arrow(310,250,640,250,GR,9)+[T(475,220,'Giao hàng',36,GR)]
s+=person(820,220,1.1,'happy','down',YL,legs=False)+coin(950,380,38)+coin(990,420,38)
s+=arrow(640,400,310,400,RD,9)+[T(475,470,'Chưa thu tiền',38,RD)]
S.append(s)
# 3 inventory
s=[T(540,80,'2. TỒN KHO',60,RD),P(L((80,540),(760,540)),None,7),P(L((80,370),(760,370)),None,7),P(L((100,540),(100,180)),None,7),P(L((740,540),(740,180)),None,7)]
for r in range(2):
    for c in range(4): s+=box(130+c*150,(450,280)[r],1.2)
s+=coin(910,320,60)+[T(910,450,'Vốn',40,RD),T(910,500,'tồn đọng',40,RD)]
S.append(s)
# 4 fixed costs
s=[T(540,80,'3. CHI PHÍ CỐ ĐỊNH',58,RD),P(R(60,190,280,350,10),'#e6ecf5'),P(Z((40,190),(200,110),(360,190)),'#c9d4e4',5)]
for r in range(3):
    for c in range(2): s.append(P(R(105+c*115,225+r*100,65,65,5),'#ffffff',4))
for k in range(3): s+=person(450+k*140,300,0.7,'ok','down',[BL,YL,GR][k])
s+=[P(C(930,320,105),'#ffffff',6),P(L((930,320),(930,250)),None,8),P(L((930,320),(980,350)),None,8),T(930,480,'Dòng tiền chưa về',34,RD)]
S.append(s)
# 5 formula big
s=[T(540,80,'CÁCH KIỂM TRA',56,'#2c5aa0'),P(R(30,170,320,150,18),'#ffffff'),T(190,238,'Tiền mặt',44,INK),T(190,290,'đang có',32,'#7a7f8a')]
s+=[T(390,272,'÷',96,INK),P(R(430,170,320,150,18),'#ffffff'),T(590,238,'Chi phí',44,INK),T(590,290,'mỗi ngày',32,'#7a7f8a')]
s+=[T(790,272,'=',96,INK),P(R(830,160,230,170,20),'#fff3d6'),T(945,238,'Số ngày',40,RD),T(945,292,'duy trì',36,RD)]
s+=[P(A(540,600,200,180,360),None,26,'#e9e1d4'),P(A(540,600,200,180,300),None,26,GR),P(L((540,600),(615,425)),None,8,RD),P(C(540,600,14),INK)]
S.append(s)
# 6 alarm 90 days
s=[P(R(60,120,560,200,24),'#ffffff',pre=True) if False else dict(P(R(60,120,560,200,24),'#ffffff'),pre=True),dict(k='c',x=340,y=212,size=88,**{'from':120},to=89,t0=0.2,t1=2.4,pre=True),T(340,290,'CẢNH BÁO',44,RD)]
s+=[P(R(60,370,560,150,20),'#eef6ff'),T(340,435,'Dự phòng tối thiểu',36,INK),T(340,490,'3 tháng chi phí',44,'#2c5aa0')]
s+=[P(C(840,300,140),'#fff3d6',6),P(L((760,220),(920,380)),None,14,RD),P(L((920,220),(760,380)),None,14,RD),T(840,500,'Tạm dừng chi mở rộng',34,INK)]
S.append(s)
# 7 teaser
s=[P(R(140,110,800,360,28),'#fff3d6',6),T(540,200,'PHẦN SAU',60,RD),T(540,300,'Thu hồi công nợ',62,INK),T(540,380,'vẫn giữ được khách hàng',44,INK)]+coin(540,520,44)
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
