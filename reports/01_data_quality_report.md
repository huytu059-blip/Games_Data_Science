# Báo cáo chất lượng dữ liệu

Notebook: `00_reduce_raw`, `01_data_quality`. Chi tiết ở chương 2 và 3 của báo cáo cuối kỳ.

## Tóm tắt

- Tệp gốc có 125.855 dòng. Dòng tiêu đề có 39 tên cột nhưng mỗi dòng có 40 giá trị, vì `DiscountDLC count` là hai cột bị dính tên.
- Sau khi rút gọn còn 21 cột, bộ nhớ giảm từ 576,87 MB xuống 75,43 MB (giảm 86,92%).
- Sau khi làm sạch còn 125.846 trò chơi. Chỉ 9 dòng bị xóa: 8 dòng trùng và 1 trò chơi chưa phát hành.

## Vấn đề chính

| Vấn đề | Số dòng | Xử lý |
|---|---|---|
| User score = 0 | 125.815 | Đổi thành NaN |
| Metacritic score = 0 | 121.597 | Đổi thành NaN |
| Tags thiếu | 42.502 | Để trống |
| Estimated owners = "0 - 0" | 24.572 | Giữ dòng, bỏ khi phân tích độ phổ biến |
| Genres, Categories thiếu | 8.423 và 8.966 | Để trống |
| Giá 0 nhưng giảm giá 1-99% | 35 | Đặt Discount = 0 |

## Lưu ý về owners = "0 - 0"

Báo cáo giữa kỳ xem nhóm này là trò chơi chưa có người dùng. Giả định đó sai vì nhóm có cả EA SPORTS FC 26, Assassin's Creed Shadows và Call of Duty: Warzone. Đây là thiếu dữ liệu, chiếm 62,7% game miễn phí và 7,9% game trả phí, và tăng từ 0,9% ở năm 2020 lên 41,2% ở năm 2025.

## Tệp liên quan

- `reports/cleaning_log.csv`: nhật ký làm sạch.
- `reports/games_data_quality_audit.xlsx`: kết quả audit.
