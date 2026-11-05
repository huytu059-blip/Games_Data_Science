# Project Charter – GameStream: Phân tích trò chơi trên Steam

## Mục tiêu

Tìm hiểu các đặc điểm của trò chơi trên Steam và mối liên hệ giữa những đặc điểm đó với **mức độ phổ biến** (số người sở hữu, số người chơi đồng thời, số lượt đánh giá và đề xuất) và **mức độ đánh giá tích cực** của người chơi.

## Câu hỏi nghiên cứu

| RQ | Câu hỏi | Câu hỏi phụ |
|---|---|---|
| **RQ1** | Những yếu tố nào có mối liên hệ với mức độ phổ biến của một trò chơi trên Steam? | Lượng người sở hữu ước tính có tương quan mạnh với đỉnh điểm người chơi đồng thời (Peak CCU) không? |
| **RQ2** | Những yếu tố nào có mối liên hệ với mức độ đánh giá tích cực của người chơi trên Steam? | Điểm đánh giá của người dùng có tương đồng với điểm đánh giá từ giới phê bình (Metacritic) không? |
| **RQ3** | Những đặc điểm nào có mối liên hệ với thời gian chơi của người dùng Steam? | Thể loại nào có thời gian chơi trung vị cao nhất, và xu hướng đó có giống nhau giữa toàn bộ lịch sử chơi và hai tuần gần nhất không? |
| **RQ4** | Mức độ phổ biến và đánh giá của trò chơi thay đổi như thế nào theo thời gian phát hành? | Các trò chơi phát hành ở những giai đoạn khác nhau có khác biệt về lượng người chơi và mức đánh giá không? |
| **RQ5** | Giá bán có mối liên hệ như thế nào với mức độ phổ biến và mức độ đánh giá của trò chơi trên Steam? | Game miễn phí có lượng người chơi đồng thời cao hơn game trả phí không? Mức giá có liên hệ với tỷ lệ đánh giá tích cực không? |

Cả 5 câu hỏi đều được phân tích: RQ1, RQ2, RQ5 ở notebook `02_eda`, RQ3 và RQ4 ở notebook `02b_eda_rq3_rq4`.

## Đối tượng phân tích

- **Đối tượng phân tích:** mỗi trò chơi được liệt kê trên Steam.
- **Đơn vị quan sát:** một dòng trong bộ dữ liệu, tương ứng với một trò chơi, định danh bằng AppID. Dữ liệu **không** theo từng người chơi, nên không phân tích được hành vi của từng tài khoản.

## Dữ liệu

- **Nguồn:** [Steam Games Dataset trên Kaggle](https://www.kaggle.com/datasets/fronkongames/steam-games-dataset).
- **Quy mô:** 125.855 trò chơi, 40 cột (header gốc ghi 39 cột vì cột `DiscountDLC count` bị dính 2 cột).
- **Dữ liệu dùng để phân tích:** 21 cột phục vụ câu hỏi nghiên cứu, 125.846 trò chơi sau khi làm sạch, trong đó 101.274 trò chơi có dữ liệu owners. Mô hình dùng 100.025 trò chơi. Mô tả chi tiết ở `docs/data_dictionary.md`.

## Phạm vi

1. **Rút gọn dữ liệu** (`00_reduce_raw`): sửa lỗi header, giữ 21 cột, giải thích lý do bỏ từng cột.
2. **Audit và làm sạch** (`01_data_quality`): kiểm tra giá trị thiếu, trùng lặp, định dạng, mâu thuẫn và outlier; làm sạch có ghi cleaning log.
3. **Phân tích khám phá** (`02_eda`, `02b_eda_rq3_rq4`): khám phá tổng quan và phân tích trả lời từng câu hỏi nghiên cứu.
4. **Chuẩn bị dữ liệu và mô hình** (`03_ml_readiness`, `04_modeling`, `05_model_evaluation`): tạo đặc trưng, hồi quy, phân loại và đánh giá mô hình.
5. **Thống kê suy luận** (`06_statistical_inference`): xác suất, khoảng tin cậy, kiểm định giả thuyết và phân tích kiểu A/B.
6. **Big data, đạo đức và thiên lệch** (`07_big_data_ethics_bias`).

**Sản phẩm:** notebook, báo cáo, dashboard và slide thuyết trình.

## Tiêu chí thành công

- Dữ liệu được đọc đúng cấu trúc (không lệch cột), mọi thay đổi khi làm sạch đều được ghi lại và kiểm tra trước/sau.
- Mỗi câu hỏi nghiên cứu (kể cả câu hỏi phụ) có câu trả lời dựa trên số liệu và biểu đồ.
- Các notebook chạy lại được từ đầu đến cuối theo thứ tự `00` → `01` → `02` → `02b` → `03` → `04` → `05` → `06` → `07`.
- Mô hình phải tốt hơn mô hình baseline trên tập test.

## Giả định và hạn chế chính

- Kết quả chỉ là **mối liên hệ**, không phải quan hệ nhân quả.
- Giá trong dữ liệu là giá hiện tại, không nhất thiết là giá lúc người chơi mua game.
- `Estimated owners` chỉ là khoảng ước tính. 24.572 game có giá trị "0 - 0" là thiếu dữ liệu, phần lớn là game miễn phí và game mới, nên khi so sánh theo giá chỉ xét game phát hành đến 2020.
- Peak CCU là đỉnh trong một ngày, không phải đỉnh trong lịch sử của game. Khoảng 81% game có dữ liệu owners có Peak CCU = 0.
- Một số game lớn ngoài nhóm "0 - 0" cũng có số liệu không hợp lý, ví dụ Portal 2 có owners "0 - 20000" và Peak CCU = 0. Không có cách tách hết các trường hợp này.
- `User score` gần như trống (chỉ 40 game có điểm), nên dùng tỷ lệ đánh giá tích cực thay thế.
- Ngày tham chiếu để xác định game chưa phát hành là 03/11/2026 (dữ liệu không ghi ngày thu thập).

## Vai trò

- **Nhóm trưởng:** huytu059-blip
- **Thành viên:** mtrieng138-del, huin23, (bổ sung thành viên thứ 4)
