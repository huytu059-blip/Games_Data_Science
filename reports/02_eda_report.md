# Báo cáo phân tích khám phá

Notebook: `02_eda` (RQ1, RQ2, RQ5), `02b_eda_rq3_rq4` (RQ3, RQ4). Chi tiết ở chương 4 của báo cáo cuối kỳ.

Peak CCU là đỉnh trong một ngày, nên "có người chơi đồng thời" nghĩa là Peak CCU > 0 vào ngày ghi nhận.

## RQ1: Mức độ phổ biến

- Số người sở hữu và Peak CCU liên hệ cùng chiều ở mức trung bình (Spearman 0,47).
- Massively Multiplayer, RPG, Strategy và Simulation có tỷ lệ game có Peak CCU > 0 cao nhất (25,2-33,6%). Casual, Indie, Racing thấp nhất (15,3-16,7%).

## RQ2: Đánh giá tích cực

- Trung vị tỷ lệ tích cực là 81,2% trên 56.662 game có từ 10 đánh giá.
- Người chơi và giới phê bình tương đồng ở mức khá (Spearman 0,58).
- Massively Multiplayer thấp hơn hẳn (66,7%). Achievements, Steam Cloud và hỗ trợ tay cầm đi kèm mức cao hơn khoảng 6-7 điểm.

## RQ3: Thời gian chơi

- Trung vị là 204 phút trên 26.173 game có dữ liệu.
- RPG (266 phút) và Strategy (253 phút) cao nhất. Trong hai tuần gần nhất, Massively Multiplayer cao nhất (224 phút). Tương quan thứ hạng giữa hai cột là 0,52.
- Giá càng cao thì thời gian chơi càng dài: 92, 184, 259 và 470,5 phút.

## RQ4: Theo thời gian phát hành

| Giai đoạn | Số game | Có Peak CCU > 0 (%) | Tỷ lệ tích cực trung vị (%) |
|---|---|---|---|
| Trước 2014 | 1.935 | 62,3 | 80,8 |
| 2014-2017 | 14.047 | 26,9 | 75,0 |
| 2018-2020 | 23.385 | 16,8 | 78,9 |
| 2021-2023 | 31.379 | 17,2 | 83,6 |
| 2024-2025 | 30.228 | 17,7 | 88,2 |

Game cũ có nhiều thời gian tích lũy hơn và dữ liệu các năm gần đây thiếu nhiều, nên không thể kết luận game ngày nay được yêu thích hơn.

## RQ5: Giá bán (game đến 2020)

| Nhóm giá | Có Peak CCU > 0 (%) | Từ 20.000 người sở hữu (%) | Tỷ lệ tích cực trung vị (%) |
|---|---|---|---|
| Miễn phí | 25,5 | 50,3 | 77,0 |
| Thấp | 19,9 | 37,0 | 76,5 |
| Trung bình | 26,5 | 33,6 | 80,0 |
| Cao | 36,4 | 35,1 | 75,7 |

Trong game trả phí, giá cao hơn đi kèm tỷ lệ có Peak CCU > 0 cao hơn nhưng không đi kèm nhiều người sở hữu hơn. Game miễn phí không thua game trả phí về độ phổ biến. Giá liên hệ rất yếu với đánh giá (Spearman 0,12).

## Insights xuyên suốt

- Mức độ phổ biến không đồng nghĩa với mức độ hài lòng: Massively Multiplayer có tỷ lệ Peak CCU > 0 cao nhất (33,6%) nhưng tỷ lệ tích cực trung vị thấp hơn mặt bằng chung (66,7% so với 81,2%).
- Trong nhóm game trả phí, tỷ lệ có Peak CCU > 0 tăng theo nhóm giá, nhưng tỷ lệ có nhiều owners không tăng tương ứng; giá và tỷ lệ tích cực chỉ có Spearman 0,12. Đây là mối liên hệ, không phải tác động của giá.
- Tỷ lệ owners = “0 - 0” cao hơn nhiều ở game miễn phí và game mới. Coi nhóm này là giá trị 0 thật đã làm sai lệch so sánh giá ở báo cáo giữa kỳ.

Các kết quả theo nhóm, kiểm định thống kê và giới hạn diễn giải được tổng hợp ở mục 4.8 của [`final_report.md`](final_report.md).
