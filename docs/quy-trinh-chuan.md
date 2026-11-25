# Quy trình chuẩn kênh "Góc nhìn kinh doanh"

Kênh cá nhân của anh Bình. Không ghi tên anh trong video. Mỗi tập chạy đủ các bước dưới đây trước khi giao anh duyệt.

## 1. Đầu vào
- Chủ đề tập: lấy từ câu hẹn "Phần sau sẽ là …" của tập trước.
- Mỗi chuỗi 5–6 tập: viết kịch bản cả chuỗi một lần, dựng lần lượt.

## 2. Định dạng
- Video dọc 1080×1920, 30 fps, dài 50–65 giây. Dùng chung TikTok, YouTube Shorts, Facebook Reels.
- Hết chuỗi: gộp thành video ngang 16:9, dài 8–10 phút, cho YouTube thường.

## 3. Kịch bản
- Đóng vai góc nhìn chủ doanh nghiệp. Giải quyết nỗi đau thật, có chiều sâu kiến thức, có công thức hoặc con số để người xem lưu lại.
- Mỗi câu có đủ chủ ngữ và vị ngữ. Văn phong học thức, lịch sự. Không suồng sã, không dạy đời, không kêu gọi "comment cho mình biết", không cảm ơn ở câu kết.
- Cấu trúc: câu hỏi nỗi đau → nguyên nhân → các ý đánh số ("Nguyên tắc thứ nhất là…") → giải pháp hoặc công thức → "Phần sau sẽ là …" (nghỉ ~0,9 giây) → "Hẹn gặp lại các bạn."

## 4. Giọng đọc
- VieNeu-TTS v3 Turbo, giọng "Đức Trí". Tốc độ khoảng 4 tiếng/giây.
- Nghỉ giữa câu: thường 0,16 giây, sau câu hỏi 0,3 giây, sau câu chốt 0,4 giây.
- Kiểm tra phát âm bằng nhận dạng lại. Câu đọc sai thì đổi từ rồi tạo lại.

## 5. Hình
- Nền đen. Nhãn trên "GÓC NHÌN KINH DOANH" in hoa, nền vàng cam.
- Khung giấy kem 1080 px giữ nguyên kích thước. Hình vẽ và chữ nằm trong vùng an toàn, cách mép trái và mép phải tối thiểu 100 px.
- Chỉ có cây bút vẽ, không có tay. Hình minh họa nét đen, màu phẳng, to.
- Phụ đề: chữ trắng đậm viền đen, ngắt theo cụm nghĩa, từ khóa có màu.
- Chuẩn chi tiết (bút không đè chữ, chữ ≥ 40 px, hình to lấp khung, phụ đề ≥ 4 từ/cụm, khung pre): xem mục "Chuẩn hình bắt buộc" trong `tools/README.md`. Tập mẫu: `tools/tap08`.

## 6. Nhạc
- "Wholesome" – Kevin MacLeod, CC BY 4.0. Ghi nguồn khi đăng.
- Nhạc đóng lúc nêu vấn đề, mở dần, mở đầy đủ ở phần giải pháp.
- Không tiếng bút, không tiếng chuyển cảnh, không dùng nhạc tự soạn.

## 7. Bàn giao mỗi tập
1. Video dọc: `video/Tap<n>.mp4` (không làm ảnh bìa từ 24/11/2026).
3. Không làm file Word hướng dẫn đăng (anh Bình bỏ 24/11/2026). Khi lên lịch Metricool, Claude điền thẳng mô tả, tiêu đề Shorts tối đa 100 ký tự, tối đa 6 hashtag, dòng ghi nguồn nhạc, nhãn "Nội dung do AI tạo" trên TikTok.
4. Kiểm tra trước khi giao: khung hình rải đều, loudness khoảng -14 LUFS, tốc độ đọc đúng, không chữ sát mép.

## 8. Đăng
- Video đưa lên kho GitHub công khai để Metricool lấy link.
- Chỉ lên lịch sau khi anh Bình duyệt.

