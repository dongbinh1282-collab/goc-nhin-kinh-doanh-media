# Kiểm tra bắt buộc trước khi giao 1 tập – chạy trong thư mục tập, sau khi đã có final.mp4
#   python3 ../studio/qa.py
# 1) Nghe lại từng câu bằng whisper MEDIUM (small hay bỏ sót lỗi) – câu nào lệch chữ phải đổi từ rồi tạo lại giọng.
# 2) Đo độ dài (50–65 s) và loudness (-14 LUFS ± 1).
# 3) Trích 21 khung (mỗi 3 giây) thành qa_sheet.jpg để XEM HẾT bằng mắt.
import json, re, glob, subprocess, sys, unicodedata
import numpy as np, soundfile as sf
from faster_whisper import WhisperModel
NUM={'một':'1','hai':'2','ba':'3','bốn':'4','năm':'5','sáu':'6','bảy':'7','tám':'8','chín':'9','mười':'10'}
def norm(s): return [w for w in re.findall(r'\w+',unicodedata.normalize('NFC',s.lower()))]
S=json.load(open('script2.json')); lines=[t for g in S for t,_ in g]
m=WhisperModel('medium',compute_type='int8'); bad=[]
for k,txt in enumerate(lines):
    a,sr=sf.read(f'v{k}.wav',dtype='float32'); a=a.mean(1) if a.ndim>1 else a
    if sr!=16000: n=int(len(a)*16000/sr); a=np.interp(np.linspace(0,len(a)-1,n),np.arange(len(a)),a).astype('float32')
    heard=' '.join(s.text for s in m.transcribe(a,language='vi',beam_size=5)[0])
    exp=[w for w in norm(txt) if w not in NUM and not w.isdigit()]
    got=set(norm(heard)); miss=[w for w in exp if w not in got and w not in ('mươi','trăm','phần','nghìn','triệu')]
    flag='OK ' if not miss else 'SAI'
    if miss: bad.append(k)
    print(f'{flag} câu {k}: {txt}\n      nghe: {heard.strip()}' + (f'\n      lệch: {miss}' if miss else ''))
dur=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','final.mp4']))
lu=subprocess.run(['ffmpeg','-i','final.mp4','-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I=float(re.findall(r'I:\s+(-?[\d.]+) LUFS',lu)[-1])
print(f'\nĐộ dài {dur:.1f}s ({"OK" if 50<=dur<=65 else "SAI"}) · Loudness {I} LUFS ({"OK" if abs(I+14)<=1 else "SAI"})')
from PIL import Image
fs=[]
for i in range(21):
    t=0.5+i*3
    if t>dur: break
    f=f'qa_{i:02d}.jpg'; subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i','final.mp4','-frames:v','1','-vf','scale=270:480','-y',f]); fs.append(f)
W=Image.new('RGB',(270*11,480*2),'white')
for i,f in enumerate(fs): W.paste(Image.open(f),(270*(i%11),480*(i//11)))
W.save('qa_sheet.jpg')
print('Khung kiểm tra: qa_sheet.jpg – phải mở xem hết trước khi giao.')
print('KẾT LUẬN:', 'CHƯA ĐẠT – sửa câu '+str(bad) if bad else 'Lời đọc đạt')
sys.exit(1 if bad else 0)
