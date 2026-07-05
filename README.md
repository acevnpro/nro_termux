# 🐉 Dự Án Cài Đặt & Chạy Server NRO Trên Termux

Chào mừng bạn đến với **hướng dẫn chi tiết** thiết lập Server Ngọc Rồng Online (NRO) bằng Python ngay trên ứng dụng Termux. Bài viết này sẽ giúp bạn từng bước cài đặt, cấu hình và trải nghiệm game một mình hoặc cùng bạn bè một cách dễ dàng nhất!

---

## 📑 Mục Lục
1. [Cộng đồng & Hỗ trợ](#-cộng-đồng--hỗ-trợ)
2. [Lưu ý quan trọng](#-lưu-ý-quan-trọng-về-ngrok--cloudflare)
3. [Tài nguyên cần tải về](#-tài-nguyên-cần-tải-về)
4. [Các bước cài đặt trên Termux](#-các-bước-cài-đặt-trên-termux)
5. [Hướng dẫn thao tác trong ứng dụng](#-hướng-dẫn-thao-tác-trong-ứng-dụng)
6. [Kết nối vào game & chơi chung](#-hướng-dẫn-kết-nối-vào-game--chơi-chung)

---

## 🌐 Cộng Đồng & Hỗ Trợ

Tham gia ngay các nhóm cộng đồng dưới đây để cùng thảo luận, giao lưu và nhận hỗ trợ khi gặp lỗi:

| Nền tảng | Liên kết |
|----------|----------|
| **Facebook Group** (Phở Bò) | [Cộng đồng NRO Termux](https://www.facebook.com/groups/nro.termux) |
| **Nhóm Zalo** | [Tham gia Nhóm Zalo](https://zalo.me/g/nran3u1pi3hgm9mq5mpc) |
| **Video hướng dẫn chi tiết** | [Xem trên YouTube](https://www.youtube.com/watch?v=D4LTha2tiVU) |

---

## ⚠️ Lưu Ý Quan Trọng (Về Ngrok & Cloudflare)

> 💡 **Mẹo nhỏ:** Ở phiên bản mới, nếu sử dụng **Ngrok** thì tài khoản của bạn bắt buộc phải ép thẻ Visa để xác minh danh tính.  
> Tuy nhiên, web tạo tài khoản này hiện đã tích hợp **Cloudflare Free**, giúp bạn có thể bật thoải mái **hoàn toàn miễn phí** mà không cần xác minh thẻ phức tạp!

---

## 📂 Tài Nguyên Cần Tải Về

Trước khi tiến hành cài đặt, hãy tải đầy đủ các file cần thiết sau:

| Tệp tin | Mô tả | Link tải |
|---------|-------|----------|
| **Thư mục tổng hợp** | Chứa toàn bộ công cụ, bao gồm khung chỉnh sửa, `antigravity`, `src`, `nro.py` | [Tải tại đây](https://drive.google.com/drive/folders/1m9yQjo7JuaKr8So16u8k2hkGrO-xVL9V?usp=sharing) |
| **Mã nguồn Game (Source)** | File nguồn cần giải nén trong thư mục **Download** của điện thoại | [Tải file Src](https://drive.google.com/file/d/17wqWUp3avOhv6xkgbX03joR3zLH6A7i1/view?usp=sharing) |
| **Termux APK** | Phiên bản GitHub v0.118.3 (bỏ qua nếu đã cài) | [Tải Termux](https://github.com/termux/termux-app/releases/tag/v0.118.3) |

---

## 🛠️ Các Bước Cài Đặt Trên Termux

> **Hướng dẫn:** Mở ứng dụng **Termux**, sao chép và dán lần lượt các lệnh bên dưới (bấm `Enter` sau mỗi lệnh).

### 🔹 Bước 1: Giữ Termux chạy ngầm
```bash
termux-wake-lock
