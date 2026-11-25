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
GN='#1f7a3e'; DB='#2c5aa0'
def bank(x,y,s=1.0,fill='#e6f0fb'):
    w=300*s
    e=[P(Z((x,y+70*s),(x+w/2,y),(x+w,y+70*s)),fill,5)]
    e+=[P(R(x+30*s+i*66*s,y+82*s,34*s,130*s,4),'#ffffff',4) for i in range(4)]
    e+=[P(R(x-10*s,y+212*s,w+20*s,30*s,4),fill,5)]
    return e
def truck(x,y,s=1.0):
    return [P(R(x,y,150*s,90*s,8),'#ffffff',5),P(R(x+150*s,y+30*s,70*s,60*s,8),BL,5),P(R(x+165*s,y+40*s,35*s,25*s,4),'#bfe3ff',3),
            P(C(x+40*s,y+100*s,18*s),INK,4),P(C(x+180*s,y+100*s,18*s),INK,4)]
def glass(x,y,r=70,col=DB):
    return [P(C(x,y,r),'#e8f3ff',7,col),P(L((x+r*0.7,y+r*0.7),(x+r*1.5,y+r*1.5)),None,16,col)]
def gauge(cx,cy,r,ang,col):
    a=math.radians(ang)
    return [P(A(cx,cy,r,180,240),None,14,RD),P(A(cx,cy,r,240,300),None,14,YL),P(A(cx,cy,r,300,360),None,14,GR),
            P(L((cx,cy),(cx+r*0.8*math.cos(a),cy+r*0.8*math.sin(a))),None,8,col),P(C(cx,cy,10),INK,3)]
def ptag(x,y,txt,col=YL,size=44):
    return [P(Z((x,y+40),(x+50,y),(x+260,y),(x+260,y+80),(x+50,y+80)),col,5),P(C(x+45,y+40,9),'#ffffff',3),T(x+155,y+56,txt,size)]
def broken(x,y):
    return [P(R(x,y,90,70,4),'#e7b97d',4),P(L((x+30,y),(x+45,y+30),(x+35,y+45),(x+55,y+70)),None,5,RD)]
