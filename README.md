# 🐉 Dự án Cài Đặt và Chạy Server NRO trên Termux

Chào mừng bạn đến với dự án setup Server Ngọc Rồng Online (NRO) bằng Python trên ứng dụng Termux. Dưới đây là hướng dẫn chi tiết từ A-Z để bạn có thể tự cài đặt và trải nghiệm game một mình hoặc cùng bạn bè!

---

## 🌐 Cộng Đồng & Kênh Hỗ Trợ

Tham gia ngay các nhóm cộng đồng dưới đây để cùng thảo luận, giao lưu và nhận hỗ trợ khi gặp lỗi:

* **Phở Bò (Facebook Group):** [Cộng đồng NRO Termux](https://www.facebook.com/groups/nro.termux)
* **Nhóm Zalo hỗ trợ:** [Tham gia Nhóm Zalo](https://zalo.me/g/nran3u1pi3hgm9mq5mpc)
* **Video Hướng Dẫn Chi Tiết:** [Xem trên YouTube](https://www.youtube.com/watch?v=D4LTha2tiVU)

---

## ⚠️ Lưu Ý Quan Trọng (Về Ngrok & Cloudflare)

> 💡 **Mẹo nhỏ:** Ở phiên bản mới, nếu sử dụng **Ngrok** thì tài khoản của bạn bắt buộc phải ép thẻ Visa để xác minh danh tính.  
> Tuy nhiên, web tạo tài khoản này hiện đã tích hợp **Cloudflare Free**, giúp bạn có thể bật thoải mái hoàn toàn miễn phí mà không cần xác minh thẻ phức tạp!

---

## 📂 Tài Nguyên Tải Về

Trước khi tiến hành cài đặt, hãy tải đầy đủ các file cần thiết sau đây:

1.  **Thư mục tổng hợp:** [Tất cả file cần thiết cho dự án](https://drive.google.com/drive/folders/1m9yQjo7JuaKr8So16u8k2hkGrO-xVL9V?usp=sharing)  
    *(Tải và giải nén toàn bộ công cụ, bao gồm file khung chỉnh sửa ném vào thư mục `antigravity` cùng với `src` và `nro.py`)*.
2.  **Mã nguồn Game (Source):** [Tải file Src tại đây](https://drive.google.com/file/d/17wqWUp3avOhv6xkgbX03joR3zLH6A7i1/view?usp=sharing)  
    *(Tải về và giải nén trong thư mục **Download** của điện thoại)*.
3.  **Ứng dụng Termux:** [Tải Termux bản GitHub (v0.118.3)](https://github.com/termux/termux-app/releases/tag/v0.118.3)  
    *(Nếu điện thoại đã cài bản này rồi thì có thể bỏ qua)*.

---

## 🛠️ Các Bước Cài Đặt Trên Termux

Mở ứng dụng Termux lên, sao chép và dán lần lượt các lệnh sau (bấm Enter sau mỗi ô lệnh):

### 1. Giữ cho Termux luôn chạy ngầm
termux-wake-lock

### 2. Cập nhật hệ thống Termux
pkg update && pkg upgrade -y

### 3. Cấp quyền truy cập bộ nhớ điện thoại (Bắt buộc)
termux-setup-storage

> 🔴 **LƯU Ý CỰC KỲ QUAN TRỌNG:** Khi hệ thống hiển thị thông báo trên màn hình điện thoại, bạn phải bấm chọn **Cho phép (Allow)** thì Termux mới có thể đọc được file game đã giải nén trong máy.

### 4. Cài đặt Python và gói Wget
pkg install python wget -y

### 5. Tải file script vận hành Server
wget https://github.com/acevnpro/nro_termux/releases/download/v1.2/nro.py

*Nếu lệnh `wget` ở trên bị lỗi, hãy dùng lệnh `curl` thay thế dưới đây:*
curl -O https://github.com/acevnpro/nro_termux/releases/download/v1.2/nro.py

### 6. Khởi chạy Tool quản lý
python nro.py

---

## 🎮 Hướng Dẫn Thao Tác Trong Ứng Dụng

Khi giao diện ứng dụng quản lý hiện lên, bạn tiến hành bấm chọn theo đúng thứ tự các con số sau để setup:

* **Bước 1:** Chọn `1` -> Chọn `2` *(Hãy tìm và chọn chính xác mục **SrcVipByVanTuan_termux**)*.
* **Bước 2:** Chọn `3` -> Chọn `4` *(Tại đây bạn có thể chọn mục **Offline** hoặc **Online** tùy thuộc vào nhu cầu)*.
* **Bước 3:** Chọn `5` -> Chọn `6` *(Nếu hệ thống hiển thị chữ **OK**, bạn có thể bỏ qua bước số 7)*.
* **Bước 4:** Chọn `8` -> Chọn tiếp `1`.
* **Bước 5 (Mở tab mới):** Chọn `9` -> Chọn `1`.

> 💡 **Mẹo mở tab nhanh:** Bạn hãy vuốt nhẹ nhàng từ cạnh bên trái phía trên màn hình sang phải để mở menu ẩn của Termux, sau đó chọn tạo Tab mới.

---

## 📱 Hướng Dẫn Kết Nối Vào Game & Chơi Chung

* **Vào game:** Cài đặt và mở file game `.apk` nằm trong file zip được cung cấp sẵn là có thể vào chơi ngay.
* **Cách chơi chung mạng Wifi:** Để chia sẻ cho máy khác chơi cùng trong một mạng Wifi, bạn chỉ cần lấy địa chỉ IP của máy chủ (máy đang chạy server) rồi nhập vào bản game trên máy của bạn bè là xong.
* **Lưu ý khi đổi IP:** Thỉnh thoảng modem Wifi sẽ tự động reset và đổi địa chỉ IP của máy bạn. Lúc này dữ liệu game của bạn không hề bị mất, bạn chỉ cần thực hiện lại từ **Bước 4** trong app để cập nhật lại IP mới là có thể tiếp tục chơi bình thường!

---
❤️ *Hãy cùng hoàn thiện khung chỉnh sửa chạy cho Termux, fix sạch lỗi và chia sẻ rộng rãi thành quả cho mọi người cùng trải nghiệm nhé! Chúc các bạn chơi game vui vẻ!*
