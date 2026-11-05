# Data Dictionary

```python
steam_columns_dict = {
    "AppID": {
        "vietnamese_name": "Mã định danh game (App ID)",
        "meaning": "Mã số định danh độc nhất của mỗi trò chơi trên hệ thống Steam.",
        "data_type": "int64 / str"
    },
    "Name": {  
        "vietnamese_name": "Tên trò chơi",
        "meaning": "Tên chính thức của tựa game trên Steam.",
        "data_type": "str"
    },
    "Release date": {
        "vietnamese_name": "Ngày phát hành",
        "meaning": "Thời gian (ngày, tháng, năm) tựa game chính thức ra mắt trên Steam.",
        "data_type": "str"
    },
    "Estimated owners": {
        "vietnamese_name": "Ước tính số lượng người sở hữu",
        "meaning": "Khoảng ước tính số lượng người đã mua hoặc sở hữu trò chơi.",
        "data_type": "str"
    },
    "Peak CCU": {
        "vietnamese_name": "Đỉnh điểm người chơi đồng thời",
        "meaning": "Số người chơi cùng lúc cao nhất trong một ngày, không phải đỉnh trong lịch sử của game (xem ghi chú ở bảng bên dưới).",
        "data_type": "int64"
    },
    "Required age": {
        "vietnamese_name": "Độ tuổi yêu cầu",
        "meaning": "Giới hạn độ tuổi tối thiểu được phép chơi (ví dụ: 0, 18...).",
        "data_type": "float64 / int64"
    },
    "Price": {
        "vietnamese_name": "Giá tiền",
        "meaning": "Giá bán hiện tại của trò chơi (tính bằng USD hoặc đơn vị tiền tệ gốc).",
        "data_type": "float64"
    },
    # LƯU Ý: trong file gốc, tên cột "DiscountDLC count" thật ra là 2 cột bị dính vào nhau
    # ("Discount" và "DLC count"). Header chỉ có 39 tên nhưng mỗi dòng có 40 giá trị,
    # nên khi đọc file gốc phải tách thành 2 tên cột (xem notebook 00_reduce_raw).
    "Discount": {
        "vietnamese_name": "Mức giảm giá",
        "meaning": "Phần trăm giảm giá hiện tại của trò chơi (0-100).",
        "data_type": "int64"
    },
    "DLC count": {
        "vietnamese_name": "Số lượng DLC",
        "meaning": "Số gói nội dung tải thêm (DLC) của trò chơi.",
        "data_type": "int64"
    },

    # Các cột từ 8 đến 38
    "About the game": {
        "vietnamese_name": "Giới thiệu về game",
        "meaning": "Mô tả chi tiết nội dung, cốt truyện hoặc giới thiệu tổng quan về tựa game.",
        "data_type": "str"
    },
    "Supported languages": {
        "vietnamese_name": "Ngôn ngữ được hỗ trợ",
        "meaning": "Danh sách các ngôn ngữ (giao diện, phụ đề) mà trò chơi hỗ trợ.",
        "data_type": "str"
    },
    "Full audio languages": {
        "vietnamese_name": "Ngôn ngữ lồng tiếng đầy đủ",
        "meaning": "Danh sách các ngôn ngữ có hỗ trợ lồng tiếng (âm thanh giọng nói) trong game.",
        "data_type": "str"
    },
    "Reviews": {
        "vietnamese_name": "Đánh giá / Tổng quan đánh giá",
        "meaning": "Tóm tắt mức độ đánh giá của người dùng trên Steam.",
        "data_type": "str"
    },
    "Header image": {
        "vietnamese_name": "Ảnh tiêu đề",
        "meaning": "Đường dẫn URL chứa hình ảnh banner/thumbnail chính thức của trò chơi.",
        "data_type": "str"
    },
    "Website": {
        "vietnamese_name": "Trang web chính thức",
        "meaning": "Đường dẫn URL trang web của nhà phát triển hoặc trang web chính thức của game.",
        "data_type": "str"
    },
    "Support url": {
        "vietnamese_name": "Đường dẫn hỗ trợ",
        "meaning": "Link trang web hoặc cổng thông tin để người chơi gửi yêu cầu hỗ trợ, báo lỗi.",
        "data_type": "str"
    },
    "Support email": {
        "vietnamese_name": "Email hỗ trợ",
        "meaning": "Địa chỉ email liên hệ của nhà phát hành/phát triển.",
        "data_type": "str"
    },
    "Windows": {
        "vietnamese_name": "Hỗ trợ Windows",
        "meaning": "Xác định game có chạy được trên hệ điều hành Windows hay không (True/False).",
        "data_type": "bool"
    },
    "Mac": {
        "vietnamese_name": "Hỗ trợ Mac",
        "meaning": "Xác định game có chạy được trên hệ điều hành macOS hay không (True/False).",
        "data_type": "bool"
    },
    "Linux": {
        "vietnamese_name": "Hỗ trợ Linux",
        "meaning": "Xác định game có chạy được trên hệ điều hành Linux hay không (True/False).",
        "data_type": "bool"
    },
    "Metacritic score": {
        "vietnamese_name": "Điểm Metacritic",
        "meaning": "Điểm số đánh giá tổng hợp từ các nhà phê bình game chuyên nghiệp.",
        "data_type": "int64 / float64"
    },
    "Metacritic url": {
        "vietnamese_name": "Đường dẫn Metacritic",
        "meaning": "Đường dẫn URL đến trang chi tiết đánh giá của game trên Metacritic.",
        "data_type": "str"
    },
    "User score": {
        "vietnamese_name": "Điểm người dùng",
        "meaning": "Điểm số đánh giá trung bình do chính người dùng thực tế chấm.",
        "data_type": "float64"
    },
    "Positive": {
        "vietnamese_name": "Số lượng đánh giá tích cực",
        "meaning": "Tổng số lượt đánh giá mang chiều hướng tích cực từ người chơi.",
        "data_type": "int64"
    },
    "Negative": {
        "vietnamese_name": "Số lượng đánh giá tiêu cực",
        "meaning": "Tổng số lượt đánh giá mang chiều hướng tiêu cực từ người chơi.",
        "data_type": "int64"
    },
    "Score rank": {
        "vietnamese_name": "Xếp hạng điểm số",
        "meaning": "Thứ hạng điểm số của game so với các tựa game khác trên hệ thống.",
        "data_type": "float64 / int64"
    },
    "Achievements": {
        "vietnamese_name": "Số lượng thành tựu",
        "meaning": "Tổng số lượng huy hiệu hoặc thành tựu có thể đạt được trong game.",
        "data_type": "int64"
    },
    "Recommendations": {
        "vietnamese_name": "Số lượt giới thiệu/đề xuất",
        "meaning": "Số lượng lượt đề xuất hoặc giới thiệu game từ cộng đồng người chơi.",
        "data_type": "int64"
    },
    "Notes": {
        "vietnamese_name": "Ghi chú thêm",
        "meaning": "Các thông tin bổ sung, lưu ý hoặc ghi chú đặc biệt về trò chơi.",
        "data_type": "str"
    },
    "Average playtime forever": {
        "vietnamese_name": "Thời gian chơi trung bình (tổng)",
        "meaning": "Số phút trung bình người chơi dành ra để chơi tựa game này từ trước đến nay.",
        "data_type": "int64"
    },
    "Average playtime two weeks": {
        "vietnamese_name": "Thời gian chơi trung bình (2 tuần gần nhất)",
        "meaning": "Số phút trung bình người chơi đã bỏ ra để chơi game trong vòng 2 tuần qua.",
        "data_type": "int64"
    },
    "Median playtime forever": {
        "vietnamese_name": "Trung vị thời gian chơi (tổng)",
        "meaning": "Giá trị trung vị của tổng thời gian chơi game tính bằng phút.",
        "data_type": "int64"
    },
    "Median playtime two weeks": {
        "vietnamese_name": "Trung vị thời gian chơi (2 tuần gần nhất)",
        "meaning": "Giá trị trung vị của thời gian chơi trong vòng 2 tuần qua tính bằng phút.",
        "data_type": "int64"
    },
    "Developers": {
        "vietnamese_name": "Nhà phát triển",
        "meaning": "Tên của cá nhân, nhóm hoặc công ty trực tiếp lập trình trò chơi.",
        "data_type": "str"
    },
    "Publishers": {
        "vietnamese_name": "Nhà phát hành",
        "meaning": "Tên công ty đứng ra chịu trách nhiệm thương mại hóa và phát hành trò chơi.",
        "data_type": "str"
    },
    "Categories": {
        "vietnamese_name": "Danh mục tính năng",
        "meaning": "Các tính năng hỗ trợ của game trên Steam (ví dụ: Single-player, Multiplayer...).",
        "data_type": "str"
    },
    "Genres": {
        "vietnamese_name": "Thể loại game",
        "meaning": "Phân loại thể loại chính của trò chơi (ví dụ: Action, Indie, Strategy, RPG...).",
        "data_type": "str"
    },
    "Tags": {
        "vietnamese_name": "Thẻ mô tả (Tags)",
        "meaning": "Các từ khóa do cộng đồng người chơi tự đặt để mô tả phong cách, chủ đề.",
        "data_type": "str"
    },
    "Screenshots": {
        "vietnamese_name": "Ảnh chụp màn hình",
        "meaning": "Danh sách các đường dẫn URL chứa hình ảnh chụp màn hình gameplay.",
        "data_type": "str"
    },
    "Movies": {
        "vietnamese_name": "Video trailer/phim giới thiệu",
        "meaning": "Danh sách các đường dẫn URL chứa video trailer hoặc đoạn phim ngắn quảng cáo.",
        "data_type": "str"
    }
}
```

