import asyncio,json
from playwright.async_api import async_playwright
I={'plus':('plus','#2C2C2A'),'upload':('photo-up','#2C2C2A'),'next':('arrow-right','#E24B4A'),'nomusic':('music-off','#888780'),
'cover':('photo','#7F77DD'),'paste':('clipboard-text','#BA7517'),'more':('dots','#2C2C2A'),'ai':('toggle-right','#1D9E75'),
'post':('send','#E24B4A'),'pin':('pin','#D85A30'),'cut':('scissors','#888780'),'title':('letter-t','#185FA5'),'desc':('file-description','#185FA5'),
'public':('world','#1D9E75'),'kid':('mood-kid','#888780'),'cloud':('cloud-upload','#E24B4A'),'reels':('movie','#378ADD'),'share':('share','#378ADD'),'comment':('message-circle','#D85A30')}
html='<html><head><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@latest/dist/tabler-icons.min.css"></head><body style="margin:0;background:transparent">'
for k,(ic,c) in I.items():
    html+=f'<div id="{k}" style="width:96px;height:96px;border-radius:24px;background:{c};display:inline-flex;align-items:center;justify-content:center;margin:4px"><i class="ti ti-{ic}" style="font-size:60px;color:#fff"></i></div>'
html+='</body></html>'
open('i.html','w').write(html)
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=await b.new_page(viewport={'width':1200,'height':600})
    await pg.goto('file://'+__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'i.html'));await pg.wait_for_timeout(2500)
    for k in I: await (await pg.query_selector('#'+k)).screenshot(path=f'{k}.png',omit_background=True)
    await b.close()
asyncio.run(m())