## 9. Quy tắc viết kịch bản (anh Bình yêu cầu, 24/11/2026)
- Trước khi viết, đọc lại toàn bộ `tools/tap01`–`tap08` (script2.json) để biết những gì đã dạy. Không lặp câu mở, tiêu đề, công thức hay ví dụ đã có.
- Chủ đề tập mới phải là lời hẹn "Phần sau sẽ là…" của tập trước. Không tự đổi chủ đề.
- Viết với vai hội đồng chuyên gia: chuyên gia tài chính kiểm tra số liệu và công thức, biên tập viên kiểm tra câu mở và độ trùng lặp, người giữ chuẩn kênh kiểm tra độ dài, văn phong và câu kết.
- Mọi con số trong ví dụ phải ghi là ví dụ minh họa, không trình bày như số liệu thống kê.

## 10. Kiểm tra bắt buộc trước khi giao – chống làm ẩu (anh Bình yêu cầu, 24/11/2026)
Bài học tập 9: giao video khi chưa nghe lại lời đọc và chưa xem hết khung hình → lời đọc sai, 3 giây đầu trống, chữ tràn, hình không khớp lời. Từ nay KHÔNG được giao nếu chưa qua đủ các bước sau:
1. Chạy `python3 ../studio/qa.py` trong thư mục tập. Mọi câu phải "OK" (whisper medium nghe lại). Câu "SAI" → đổi từ (vd "dồn"→"xếp", "mùa Tết"→"dịp Tết", "thanh toán"→"trả tiền", tránh "thưởng" cạnh "thường"), xóa cache câu đó, tạo lại giọng, chạy lại qa.py.
2. Mở `qa_sheet.jpg` (21 khung, mỗi 3 giây) và xem HẾT. Đạt khi:
   - 3 giây đầu đã có hình đầy đủ, rõ chủ đề (khung, bảng, lịch dùng `pre(...)` để hiện ngay).
   - Không chữ tràn khỏi ô, không chữ bị cắt ở mép dưới khung giấy (toạ độ y của chữ ≤ 610), chữ ≥ 40 px.
   - Mọi con số, nhãn trên hình khớp với lời đọc và có nghĩa (không để số mặc định như "30" của hàm `cal`).
   - Không cảnh nào đứng yên quá 5 giây: câu ví dụ dài phải có hình mới xuất hiện theo.
   - Không ô, khung nào để trống.
3. Khi giao, báo kèm kết quả: số câu OK, độ dài, loudness, đã xem 21 khung, và thời gian làm.

## 11. Công cụ kiểm tra tự động bắt buộc (25/11/2026)
- Kịch bản: `python3 studio/check_trung.py tapNN` (trong tools/) phải ĐẠT trước khi gửi anh duyệt.
- Hình: sau `python3 scenes.py`, chạy `python3 ../studio/check_de.py` trong thư mục tập, phải ĐẠT (0 chữ đè lên khung, 0 chữ sát đáy > 615) trước khi dựng video. Lỗi tập 11: chữ "Ghi vào hợp đồng" đè lên khung giấy.

## 12. Quy trình nhanh – mục tiêu ≤ 15 phút sau khi anh duyệt kịch bản (25/11/2026)
Bài học tập 11 (48 phút): 4 vòng tạo lại giọng vì từ đọc sai (~20 phút), dựng video 3 lần vì lỗi hình phát hiện muộn (~6 phút), tạo giọng chạy tuần tự (~9 phút).
1. Trước khi gửi kịch bản: chạy `python3 studio/check_trung.py tapNN` VÀ `python3 studio/check_tu.py tapNN`, cả hai ĐẠT. Kịch bản gửi anh đã là bản đọc được, không đổi từ sau khi duyệt.
2. Ngay khi anh duyệt: chạy giọng NỀN `nohup python3 ../studio/tts_vn.py > /tmp/tts.log 2>&1 &`.
3. Trong lúc chờ giọng: viết scenes.py, chạy `scenes.py` + `../studio/check_de.py` tới ĐẠT, xem 1–2 khung `cap.py pv`.
4. Giọng xong → `qa.py` một lần → `make.sh` một lần → `qa.py` → xem qa_sheet → giao.
5. Câu SAI mới: thêm từ đó vào RUI_RO trong check_tu.py để tập sau không lặp.
