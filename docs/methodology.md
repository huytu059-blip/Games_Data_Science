# Methodology

## Quy trình

| Bước | Notebook | Đầu vào | Đầu ra |
|---|---|---|---|
| 1. Rút gọn dữ liệu | `00_reduce_raw` | `data/raw/games.csv` | `data/processed/games_reduced.csv` |
| 2. Audit chất lượng và làm sạch | `01_data_quality` | `games_reduced.csv` | `data/processed/games_cleaned.csv`, `reports/games_data_quality_audit.xlsx`, `reports/cleaning_log.csv` |
<<<<<<< HEAD
| 3. Phân tích khám phá theo câu hỏi nghiên cứu | `02_eda` | `games_cleaned.csv` | Biểu đồ, bảng và câu trả lời cho RQ1, RQ2, RQ5 |
| 4. Mô hình (không bắt buộc) | `04_modeling` | `games_cleaned.csv` | Kết quả mô hình dự đoán Peak CCU |
=======
| 3. Phân tích khám phá theo câu hỏi nghiên cứu | `02_eda`, `02b_eda_rq3_rq4` | `games_cleaned.csv` | Biểu đồ, bảng và câu trả lời cho cả 5 câu hỏi |
| 4. Chuẩn bị dữ liệu cho mô hình | `03_ml_readiness` | `games_cleaned.csv` | `data/processed/games_features.csv` |
| 5. Mô hình | `04_modeling` | `games_cleaned.csv`, `games_features.csv` | Hồi quy, phân loại, `models/mo_hinh.joblib` |
| 6. Đánh giá mô hình | `05_model_evaluation` | `games_features.csv`, mô hình đã lưu | So sánh với baseline, kiểm định chéo, đặc trưng quan trọng |
| 7. Thống kê suy luận | `06_statistical_inference` | `games_features.csv` | Xác suất, khoảng tin cậy, kiểm định, phân tích kiểu A/B |
| 8. Big data, đạo đức, thiên lệch | `07_big_data_ethics_bias` | `games_reduced.csv`, `games_cleaned.csv`, `games_features.csv`, mô hình đã lưu | Đánh giá thiên lệch của dữ liệu và mô hình |
>>>>>>> ef668bcffbfa37c916799aad799b1c884027c2ad

Chỉ notebook `00_reduce_raw` đọc file gốc. Các notebook sau chỉ dùng dữ liệu đã xử lý.

## Phương pháp phân tích

- **Tương quan Spearman** thay cho Pearson, vì các biến (Peak CCU, số đánh giá, số người sở hữu) lệch rất mạnh và có nhiều giá trị 0. Pearson bị vài game rất lớn chi phối.
- **Trung vị và tỷ lệ %** thay cho trung bình khi so sánh các nhóm, vì trung bình bị outlier kéo lệch. Ví dụ dùng "% game có Peak CCU > 0" thay cho Peak CCU trung bình.
- **Tỷ lệ đánh giá tích cực** = Positive / (Positive + Negative) × 100, chỉ tính cho game có từ 10 đánh giá, để tránh tỷ lệ không đáng tin ở game quá ít đánh giá. Dùng chỉ số này thay cho `User score` (gần như trống).
- **Số người sở hữu**: lấy điểm giữa của khoảng `Estimated owners`.
- **Nhóm giá**: Miễn phí (0), Thấp (dưới 5 USD), Trung bình (5 đến dưới 15 USD), Cao (từ 15 USD). Mốc 5 USD được chọn vì khoảng 74% game có giá dưới 5 USD.
- **Phân tích theo thể loại**: một game có nhiều thể loại nên được tính vào từng thể loại; bỏ nhãn "Free To Play" (trùng với giá) và "Early Access" (trạng thái phát hành); chỉ xét 12 thể loại nhiều game nhất.
- **Kiểm tra trong từng nhóm**: mối liên hệ giữa giá với độ phổ biến và đánh giá được kiểm tra lại trong từng thể loại, để tránh kết luận sai do khác biệt giữa các thể loại.
<<<<<<< HEAD
=======
- **Thể loại trong RQ3, RQ4 và mô hình**: dùng 10 thể loại nội dung, bỏ Utilities và Design & Illustration vì đây là phần mềm.
- **Giai đoạn phát hành** (RQ4): Trước 2014, 2014-2017, 2018-2020, 2021-2023, 2024-2025. Bỏ năm 2026 vì dữ liệu chỉ có vài tháng đầu năm.
- **Biến đổi log1p** cho giá, số đánh giá, số thành tựu và thời gian chơi khi đưa vào mô hình, vì các biến này lệch rất mạnh và có nhiều số 0.
- **Kiểm định phi tham số** (Mann-Whitney U, Kruskal-Wallis, chi bình phương, Spearman) vì dữ liệu không theo phân phối chuẩn. Có hiệu chỉnh Bonferroni và báo cáo cỡ ảnh hưởng, vì với cỡ mẫu lớn thì khác biệt nhỏ cũng có p rất bé.
- **Hồi quy tuyến tính** với sai số chuẩn HC3 để xem liên hệ của từng yếu tố khi giữ các yếu tố khác không đổi. Mô hình phân loại (Logistic Regression, Random Forest) dự đoán game có Peak CCU > 0, chỉ dùng thông tin có trước khi phát hành để tránh data leakage.
- **Phân tích kiểu A/B** chỉ so sánh hai nhóm theo các bước của A/B test. Dữ liệu không được chia ngẫu nhiên nên kết quả chỉ là mối liên hệ.
>>>>>>> ef668bcffbfa37c916799aad799b1c884027c2ad

