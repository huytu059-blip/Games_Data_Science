# Games Data Science

Dự án GameStream dùng Python và Jupyter để tìm hiểu những đặc điểm nào của trò chơi trên Steam có liên hệ với mức độ phổ biến, đánh giá của người chơi và thời gian chơi. Dự án gồm làm sạch dữ liệu, phân tích khám phá, thống kê suy luận, xây dựng mô hình và đánh giá thiên lệch.

## Câu hỏi nghiên cứu

- RQ1: Những yếu tố nào có mối liên hệ với mức độ phổ biến của một trò chơi?
- RQ2: Những yếu tố nào có mối liên hệ với mức độ đánh giá tích cực của người chơi?
- RQ3: Những đặc điểm nào có mối liên hệ với thời gian chơi?
- RQ4: Mức độ phổ biến và đánh giá thay đổi như thế nào theo thời gian phát hành?
- RQ5: Giá bán có mối liên hệ như thế nào với mức độ phổ biến và mức độ đánh giá?

Kết quả nằm trong `reports/final_report.md`. Phạm vi dự án xem ở `docs/project_charter.md`.

## Cấu trúc thư mục

- `data/raw/`: dữ liệu gốc, không sửa file `games.csv`.
- `data/processed/`: dữ liệu đã rút gọn và đã xử lý.
- `notebooks/`: các notebook phân tích theo thứ tự. `notebooks/archive/` chứa các bản cũ.
- `src/`: code dùng lại. `01_data_quality` dùng `data_quality.py` và `cleaning.py`, `03_ml_readiness` dùng `features.py`.
- `scripts/`: script chạy các notebook theo thứ tự.
- `tests/`: unit test cho `src/` và danh sách notebook.
- `docs/`: từ điển dữ liệu và tài liệu dự án.
- `reports/`: báo cáo, biểu đồ và bảng kết quả.
- `models/`: mô hình đã huấn luyện, do `04_modeling` tạo ra và không đưa lên GitHub.

## Dữ liệu

- Nguồn: [Steam Games Dataset trên Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset) (`games.csv`, khoảng 400 MB, 125.855 trò chơi).
- File `data/raw/games.csv` trong repo chỉ là mẫu 8 dòng, vì GitHub không nhận file lớn hơn 100 MB. Chạy `00_reduce_raw` trên file này sẽ cho kết quả sai.
- Muốn chạy `00_reduce_raw`, tải `games.csv` đầy đủ từ Kaggle và đặt vào `data/raw/games.csv`. Để Git không báo file này bị sửa, chạy `git update-index --skip-worktree data/raw/games.csv`.
- `data/processed/games_reduced.csv` (đủ dữ liệu, 21 cột) đã có trong repo, nên `01_data_quality` và các notebook sau chạy được mà không cần file gốc.
- `data/processed/games_cleaned.csv` và `data/processed/games_features.csv` không có trong repo. Chạy `01_data_quality` và `03_ml_readiness` để tạo hai file này.

## Cách chạy

1. Cài thư viện bằng `pip install -r requirements.txt`.
2. Chạy toàn bộ notebook bằng `python scripts/run_pipeline.py`, hoặc chạy từ một notebook bằng `python scripts/run_pipeline.py 03`. `python scripts/run_data_quality.py` chỉ chạy `00` và `01`. Các script tự bỏ qua `00_reduce_raw` khi không có file `games.csv` đầy đủ.
3. Nếu muốn làm trong Jupyter, mở Jupyter từ thư mục `notebooks/` để đường dẫn tương đối chạy đúng, rồi mở các notebook theo thứ tự.
4. Chạy test bằng `pytest`.

Notebook rút gọn ghi ra `data/processed/games_reduced.csv`. Chạy lại notebook này sẽ ghi đè file đó.

## Quy tắc về luồng dữ liệu

Chạy các notebook theo thứ tự: `00_reduce_raw` → `01_data_quality` → `02_eda` → `02b_eda_rq3_rq4` → `03_ml_readiness` → `04_modeling` → `05_model_evaluation` → `06_statistical_inference` → `07_big_data_ethics_bias`.

- Chỉ `00_reduce_raw` đọc file gốc. Notebook này kiểm tra cấu trúc file gốc, giải thích lý do bỏ cột, rồi tạo `data/processed/games_reduced.csv` từ `data/raw/games.csv` (giữ 21 cột phục vụ câu hỏi nghiên cứu và giữ toàn bộ dòng).
- `01_data_quality` kiểm tra và làm sạch `games_reduced.csv`, sau đó ghi ra `data/processed/games_cleaned.csv`, `reports/games_data_quality_audit.xlsx` và `reports/cleaning_log.csv`.
- `02_eda` và `02b_eda_rq3_rq4` đọc `games_cleaned.csv`. `03_ml_readiness` cũng đọc file này và ghi ra `data/processed/games_features.csv`, trong đó cột `split` đánh dấu tập train và test.
- Phần sau của `04_modeling` và các notebook `05`, `06`, `07` đọc `games_features.csv`. `04_modeling` lưu mô hình vào `models/mo_hinh.joblib`, `05` và `07` sẽ nạp file này. Ngoài `00_reduce_raw`, không notebook nào đọc `games.csv`.
- Các dòng có `Estimated owners` = "0 - 0" vẫn nằm trong `games_cleaned.csv`, nhưng được xem là thiếu dữ liệu và bị bỏ khỏi mọi phân tích độ phổ biến và mô hình, vì nhóm này có cả những game rất lớn như Call of Duty: Warzone.
- Không notebook nào ghi đè `data/raw/games.csv`.
- Tên cột `DiscountDLC count` trong file gốc thực chất là hai cột `Discount` và `DLC count` bị dính liền. Khi đọc file gốc luôn phải tách ra, nếu không mọi cột từ đó trở đi sẽ lệch một cột.
- `notebooks/archive/` chứa các bản cũ và không thuộc quy trình chạy.
