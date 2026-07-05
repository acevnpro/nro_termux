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
> 
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

Mở ứng dụng Termux lên, sao chép và dán lần lượt các lệnh sau (bấm Enter sau mỗi block lệnh):

### 1. Giữ cho Termux luôn chạy ngầm
```bash
termux-wake-lock
