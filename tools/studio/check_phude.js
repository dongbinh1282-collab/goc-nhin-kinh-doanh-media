const fs=require('fs');const h=fs.readFileSync('page.html','utf8');
const a=h.indexOf('const GLUE');const b=h.indexOf('</script>',a);
let CH=[];eval(h.slice(a,b).replace('function init','var init=function'));
init(null,JSON.parse(fs.readFileSync('dur.json')),JSON.parse(fs.readFileSync('words.json')));
CH.forEach(c=>console.log(c.w.map(x=>x.t).join(' ')));
