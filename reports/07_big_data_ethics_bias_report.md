# Báo cáo big data, đạo đức và thiên lệch

Notebook: `07_big_data_ethics_bias`. Chi tiết ở chương 7 của báo cáo cuối kỳ.

## Big data

Dữ liệu chưa phải big data vì một máy tính cá nhân xử lý được. Thách thức chính là độ tin cậy. Nhóm đã thử đổi kiểu dữ liệu (75,2 MB xuống 61,1 MB, bỏ thêm 4 cột văn bản còn 14,4 MB), đọc theo từng phần và lấy mẫu (mẫu 10% cho 19,50%, gần với 19,40% trên toàn bộ).

## Thiên lệch trong dữ liệu

- Thiếu dữ liệu owners không ngẫu nhiên: từ 2021 đến 2024 có 73,5% game miễn phí bị thiếu, so với 1,9% game trả phí.
- Điểm Metacritic có ở 53,6% game trên 1 triệu người sở hữu nhưng chỉ 0,8% game dưới 20 nghìn.
- Một số game lớn ngoài nhóm "0 - 0" cũng có số liệu không hợp lý, ví dụ Portal 2.
- Không đo được: người đánh giá tự chọn, game đã gỡ khỏi Steam, Peak CCU phụ thuộc ngày ghi nhận.

## Thiên lệch của mô hình

Random Forest hoạt động không đều: recall 0,806 ở game không có nhãn Indie và 0,615 ở game Indie; 0,846 ở game trước 2018 và khoảng 0,63-0,64 ở game mới hơn. Nếu dùng để chọn game đáng chú ý, game Indie và game mới dễ bị bỏ sót.

## Đạo đức

Dữ liệu không có thông tin cá nhân. Nhóm cần đọc giấy phép trên Kaggle trước khi chia sẻ lại dữ liệu. Mọi kết quả chỉ là mối liên hệ, và mô hình không nên dùng để quyết định đầu tư hay gợi ý game.
