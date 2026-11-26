#!/bin/bash
# Ráp video 1 tập – chạy trong thư mục tập (đã có voice.wav, dur.json, words.json, scenes.json)
set -e
S=$(dirname "$(readlink -f "$0")")
N=$(python3 -c "import json;print(round(sum(json.load(open('dur.json')))*30))")
T=$(python3 -c "import json;print(sum(json.load(open('dur.json'))))")

# Xóa khung cũ của lần dựng trước (khung cũ lệch số sẽ chèn vào video gây nhảy hình)
find fr0 fr1 fr2 fr3 all -maxdepth 1 \( -name "*.jpg" -o -type l \) -delete 2>/dev/null || true  # thư mục chưa có thì bỏ qua (lỗi cũ: dựng tập mới bị dừng)
# 1) Chụp khung hình song song 4 phần
q=$((N/4)); python3 $S/cap.py 0 $q 0 & python3 $S/cap.py $q $((2*q)) 1 & python3 $S/cap.py $((2*q)) $((3*q)) 2 & python3 $S/cap.py $((3*q)) $N 3 & wait
mkdir -p all && for d in fr0 fr1 fr2 fr3; do for f in $d/*.jpg; do ln -sf ../$f all/$(basename $f); done; done
ffmpeg -y -loglevel error -framerate 30 -i all/%05d.jpg -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p vid.mp4

# 2) Nhạc Wholesome theo đoạn: 3 bản lọc (đóng tiếng / mở dần / đầy đủ) → mkscore.py trộn theo cảnh
for p in "lo:lowpass=f=650" "mid:lowpass=f=2600" "full:anull"; do
  n=${p%%:*}; f=${p#*:}
  ffmpeg -y -loglevel error -i $S/music/Wholesome.mp3 -af "$f" -ac 2 -ar 44100 -t $T -f f32le w_$n.raw
done
python3 $S/mkscore.py            # → score.wav

# 3) Trộn giọng + nhạc (đã kiểm chứng Tập 3: −14 LUFS, nhạc cuối ≈ −25 dB như Tập 2)
ffmpeg -y -loglevel error -i voice_dry.wav -i score.wav -filter_complex \
 "[0:a]aresample=44100,pan=stereo|c0=c0|c1=c0,highpass=f=70,acompressor=threshold=0.1:ratio=2.5:attack=8:release=120,asplit=2[v][sc];[1:a]volume=0.21[m];[m][sc]sidechaincompress=threshold=0.02:ratio=5:attack=25:release=400[d];[v][d]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11" \
 -ar 48000 -c:a aac -b:a 192k mix.m4a

# 4) Ráp thành phẩm (không còn ảnh bìa từ 24/11/2026 – anh Bình bỏ)
ffmpeg -y -loglevel error -i vid.mp4 -i mix.m4a -map 0:v -map 1:a -t $T -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart final.mp4
echo "Xong: final.mp4"
