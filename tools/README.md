# Công cụ làm video kênh "Góc nhìn kinh doanh"

Kênh cá nhân của anh Bình (TikTok · YouTube Shorts · Facebook Reels – Fanpage DNB Việt Nam).
Kiểu video: cây bút vẽ minh họa trên khung giấy kem, giọng đọc VieNeu "Đức Trí", nhạc "Wholesome".

## Cấu trúc
```
studio/            bộ máy dùng chung cho mọi tập
  page.html        khung hình 1080x1920 (nhãn, khung giấy, tiêu đề, phụ đề chạy theo từ) – BẢN VÙNG AN TOÀN
  cap.py           chụp khung hình bằng Playwright (chạy song song 4 phần)
  tts_vn.py        đọc lời (VieNeu Đức Trí) + whisper canh thời điểm từng từ → dur.json, words.json, voice.wav
  vn.py            vá tải model VieNeu (biến môi trường VIENEU_DIR = thư mục model v3 Turbo)
  mkscore.py       dựng nhạc theo đoạn từ 3 bản Wholesome (lowpass 650 / 2600 / đầy đủ) → score.wav
  cover.html       mẫu ảnh bìa 1080x1920 (chữ trong vùng 3:4 giữa)
  build_guide.js   (KHÔNG DÙNG NỮA từ 24/11/2026 – bỏ file Word hướng dẫn đăng)
  make.sh          các lệnh ffmpeg ráp video
  music/Wholesome.mp3  Kevin MacLeod, CC BY 4.0 (bắt buộc ghi nguồn khi đăng)
tap01/  Doanh thu tăng mà không có tiền?  (script2.json, scenes.py, scenes.json, dur.json, words.json)
tap02/  Thu hồi công nợ mà không mất khách
tap03/  Hàng tồn kho đang giam vốn (đăng 26/11/2026)
```
Video thành phẩm KHÔNG lưu ở đây – nằm ở kho công khai `goc-nhin-kinh-doanh-media` (link cho Metricool).

## Quy trình 1 tập
1. Viết `script2.json` (lời đọc chia cảnh) + `scenes.py` → `python3 scenes.py` ra `scenes.json`.
2. `python3 ../studio/tts_vn.py` (chạy trong thư mục tập) → voice_dry.wav, dur.json, words.json. Mỗi câu đọc tối đa 6 lần, whisper nghe lại, chọn bản ít sai chữ nhất. Tránh chữ cái rời (A, B, C) và từ tiếng Anh trong lời đọc.
3. Xem thử: `python3 ../studio/cap.py pv 3 20 40` → pv_*.jpg.
4. Chụp đủ khung (N = tổng dur × 30): `cap.py 0 a 0 & cap.py a b 1 & ...` → fr0..fr3.
5. Nhạc + ráp: xem `studio/make.sh`.
6. Không làm ảnh bìa và file Word hướng dẫn đăng (anh Bình bỏ từ 24/11/2026).
7. Đẩy mp4 lên kho media → lên lịch Metricool (blogId 8047642) TikTok + YouTube short + Facebook REEL, 20:00.

## Chuẩn bắt buộc (anh Bình chốt 23/11/2026)
- Video dọc 9:16 dùng chung 3 nền tảng; hết chuỗi 5–6 tập gộp 1 video ngang 16:9 8–10 phút.
- Nhãn "GÓC NHÌN KINH DOANH" in hoa nền vàng cam; chỉ cây bút vẽ (không tay); không tiếng bút, không tiếng chuyển cảnh; chữ chạy nhiều màu.
- VÙNG AN TOÀN: giữ khung giấy rộng 1080 như cũ, nhóm hình vẽ + bút trong `translate(97,50) scale(0.82)`; tiêu đề 62px, phụ đề 54px rộng 860px – hình và chữ không sát hai mép. Không co cả khung hình.
- Lời đọc đủ chủ ngữ – vị ngữ, văn phong học thức, lịch sự; kết "Phần sau sẽ là…", ngắt nghỉ, "Hẹn gặp lại các bạn." (không cảm ơn).
- Dài 50–65 giây; giọng ~4 tiếng/giây; loudness −14 LUFS.

## Cài đặt khi mở phiên mới (không mất thời gian chờ)
- Việc ĐẦU TIÊN: `nohup bash tools/setup.sh > /tmp/setup.log 2>&1 &` (chạy ngầm 2–5 phút: thư viện, model VieNeu, whisper, sửa symlink, nạp thử giọng).
- Trong lúc chờ: viết `script2.json`, `scenes.py`, `cover.html`, sửa tiêu đề `page.html`.
- Chỉ chạy `tts_vn.py` khi đã có `/tmp/setup.done`.
