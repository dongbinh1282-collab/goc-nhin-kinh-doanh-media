#!/bin/bash
# Ráp video 1 tập – chạy trong thư mục tập (đã có voice.wav, dur.json, words.json, scenes.json)
set -e
S=$(dirname "$(readlink -f "$0")")
N=$(python3 -c "import json;print(round(sum(json.load(open('dur.json')))*30))")
T=$(python3 -c "import json;print(sum(json.load(open('dur.json'))))")

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

# 4) Ảnh bìa 1 giây cuối (cover.jpg 1080x1920) rồi ráp thành phẩm
ffmpeg -y -loglevel error -loop 1 -framerate 30 -i cover.jpg -t 1 -vf format=yuv420p -c:v libx264 -crf 18 tail.mp4
ffmpeg -y -loglevel error -i vid.mp4 -i tail.mp4 -i mix.m4a -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[v];[2:a]apad[a]" \
 -map "[v]" -map "[a]" -t $(python3 -c "print($T+1.05)") -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart final.mp4
echo "Xong: final.mp4"
