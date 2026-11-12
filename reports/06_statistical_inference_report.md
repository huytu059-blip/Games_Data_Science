# Báo cáo thống kê suy luận

Notebook: `06_statistical_inference`. Chi tiết ở chương 5 của báo cáo cuối kỳ. Bảng đầy đủ ở `reports/tables/kiem_dinh_gia_thuyet.csv`.

## Xác suất và khoảng tin cậy

- Game có Steam Cloud có xác suất có Peak CCU > 0 là 35,4%, so với 13,2% ở game không có. Hai sự kiện không độc lập.
- Tỷ lệ game có Peak CCU > 0 là 19,40%, khoảng tin cậy 95% là 19,15% đến 19,64%.
- Chênh lệch trung vị Positive ratio giữa game có và không có Achievements là 6,75 điểm, khoảng tin cậy bootstrap 6,41 đến 7,14.

## Kiểm định giả thuyết

Cả 11 kiểm định đều bác bỏ H0 sau hiệu chỉnh Bonferroni, vì cỡ mẫu rất lớn. Cỡ ảnh hưởng mới cho biết khác biệt lớn hay nhỏ:

- Rõ: Metacritic và tỷ lệ tích cực (rho 0,583), owners và Peak CCU (rho 0,469), MMO có tỷ lệ tích cực thấp hơn (r = -0,42).
- Rất yếu: giá và tỷ lệ tích cực (rho 0,12), Peak CCU của game miễn phí và trả phí (r = 0,035).

## Phân tích kiểu A/B

Dữ liệu không được chia ngẫu nhiên nên đây không phải A/B test thật. Game có Achievements có tỷ lệ được đánh giá tốt là 58,6%, so với 44,2% ở game không có (chênh 14,5 điểm, khoảng tin cậy 13,6 đến 15,3). Chênh lệch vẫn còn trong từng giai đoạn và từng nhóm giá, nhưng kết quả chỉ là mối liên hệ.
