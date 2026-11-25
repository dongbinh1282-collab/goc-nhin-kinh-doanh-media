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
# 0 hook: biểu đồ tăng hiện ngay, bút vẽ nhãn "vội kết luận"
s=pre([T(540,80,'SAU KHI TĂNG GIÁ',60,OR),P(L((150,500),(930,500)),None,6,INK)])
s+=pre([P(R(200,390,110,110,8),BL,4),P(R(360,330,110,170,8),BL,4),P(R(520,270,110,230,8),BL,4),P(R(680,210,110,290,8),BL,4)])
s+=pre([T(540,560,'Doanh thu tuần đầu',42,DB)])
s+=ptag(90,200,'Đã ổn?',YL,48)
S.append(s)
# 1 ba chỉ số
s=[T(540,80,'BA CHỈ SỐ CẦN THEO DÕI',54,RD)]
s+=pre([P(R(50,140,300,350,22),'#ffffff',5),P(R(390,140,300,350,22),'#ffffff',5),P(R(730,140,300,350,22),'#ffffff',5)])
s+=pre(box(120,250,1.4))+pre(person(540,290,0.75,'ok','down',BL,legs=False))+pre(coin(880,290,58))
s+=pre([T(200,470,'Sản lượng',38,DB,w=290),T(540,470,'Khách quay lại',38,DB,w=290),T(880,470,'Lợi nhuận gộp',38,DB,w=290)])
S.append(s)
# 2 sản lượng theo nhóm khách
s=[T(540,70,'SẢN LƯỢNG THEO NHÓM',54,RD),T(540,130,'Xám: trước khi tăng giá',42,INK),T(540,180,'Màu: sau khi tăng giá',42,DB)]
s+=[P(L((150,500),(930,500)),None,6,INK)]
s+=[P(R(230,300,90,200,8),GY,4),P(R(340,340,90,160,8),BL,4),P(R(610,230,90,270,8),GY,4),P(R(720,300,90,200,8),OR,4)]
s+=[T(325,540,'Khách lớn',40,INK),T(665,540,'Khách nhỏ',40,INK)]
S.append(s)
# 3 mốc cảnh báo: đồng hồ đo
s=[T(540,70,'MỐC CẢNH BÁO',60,RD)]
s+=gauge(540,400,200,205,INK)
s+=[T(300,470,'Vượt mức',42,RD),T(780,470,'An toàn',42,GN),T(540,545,'Mỗi nhóm khách một mốc',42,DB)]
S.append(s)
# 4 khách quay lại trong 60 ngày
s=[T(540,70,'KHÁCH QUAY LẠI',56,RD)]
s+=pre(cal2(440,150,'60',1.0))+pre(person(240,300,0.8,'ok','point',BL,legs=False))
s+=tag(90,430,380,'Khách lớn',GN,44)+tag(580,430,380,'Khách nhỏ lẻ',OR,44)
s+=[T(540,545,'Tỷ lệ khách cũ quay lại',42,DB)]
S.append(s)
# 5 lợi nhuận gộp bằng tiền
s=[T(540,70,'LỢI NHUẬN GỘP BẰNG TIỀN',50,RD)]
s+=pre(coin(300,440,64)+coin(440,440,64)+coin(580,440,64)+coin(370,360,64))
s+=arrow(760,470,760,280,GN,10)+[T(860,250,'Giữ hoặc tăng',42,GN)]
s+=[T(540,545,'Chỉ số phải theo dõi mỗi tháng',40,DB)]
S.append(s)
# 6 giảm hai tháng liên tiếp
s=[T(540,70,'GIẢM HAI THÁNG LIÊN TIẾP',50,RD)]
s+=[P(L((120,500),(960,500)),None,6,INK)]
s+=[P(L((160,200),(300,240),(440,300),(580,360),(720,420),(860,460)),None,9,RD)]
s+=[P(C(440,300,14),RD,4),P(C(720,420,14),RD,4),T(440,540,'Tháng 1',40,INK),T(720,540,'Tháng 2',40,INK)]
s+=glass(880,220,50,DB)
S.append(s)
# 7 họp định kỳ
s=[T(540,70,'HỌP ĐỊNH KỲ',60,RD)]
s+=pre(cal(110,160,'HỌP',1.2))+pre(doc(400,160,380,260,4))
s+=tag(260,430,560,'Ghi rõ lý do khách rời',YL,42)
S.append(s)
# 8 teaser
s=pre([P(R(140,110,800,330,28),'#fff3d6',6),T(540,210,'PHẦN SAU',60,RD),T(540,310,'Cách trình bày bảng giá mới',48,INK),T(540,380,'để khách dễ chấp nhận',46,DB)])
s+=ptag(300,450,'Giá mới',YL,44)+[check(700,490,1.6,GR)]
S.append(s)
json.dump(S,open('scenes.json','w'),ensure_ascii=False); print([len(x) for x in S])
