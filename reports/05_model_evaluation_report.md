# Báo cáo đánh giá mô hình

Notebook: `05_model_evaluation`. Chi tiết ở mục 6.3 và 6.4 của báo cáo cuối kỳ.

## Hồi quy (R2 trên tập test)

| Mục tiêu | Baseline | Hồi quy tuyến tính | Random Forest |
|---|---|---|---|
| A: Số đánh giá | 0,000 | 0,365 | 0,432 |
| B: Tỷ lệ tích cực | 0,000 | 0,134 | 0,192 |
| C: Thời gian chơi | 0,000 | 0,138 | 0,166 |

## Phân loại (tập test)

| Mô hình | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Baseline | 0,806 | 0,000 | 0,000 | 0,000 | 0,500 |
| Logistic Regression | 0,719 | 0,379 | 0,698 | 0,491 | 0,779 |
| Random Forest | 0,751 | 0,414 | 0,689 | 0,518 | 0,805 |

## Nhận xét

- Các mô hình đều tốt hơn baseline nên đạt tiêu chí trong project charter.
- Baseline có accuracy cao nhất dù không phát hiện được game nào, nên không dùng accuracy một mình.
- Kiểm định chéo 5 phần cho F1 trung bình 0,521 (Random Forest) và 0,491 (Logistic Regression), kết quả ổn định.
- Random Forest có dấu hiệu overfitting ở mô hình C (R2 train 0,289, test 0,166).
- Bốn đặc trưng quan trọng nhất là số Achievements, năm phát hành, Steam Cloud và giá.

Khả năng dự đoán ở mức vừa phải vì mô hình không có thông tin về chất lượng và ngân sách quảng bá. Mô hình hỗ trợ trả lời câu hỏi nghiên cứu, chưa đủ tốt để dự đoán cho từng game.