## Bộ dữ liệu dùng để phân tích

Hai file trong `data/processed/` có cùng 21 cột. `games_reduced.csv` được tạo ở notebook `00_reduce_raw`, giữ nguyên mọi dòng của file gốc. `games_cleaned.csv` được tạo ở notebook `01_data_quality` sau khi làm sạch.

| Cột | Ý nghĩa | Kiểu dữ liệu | Ghi chú sau khi làm sạch |
|---|---|---|---|
| id | Mã game trên Steam | int64 | Đổi tên từ `AppID` ở notebook 00 |
| Name | Tên game | str | Gộp khoảng trắng thừa; 1 tên thiếu được điền "Unknown" |
| Release date | Ngày phát hành | datetime | Đổi từ chuỗi "Jul 29, 2016" sang ngày tháng |
| Estimated owners | Khoảng số người sở hữu ước tính | str | Dạng "min - max"; "0 - 0" là thiếu dữ liệu, dòng được giữ trong file nhưng bị bỏ khi phân tích độ phổ biến |
| Peak CCU | Số người chơi đồng thời cao nhất trong một ngày | int64 | SteamSpy định nghĩa cột này là đỉnh của ngày hôm trước, nên 0 nghĩa là không ghi nhận người chơi vào ngày đó, không phải game chưa từng có người chơi. Trang Kaggle chưa đọc được nên đây là suy ra từ nguồn SteamSpy |
| Price | Giá bán hiện tại (USD) | float64 | |
| Discount | Mức giảm giá (%) | int64 | Game giá 0 có giảm giá 1-99% được đặt về 0 |
| DLC count | Số DLC | int64 | |
| Positive | Số đánh giá tích cực | int64 | |
| Negative | Số đánh giá tiêu cực | int64 | |
| User score | Điểm người dùng (1-100) | float64 | 0 được đổi thành trống (NaN) vì 0 = chưa có điểm; chỉ 40 game có điểm |
| Metacritic score | Điểm Metacritic (1-100) | float64 | 0 được đổi thành trống (NaN) vì 0 = chưa có điểm |
| Recommendations | Số lượt đề xuất | int64 | Steam chỉ hiện khi có trên 100 lượt, nên giá trị khác 0 nhỏ nhất là 101 |
| Achievements | Số thành tựu | int64 | |
| Average playtime forever | Thời gian chơi trung bình từ trước đến nay (phút) | int64 | |
| Average playtime two weeks | Thời gian chơi trung bình 2 tuần gần nhất (phút) | int64 | |
| Median playtime forever | Thời gian chơi trung vị từ trước đến nay (phút) | int64 | |
| Median playtime two weeks | Thời gian chơi trung vị 2 tuần gần nhất (phút) | int64 | |
| Categories | Danh sách tính năng, cách nhau bởi dấu phẩy | str | Bỏ nhãn lặp; giá trị thiếu để trống |
| Genres | Danh sách thể loại, cách nhau bởi dấu phẩy | str | Giá trị thiếu để trống |
| Tags | Danh sách thẻ do người chơi gắn, cách nhau bởi dấu phẩy | str | Giá trị thiếu để trống (thiếu vì game chưa có đánh giá) |

