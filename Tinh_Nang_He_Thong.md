# 🎮 NRO VNPro4 – Bộ Công Cụ Quản Lý Game NRO Trên Termux đây là kịch bản dành riêng cho src_4 các phiên bản src khác có thể sẽ khác biệt!

> Dự án mã nguồn mở, **HOÀN TOÀN MIỄN PHÍ**, được chia sẻ bởi Nhiều nguồn!  
> Nếu ai bắt bạn trả phí — đó là **SCAM**!

**NRO VNPro** là bộ công cụ CLI (Command Line Interface) chạy trên **Termux** (Android), giúp bạn **cài đặt, cấu hình, biên dịch và vận hành** một máy chủ game NRO ngay trên điện thoại mà không cần máy tính hay VPS.

---

## 📋 Mục Lục

- [Yêu Cầu Hệ Thống](#-yêu-cầu-hệ-thống)
- [Bắt Đầu Nhanh](#-bắt-đầu-nhanh)
- [Tổng Quan Menu Chính](#-tổng-quan-menu-chính)
- [Hướng Dẫn Chi Tiết Từng Tính Năng](#-hướng-dẫn-chi-tiết-từng-tính-năng)
  - [\[1\] Cài Đặt Môi Trường](#1-cài-đặt-môi-trường)
  - [\[2\] Giải Nén Source Game](#2-giải-nén-source-game)
  - [\[3\] Thiết Lập Database & Web](#3-thiết-lập-database--web)
  - [\[4\] Cấu Hình Kết Nối (Online/Offline)](#4-cấu-hình-kết-nối-onlineoffline)
  - [\[5\] Vá IP & Build Game](#5-vá-ip--build-game)
  - [\[6\] Cấu Hình RAM & Swap](#6-cấu-hình-ram--swap)
  - [\[7\] Quản Lý Dịch Vụ LEMP / KSWEB](#7-quản-lý-dịch-vụ-lemp--ksweb)
  - [\[8\] Vận Hành Game Server](#8-vận-hành-game-server)
  - [\[9\] Quản Lý Tài Khoản](#9-quản-lý-tài-khoản)
  - [\[W\] Quản Lý Giao Diện Web & Admin](#w-quản-lý-giao-diện-web--admin)
  - [\[A\] Tự Động Sao Lưu Xoay Vòng](#a-tự-động-sao-lưu-xoay-vòng-backup-daemon)
  - [\[B\] Giám Sát Tiến Trình TMux](#b-giám-sát-tiến-trình-tmux)
  - [\[K\] Chuyển Đổi Backend (LEMP ↔ KSWEB)](#k-chuyển-đổi-backend-lemp--ksweb)
  - [\[D\] Làm Mới Kết Nối Nhanh](#d-làm-mới-kết-nối-nhanh)
- [Cộng Đồng & Liên Hệ](#-cộng-đồng--liên-hệ)

---

## 📱 Yêu Cầu Hệ Thống

| Thành phần | Yêu cầu |
|---|---|
| **Thiết bị** | Điện thoại Android (khuyến nghị ARM64) |
| **Ứng dụng** | [Termux](github) hoặc (bản F-Droid) không dùng bản Playstore| 
| **RAM** | Tối thiểu 2GB (khuyến nghị 4GB+) |
| **Bộ nhớ** | Tối thiểu 2GB trống |
| **Tùy chọn** | App **KSWEB** (nếu LEMP bị lỗi trên máy bạn) |
| **Tùy chọn** | Tài khoản **Ngrok** miễn phí (chơi Online) nhưng chỉ được 1GB/ tháng khuyến nghị dùng VPN Tailscale |

---

## 🚀 Bắt Đầu Nhanh

```bash
# 1. Mở Termux và cấp quyền bộ nhớ
termux-setup-storage

# 2. Tải file nro4.py về thư mục Home (~/)
```bash
curl -LO https://github.com/acevnpro/nro_termux/releases/download/v1.2/nro4.py
```

# 3. Chạy kịch bản
python nro4.py
```

**Quy trình thiết lập lần đầu tiên theo thứ tự:**
```
[1] Cài đặt Môi trường → [2] Giải nén Source → [3] Thiết lập Database & Web
→ [4] Cấu hình kết nối → [5] Vá IP & Build → [8] Chạy Game Server
```

---

## 🖥️ Tổng Quan Menu Chính

Khi chạy `python nro4.py`, bạn sẽ thấy Menu chính hiển thị đầy đủ thông tin:

```
==========================================
      NRO VNPro4 - Danh Rieng Cho SRC_4
==========================================
 RAM: [████████████░░░░░░░░] 60% (1843MB/3072MB)
 IP:  192.168.1.7 | MODE: OFFLINE | BACKEND: TERMUX (LEMP)
 WEB ĐĂNG KÝ: http://192.168.1.7:8080
 PHPMYADMIN:  http://192.168.1.7:8081
------------------------------------------
 [1] Cài đặt môi trường hệ thống
 [2] Giải nén Source game (Scan Download)
 [3] Thiết lập Database & Web (Auto Fix)
 [4] Cấu hình Kết nối (Online/Offline)
 [5] Vá IP & Build Game
 [6] Cấu hình RAM & Swap (Hybrid)
 [7] Quản lý Dịch vụ LEMP / KSWEB
 [8] VẬN HÀNH GAME SERVER
 [9] QUẢN LÝ TÀI KHOẢN
 [W] QUẢN LÝ GIAO DIỆN WEB ĐĂNG KÝ
 [A] TỰ ĐỘNG SAO LƯU XOAY VÒNG (BACKUP DAEMON)
 [B] GIÁM SÁT TIẾN TRÌNH TMUX
 [K] CHUYỂN ĐỔI BACKEND (LEMP ↔ KSWEB)
 [D] LÀM MỚI KẾT NỐI NHANH
 [0] THOÁT CHƯƠNG TRÌNH
------------------------------------------
```

---

## 📖 Hướng Dẫn Chi Tiết Từng Tính Năng

---

### [1] Cài Đặt Môi Trường

> **Mục đích:** Cài đặt tất cả các gói phần mềm cần thiết để chạy máy chủ game trên Termux.

**Cách sử dụng:**
1. Chọn `[1]` từ Menu chính.
2. Chọn kiến trúc Web & Database:
   - **`[1] LEMP Termux`** *(Mặc định)*: Cài đầy đủ MariaDB, Nginx, PHP-FPM, Java 17, Maven, Ant, TMux, Ngrok và các công cụ hỗ trợ.
   - **`[2] KSWEB`** *(Dành cho máy bị lỗi CSDL)*: Chỉ cài Java 17, Maven và các công cụ thiết yếu. Web & MySQL sẽ do app KSWEB đảm nhận.
3. Hệ thống sẽ tự động `pkg update`, `apt upgrade` và cài đặt toàn bộ gói cần thiết.
4. Nếu chọn LEMP, Nginx sẽ được cấu hình tự động với 2 cổng:
   - **Port 8080**: Trang Web Đăng Ký tài khoản
   - **Port 8081**: phpMyAdmin quản lý Database

**⚠️ Lưu ý:** Bước này chỉ cần chạy **một lần duy nhất** sau khi cài Termux. Trạng thái `(OK)` sẽ hiển thị bên cạnh khi hoàn tất.

---

### [2] Giải Nén Source Game

> **Mục đích:** Quét và giải nén file source game (`.zip`, `.rar`, `.tar.gz`) từ thư mục Home hoặc Download của điện thoại.

**Cách sử dụng:**
1. Copy file source game (VD: `SRC_NRO.zip`) vào thư mục `/sdcard/Download/` hoặc `~/`.
2. Chọn `[2]` từ Menu chính.
3. Hệ thống sẽ liệt kê tất cả file nén tìm được, bạn chọn file cần giải nén.
4. Nếu phát hiện thư mục dự án cũ, hệ thống sẽ hỏi bạn có muốn xóa trước không.

**Sau khi giải nén, hệ thống tự động:**
- Quét tìm thư mục chứa `pom.xml` hoặc `build.xml` → Đặt vào `SrcVIP/`
- Quét tìm `ServerLogin/` → Đặt vào `ServerLogin/`
- Quét tìm file `.sql` → Đặt vào thư mục gốc dự án
- Các file thừa → Đặt vào `SanPhamMod_Thua/`

---

### [3] Thiết Lập Database & Web

> **Mục đích:** Tạo Database, Import SQL và sinh giao diện Web đăng ký tài khoản.

**Menu con:**
| Phím | Chức năng |
|---|---|
| `[1]` | **Tự động thiết lập** Database & Web (Auto Fix) — *Khuyên dùng cho lần đầu* |
| `[2]` | Chọn file `.sql` tùy chỉnh từ Termux/Download để Import thủ công |
| `[3]` | Xuất (Export/Backup) Database ra file `.sql` vào thư mục Download |

**Quy trình Auto Fix `[1]`:**
- **Chế độ LEMP:** Khởi động MariaDB → Tạo Database → Import SQL → Tạo Web đăng ký → Cài phpMyAdmin → Cấu hình Nginx → Khởi động LEMP.
- **Chế độ KSWEB:** Kết nối MySQL trên app KSWEB → Tạo Database → Import SQL → Deploy Web sang `/sdcard/htdocs/`.

**Trang Web đăng ký** có giao diện Dark Mode hiện đại, hỗ trợ:
- Đăng ký tài khoản game (username, password, email)
- Tùy chọn nạp VND test
- Tùy chọn kích hoạt quyền Admin
- Hiển thị IP kết nối game (copy 1 chạm)
- Liên kết nhóm Zalo & Facebook

---

### [4] Cấu Hình Kết Nối (Online/Offline)

> **Mục đích:** Cấu hình chế độ kết nối để người chơi có thể truy cập vào máy chủ game.

**Các chế độ kết nối:**

| Phím | Chế độ | Mô tả |
|---|---|---|
| `[1]` | Cài Ngrok | Tải và cài đặt Ngrok ARM64 cho Termux, nhập AuthToken |
| `[2]` | Khởi chạy Ngrok TCP | Chạy trực tiếp hoặc chạy ngầm qua TMux |
| `[3]` | Auto lấy link Ngrok | Tự động lấy IP:Port từ API Ngrok (Port 4040) |
| `[4]` | Nhập link thủ công | Hỗ trợ Ngrok / Playit / Bore |
| `[5]` | Offline LAN/WiFi | Dùng IP nội bộ máy, chơi cùng mạng WiFi |
| `[6]` | Offline Localhost | Chạy trên 127.0.0.1, chỉ chơi được trên chính máy đó |
| `[7]` | Cloudflare Tunnel | Mở cổng Web đăng ký qua Cloudflare (miễn phí, link tạm thời) |
| `[8]` | Ngrok Domain cố định | Mở cổng Web đăng ký qua Ngrok Static Domain (link không đổi) |

**💡 Mẹo:**
- Chơi **một mình / cùng WiFi** → Chọn `[5]`
- Chơi **online với bạn bè qua Internet** → Chọn `[1]` → `[2]` → `[3]`
- Muốn **trang đăng ký truy cập được từ Internet** → Chọn `[7]` hoặc `[8]`

---

### [5] Vá IP & Build Game

> **Mục đích:** Tự động vá tất cả file cấu hình Java với IP/Port/Database đúng, rồi biên dịch source thành file `.jar` chạy được.

**Quy trình tự động:**

1. **Vá `DBService.java` / `LocalManager.java`**: Cập nhật thông tin Database (Host, Name, User, Password). Tự động áp dụng JDBC Collation Patch cho MariaDB 11+.
2. **Vá `DataGame.java`**: Cập nhật `LINK_IP_PORT` với IP/Port kết nối.
3. **Vá `server.ini`** (Login Server): Ghi lại cổng và thông tin DB.
4. **Vá `server.properties`** (Game Server): Cập nhật toàn bộ thông số server.
5. **GUI Bypass cho `ServerManager.java`**: Comment tất cả mã GUI (JFrame, JPanel...) và vá hàm `canConnectWithIp()` luôn trả về `true`.
6. **Sửa lỗi BOM**: Quét toàn bộ file `.java` và xóa ký tự BOM ẩn gây lỗi biên dịch.
7. **Nâng cấp Lombok**: Tự động nâng lên phiên bản 1.18.32 (fix lỗi Java 17+).
8. **Nâng cấp MySQL Driver**: Cập nhật MySQL Connector lên 5.1.49 (fix MariaDB 11).
9. **Vá lỗi CPU âm / RAM ảo**: Tự động thay thế các hàm `getSystemCpuLoad()`, `getProcessCpuLoad()`, `getFreePhysicalMemorySize()` bằng biểu thức an toàn trên Termux.
10. **Biên dịch**: Tự động nhận diện Ant (`build.xml`) hoặc Maven (`pom.xml`) để build.

**⚠️ Lưu ý:** Mỗi khi đổi IP/chế độ kết nối, bạn cần chạy lại mục `[5]` để vá và build lại.

---

### [6] Cấu Hình RAM & Swap

> **Mục đích:** Tối ưu bộ nhớ RAM cấp phát cho JVM và thiết lập RAM ảo (Swap).

**Các chế độ RAM:**

| Phím | Chế độ | Mô tả |
|---|---|---|
| `[1]` | Tối ưu (Cân bằng) | Cân bằng giữa hiệu năng và tiết kiệm RAM. **Khuyên dùng.** |
| `[2]` | Hiệu năng cao | Cấp nhiều RAM hơn, phù hợp máy khỏe (≥4GB RAM). Dùng G1GC. |
| `[3]` | Tiết kiệm tối đa | Dành cho máy yếu (≤2GB RAM). Dùng SerialGC, giảm tối đa Metaspace. |
| `[4]` | Thiết lập Swap | Tạo RAM ảo (yêu cầu ROOT). Khuyến nghị 2048MB. |

**Hệ thống tự động:**
- Quét RAM thật và Swap hiện tại từ `/proc/meminfo`
- Đề xuất mức RAM phù hợp dựa trên cấu hình máy
- Hiển thị thanh tiến trình RAM trực quan

---

### [7] Quản Lý Dịch Vụ LEMP / KSWEB

> **Mục đích:** Bật/tắt và chẩn đoán lỗi các dịch vụ Web & Database.

**Chế độ LEMP (Termux):**

| Phím | Chức năng |
|---|---|
| `[1]` | Khởi chạy toàn bộ (MariaDB + PHP-FPM + Nginx) |
| `[2]` | Tắt toàn bộ dịch vụ |
| `[3]` | Hướng dẫn quản lý SQL bằng App ngoài (SQL Client, Termius...) |
| `[4]` | **Chẩn đoán chuyên sâu** — Quét cổng, kiểm tra config, chạy test cú pháp, hiển thị log lỗi |

**Chế độ KSWEB:**
- Hiển thị hướng dẫn cách bật Web & MySQL trên app KSWEB.

**💡 Mẹo:** Nếu LEMP không hoạt động trên máy bạn (do Android 12+ tự kill tiến trình nền), hãy:
- Chạy lệnh ADB: `adb shell device_config put activity_manager max_phantom_processes 2147483647`
- Hoặc chuyển sang dùng **KSWEB** bằng phím `[K]`.

---

### [8] Vận Hành Game Server

> **Mục đích:** Khởi chạy, giám sát và dừng Game Server.

**Các tùy chọn:**

| Phím | Chức năng |
|---|---|
| `[1]` | **Chạy trực tiếp** — Xem log realtime trên màn hình. Bấm `Ctrl+C` để dừng. |
| `[2]` | **Chạy ngầm (TMux + Watchdog)** — *Khuyên dùng*. Server chạy ổn định trong TMux session. |
| `[3]` | Dừng Server (Kill Port & Session) |

**🛡️ Hệ thống Watchdog thông minh (Chế độ ngầm):**
- Chờ Database online trước khi khởi động Server.
- Giám sát liên tục mỗi 5 giây.
- Nếu phát hiện mất kết nối: Đợi 20 giây → Kiểm tra lại → Tự động khởi động lại Server.
- Hoàn toàn tự vận hành, không cần can thiệp.

**💡 JVM Flags** được tối ưu tự động dựa trên chế độ RAM bạn đã chọn ở mục `[6]`.

---

### [9] Quản Lý Tài Khoản

> **Mục đích:** Quản lý tài khoản người chơi trực tiếp qua Terminal.

| Phím | Chức năng |
|---|---|
| `[1]` | Liệt kê danh sách 30 tài khoản gần nhất |
| `[2]` | Tạo tài khoản nhanh (Username + Password) |
| `[3]` | Đổi mật khẩu tài khoản |
| `[4]` | Xóa tài khoản khỏi Database |

---

### [W] Quản Lý Giao Diện Web & Admin

> **Mục đích:** Quản lý trang Web đăng ký và trang Admin Panel trên trình duyệt.

**Tại Menu `[W]` trên Terminal**, bạn sẽ thấy:
- Đường dẫn truy cập trang **Admin Web** (VD: `http://192.168.1.7:8080/admin.php`)
- Mật khẩu truy cập hiện tại (mặc định: `admin`)
- Tùy chọn `[1]` để đổi mật khẩu Admin Web

**Tại trang `admin.php` trên trình duyệt**, bạn có giao diện quản trị trực quan với 2 Tab:

| Tab | Chức năng |
|---|---|
| **Cài Đặt Form** | Bật/tắt ô nhập tiền VND, bật/tắt checkbox cấp quyền Admin, viết thông báo hiển thị trên trang đăng ký (hỗ trợ tiếng Việt 100%). |
| **Sửa Code index.php** | Trình soạn thảo mã nguồn tích hợp — cho phép bạn tùy chỉnh giao diện trang đăng ký trực tiếp trên trình duyệt. |

**💡 Lợi ích:**
- Không bao giờ bị lỗi font tiếng Việt (như khi gõ trên Terminal SSH).
- Thay đổi có hiệu lực ngay lập tức mà không cần build lại.
- `nro4.py` sẽ **không ghi đè** `index.php` / `admin.php` nếu chúng đã tồn tại, cho phép bạn tự do chỉnh sửa.

---

### [A] Tự Động Sao Lưu Xoay Vòng (Backup Daemon)

> **Mục đích:** Tự động backup Database theo lịch trình, có cơ chế xoay vòng xóa bản cũ.

**Dashboard hiển thị:**
- Trạng thái Daemon (ONLINE/OFFLINE)
- Chu kỳ sao lưu (mặc định: 1 giờ/lần)
- Giới hạn lưu trữ (mặc định: tối đa 24 file)
- Danh sách 5 bản backup gần nhất

| Phím | Chức năng |
|---|---|
| `[1]` | Bật tiến trình sao lưu tự động (chạy ngầm TMux) |
| `[2]` | Tắt tiến trình sao lưu |
| `[3]` | Thay đổi chu kỳ (VD: 2 giờ, 6 giờ...) |
| `[4]` | Thay đổi số bản lưu tối đa |
| `[5]` | Thay đổi thư mục lưu trữ (Nội bộ / Download / Tùy chỉnh) |
| `[6]` | Xem Log chi tiết tiến trình backup |

**📁 Đặt tên file backup:** `backup_team2026_Ngay_11-07-2026_Luc_03h00p.sql`

---

### [B] Giám Sát Tiến Trình TMux

> **Mục đích:** Xem, kết nối và quản lý tất cả các session TMux đang chạy ngầm.

**Chức năng:**
- Liệt kê tất cả TMux session đang hoạt động
- Kết nối nhanh vào session bất kỳ (VD: Ngrok, Game Server, Backup Daemon...)
- Phím tắt: `[N]` → Ngrok, `[G]` → Game Server
- `[K]` Tắt một session cụ thể
- `[T]` Tắt toàn bộ TMux server

**💡 Cách thoát TMux mà không tắt tiến trình:** Nhấn `Ctrl + B`, thả ra, rồi bấm `D`.

---

### [K] Chuyển Đổi Backend (LEMP ↔ KSWEB)

> **Mục đích:** Chuyển đổi giữa 2 hệ thống Web & Database.

| Backend | Mô tả |
|---|---|
| **LEMP Termux** | MariaDB + Nginx + PHP-FPM chạy bên trong Termux. Toàn bộ do `nro4.py` quản lý. |
| **KSWEB** | MySQL + Lighttpd chạy bởi app KSWEB bên ngoài. Không bị Android kill tiến trình. |

**Menu chuyển đổi:**

| Phím | Chức năng |
|---|---|
| `[1]` | Chuyển sang LEMP Termux |
| `[2]` | Chuyển sang KSWEB |
| `[3]` | Đồng bộ Web đăng ký sang thư mục KSWEB (`/sdcard/htdocs/`) |
| `[4]` | Thiết lập / thay đổi mật khẩu MySQL KSWEB |

**💡 Khi nào nên dùng KSWEB?**
- Máy bạn chạy Android 12+ và LEMP bị kill liên tục.
- MariaDB trên Termux hay bị crash không rõ nguyên nhân.
- Bạn muốn ổn định hơn mà không cần chạy lệnh ADB (hên xui nha )

---

### [D] Làm Mới Kết Nối Nhanh

> **Mục đích:** Tự động kill port cũ, cập nhật IP mới và vá + build lại source.

Phù hợp khi:
- Bạn đổi mạng WiFi và IP thay đổi.
- Server bị treo cổng không giải phóng.
- Muốn refresh nhanh mà không cần vào từng mục.

---

## 🔧 Cấu Hình Hệ Thống

Toàn bộ cấu hình được lưu tại `~/nro_config.json`, bao gồm:

```json
{
    "base_dir": "~/nro_termux",
    "db_name": "team2026",
    "tcp_domain": "192.168.1.7",
    "tcp_port": 14445,
    "mode": "offline",
    "backend": "termux",
    "jvm_xmx": "512m",
    "jvm_mode": "opt",
    "web_show_vnd": true,
    "web_show_admin": true,
    "web_admin_notice": "",
    "web_admin_pass": "admin"
}
```

---

## 👥 Cộng Đồng & Liên Hệ

| Kênh | Liên kết |
|---|---|
| 📱 **Nhóm Zalo** | [Tham gia ngay](https://zalo.me/g/nran3u1pi3hgm9mq5mpc) |
| 📘 **Nhóm Facebook** | [Cộng đồng NRO Termux](https://www.facebook.com/groups/nro.termux) |
| 🎬 **YouTube** | [DAITEN Studio](https://www.youtube.com/watch?v=YTnZo66T0Tk) |

---

## 📜 Giấy Phép

Dự án này được chia sẻ **MIỄN PHÍ** cho cộng đồng.  
Nếu ai bắt bạn trả phí để sử dụng — **đó là lừa đảo (SCAM)**!

---

> **NRO VNPro** — *Tạo ra để mod game NRO thành PVP hoặc các chế độ khác mà không cần cày cuốc. Ai có chung ý tưởng nhớ share cho mọi người để chúng ta cùng vui vẻ nhé!*
