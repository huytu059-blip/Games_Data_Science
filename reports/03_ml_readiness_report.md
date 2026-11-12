# Báo cáo chuẩn bị dữ liệu cho mô hình

Notebook: `03_ml_readiness`. Chi tiết ở mục 6.1 của báo cáo cuối kỳ. Đầu ra là `data/processed/games_features.csv`.

## Dữ liệu dùng cho mô hình

Từ 125.846 game, bỏ nhóm owners "0 - 0", năm 2026 và game thiếu Genres hoặc Categories, còn 100.025 game (79,5%) với 43 cột.

## Các bước chính

- Biến đổi: lấy log1p cho giá, số đánh giá, số thành tựu, thời gian chơi. Độ lệch của Total reviews giảm từ 159,47 xuống 0,81.
- Ghép bảng: tách Genres và Categories thành bảng riêng, tạo 16 cột cờ rồi ghép lại theo id.
- Giảm chiều: PCA cần 11 trên 16 thành phần để giữ 80% phương sai nên không dùng.
- Chia dữ liệu: 80.020 game train và 20.005 game test, giữ tỷ lệ has_ccu 19,4% ở hai tập.

## Kiểm tra data leakage

Chỉ dùng thông tin có trước khi phát hành: giá, Achievements, thể loại, tính năng, năm phát hành. Không dùng Tags, số đánh giá, lượt đề xuất, owners, Peak CCU, thời gian chơi, Discount, DLC count và Metacritic. Tags bị loại vì 97,8% game chưa có đánh giá bị thiếu Tags, còn game đã có đánh giá thì không thiếu.
