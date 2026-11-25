#!/bin/bash
# Một lệnh cho mỗi bước, chỉ in vài dòng kết luận (tiết kiệm token).
# Chạy trong tools/:  bash studio/lam_tap.sh tapNN kiemtra|nen|dung|day
T=$1; B=$2; cd "$(dirname "$0")/.." || exit 1
case $B in
 kiemtra) # sau khi viết script2.json: kiểm trùng + từ đọc sai
  python3 studio/check_trung.py $T | grep -E "đã có|đã mở|KẾT"; python3 studio/check_tu.py $T | grep -E "RỦI RO|KẾT";;
 nen) # ngay khi gửi kịch bản cho anh: giọng + nghe lại + kiểm hình, chạy nền, log /tmp/$T.log
  (cd $T && python3 scenes.py >/dev/null && python3 ../studio/check_de.py | tail -3; python3 ../studio/tts_vn.py >/dev/null 2>&1; python3 ../studio/qa.py 2>&1 | grep -E "^SAI|lệch|Độ dài") > /tmp/$T.log 2>&1 &
  echo "Đang chạy nền, xem: cat /tmp/$T.log";;
 dung) # sau khi anh duyệt: dựng + kiểm tra cuối
  cd $T && python3 ../studio/check_de.py | tail -1 && bash ../studio/make.sh >/dev/null 2>&1; python3 ../studio/qa.py 2>&1 | grep -E "^SAI|Độ dài|KẾT"; echo "Xem 1 lần: tools/$T/qa_sheet.jpg";;
 day) # đẩy video lên kho công khai, in link
  N=$(echo $T | sed 's/tap0*//'); cd .. && cp tools/$T/final.mp4 video/Tap$N.mp4 && git add --sparse video/Tap$N.mp4 && git add tools/$T/{script2.json,scenes.py,scenes.json,dur.json,words.json,page.html} && git -c user.name=Claude -c user.email=noreply@anthropic.com commit -qm "Tập $N (bản duyệt)" && git push -q origin HEAD 2>&1 | tail -1
  H=$(git rev-parse HEAD); sleep 4; U=https://raw.githubusercontent.com/dongbinh1282-collab/goc-nhin-kinh-doanh-media/$H/video/Tap$N.mp4; echo "$U $(curl -sL -o /dev/null -w '%{http_code}' $U)";;
 *) echo "Dùng: bash studio/lam_tap.sh tapNN kiemtra|nen|dung|day";;
esac
