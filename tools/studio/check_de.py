#!/usr/bin/env python3
"""Kiểm tra chữ đè lên hình (chữ nằm một phần trong, một phần ngoài khung).
Chạy trong thư mục tập, sau `python3 scenes.py`:  python3 ../studio/check_de.py
Đạt khi 0 chỗ đè. Chữ nằm trọn trong khung (nhãn trong ô) không tính là lỗi."""
import json, re, sys
S = json.load(open('scenes.json', encoding='utf-8'))
def tbox(e):
    w = min(len(e['txt']) * e['size'] * 0.56, e.get('w', 800)); h = e['size']
    x0 = e['x'] - w/2 if e['anchor'] == 'middle' else (e['x'] if e['anchor'] == 'start' else e['x'] - w)
    return (x0, e['y'] - h*0.78, x0 + w, e['y'] + h*0.22)
def pbox(e):
    n = [float(v) for v in re.findall(r'-?\d+\.?\d*', e['d'])]
    xs, ys = n[0::2], n[1::2]
    return (min(xs), min(ys), max(xs), max(ys))
bad = 0
for i, sc in enumerate(S):
    shapes = [pbox(e) for e in sc if e['k'] == 'p' and e.get('fill') and e['d'].count('L') >= 3]
    shapes = [b for b in shapes if (b[2]-b[0]) > 150 and (b[3]-b[1]) > 60]  # chỉ khung, thẻ, ô lớn
    for e in sc:
        if e['k'] != 't': continue
        t = tbox(e)
        for b in shapes:
            ix = min(t[2], b[2]) - max(t[0], b[0]); iy = min(t[3], b[3]) - max(t[1], b[1])
            if ix <= 0 or iy <= 0: continue
            inside = t[0] >= b[0]-4 and t[2] <= b[2]+4 and t[1] >= b[1]-4 and t[3] <= b[3]+4
            if not inside:
                bad += 1; print(f'ĐÈ cảnh {i}: "{e["txt"]}" chạm khung {tuple(int(v) for v in b)}')
        if t[3] > 615: bad += 1; print(f'SÁT ĐÁY cảnh {i}: "{e["txt"]}" (đáy chữ {int(t[3])} > 615)')
print('KẾT LUẬN:', 'ĐẠT' if bad == 0 else f'CHƯA ĐẠT, {bad} chỗ'); sys.exit(1 if bad else 0)
