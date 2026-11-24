#!/bin/bash
# Cài môi trường làm video "Góc nhìn kinh doanh" ở cửa sổ mới – chạy NGẦM ngay đầu phiên:
#   nohup bash tools/setup.sh > /tmp/setup.log 2>&1 &
# Trong lúc chờ (2–5 phút), viết kịch bản + scenes.py như bình thường.
# Xong khi /tmp/setup.done tồn tại.
set -e
rm -f /tmp/setup.done
export VIENEU_DIR=${VIENEU_DIR:-/home/claude/vn/v3t}

# 1) Thư viện Python + ffmpeg (song song)
pip install -q --break-system-packages vieneu faster-whisper soundfile playwright pillow &
command -v ffmpeg >/dev/null || (apt-get update -qq && apt-get install -y -qq ffmpeg) &
wait

# 2) Model giọng đọc VieNeu v3 Turbo + whisper small (song song)
python3 - <<'EOF' &
import os
from huggingface_hub import snapshot_download
snapshot_download('pnnbao-ump/VieNeu-TTS-v3-Turbo', local_dir=os.environ['VIENEU_DIR'])
EOF
python3 -c "from faster_whisper import WhisperModel; WhisperModel('small',compute_type='int8')" &
wait

# 3) Sửa lỗi onnxruntime "External data path escapes model directory": thay symlink cache bằng file thật
find /root/.cache/huggingface/hub -type l | while read l; do t=$(readlink -f "$l"); rm "$l"; cp "$t" "$l"; done

# 4) Trình duyệt + font
[ -x /usr/bin/google-chrome ] || python3 -m playwright install --with-deps chromium
[ -f "/usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf" ] || echo "THIẾU FONT Montserrat – tải từ google/fonts"

# 5) Nạp thử giọng Đức Trí
cd "$(dirname "$(readlink -f "$0")")/studio" && python3 -c "from vn import load; t=load(); t.get_preset_voice('Đức Trí'); print('giọng OK')"
touch /tmp/setup.done && echo "SETUP XONG"
