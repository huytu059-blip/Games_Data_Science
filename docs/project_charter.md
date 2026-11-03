# Project Charter – GameStream: Phân tích trò chơi trên Steam

## Mục tiêu

Tìm hiểu các đặc điểm của trò chơi trên Steam và mối liên hệ giữa những đặc điểm đó với **mức độ phổ biến** (số người sở hữu, số người chơi đồng thời, số lượt đánh giá và đề xuất) và **mức độ đánh giá tích cực** của người chơi.

## Câu hỏi nghiên cứu

| RQ | Câu hỏi | Câu hỏi phụ |
|---|---|---|
| **RQ1** | Những yếu tố nào có mối liên hệ với mức độ phổ biến của một trò chơi trên Steam? | Lượng người sở hữu ước tính có tương quan mạnh với đỉnh điểm người chơi đồng thời (Peak CCU) không? |
| **RQ2** | Những yếu tố nào có mối liên hệ với mức độ đánh giá tích cực của người chơi trên Steam? | Điểm đánh giá của người dùng có tương đồng với điểm đánh giá từ giới phê bình (Metacritic) không? |
| **RQ5** | Giá bán có mối liên hệ như thế nào với mức độ phổ biến và mức độ đánh giá của trò chơi trên Steam? | Game miễn phí có lượng người chơi đồng thời cao hơn game trả phí không? Mức giá có liên hệ với tỷ lệ đánh giá tích cực không? |

RQ3 (thời gian chơi) và RQ4 (thay đổi theo thời gian phát hành) đã được đề xuất nhưng không chọn, để tập trung vào 3 câu hỏi trên.

## Đối tượng phân tích

- **Đối tượng phân tích:** mỗi trò chơi được liệt kê trên Steam.
- **Đơn vị quan sát:** một dòng trong bộ dữ liệu, tương ứng với một trò chơi, định danh bằng AppID. Dữ liệu **không** theo từng người chơi, nên không phân tích được hành vi của từng tài khoản.

## Dữ liệu

- **Nguồn:** [Steam Games Dataset trên Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset).
- **Quy mô:** 125.855 trò chơi, 40 cột (header gốc ghi 39 cột vì cột `DiscountDLC count` bị dính 2 cột).
- **Dữ liệu dùng để phân tích:** 21 cột phục vụ câu hỏi nghiên cứu, 125.846 trò chơi sau khi làm sạch. Mô tả chi tiết ở `docs/data_dictionary.md`.

## Phạm vi

1. **Rút gọn dữ liệu** (`00_reduce_raw`): sửa lỗi header, giữ 21 cột, giải thích lý do bỏ từng cột.
2. **Audit và làm sạch** (`01_data_quality`): kiểm tra giá trị thiếu, trùng lặp, định dạng, mâu thuẫn và outlier; làm sạch có ghi cleaning log.
3. **Phân tích khám phá** (`02_eda`): khám phá tổng quan và phân tích trả lời từng câu hỏi nghiên cứu.
4. **Mô hình** (`04_modeling`): thử dự đoán Peak CCU. Không bắt buộc, vì các câu hỏi nghiên cứu đều hỏi về mối liên hệ.

**Sản phẩm:** notebook, báo cáo, dashboard và slide thuyết trình.

## Tiêu chí thành công

- Dữ liệu được đọc đúng cấu trúc (không lệch cột), mọi thay đổi khi làm sạch đều được ghi lại và kiểm tra trước/sau.
- Mỗi câu hỏi nghiên cứu (kể cả câu hỏi phụ) có câu trả lời dựa trên số liệu và biểu đồ.
- Các notebook chạy lại được từ đầu đến cuối theo thứ tự `00` → `01` → `02` → `04`.
- Nếu làm mô hình: mô hình phải tốt hơn mô hình baseline trên tập test.

## Giả định và hạn chế chính

- Kết quả chỉ là **mối liên hệ**, không phải quan hệ nhân quả.
- Giá trong dữ liệu là giá hiện tại, không nhất thiết là giá lúc người chơi mua game.
- `Estimated owners` chỉ là khoảng ước tính; 84% game có Peak CCU = 0.
- `User score` gần như trống (chỉ 40 game có điểm), nên dùng tỷ lệ đánh giá tích cực thay thế.
- Ngày tham chiếu để xác định game chưa phát hành là 03/11/2026 (dữ liệu không ghi ngày thu thập).

## Vai trò

- **Nhóm trưởng:** huytu059-blip
- **Thành viên:** mtrieng138-del, huin23, (bổ sung thành viên thứ 4)
