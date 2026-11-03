# Methodology

## Quy trình

| Bước | Notebook | Đầu vào | Đầu ra |
|---|---|---|---|
| 1. Rút gọn dữ liệu | `00_reduce_raw` | `data/raw/games.csv` | `data/processed/games_reduced.csv` |
| 2. Audit chất lượng và làm sạch | `01_data_quality` | `games_reduced.csv` | `data/processed/games_cleaned.csv`, `reports/games_data_quality_audit.xlsx`, `reports/cleaning_log.csv` |
| 3. Phân tích khám phá theo câu hỏi nghiên cứu | `02_eda` | `games_cleaned.csv` | Biểu đồ, bảng và câu trả lời cho RQ1, RQ2, RQ5 |
| 4. Mô hình (không bắt buộc) | `04_modeling` | `games_cleaned.csv` | Kết quả mô hình dự đoán Peak CCU |

Chỉ notebook `00_reduce_raw` đọc file gốc. Các notebook sau chỉ dùng dữ liệu đã xử lý.

## Phương pháp phân tích

- **Tương quan Spearman** thay cho Pearson, vì các biến (Peak CCU, số đánh giá, số người sở hữu) lệch rất mạnh và có nhiều giá trị 0. Pearson bị vài game rất lớn chi phối.
- **Trung vị và tỷ lệ %** thay cho trung bình khi so sánh các nhóm, vì trung bình bị outlier kéo lệch. Ví dụ dùng "% game có Peak CCU > 0" thay cho Peak CCU trung bình.
- **Tỷ lệ đánh giá tích cực** = Positive / (Positive + Negative) × 100, chỉ tính cho game có từ 10 đánh giá, để tránh tỷ lệ không đáng tin ở game quá ít đánh giá. Dùng chỉ số này thay cho `User score` (gần như trống).
- **Số người sở hữu**: lấy điểm giữa của khoảng `Estimated owners`.
- **Nhóm giá**: Miễn phí (0), Thấp (dưới 5 USD), Trung bình (5 đến dưới 15 USD), Cao (từ 15 USD). Mốc 5 USD được chọn vì khoảng 74% game có giá dưới 5 USD.
- **Phân tích theo thể loại**: một game có nhiều thể loại nên được tính vào từng thể loại; bỏ nhãn "Free To Play" (trùng với giá) và "Early Access" (trạng thái phát hành); chỉ xét 12 thể loại nhiều game nhất.
- **Kiểm tra trong từng nhóm**: mối liên hệ giữa giá với độ phổ biến và đánh giá được kiểm tra lại trong từng thể loại, để tránh kết luận sai do khác biệt giữa các thể loại.

## Nguyên tắc làm sạch dữ liệu

- Làm trên bản sao, không ghi đè file gốc hay file rút gọn.
- Mọi thay đổi đều ghi vào cleaning log; chỉ sửa khi có căn cứ.
- Số 0 có nghĩa "chưa có điểm" (Metacritic score, User score) được đổi thành giá trị trống.
- Outlier là giá trị thật (ví dụ Counter-Strike 2 có hơn 1 triệu người chơi đồng thời) nên được giữ nguyên.
- Mâu thuẫn không đủ căn cứ để sửa (ví dụ số đánh giá lớn hơn số người sở hữu ước tính) chỉ được ghi log.

## Giả định

- Dữ liệu đại diện cho các game được liệt kê trên Steam tại thời điểm thu thập.
- `Estimated owners` = "0 - 0" là game chưa có người dùng: không game nào trong nhóm này có người chơi, đánh giá hay thời gian chơi.
- Ngày tham chiếu để xác định game chưa phát hành là 03/11/2026.

## Kiểm tra kết quả

- Sau khi làm sạch: so sánh trước/sau về số dòng, giá trị thiếu, trùng lặp, định dạng và các lỗi đã sửa (notebook 01, mục B8).
- Mọi con số trong phần nhận xét được đối chiếu với kết quả tính trong notebook.
- Mô hình (nếu có): chia train/test, so sánh với mô hình baseline, kiểm tra chênh lệch train/test để phát hiện overfitting.
