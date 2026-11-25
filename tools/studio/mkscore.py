import numpy as np,json,wave
SR=44100;D=json.load(open('dur.json'));W=json.load(open('words.json'));T=sum(D);N=int(T*SR)
ld=lambda f:np.fromfile(f,np.float32).reshape(-1,2)[:N]
F,Lo,Mi=ld('w_full.raw'),ld('w_lo.raw'),ld('w_mid.raw')
t=np.arange(N)/SR;S=[0]+list(np.cumsum(D));nS=len(D)
def wt(sc,pid): return S[sc]+[x for x in W[sc] if x[3]==pid][0][0]
def env(pts): x,y=zip(*pts);return np.interp(t,x,y)[:,None]
sol=S[nS-2]
gLo=env([(0,0),(1.0,0),(1.6,0.55),(S[2]-0.4,0.55),(S[2]+0.4,0),(T,0)])
gMi=env([(0,0),(S[2]-0.4,0),(S[2]+0.4,0.65),(sol-0.5,0.65),(sol+0.2,0),(T,0)])
gF=env([(0,0),(sol-0.5,0),(sol+0.2,1.0),(S[nS-1]-0.3,1.0),(S[nS-1]+0.5,0.8),(T-3.0,0.8),(T-2.4,1.0),(T-2.0,1.0),(T,0)])
out=Lo*gLo*1.25+Mi*gMi+F*gF
def bell(f,dur=2.2):
    tt=np.arange(int(dur*SR))/SR
    return sum(a*np.sin(2*np.pi*f*r*tt)*np.exp(-tt*d) for r,a,d in [(1,1,3.5),(2.76,0.4,6),(5.4,0.18,9)])*np.minimum(1,tt/0.002)
def put(sig,t0,g):
    s=int(t0*SR);e=min(N,s+len(sig));out[s:e,0]+=sig[:e-s]*g;out[s:e,1]+=sig[:e-s]*g
m=lambda n:440*2**((n-69)/12)
for tt in [wt(i,0) for i in range(2,nS-2)]: put(bell(m(96),1.4),tt-0.03,0.05)
k=wt(nS-2,0);put(bell(m(91),2.5),k-0.03,0.07);put(bell(m(96),2.5),k-0.01,0.05)
out/=np.abs(out).max()*1.1
w=wave.open('score.wav','wb');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes());w.close()