Các chỉ số tính thêm khi phân tích (tính trong notebook `02_eda`, `02b_eda_rq3_rq4` và lưu trong `games_features.csv`):

- **Owners_mid**: điểm giữa của khoảng `Estimated owners`.
- **Total reviews** = Positive + Negative.
- **Positive ratio** = Positive / Total reviews × 100, chỉ tính cho game có từ 10 đánh giá.
- **Nhóm giá**: Miễn phí (0), Thấp (dưới 5 USD), Trung bình (5 đến dưới 15 USD), Cao (từ 15 USD).

## Bộ dữ liệu cho mô hình

`games_features.csv` được tạo ở notebook `03_ml_readiness`, gồm 100.025 game và 43 cột. File này đã bỏ nhóm owners = "0 - 0", năm 2026 và các game thiếu Genres hoặc Categories. Ngoài các cột giữ lại từ `games_cleaned.csv` và các chỉ số ở trên, file có thêm:

| Cột | Ý nghĩa |
|---|---|
| Năm phát hành | Năm trong `Release date` |
| Giai đoạn | Trước 2014, 2014-2017, 2018-2020, 2021-2023, 2024-2025 |
| log_price, log_reviews, log_playtime, log_achievements | log1p của Price, Total reviews, Median playtime forever, Achievements |
| is_free | 1 nếu Price = 0 |
| has_achievements | 1 nếu game có Achievements |
| has_ccu | Nhãn phân loại: 1 nếu Peak CCU > 0 |
| n_genres | Số thể loại của game |
| genre_... | 10 cờ 0/1 theo thể loại: Indie, Casual, Action, Adventure, Simulation, Strategy, RPG, Sports, Racing, Massively Multiplayer |
| cat_... | 6 cờ 0/1 theo tính năng: Single-player, Multi-player, Co-op, Online PvP, Steam Cloud, Full controller support |
| split | train hoặc test (80% và 20%) |
