#!/usr/bin/env python3
"""Kiểm tra trùng kịch bản tập mới so với các tập cũ (tap01..tap09).

Cách dùng (chạy trong thư mục tools/):
    python3 studio/check_trung.py tap10

Bốn kiểm tra:
  1. Câu trùng: câu mới giống câu cũ từ 60% trở lên.
  2. Số liệu/ví dụ trùng: cùng một con số + đơn vị đã dùng ở tập cũ.
  3. Cách mở câu trùng: ba chữ đầu giống một câu cũ.
  4. Cấu trúc đánh số: cảnh báo để tự xem lại (không tính là lỗi).

Kết quả: "ĐẠT" khi mục 1–3 không có cặp nào; ngược lại in danh sách và thoát với mã lỗi 1.
Bản quy trình: docs/quy-trinh-chuan.md, mục 11.
"""
import difflib
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # thư mục tools/
cur = sys.argv[1] if len(sys.argv) > 1 else None
if not cur:
    print(__doc__)
    sys.exit(2)


def lines_of(tap):
    path = os.path.join(ROOT, tap, 'script2.json')
    if not os.path.exists(path):
        return []
    return [c[0] for scene in json.load(open(path, encoding='utf-8')) for c in scene]


def norm(s):
    return re.sub(r'\W+', ' ', s.lower()).strip()


old = []
for d in sorted(glob.glob(os.path.join(ROOT, 'tap[0-9][0-9]'))):
    name = os.path.basename(d)
    if name == cur:
        continue
    old += [(name, l) for l in lines_of(name)]

new = lines_of(cur)
if not new:
    print(f'Không tìm thấy {cur}/script2.json')
    sys.exit(2)

# Câu cố định của kênh (chào kết và hẹn tập sau) không tính là trùng nội dung.
FIXED = ('hẹn gặp lại các bạn', 'phần sau sẽ là')


def is_fixed(line):
    return norm(line).startswith(FIXED)


old = [(n, l) for n, l in old if not is_fixed(l)]
new_checked = [l for l in new if not is_fixed(l)]

NUM_WORDS = (r'(?:một|hai|ba|bốn|năm|sáu|bảy|tám|chín|mười|trăm|nghìn|triệu|tỷ|'
             r'hai mươi|ba mươi|bốn mươi|năm mươi|sáu mươi|bảy mươi|tám mươi|chín mươi|'
             r'một trăm|hai trăm|ba trăm|bốn trăm|năm trăm|sáu trăm|bảy trăm|tám trăm|chín trăm)')
UNITS = r'(?:phần trăm|%|triệu|tỷ|nghìn|ngày|tuần|tháng|năm|đồng|lần)'
FACT = re.compile(rf'(?:\d[\d.,]*|{NUM_WORDS}(?:\s+{NUM_WORDS})*)\s*{UNITS}', re.IGNORECASE)


def facts(line):
    return {norm(m.group(0)) for m in FACT.finditer(line)}


hits = 0
print(f'Kiểm tra {cur} với {len(old)} câu của các tập cũ\n')

print('1. Câu trùng (độ giống từ 60% trở lên):')
n1 = 0
for l in new_checked:
    for name, o in old:
        r = difflib.SequenceMatcher(None, norm(l), norm(o)).ratio()
        if r >= 0.6:
            print(f'   [{r:.2f}] {name}: "{o}"\n           mới: "{l}"')
            n1 += 1
print(f'   → {n1} cặp\n')
hits += n1

print('2. Số liệu/ví dụ trùng:')
oldf = {}
for name, o in old:
    for f in facts(o):
        oldf.setdefault(f, set()).add(name)
n2 = 0
for l in new_checked:
    for f in facts(l):
        if f in oldf:
            print(f'   "{f}" đã có ở {sorted(oldf[f])}: "{l}"')
            n2 += 1
print(f'   → {n2} mục\n')
hits += n2

print('3. Cách mở câu trùng (ba chữ đầu):')
opens = {}
for name, o in old:
    opens.setdefault(' '.join(norm(o).split()[:3]), set()).add(name)
n3 = 0
for l in new_checked:
    k = ' '.join(norm(l).split()[:3])
    if k in opens:
        print(f'   "{k}" đã mở ở {sorted(opens[k])}: "{l}"')
        n3 += 1
print(f'   → {n3} mục\n')
hits += n3

print('4. Cấu trúc đánh số (chỉ cảnh báo, tự xem lại):')
pat = re.compile(r'^(Nguyên tắc|Điều|Cách|Việc|Bước) thứ')
n4 = sum(1 for l in new_checked if pat.match(l))
print(f'   {n4} câu đánh số trong tập mới\n')

if hits == 0:
    print('KẾT LUẬN: ĐẠT, không có câu, số liệu hay cách mở câu trùng.')
    sys.exit(0)
print(f'KẾT LUẬN: CHƯA ĐẠT, {hits} mục trùng. Sửa rồi chạy lại.')
sys.exit(1)
