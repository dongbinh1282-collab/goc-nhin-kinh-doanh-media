#!/usr/bin/env python3
"""Dò từ giọng đọc hay đọc sai, chạy NGAY khi viết kịch bản (trước khi gửi anh duyệt).
Cách dùng (trong tools/): python3 studio/check_tu.py tapNN   → 0 từ rủi ro mới ĐẠT.
Danh sách lấy từ lỗi thật tập 09–11; gặp từ sai mới thì thêm vào RUI_RO."""
import json, re, sys, os
RUI_RO = {  # từ hay sai : cách thay đã đọc đúng
 'vay': 'xoay tiền / cho vay (cụm "ngân hàng cho vay" đọc đúng)',
 'hạn mức': 'chỉ dùng trong cụm "hạn mức ngắn hạn"',
 'tín dụng': 'chỉ dùng cuối câu ("siết tín dụng ngay")',
 'nhưng biên lợi nhuận': 'nhưng lợi nhuận gộp trên mỗi đồng doanh thu (tập 13 đọc sai)',
 'lãi': 'chi phí / tiền lãi',
 'cạn': 'hết',
 'suất': 'mức', 'nên': 'hãy', 'lăm': 'nửa tháng / một tháng rưỡi',
 'ví dụ': 'số liệu minh họa', 'khoản này': 'điều kiện này',
 'thưởng': 'tiền thưởng (tránh cạnh "thường")', 'dồn': 'xếp', 'mùa tết': 'dịp Tết', 'ròng': 'sau thuế', 'minh họa bằng số': 'giả định', 'ghi vào': 'hợp đồng cần có',
}
OK_CUM = ['ngân hàng cho vay', 'chi phí vay', 'hạn mức ngắn hạn', 'siết tín dụng', 'tiền lãi']
tap = sys.argv[1]
d = json.load(open(os.path.join(tap, 'script2.json'), encoding='utf-8'))
bad = 0
for s in d:
    for c in s:
        t = c[0].lower()
        for ok in OK_CUM: t = t.replace(ok, '#')
        for w, fix in RUI_RO.items():
            if re.search(r'(?<!\w)' + w + r'(?!\w)', t):
                bad += 1; print(f'RỦI RO "{w}" → {fix}\n   câu: {c[0]}')
print('KẾT LUẬN:', 'ĐẠT' if not bad else f'CHƯA ĐẠT, {bad} từ'); sys.exit(1 if bad else 0)
