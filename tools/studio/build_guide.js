const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,HeadingLevel,AlignmentType,Table,TableRow,TableCell,WidthType,ShadingType,BorderStyle,LevelFormat}=require('docx');
const F='Arial';
const {ImageRun}=require('docx');
const ICD=__dirname+'/icons/';
const icon=(k,s=30)=>new ImageRun({type:'png',data:fs.readFileSync(ICD+k+'.png'),transformation:{width:s,height:s}});
const numI=(t,ref,ics)=>new Paragraph({numbering:{reference:ref,level:0},spacing:{after:90},children:[...ics.flatMap(k=>[icon(k),new TextRun({text:' ',font:F,size:22})]),new TextRun({text:' '+t,font:F,size:23})]});
const LG=[['plus','Nút tạo mới (+)'],['upload','Tải lên / chọn video'],['nomusic','Không thêm nhạc'],['next','Tiếp'],['cover','Ảnh bìa'],['paste','Dán mô tả'],['more','Ba chấm: tùy chọn khác'],['ai','Bật nhãn AI'],['post','Đăng'],['comment','Bình luận'],['pin','Ghim'],['cut','Cắt video'],['title','Tiêu đề'],['desc','Mô tả'],['public','Công khai'],['kid','Không dành cho trẻ em'],['cloud','Tải lên YouTube'],['reels','Thước phim (Reels)'],['share','Chia sẻ ngay']];
const legend=()=>new Table({width:{size:W,type:WidthType.DXA},columnWidths:[W/2,W/2],rows:Array.from({length:Math.ceil(LG.length/2)},(_,r)=>new TableRow({children:[0,1].map(c=>{const it=LG[r*2+c];return new TableCell({width:{size:W/2,type:WidthType.DXA},margins:{top:60,bottom:60,left:100,right:100},children:[new Paragraph({children:it?[icon(it[0],26),new TextRun({text:'  '+it[1],font:F,size:21})]:[]})]});})}))});

const P=(t,o={})=>new Paragraph({spacing:{after:100},...o,children:(Array.isArray(t)?t:[t]).map(x=>typeof x==='string'?new TextRun({text:x,font:F,size:22}):x)});
const B=(t)=>new TextRun({text:t,font:F,size:22,bold:true});
const H1=t=>new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun({text:t})]});
const H2=t=>new Paragraph({heading:HeadingLevel.HEADING_2,children:[new TextRun({text:t})]});
const bul=(t,lvl=0)=>new Paragraph({numbering:{reference:'b',level:lvl},spacing:{after:60},children:(Array.isArray(t)?t:[t]).map(x=>typeof x==='string'?new TextRun({text:x,font:F,size:22}):x)});
const num=(t,ref)=>new Paragraph({numbering:{reference:ref,level:0},spacing:{after:60},children:(Array.isArray(t)?t:[t]).map(x=>typeof x==='string'?new TextRun({text:x,font:F,size:22}):x)});
const W=9026;
const copyBox=(label,lines)=>new Table({width:{size:W,type:WidthType.DXA},columnWidths:[W],rows:[
 new TableRow({children:[new TableCell({width:{size:W,type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill:'FFE9B0',color:'auto'},margins:{top:80,bottom:80,left:140,right:140},children:[new Paragraph({children:[new TextRun({text:'📋 '+label+'  (bấm giữ để chọn rồi Sao chép)',font:F,size:20,bold:true,color:'7A4A00'})]})]})]}),
 new TableRow({children:[new TableCell({width:{size:W,type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill:'FFF8E6',color:'auto'},margins:{top:100,bottom:100,left:140,right:140},children:lines.map(l=>new Paragraph({spacing:{after:60},children:[new TextRun({text:l,font:F,size:22})]}))})]})]});
