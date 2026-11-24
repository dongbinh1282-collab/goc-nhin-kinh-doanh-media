import json, sys, os, asyncio
from playwright.async_api import async_playwright
S=json.load(open('scenes.json')); D=json.load(open('dur.json')); W=json.load(open('words.json'))
FPS=30; N=int(round(sum(D)*FPS))
async def run(a,b,tag):
    os.makedirs(f'fr{tag}',exist_ok=True)
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
        pg=await br.new_page(viewport={'width':1080,'height':1920})
        await pg.goto('file://'+(os.path.abspath('page.html') if os.path.exists('page.html') else os.path.join(os.path.dirname(os.path.abspath(__file__)),'page.html'))); await pg.wait_for_timeout(300)
        await pg.evaluate('([s,d,w])=>init(s,d,w)',[S,D,W])
        for k in range(a,b):
            await pg.evaluate(f'setT({k/FPS})')
            await pg.screenshot(path=f'fr{tag}/{k:05d}.jpg',type='jpeg',quality=96)
        await br.close()
if __name__=='__main__':
    if sys.argv[1]=='pv':
        ts=[float(x) for x in sys.argv[2:]]
        async def pv():
            async with async_playwright() as p:
                br=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
                pg=await br.new_page(viewport={'width':1080,'height':1920})
                await pg.goto('file://'+(os.path.abspath('page.html') if os.path.exists('page.html') else os.path.join(os.path.dirname(os.path.abspath(__file__)),'page.html'))); await pg.wait_for_timeout(300)
                await pg.evaluate('([s,d,w])=>init(s,d,w)',[S,D,W])
                for t in ts:
                    await pg.evaluate(f'setT({t})'); await pg.screenshot(path=f'pv_{t}.jpg',type='jpeg',quality=85)
                await br.close()
        asyncio.run(pv())
    else:
        a,b,tag=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]; asyncio.run(run(a,b,tag))
