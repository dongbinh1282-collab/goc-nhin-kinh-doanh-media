# Kiểm tra lặp ý: so kịch bản một tập với mọi tập cũ (cụm 6 từ liên tiếp).
# Dùng: python3 studio/check_lap.py tap15   → in số cụm trùng và tối đa 8 ví dụ. Không cần đọc kịch bản cũ.
import json, re, sys, glob, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
N = 6
def words(path):
    S = json.load(open(path, encoding='utf-8'))
    txt = ' '.join(sc[j][0] for sc in S for j in range(len(sc)))
    return re.findall(r'\w+', txt.lower())
def grams(ws):
    return {' '.join(ws[i:i+N]): i for i in range(len(ws)-N+1)}
me = sys.argv[1]
mine_ws = words(os.path.join(ROOT, me, 'script2.json'))
mine = grams(mine_ws)
hits = []
for p in sorted(glob.glob(os.path.join(ROOT, 'tap*', 'script2.json'))):
    t = os.path.basename(os.path.dirname(p))
    if t == me: continue
    other = grams(words(p))
    for g in mine:
        if g in other: hits.append((t, g))
print(f'{me}: {len(hits)} cụm {N} từ trùng với tập cũ')
for t, g in hits[:8]: print(f'  {t}: "{g}"')
print('KẾT: ' + ('AN TOÀN (0 trùng)' if not hits else 'CẦN SỬA câu trùng'))
