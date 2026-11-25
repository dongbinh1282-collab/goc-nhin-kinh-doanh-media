"""Gắn dấu câu từ script2.json vào words.json (x[4]=1 sau dấu phẩy/chấm) để chữ chạy ngắt đúng cụm nghĩa.
Chạy trong thư mục tập, trước make.sh."""
import json,re
S=json.load(open('script2.json')); W=json.load(open('words.json'))
for i,sc in enumerate(S):
    toks=[t for s,_ in sc for t in s.split()]
    ws=W[i]
    if len(toks)!=len(ws): print('lệch số từ cảnh',i,len(toks),len(ws)); continue
    for t,x in zip(toks,ws):
        x[:]=x[:4]+[2 if re.search(r'[.?!]$',t) else (1 if re.search(r'[,;:]$',t) else 0)]
json.dump(W,open('words.json','w'),ensure_ascii=False)
print('punct OK')
