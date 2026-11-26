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
- Không đọc lại kịch bản cũ. Sau khi viết `script2.json`, chạy `python3 studio/check_lap.py tapNN` (trong `tools/`) để kiểm tra cụm từ trùng với mọi tập cũ. Kết quả phải là "AN TOÀN (0 trùng)"; nếu có trùng thì sửa câu đó. Câu mở, tiêu đề, công thức và ví dụ không được lặp nguyên văn.
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

## 13. Mục tiêu 10 phút (25/11/2026, bài học tập 12: 21 phút do 2 vòng đọc lại giọng + 1 lần dựng lại)
- Tạo giọng + qa.py NGAY KHI VIẾT KỊCH BẢN, trước khi gửi anh duyệt. Kịch bản gửi anh = bản đã đọc đúng 100%. Anh sửa câu nào chỉ tạo lại câu đó (có cache).
- Viết scenes.py cũng trước khi gửi duyệt; chạy check_de.py + `cap.py pv` 3–4 khung xem trước. Nhãn ≥ 42 px, cảnh PHẦN SAU để chữ trong pre().
- Sau khi anh duyệt chỉ còn: make.sh (2') → qa.py + xem qa_sheet (2') → đẩy kho + lên lịch (1').
- CHỐT (anh Bình 25/11/2026): gửi kịch bản cho anh NGAY sau check_trung + check_tu, đồng thời chạy NỀN giọng đọc + qa.py + scenes/check_de. Anh duyệt xong chỉ còn make.sh → qa → giao (~5–7 phút). Câu anh sửa thì tạo lại riêng câu đó.

## 14. Tiết kiệm token (anh Bình 25/11/2026) – BẮT BUỘC
1. Lên lịch Metricool: KHÔNG tải cả tháng. Ngày đăng = ngày sau tập trước (bảng dưới), getScheduledPosts chỉ tra đúng 1 ngày nếu cần.
2. Chỉ dùng `bash studio/lam_tap.sh tapNN kiemtra|nen|dung|day`. Không cat cả file, không in toàn bộ qa.py.
3. Xem qa_sheet.jpg MỘT lần, sau khi các bước dò đã ĐẠT.
4. Trả lời anh ngắn: kết quả + thời gian + việc cần duyệt.
5. Mở cửa sổ mới sau khoảng 3 tập.
Lịch đã lên (19:30): Tập 10 → 05/12/2026 · Tập 11 → 06/12 · Tập 12 → 07/12. Tập 13 → 08/12 (đã lên lịch). Tập 14 → 09/12 (tiếp theo +1 ngày). Chủ đề tập 14: cách định giá lại sản phẩm có biên lợi nhuận gộp thấp mà không mất khách hàng. Tập mới copy page.html + scenes.py từ tap13 (mẫu chuẩn mới).

## 15. Rà chuyên môn TRƯỚC khi gửi kịch bản (anh Bình 25/11/2026 – không để anh phải bảo "kiểm tra lại")
Trước khi gửi, tự rà từng câu theo bảng này, sửa xong mới gửi:
1. Thuật ngữ kế toán đúng chỗ: chiết khấu cho khách trừ vào DOANH THU; vận chuyển giao khách, bảo hành, hoa hồng là CHI PHÍ BÁN HÀNG, không nằm trong giá vốn; giá vốn = giá nhập + vận chuyển về kho + hao hụt.
2. Phân biệt % và tiền: biên (%) có thể giảm trong khi lợi nhuận (tiền) vẫn tăng – câu nêu nỗi đau phải nói đúng đại lượng.
3. Mỗi lời khuyên có lý do/điều kiện kèm theo (vd giữ sản phẩm biên thấp VÌ tổng lợi nhuận gộp bằng tiền lớn).
4. Không có "lãi" kể cả "tiền lãi gộp"; không viết "nhưng biên lợi nhuận" (máy đọc sai).
5. Đọc lại cả bài một lượt như người xem: câu nào hiểu được hai nghĩa thì viết lại.

## 16. Hình vẽ phong phú (anh Bình 25/11/2026)
- Mỗi câu đọc một cảnh riêng (tách nhóm trong script2.json), không gộp 2–3 câu vào một cảnh.
- Cảnh mở đầu KHÔNG dùng lại hình người ôm đầu; mỗi tập mở bằng hình minh họa đúng nỗi đau (biểu đồ, đồ vật, con số).
- Mỗi cảnh có hình vẽ minh họa riêng (biểu đồ, xe, kính lúp, đồng hồ đo, bục xếp hạng, nhãn giá…), phần lớn nét vẽ dần, không chỉ chữ trong ô.
- Không lặp bộ hình của tập trước.
- Khung ĐẦU TIÊN phải hiện đủ thông tin nổi bật ngay (dùng pre() cho biểu đồ + chữ chính của cảnh mở đầu), không để khung đầu chỉ có trục/nét trống – anh Bình 25/11/2026.
- Chữ chạy phải ngắt đúng cụm nghĩa, không tách đôi từ ghép (lợi | nhuận, sản | phẩm): dùng page.html của tap13 trở đi (có GLUE) + studio/punct.py (lam_tap.sh dung tự chạy). Gặp từ ghép bị tách thì thêm vào GLUE.
- Kiểm chữ chạy trước khi dựng: (cd tapNN && python3 ../studio/punct.py && node ../studio/check_phude.js) – mỗi dòng 4–10 từ, không tách từ ghép, không vắt qua 2 câu.
- Nhảy hình: make.sh xóa khung cũ trước khi chụp; lam_tap.sh dung in 'Nhảy hình: N chỗ' – phải bằng 0 mới giao (anh Bình 25/11/2026).
- Khung đầu giống Tập 1–2 (ảnh lưới TikTok anh gửi 25/11): tiêu đề nỗi đau chữ to + ô chữ phụ hiện ngay bằng pre(); bút bắt đầu vẽ hình minh họa ngay từ giây đầu và vẽ gần hết cảnh, không để hình đứng yên.

## 11. Quy tắc tối ưu (đánh giá từ lượt chạy thử 26/11/2026)

Đo trên máy hiện tại (2 nhân). Một tập 60 giây, câu đã có cache: lồng giọng ~2 giây, dựng ~105 giây, kiểm tra ~90 giây, tổng ~3,5 phút. Câu mới phải tạo lại làm tăng thêm khoảng 15–20 giây cho mỗi câu.

Đã hiệu quả, giữ lại:
- Cache giọng đọc dùng chung (`tools/studio/tts_cache`). Câu lặp lại chỉ tốn vài giây thay vì ~100 giây.
- Kiểm tra lặp ý bằng `check_lap.py` thay cho đọc lại kịch bản cũ. Tiết kiệm token, không đổi chất lượng.

Không hiệu quả, không làm:
- Giảm chất lượng ảnh chụp (JPEG 90 thay 96): thời gian gần như không đổi.
- Chỉ chụp khung khi hình thay đổi: chữ chạy từng từ nên hầu hết khung đều thay đổi.

Quy tắc khi làm tập mới:
1. Mở phiên mới: chạy `tools/setup.sh` ở nền ngay (khoảng 90 giây).
2. Viết kịch bản, rồi chạy `lam_tap.sh tapNN kiemtra`. Không đọc lại kịch bản cũ.
3. Câu nào máy đọc nhận diện sai sau 6 lần thử thì viết lại câu, không lưu cache câu sai (đã được chặn tự động).
4. Dựng bằng `make.sh`, kiểm tra bằng `qa.py`. Chỉ xem `qa_sheet.jpg` một lần. Nếu chỉ một vài câu lỗi, sửa câu đó; không cần dựng lại toàn bộ nếu không cần.
5. Sau mỗi tập, ghi một dòng số liệu (thời gian từng bước, số câu phải tạo lại) để theo dõi.
