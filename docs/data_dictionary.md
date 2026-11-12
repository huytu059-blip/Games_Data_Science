# Từ điển dữ liệu

Từ điển này mô tả **40 trường sau khi sửa header của tệp gốc**. Trong `games_reduced.csv`, 21 trường được giữ lại; `AppID` được đổi tên thành `id`. Kiểu dữ liệu bên dưới là kiểu ban đầu trước bước làm sạch; `Release date` được chuyển sang ngày tháng, còn hai cột điểm số được đổi số 0 thành giá trị thiếu.

| Cột gốc → tên trong dữ liệu rút gọn | Tên tiếng Việt và ý nghĩa | Kiểu ban đầu | Quyết định trong bước rút gọn |
|---|---|---|---|
| `AppID` → `id` trong file rút gọn | **Mã định danh game (App ID).** Mã số định danh độc nhất của mỗi trò chơi trên hệ thống Steam. | int64 / str | Giữ — đổi tên thành `id` để định danh trò chơi. |
| `Name` | **Tên trò chơi.** Tên chính thức của tựa game trên Steam. | str | Giữ — để tra cứu tên trò chơi. |
| `Release date` | **Ngày phát hành.** Thời gian (ngày, tháng, năm) tựa game chính thức ra mắt trên Steam. | str | Giữ — để so sánh theo thời điểm phát hành (RQ4) và làm biến kiểm soát. |
| `Estimated owners` | **Ước tính số lượng người sở hữu.** Khoảng ước tính số người sở hữu (ví dụ 0–20.000), không phải số chính xác; `0 - 0` được xem là thiếu dữ liệu trong phân tích. | str | Giữ — cho phân tích độ phổ biến (RQ1, RQ4, RQ5); giá trị là khoảng ước tính. |
| `Peak CCU` | **Đỉnh điểm người chơi đồng thời.** Số người chơi cùng lúc cao nhất được ghi nhận trong một ngày; không phải đỉnh lịch sử của trò chơi. | int64 | Giữ — làm chỉ số người chơi đồng thời (RQ1, RQ4, RQ5). |
| `Required age` | **Độ tuổi yêu cầu.** Giới hạn độ tuổi tối thiểu được phép chơi (ví dụ: 0, 18...). | float64 / int64 | Loại — Gần như toàn bộ bằng 0, không thuộc các câu hỏi nghiên cứu  |
| `Price` | **Giá tiền.** Giá hiện tại trong bộ dữ liệu (được xem là USD trong phân tích); không nhất thiết là giá người chơi đã trả khi mua. | float64 | Giữ — cho phân tích giá (RQ5). |
| `Discount` | **Mức giảm giá.** Phần trăm giảm giá hiện tại của trò chơi (0-100). | int64 | Giữ — như thông tin giá hiện tại; không dùng làm biến chính trong kết luận RQ5. |
| `DLC count` | **Số lượng DLC.** Số gói nội dung tải thêm (DLC) của trò chơi. | int64 | Giữ — như đặc điểm sản phẩm; không dùng làm biến chính trong kết luận hiện tại. |
| `About the game` | **Giới thiệu về game.** Mô tả chi tiết nội dung, cốt truyện hoặc giới thiệu tổng quan về tựa game. | str | Loại — Văn bản mô tả dài, không dùng cho câu hỏi nghiên cứu 6,7% ô trống. |
| `Supported languages` | **Ngôn ngữ được hỗ trợ.** Danh sách các ngôn ngữ (giao diện, phụ đề) mà trò chơi hỗ trợ. | str | Loại — Danh sách ngôn ngữ, không thuộc các câu hỏi nghiên cứu |
| `Full audio languages` | **Ngôn ngữ lồng tiếng đầy đủ.** Danh sách các ngôn ngữ có hỗ trợ lồng tiếng (âm thanh giọng nói) trong game. | str | Loại — Danh sách ngôn ngữ lồng tiếng, phần lớn trống |
| `Reviews` | **Đánh giá / Tổng quan đánh giá.** Nội dung/đoạn trích đánh giá dạng văn bản; không phải số lượt đánh giá tích cực hay tiêu cực (các số lượt nằm ở Positive và Negative). | str | Loại — Trích dẫn đánh giá dạng văn bản; 90,3% ô trống. |
| `Header image` | **Ảnh tiêu đề.** Đường dẫn URL chứa hình ảnh banner/thumbnail chính thức của trò chơi. | str | Loại — Link ảnh, không có thông tin để phân tích 0,1% ô trống. |
| `Website` | **Trang web chính thức.** Đường dẫn URL trang web của nhà phát triển hoặc trang web chính thức của game. | str | Loại — Link website, không có thông tin để phân tích 59,9% ô trống. |
| `Support url` | **Đường dẫn hỗ trợ.** Link trang web hoặc cổng thông tin để người chơi gửi yêu cầu hỗ trợ, báo lỗi. | str | Loại — Link hỗ trợ, không có thông tin để phân tích 56,1% ô trống. |
| `Support email` | **Email hỗ trợ.** Địa chỉ email liên hệ của nhà phát hành/phát triển. | str | Loại — Email hỗ trợ, không có thông tin để phân tích 18,0% ô trống. |
| `Windows` | **Hỗ trợ Windows.** Xác định game có chạy được trên hệ điều hành Windows hay không (True/False). | bool | Loại — Nền tảng hỗ trợ, không thuộc các câu hỏi nghiên cứu; 99,97% trò chơi hỗ trợ Windows. |
| `Mac` | **Hỗ trợ Mac.** Xác định game có chạy được trên hệ điều hành macOS hay không (True/False). | bool | Loại — Nền tảng hỗ trợ, không thuộc các câu hỏi nghiên cứu |
| `Linux` | **Hỗ trợ Linux.** Xác định game có chạy được trên hệ điều hành Linux hay không (True/False). | bool | Loại — Nền tảng hỗ trợ, không thuộc các câu hỏi nghiên cứu |
| `Metacritic score` | **Điểm Metacritic.** Điểm số đánh giá tổng hợp từ các nhà phê bình game chuyên nghiệp. | int64 / float64 | Giữ — để so sánh với đánh giá người chơi (RQ2). |
| `Metacritic url` | **Đường dẫn Metacritic.** Đường dẫn URL đến trang chi tiết đánh giá của game trên Metacritic. | str | Loại — Link Metacritic, đã có cột Metacritic score 96,6% ô trống. |
| `User score` | **Điểm người dùng.** Điểm số đánh giá trung bình do chính người dùng thực tế chấm. | float64 | Giữ — để đối chiếu; chỉ 40 game có điểm khác 0 nên không dùng làm thước đo chính. |
| `Positive` | **Số lượng đánh giá tích cực.** Tổng số lượt đánh giá mang chiều hướng tích cực từ người chơi. | int64 | Giữ — để tính tỷ lệ đánh giá tích cực (RQ2, RQ4, RQ5). |
| `Negative` | **Số lượng đánh giá tiêu cực.** Tổng số lượt đánh giá mang chiều hướng tiêu cực từ người chơi. | int64 | Giữ — để tính tỷ lệ đánh giá tích cực (RQ2, RQ4, RQ5). |
| `Score rank` | **Xếp hạng điểm số.** Thứ hạng điểm số của game so với các tựa game khác trên hệ thống. | float64 / int64 | Loại — Gần như toàn bộ trống 99,97% ô trống. |
| `Achievements` | **Số lượng thành tựu.** Tổng số lượng huy hiệu hoặc thành tựu có thể đạt được trong game. | int64 | Giữ — làm đặc điểm trò chơi, dùng khi phân tích nhóm và mô hình. |
| `Recommendations` | **Số lượt giới thiệu/đề xuất.** Số lượng lượt đề xuất hoặc giới thiệu game từ cộng đồng người chơi. | int64 | Giữ — như một chỉ số phổ biến (RQ1) và để kiểm tra giả định owners = 0 - 0. |
| `Notes` | **Ghi chú thêm.** Các thông tin bổ sung, lưu ý hoặc ghi chú đặc biệt về trò chơi. | str | Loại — Ghi chú nội dung dạng văn bản, phần lớn trống 81,5% ô trống. |
| `Average playtime forever` | **Thời gian chơi trung bình (tổng).** Số phút trung bình người chơi dành ra để chơi tựa game này từ trước đến nay. | int64 | Giữ — cho phân tích thời gian chơi dài hạn (RQ3). |
| `Average playtime two weeks` | **Thời gian chơi trung bình (2 tuần gần nhất).** Số phút trung bình người chơi đã bỏ ra để chơi game trong vòng 2 tuần qua. | int64 | Giữ — cho phân tích thời gian chơi gần đây (RQ3). |
| `Median playtime forever` | **Trung vị thời gian chơi (tổng).** Giá trị trung vị của tổng thời gian chơi game tính bằng phút. | int64 | Giữ — làm chỉ số bền vững hơn với giá trị cực lớn (RQ3). |
| `Median playtime two weeks` | **Trung vị thời gian chơi (2 tuần gần nhất).** Giá trị trung vị của thời gian chơi trong vòng 2 tuần qua tính bằng phút. | int64 | Giữ — để so sánh thời gian chơi gần đây theo nhóm (RQ3). |
| `Developers` | **Nhà phát triển.** Tên của cá nhân, nhóm hoặc công ty trực tiếp lập trình trò chơi. | str | Loại — Tên quá rời rạc để phân tích trong phạm vi hiện tại; 72.859 giá trị khác nhau. |
| `Publishers` | **Nhà phát hành.** Tên công ty đứng ra chịu trách nhiệm thương mại hóa và phát hành trò chơi. | str | Loại — Tên quá rời rạc để phân tích trong phạm vi hiện tại; 64.607 giá trị khác nhau. |
| `Categories` | **Danh mục tính năng.** Các tính năng hỗ trợ của game trên Steam (ví dụ: Single-player, Multiplayer...). | str | Giữ — để phân nhóm theo tính năng và hệ điều hành của game (RQ1–RQ3). |
| `Genres` | **Thể loại game.** Phân loại thể loại chính của trò chơi (ví dụ: Action, Indie, Strategy, RPG...). | str | Giữ — để so sánh kết quả theo thể loại (RQ1–RQ5). |
| `Tags` | **Thẻ mô tả (Tags).** Các từ khóa do cộng đồng người chơi tự đặt để mô tả phong cách, chủ đề. | str | Giữ — để mô tả chủ đề do cộng đồng gắn; thiếu Tags thường gắn với game chưa có đánh giá. |
| `Screenshots` | **Ảnh chụp màn hình.** Danh sách các đường dẫn URL chứa hình ảnh chụp màn hình gameplay. | str | Loại — Danh sách link ảnh 4,8% ô trống. |
| `Movies` | **Video trailer/phim giới thiệu.** Danh sách các đường dẫn URL chứa video trailer hoặc đoạn phim ngắn quảng cáo. | str | Loại — Trống hoàn toàn (100%). |

