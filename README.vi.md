# Tredecadia

[English](README.md) · **Tiếng Việt** · [Tất cả ngôn ngữ](README.languages.md)

Tredecadia là một dự án mở về lịch vĩnh cửu gồm **13 tháng, mỗi tháng 28 ngày**. Mỗi tháng có đúng bốn tuần, nên cùng một ngày trong tháng luôn nằm ở cùng một vị trí trong chu kỳ tuần. Những ngày dùng để điều chỉnh độ dài năm được đặt ngoài tháng và ngoài chu kỳ tuần bảy ngày.

> **Phiên bản công khai hiện tại: `1.1.0-rc.1`.**

## Cấu trúc cơ bản

- 13 × 28 = 364 ngày thông thường nằm trong các tháng.
- Mỗi tháng gồm đúng bốn tuần trọn vẹn.
- Ngày `01` luôn là **Mene (`W1`)**, ngày `28` luôn là **Toze (`W7`)**.
- `EQ` — **Ngày Xuân phân / Năm mới** — mở đầu mỗi năm và không thuộc tháng hay tuần nào.
- Trong năm nhuận, sau `13-28` có thêm `ED` — **Ngày Trái Đất** — rồi mới đến `EQ` của năm tiếp theo.

Chu kỳ bảy ngày chuẩn:

`W1 Mene → W2 Noko → W3 Kese → W4 Zoyo → W5 Sote → W6 Yemo → W7 Toze`

Các tên này là định danh chuẩn của Tredecadia, không phải bản dịch hay đổi tên của thứ Hai đến Chủ nhật. RC2 chưa định nghĩa các bí danh ngày trong tuần đã được thẩm định cho tiếng Việt, vì vậy dùng trực tiếp dạng Latinh chuẩn.

Năm thường:

`Y-EQ → Y-01-01 → … → Y-13-28 → (Y+1)-EQ`

Năm nhuận:

`Y-EQ → Y-01-01 → … → Y-13-28 → Y-ED → (Y+1)-EQ`

## Kỷ nguyên Tredecadia

Tredecadia dùng một trục số nguyên liên tục cho năm và có **năm 0 thực sự**. Vì vậy bên trong lịch không cần chia thời gian thành hai kỷ nguyên riêng.

Các chữ viết tắt tiếng Anh **BCE/CE** là **Before Common Era / Common Era**, tương ứng với cách nói **trước Công nguyên / Công nguyên**.

Mốc gốc toán học:

`TE 00000-EQ ↔ năm Gregory thiên văn -9999, ngày 20 tháng 3`

Theo cách ghi lịch sử thông thường, mốc này tương ứng với **năm 10000 trước Công nguyên (`10000 BCE`)**. Nó không được coi là “khởi đầu của loài người”, của nền văn minh hay của một giai đoạn lịch sử nào; đây chỉ là điểm 0 toán học của trục năm Tredecadia.

Đối với chuyển đổi dân dụng:

`năm TE = năm Gregory thiên văn + 9999`

Vì vậy năm 2026 Công nguyên tương ứng với **TE 12025**.

## Định dạng ngày

Dạng chuẩn để trao đổi dữ liệu dùng ASCII nghiêm ngặt và phần năm có ít nhất năm chữ số:

`12025-07-11` · `00000-EQ` · `-00001-01-01`

Giao diện dành cho người dùng có thể bỏ các số 0 ở đầu và dùng dấu trừ kiểu chữ cho năm âm. Đó chỉ là cách hiển thị, không phải một định danh chuẩn khác.

## Các tháng

Tên tháng là các định danh quốc tế cố định và trong tiếng Việt có thể dùng trực tiếp dạng Latinh chuẩn.

| # | Tên đầy đủ | Dạng rút gọn 3 âm tiết (`Short-6`) | Dạng nói 2 âm tiết (`Short-4`) |
|---:|---|---|---|
| 01 | Masanumika | Masanu | Masa |
| 02 | Tasuzunumu | Tasuzu | Tasu |
| 03 | Nazumasanu | Nazuma | Nazu |
| 04 | Mikasumani | Mikasu | Mika |
| 05 | Yanimuzunu | Yanimu | Yani |
| 06 | Zumitanasu | Zumita | Zumi |
| 07 | Muyasanumi | Muyasa | Muya |
| 08 | Sunizusaka | Sunizu | Suni |
| 09 | Numanamuta | Numana | Numa |
| 10 | Kazunusuya | Kazunu | Kazu |
| 11 | Yanazumasa | Yanazu | Yana |
| 12 | Sanumikazu | Sanumi | Sanu |
| 13 | Nimutazuna | Nimuta | Nimu |

Trong giao tiếp, dạng hai âm tiết được ưu tiên khi ngữ cảnh đã cho thấy rõ đang nói về một tháng. Cách đọc tham chiếu dùng **độ nhấn nhẹ ở âm tiết đầu**; trọng âm không phải là một phần của danh tính tên tháng.

## Đặc tả và mã nguồn

Bộ chuyển đổi tham chiếu bằng Python nằm tại [`reference/python/tredecadia.py`](reference/python/tredecadia.py). Tài liệu quy chuẩn ở [`specification/`](specification/), còn các sổ đăng ký máy đọc được ở [`registry/`](registry/).

README này là phần giới thiệu dành cho người đọc tiếng Việt và không thay thế đặc tả quy chuẩn.

## Giấy phép

Tài liệu, đặc tả và dữ liệu: **CC BY 4.0**. Mã nguồn và tập lệnh: **MIT**, trừ khi có ghi chú khác. Xem [`LICENSE.md`](LICENSE.md).