## Nguyên tắc làm sạch dữ liệu

- Làm trên bản sao, không ghi đè file gốc hay file rút gọn.
- Mọi thay đổi đều ghi vào cleaning log; chỉ sửa khi có căn cứ.
- Số 0 có nghĩa "chưa có điểm" (Metacritic score, User score) được đổi thành giá trị trống.
- Outlier là giá trị thật (ví dụ Counter-Strike 2 có hơn 1 triệu người chơi đồng thời) nên được giữ nguyên.
- Mâu thuẫn không đủ căn cứ để sửa (ví dụ số đánh giá lớn hơn số người sở hữu ước tính) chỉ được ghi log.

## Giả định

- Dữ liệu đại diện cho các game được liệt kê trên Steam tại thời điểm thu thập.
<<<<<<< HEAD
- `Estimated owners` = "0 - 0" là game chưa có người dùng: không game nào trong nhóm này có người chơi, đánh giá hay thời gian chơi.
=======
- `Estimated owners` = "0 - 0" là thiếu dữ liệu, không phải game chưa có người dùng. Nhóm này có cả những game rất lớn như Call of Duty: Warzone và chiếm 62,7% game miễn phí. Các dòng này được giữ trong file, nhưng mọi phân tích về độ phổ biến và mô hình đều bỏ nhóm này. Khi so sánh game miễn phí với game trả phí, chỉ xét game phát hành đến 2020.
>>>>>>> ef668bcffbfa37c916799aad799b1c884027c2ad
- Ngày tham chiếu để xác định game chưa phát hành là 03/11/2026.

## Kiểm tra kết quả

- Sau khi làm sạch: so sánh trước/sau về số dòng, giá trị thiếu, trùng lặp, định dạng và các lỗi đã sửa (notebook 01, mục B8).
- Mọi con số trong phần nhận xét được đối chiếu với kết quả tính trong notebook.
<<<<<<< HEAD
- Mô hình (nếu có): chia train/test, so sánh với mô hình baseline, kiểm tra chênh lệch train/test để phát hiện overfitting.
=======
- Mô hình: chia train/test, so sánh với mô hình baseline, kiểm định chéo 5 phần, kiểm tra chênh lệch train/test để phát hiện overfitting.

## Nội dung môn học trong dự án

| Buổi | Nội dung | Nơi thực hiện |
|---|---|---|
| 1 | What is Data Science | `docs/project_charter.md` |
| 2 | Data Collection | `docs/project_charter.md`, `00_reduce_raw` |
| 3 | Data quality and Processing | `01_data_quality` |
| 4 | Outliers, noise & consistency | `01_data_quality` (mục A6, B5) |
| 5 | Transformation, reduction & integration | `00_reduce_raw`, `03_ml_readiness` |
| 6 | Probability & descriptive statistics | `02_eda`, `06_statistical_inference` |
| 7 | Data visualization | `02_eda`, `02b_eda_rq3_rq4` |
| 9 | Statistical inference & AB testing | `06_statistical_inference` |
| 10 | Regression analysis | `04_modeling`, `05_model_evaluation` |
| 11 | Classification & feature engineering | `03_ml_readiness`, `04_modeling`, `05_model_evaluation` |
| 12 | Big data, ethics and bias | `07_big_data_ethics_bias` |
>>>>>>> ef668bcffbfa37c916799aad799b1c884027c2ad