# 0 hook: chữ tiêu đề hiện ngay khung đầu (như tập 1–2), bút vẽ biểu đồ ngay sau đó
s=pre([T(540,150,'DOANH THU TĂNG',76,GN),P(L((190,190),(890,190)),None,6,GN)])
s+=pre([P(R(110,250,860,120,20),'#fde3e3',6,RD),T(540,332,'BIÊN LỢI NHUẬN GỘP LẠI GIẢM?',46,RD)])
s+=[P(L((300,610),(780,610)),None,5),P(L((300,610),(300,410)),None,5)]
s+=[P(R(340,540,80,70,5),GR,4),P(R(470,490,80,120,5),GR,4),P(R(600,430,80,180,5),GR,4)]
s+=[P(L((380,420),(510,460),(640,520)),None,8,RD),*arrow(640,520,740,580,RD,8)]
s+=coin(180,500,70)+[P(C(890,500,80),'#fff3d6',6,RD),T(890,535,'?',100,RD)]
S.append(s)
# 1 con số trung bình che mất
s=[T(540,80,'CON SỐ TRUNG BÌNH',58,RD)]
s+=tag(70,170,240,'38%',GR,50)+tag(70,300,240,'25%',YL,50)+tag(70,430,240,'12%',PK,50)
s+=arrow(330,200,560,320,INK,6)+arrow(330,330,560,330,INK,6)+arrow(330,460,560,345,INK,6)
s+=[P(C(760,335,150),'#e9ecf2',6),T(760,320,'25%',72,INK),T(760,390,'cả công ty',40,DB)]
S.append(s)
# 2 công thức
s=[T(540,80,'BIÊN LỢI NHUẬN GỘP',58,RD)]
s+=[T(330,230,'Doanh thu',50,GN),T(540,230,'−',60,INK),T(760,230,'Giá vốn',50,RD)]
s+=[P(L((150,280),(930,280)),None,8)]
s+=[T(540,360,'Doanh thu',50,GN)]
s+=coin(200,480,60)+box(420,440,1.3)+[T(780,500,'= %',60,DB)]
S.append(s)
# 3 việc đầu tiên: soi từng sản phẩm
s=[T(540,80,'TỪNG SẢN PHẨM',60,RD)]
s+=pre(box(90,250,1.6)+box(400,250,1.6)+box(710,250,1.6))
s+=glass(250,300,95,DB)
s+=[T(165,480,'38%',48,GN),T(475,480,'25%',48,OR),T(785,480,'12%',48,RD)]
s+=[T(540,590,'Không tính chung',46,DB)]
S.append(s)
# 4 ví dụ: biên chung tụt khi sản phẩm biên thấp bán chạy
s=pre([P(L((60,470),(600,470)),None,6)])
s+=[P(R(80,190,150,280,10),GR,5),T(155,170,'38%',50,GN),T(155,530,'Loại 1',44,GN)]
s+=[P(R(360,380,150,90,10),PK,5),T(435,360,'12%',50,RD),T(435,530,'Loại 2',44,RD)]
s+=arrow(560,440,560,230,OR,9)+[T(435,280,'Bán chạy',42,OR)]
s+=gauge(830,380,160,215,RD)
s+=[T(830,460,'Biên chung',44,RD),*arrow(830,500,830,590,RD,8)]
S.append(s)
# 5 tính đủ giá vốn
s=[T(540,80,'TÍNH ĐỦ GIÁ VỐN',60,RD)]
s+=tag(70,150,300,'Giá nhập',BL,44)+box(400,150,1.1)
s+=tag(70,260,300,'Vận chuyển',YL,44)+truck(400,250,0.9)
s+=tag(70,370,300,'Hao hụt',GR,44)+broken(420,375)
s+=[P(R(650,160,370,300,18),'#fff3d6',5),T(835,240,'Doanh thu',46,GN),T(835,320,'−',60,INK),T(835,400,'Chiết khấu',46,OR)]
s+=[T(540,560,'Trừ chiết khấu khỏi doanh thu',44,DB)]
S.append(s)
# 6 xếp hạng bằng tiền: bục 1-2-3
s=[T(540,80,'XẾP HẠNG BẰNG TIỀN',58,RD)]
s+=[P(R(390,330,300,260,8),YL,5),T(540,420,'1',80,INK)]
s+=[P(R(90,410,300,180,8),GY,5),T(240,490,'2',70,INK)]
s+=[P(R(690,460,300,130,8),'#e7b97d',5),T(840,535,'3',64,INK)]
s+=coin(540,230,70)+coin(240,320,55)+coin(840,390,45)
S.append(s)
# 7 giữ hay đổi
s=[T(540,80,'GIỮ HAY ĐỔI?',60,RD)]
s+=pre([P(R(70,140,450,200,18),'#e6f6ea',5),P(R(560,140,450,200,18),'#fde3e3',5)])
s+=[T(295,215,'Biên thấp',42,INK),T(295,280,'Bán nhiều',46,GN)]
s+=[T(785,215,'Biên thấp',42,INK),T(785,280,'Bán ít',46,RD)]
s+=[T(250,480,'GIỮ',80,GN),check(340,455,1.2)]
s+=tag(560,370,450,'Tăng giá',YL,44)+tag(560,445,450,'Đổi cấu hình',BL,44)+tag(560,520,450,'Dừng bán',PK,44)
S.append(s)
# 8 teaser
s=pre([P(R(140,90,800,330,28),'#fff3d6',6),T(540,180,'PHẦN SAU',60,RD),T(540,280,'Định giá lại',56,INK),T(540,360,'không mất khách',50,DB)])
s+=ptag(160,480,'Giá mới',YL,46)+arrow(450,520,560,520,GN,9)+person(800,440,0.9,'happy','down',GR,legs=False)
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