const sp=()=>new Paragraph({spacing:{after:120},children:[]});
const tbl=(head,rows,widths)=>new Table({width:{size:W,type:WidthType.DXA},columnWidths:widths,rows:[
 new TableRow({tableHeader:true,children:head.map((h,i)=>new TableCell({width:{size:widths[i],type:WidthType.DXA},shading:{type:ShadingType.CLEAR,fill:'1F2533',color:'auto'},margins:{top:80,bottom:80,left:120,right:120},children:[new Paragraph({children:[new TextRun({text:h,font:F,size:21,bold:true,color:'FFFFFF'})]})]}))}),
 ...rows.map(r=>new TableRow({children:r.map((c,i)=>new TableCell({width:{size:widths[i],type:WidthType.DXA},margins:{top:70,bottom:70,left:120,right:120},children:[new Paragraph({children:[new TextRun({text:c,font:F,size:21,bold:i===0})]})]}))}))]});

const MUSIC='Music: "Wholesome" by Kevin MacLeod (incompetech.com), Licensed under Creative Commons: By Attribution 4.0';
const HASH='#kinhdoanh #chudoanhnghiep #congno #dongtien #quantri #taichinhdoanhnghiep';
const children=[
 new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new TextRun({text:'HƯỚNG DẪN ĐĂNG VIDEO',font:F,size:40,bold:true,color:'1F2533'})]}),
 new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:60},children:[new TextRun({text:'TikTok · YouTube Shorts · Facebook Reels',font:F,size:26,color:'B35C00',bold:true})]}),
 new Paragraph({alignment:AlignmentType.CENTER,spacing:{after:240},children:[new TextRun({text:'Kênh Góc nhìn kinh doanh – Tập 2: Thu hồi công nợ mà không mất khách',font:F,size:22,italics:true})]}),

 H1('1. Chuẩn bị trước khi đăng'),
 bul([B('File video: '),'Tap2_Thu-hoi-cong-no_TikTok-YouTube-Facebook.mp4 (dọc 9:16, 60 giây, dùng chung cho cả 3 nền tảng, ảnh bìa nằm ở 1 giây cuối).']),
 bul([B('Ảnh bìa: '),'Anh-bia_Tap2_Thu-hoi-cong-no.jpg (khung có tiêu đề to, dùng cho YouTube và Facebook).']),
 bul('Lưu cả hai file vào điện thoại (mở file → Chia sẻ → Lưu video / Lưu ảnh).'),
 bul('Mở sẵn tài liệu này để sao chép phần chữ ở mục 2.'),

 H1('2. Nội dung sao chép sẵn'),
 H2('2.1. TikTok – phần mô tả'),
 copyBox('Mô tả TikTok',['Khách hàng còn nợ nhưng ngại nhắc vì sợ mất khách? 4 nguyên tắc giúp doanh nghiệp thu hồi công nợ mà vẫn giữ được quan hệ tốt. Lưu video lại để áp dụng cho đội kinh doanh.',HASH,MUSIC]),
 sp(),
 H2('2.2. YouTube Shorts'),
 copyBox('Tiêu đề YouTube (tối đa 100 ký tự)',['Thu hồi công nợ mà không mất khách – 4 nguyên tắc chủ doanh nghiệp cần biết #Shorts']),
 sp(),
 copyBox('Mô tả YouTube',['Công nợ càng kéo dài, khả năng thu hồi càng thấp. Video trình bày 4 nguyên tắc thu hồi công nợ mà vẫn giữ được khách hàng: thỏa thuận rõ ràng, nhắc nợ sớm và đều đặn, chiết khấu thanh toán sớm 1–2%, tách người bán hàng khỏi người thu nợ.',HASH+' #Shorts',MUSIC]),
 sp(),
 H2('2.3. Facebook Reels'),
 copyBox('Mô tả Facebook',['Khách hàng còn nợ, nhưng ngại nhắc vì sợ mất khách? 🤝','4 nguyên tắc thu hồi công nợ mà vẫn giữ được quan hệ tốt với khách hàng: thỏa thuận rõ ràng, nhắc nợ sớm, chiết khấu thanh toán sớm và tách vai trò bán hàng – thu nợ.',HASH,MUSIC]),
 sp(),
 H2('2.4. Bình luận ghim (dùng cho cả 3 nền tảng)'),
 copyBox('Bình luận để ghim',['Doanh nghiệp của anh chị đang áp dụng nguyên tắc nào trong 4 nguyên tắc này? Phần sau: cách quản lý hàng tồn kho để giải phóng nguồn vốn.']),

 H1('3. Cách đăng từng nền tảng (trên điện thoại)'),
 P([new TextRun({text:'Nhìn biểu tượng màu ở đầu mỗi bước để biết bấm vào nút nào.',font:F,size:21,italics:true,color:'666666'})]),
 H2('3.1. TikTok'),
 numI('Bấm nút dấu cộng + ở giữa thanh dưới cùng.','t',['plus']),
 numI('Bấm Tải lên (góc phải), chọn video.','t',['upload']),
 numI('Không bấm "Thêm âm thanh" (video đã có nhạc). Bấm Tiếp.','t',['nomusic','next']),
 numI('Bấm Chọn ảnh bìa, kéo thanh chọn về khung cuối cùng, bấm Lưu.','t',['cover']),
 numI('Bấm vào ô mô tả, dán Mô tả TikTok (mục 2.1).','t',['paste']),
 numI('Bấm Tùy chọn khác (dấu ba chấm), bật Nội dung do AI tạo.','t',['more','ai']),
 numI('Bấm nút Đăng màu đỏ.','t',['post']),
 numI('Mở video vừa đăng, bấm biểu tượng bình luận, dán Bình luận ghim (mục 2.4). Bấm giữ bình luận, chọn Ghim.','t',['comment','pin']),
 H2('3.2. YouTube Shorts'),
 numI('Bấm nút dấu cộng + ở giữa thanh dưới cùng, chọn Tải video lên, chọn video.','y',['plus','upload']),
 numI('Nếu YouTube hỏi cắt video: giữ nguyên toàn bộ, bấm Tiếp.','y',['cut','next']),
 numI('Bấm ô Tiêu đề, dán Tiêu đề YouTube (mục 2.2).','y',['title']),
 numI('Bấm Thêm nội dung mô tả, dán Mô tả YouTube.','y',['desc']),
 numI('Chế độ hiển thị: chọn Công khai.','y',['public']),
 numI('Đối tượng: chọn "Không, video này không dành cho trẻ em".','y',['kid']),
 numI('Bấm Tải video Shorts lên.','y',['cloud']),
 numI('Mở video, bình luận nội dung mục 2.4, bấm ba chấm cạnh bình luận, chọn Ghim.','y',['comment','pin']),
 H2('3.3. Facebook Reels'),
 numI('Bấm Thước phim (Reels), bấm Tạo, chọn video.','f',['reels','upload']),
 numI('Không thêm nhạc. Bấm Tiếp.','f',['nomusic','next']),
 numI('Bấm vào ô mô tả, dán Mô tả Facebook (mục 2.3).','f',['paste']),
 numI('Bấm Chỉnh sửa ảnh bìa, chọn khung cuối video (hoặc Tải lên ảnh bìa).','f',['cover']),
 numI('Quyền riêng tư: chọn Công khai.','f',['public']),
 numI('Bấm Chia sẻ ngay.','f',['share']),
 numI('Bình luận nội dung mục 2.4, bấm giữ bình luận, chọn Ghim.','f',['comment','pin']),
 H2('Bảng biểu tượng'),
 legend(),
 H1('4. Giờ đăng tốt nhất'),
 tbl(['Khung giờ','Lý do','Ưu tiên'],[
  ['6:30 – 7:30 sáng','Chủ doanh nghiệp xem điện thoại trước giờ làm','★★★'],
  ['11:30 – 12:30 trưa','Giờ nghỉ trưa, lướt nội dung ngắn','★★'],
  ['20:00 – 21:00 tối','Thời gian rảnh, xem lâu và dễ lưu video','★★★']],[2400,4826,1800]),
 sp(),
 bul('Đăng cả 3 nền tảng trong cùng một ngày; TikTok đăng trước, YouTube và Facebook cách nhau 1–2 giờ.'),
 bul('Sau 2 tuần, mở mục Phân tích của từng nền tảng để xem giờ người theo dõi hoạt động nhiều nhất và đăng theo giờ đó.'),

 H1('5. Kỹ thuật để lên xu hướng'),
 tbl(['Việc cần làm','Vì sao hiệu quả'],[
  ['Trả lời mọi bình luận trong 1 giờ đầu','Tương tác sớm giúp nền tảng đẩy video tới nhiều người hơn'],
  ['Đăng đều 3–5 video mỗi tuần, cùng giờ','Thuật toán ưu tiên kênh đăng ổn định'],
  ['Mỗi video hẹn tập sau','Người xem bấm Theo dõi để không bỏ lỡ'],
  ['Kêu gọi lưu video khi có công thức, con số','Lượt lưu là tín hiệu mạnh nhất với thuật toán'],
  ['Không xóa video ít lượt xem','Xóa nhiều làm kênh bị giảm phân phối'],
  ['Không đăng lại video y hệt','Bị coi là nội dung trùng lặp; muốn đăng lại hãy đổi câu mở đầu'],
  ['Không dùng hashtag lạc đề hoặc quá 6 hashtag','Nền tảng khó xác định đúng người xem']],[3600,5426]),

 H1('6. Theo dõi sau khi đăng'),
 bul([B('Tỷ lệ xem hết: '),'trên 40% là tốt. Thấp hơn thì câu mở đầu chưa đủ hấp dẫn.']),
 bul([B('Thời điểm người xem rời đi: '),'xem trong Phân tích để biết đoạn nào cần rút gọn.']),
 bul([B('Lượt lưu và chia sẻ: '),'càng cao, video càng được đẩy lâu.']),
 bul('Gửi số liệu sau 48 giờ để rút kinh nghiệm cho video tiếp theo.'),

 H1('7. Danh sách kiểm tra trước khi bấm Đăng'),
 ...['Đã chọn ảnh bìa có tiêu đề rõ','Đã dán mô tả và hashtag','Đã ghi nguồn nhạc (dòng Music: ...)','TikTok: đã bật nhãn Nội dung do AI tạo','Không thêm nhạc của nền tảng','Đăng đúng khung giờ vàng','Sau khi đăng: ghim bình luận và trả lời bình luận trong 1 giờ đầu'].map(t=>bul('☐  '+t)),
];
const doc=new Document({
 styles:{default:{document:{run:{font:F,size:22}}},paragraphStyles:[
  {id:'Heading1',name:'Heading 1',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:F,size:30,bold:true,color:'B35C00'},paragraph:{spacing:{before:280,after:120},keepNext:true,outlineLevel:0}},
  {id:'Heading2',name:'Heading 2',basedOn:'Normal',next:'Normal',quickFormat:true,run:{font:F,size:25,bold:true,color:'1F2533'},paragraph:{spacing:{before:180,after:100},keepNext:true,outlineLevel:1}}]},
 numbering:{config:[{reference:'b',levels:[{level:0,format:LevelFormat.BULLET,text:'•',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:280}}}}]},
  ...['t','y','f'].map(r=>({reference:r,levels:[{level:0,format:LevelFormat.DECIMAL,text:'%1.',alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left:540,hanging:320}}}}]}))]},
 sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1200,bottom:1200,left:1440,right:1440}}},children}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync('Huong-dan-dang_Tap2_Thu-hoi-cong-no.docx',b));
