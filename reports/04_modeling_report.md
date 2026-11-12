# Báo cáo xây dựng mô hình

Notebook: `04_modeling`. Chi tiết ở mục 6.2 của báo cáo cuối kỳ. Bảng đầy đủ ở `reports/tables/he_so_hoi_quy.csv`.

## Hồi quy tuyến tính

| Mô hình | Mục tiêu | Dữ liệu | Câu hỏi |
|---|---|---|---|
| A | log1p(Total reviews) | Tất cả game | RQ1, RQ4, RQ5 |
| B | Positive ratio | Game có từ 10 đánh giá | RQ2, RQ4, RQ5 |
| C | log1p(Median playtime forever) | Game có thời gian chơi > 0 | RQ3 |

Kết quả chính khi giữ các yếu tố khác không đổi:

- Steam Cloud (gấp khoảng 2,3 lần) và Achievements (gấp khoảng 2,2 lần) đi kèm nhiều đánh giá hơn.
- Massively Multiplayer (-6,9 điểm) và Simulation (-5,1 điểm) có tỷ lệ tích cực thấp nhất. Steam Cloud (+4,3), hỗ trợ tay cầm (+3,6) và Achievements (+3,5) đi kèm mức cao hơn. Multi-player và Online PvP không còn ý nghĩa thống kê.
- Mỗi năm phát hành mới hơn, số đánh giá giảm khoảng 28%, tỷ lệ tích cực tăng khoảng 1 điểm.
- Giá từ 5 lên 15 USD chỉ tăng tỷ lệ tích cực khoảng 1,4 điểm.

## Phân loại

Dự đoán game có Peak CCU > 0 bằng Logistic Regression và Random Forest, dùng class_weight="balanced". Phần đầu notebook còn có mô hình hai giai đoạn dự đoán Peak CCU, với R2 trên toàn bộ tập test chỉ 0,0049.

Mô hình đã lưu ở `models/mo_hinh.joblib`, không đưa lên GitHub. Chạy notebook 04 để tạo lại.