## Tác động của việc bỏ cột ngôn ngữ

`Supported languages` và `Full audio languages` không được giữ vì dự án hiện không đặt câu hỏi nghiên cứu về bản địa hóa. Cột ngôn ngữ giao diện/phụ đề thiếu 6,7% dữ liệu; cột lồng tiếng thiếu 59,3%. Việc bỏ hai cột này **không làm thay đổi** các phép tính cho RQ1–RQ5 hiện tại, nhưng dự án không thể kết luận liệu độ phủ ngôn ngữ có liên quan đến mức độ phổ biến, đánh giá hay thời gian chơi. Nếu mở rộng phạm vi, cần giữ hai cột này và phân biệt “không hỗ trợ” với “không có dữ liệu”; không nên suy đoán giá trị còn thiếu.

## Ghi chú về rút gọn và làm sạch

Rút gọn dữ liệu là bước chọn cột trước khi làm sạch: giữ nguyên 125.855 dòng và mọi giá trị, giảm từ 40 xuống 21 cột. Dung lượng bộ nhớ DataFrame giảm từ 576,87 MB xuống 75,43 MB (86,92%). Làm sạch ở notebook `01_data_quality` mới sửa định dạng, giá trị thiếu ẩn, dòng trùng và mâu thuẫn có căn cứ; so sánh trước/sau nằm ở mục B8 và chương 3 của báo cáo cuối kỳ.
