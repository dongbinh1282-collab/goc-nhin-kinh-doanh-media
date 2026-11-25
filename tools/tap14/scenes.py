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
def shield(x,y,s=1.0,col=GR):
    return [P(f"M{x},{y} L{x+50*s},{y+15*s} L{x+50*s},{y+60*s} Q{x+50*s},{y+100*s} {x},{y+120*s} Q{x-50*s},{y+100*s} {x-50*s},{y+60*s} L{x-50*s},{y+15*s} Z",col,5),check(x-22*s,y+60*s,0.8,'#ffffff')]
def wrench(x,y,s=1.0):
    return [P(L((x,y),(x+110*s,y+110*s)),None,16*s,GY),P(C(x,y,26*s),'#ffffff',6,GY),P(C(x+110*s,y+110*s,14*s),GY,4)]
def star(cx,cy,r,col=YL):
    pts=[]
    for k in range(10):
        a=math.radians(-90+k*36); rr=r if k%2==0 else r*0.45
        pts.append((round(cx+rr*math.cos(a),1),round(cy+rr*math.sin(a),1)))
    return P(Z(*pts),col,4)
# 0 hook: chữ hiện ngay, bút vẽ nhãn giá và khách
s=pre([T(540,150,'BÁN CHẠY, BIÊN MỎNG',72,OR),P(L((170,190),(910,190)),None,6,OR)])
s+=pre([P(R(90,250,900,120,20),'#fde3e3',6,RD),T(540,330,'MUỐN TĂNG GIÁ NHƯNG SỢ MẤT KHÁCH?',36,RD)])
s+=ptag(110,450,'Giá +?',YL,44)+arrow(400,490,560,490,RD,8)
s+=person(700,440,0.75,'ok','down',BL,legs=False)+arrow(790,500,930,500,RD,8)
S.append(s)
# 1 nỗi sợ lớn hơn rủi ro thật: cái cân
s=[T(540,80,'NỖI SỢ LỚN HƠN THỰC TẾ',54,RD)]
s+=[P(Z((540,420),(500,560),(580,560)),GY,5),P(L((470,560),(610,560)),None,6)]
s+=[P(L((220,470),(860,330)),None,8)]
s+=[P(L((220,470),(170,520)),None,4),P(L((220,470),(270,520)),None,4),P(A(220,520,60,0,180),'#fde3e3',5,RD)]
s+=[P(L((860,330),(810,380)),None,4),P(L((860,330),(910,380)),None,4),P(A(860,380,60,0,180),'#e6f6ea',5,GN)]
s+=[T(220,420,'Nỗi sợ',46,RD),T(860,290,'Thiệt hại thật',44,GN)]
S.append(s)
# 2 công thức
s=[T(540,80,'SẢN LƯỢNG ĐƯỢC PHÉP MẤT',54,RD)]
s+=pre([P(R(80,150,920,320,24),'#fff3d6',5)])
s+=[T(540,250,'Mức tăng giá',52,GN),P(L((150,295),(930,295)),None,8),T(540,370,'Biên lợi nhuận gộp cũ + Mức tăng giá',38,DB)]
s+=stack(380,560,4,1,0.9)+X(780,560,40,9)
S.append(s)
# 3 ví dụ số: 14% + 7% → mất 1/3 vẫn giữ lợi nhuận gộp
s=[T(540,80,'GIẢ ĐỊNH',60,RD)]
s+=tag(70,150,300,'Biên 14%',YL,46)+tag(70,250,300,'Tăng giá 7%',GR,42)
s+=[T(220,420,'7 ÷ (14 + 7)',48,INK),T(220,500,'= 1/3',60,RD)]
s+=[P(C(760,350,190),'#e6f6ea',6,GN),P(f"M760,350 L760,160 A190,190 0 0 1 924.5,445 Z",'#fde3e3',6,RD)]
s+=[T(860,330,'1/3',48,RD),T(700,420,'Lợi nhuận',40,GN),T(700,470,'gộp giữ nguyên',40,GN)]
S.append(s)
# 4 hướng 1: tách dịch vụ đi kèm
s=[T(540,80,'TÁCH DỊCH VỤ ĐI KÈM',58,RD)]
s+=box(90,200,2.0)
s+=[P(L((300,270),(380,270)),None,6,RD),T(340,250,'✂',50,RD)]
s+=truck(420,170,0.9)+wrench(670,170,0.9)+shield(910,165,0.9)
s+=[T(520,380,'Vận chuyển',40,DB),T(720,380,'Lắp đặt',40,DB),T(910,380,'Bảo hành',40,DB)]
s+=tag(90,460,900,'Tính phí riêng, giá sản phẩm giữ nguyên',YL,42)
S.append(s)
# 5 hướng 2: hai phiên bản
s=[T(540,80,'HAI PHIÊN BẢN',60,RD)]
s+=[P(R(80,150,420,400,22),'#ffffff',5),T(290,220,'TIÊU CHUẨN',46,INK)]+box(220,270,1.5)+[T(290,480,'Giữ giá',48,GN)]
s+=[P(R(580,150,420,400,22),'#fff3d6',6,OR),T(790,220,'NÂNG CẤP',46,OR)]+box(720,270,1.5)+[star(900,290,45),T(790,480,'Giá cao hơn',46,OR)]
s+=[T(540,600,'Khách hàng tự chọn',46,DB)]
S.append(s)
# 6 hướng 3: áp giá theo nhóm khách
s=[T(540,80,'ÁP GIÁ THEO NHÓM KHÁCH',56,RD)]
s+=[P(R(70,150,440,420,22),'#fde3e3',5)]+ptag(140,200,'Giá mới',YL,44)
s+=[T(290,380,'Đơn hàng mới',44,RD),T(290,450,'Khách nhỏ lẻ',44,RD)]
s+=[P(R(570,150,440,420,22),'#e6f6ea',5)]+doc(640,180,300,200,3)
s+=[T(790,450,'Khách lớn',44,GN),T(790,520,'Giữ giá hết kỳ',42,GN)]
S.append(s)
# 7 chốt: báo trước 4 tuần, tăng một đợt
s=[T(540,80,'BÁO TRƯỚC, TĂNG MỘT ĐỢT',54,RD)]
s+=[P(R(80,160,260,260,16),'#ffffff',5),P(R(80,160,260,70,16),RD,5),T(210,212,'BÁO TRƯỚC',38,'#ffffff'),T(210,340,'4',100,INK),T(210,400,'tuần',40,INK)]
s+=[P(L((420,420),(520,420),(520,370),(620,370),(620,320),(720,320),(720,270),(820,270)),None,7,GY)]+X(620,350,70,8)
s+=[P(L((420,560),(700,560),(700,440),(980,440)),None,9,GN),check(870,410,1.0)]
s+=[T(560,600,'Một đợt đủ mức',42,GN)]
S.append(s)
# 8 teaser
s=pre([P(R(140,90,800,330,28),'#fff3d6',6),T(540,180,'PHẦN SAU',60,RD),T(540,280,'Theo dõi khách hàng',54,INK),T(540,360,'ba tháng đầu',50,DB)])
s+=[P(L((200,600),(330,540),(460,570),(600,500),(740,520),(880,470)),None,8,GN)]+glass(880,470,45,DB)
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
