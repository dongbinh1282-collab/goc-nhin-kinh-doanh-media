import sys,json,subprocess,re
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from vn import load
import soundfile as sf,numpy as np
from faster_whisper import WhisperModel
WM=WhisperModel('small',compute_type='int8')
tts=load();voice=tts.get_preset_voice('Đức Trí')
GAP={'n':0.16,'q':0.3,'k':0.4,'l':0.1,'f':0.16,'p':0.9}
S=json.load(open('script2.json'));W=[];D=[];parts=[];k=0
def dur(fn): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',fn]))
for i,sc in enumerate(S):
    t=0.2;ws=[]
    for j,(txt,st) in enumerate(sc):
        NUM={'hai','ba','bốn','năm','tám','chín','mươi','mười','một','phần','trăm','thứ'}
        exp=[w for w in re.findall(r'\w+',txt.lower()) if w not in NUM]
        best=None
        for tr in range(6):
            a=tts.infer(text=txt,voice=voice);tts.save(a,f'r{k}.wav')
            subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'r{k}.wav','-af','silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.03,areverse,silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.06,areverse,atempo=1.3','-ar','48000','-ac','1',f'c{k}_{tr}.wav'],check=True)
            subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'c{k}_{tr}.wav','-ar','16000','-ac','1','/tmp/al.wav'])
            au,_=sf.read('/tmp/al.wav',dtype='float32')
            got=set(re.findall(r'\w+',' '.join(x.text for x in WM.transcribe(au,language='vi')[0]).lower()))
            miss=[w for w in exp if w not in got]
            if best is None or len(miss)<best[0]: best=(len(miss),tr,miss)
            if not miss: break
        print('line',k,'try',best[1],'miss',best[2])
        subprocess.run(['cp',f'c{k}_{best[1]}.wav',f'v{k}.wav'])
        d=dur(f'v{k}.wav')
        words=txt.split();lens=np.array([len(re.sub(r'[^\w]','',w))+1 for w in words],float)
        span=d-0.1;cum=np.concatenate([[0],np.cumsum(lens)])/lens.sum()*span+0.03
        tm=[[cum[n],cum[n+1]] for n in range(len(words))]
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'v{k}.wav','-ar','16000','-ac','1','/tmp/al.wav'])
        au,_=sf.read('/tmp/al.wav',dtype='float32')
        ww=[w for sg in WM.transcribe(au,language='vi',word_timestamps=True,initial_prompt=txt)[0] for w in sg.words]
        if len(ww)==len(words): tm=[[w.start,w.end] for w in ww]; print('align ok',k)
        else: print('align fallback',k,len(ww),len(words))
        ws+=[[t+tm[n][0],t+tm[n][1],re.sub(r'[,.?:!]','',words[n]),j] for n in range(len(words))]
        parts.append((i,t,f'v{k}.wav'));k+=1
        t+=d+(GAP[st] if j<len(sc)-1 else 0.25)
    if i==len(S)-1: t+=2.6
    D.append(round(t,2));W.append(ws)
json.dump(W,open('words.json','w'),ensure_ascii=False);json.dump(D,open('dur.json','w'))
T0=[0]+[sum(D[:i+1]) for i in range(len(D))];inp=[];flt=[]
for n,(i,t,fn) in enumerate(parts):
    ms=int((T0[i]+t)*1000);inp+=['-i',fn];flt.append(f'[{n}]adelay={ms}|{ms}[a{n}]')
fc=';'.join(flt)+';'+''.join(f'[a{n}]' for n in range(len(parts)))+f'amix=inputs={len(parts)}:normalize=0,apad,atrim=0:{sum(D)}[o]'
subprocess.run(['ffmpeg','-y','-loglevel','error']+inp+['-filter_complex',fc,'-map','[o]','voice_dry.wav'],check=True)
print(D,sum(D))
