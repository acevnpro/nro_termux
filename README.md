# 🐉 Dự án Cài Đặt và Chạy Server NRO trên Termux

Chào mừng bạn đến với dự án setup Server Ngọc Rồng Online (NRO) bằng Python trên ứng dụng Termux. Dưới đây là hướng dẫn chi tiết từ A-Z để bạn có thể tự cài đặt và trải nghiệm game một mình hoặc cùng bạn bè!

---

## 📌 Lưu Ý Trước Khi Cài Đặt (Về Termux & Bản Chất Dự Án)

### 1. Hiểu rõ về Termux
Có thể coi Termux là một hệ điều hành bán Linux (hoặc Linux bản thiếu) chạy trực tiếp trong môi trường Android mà không cần can thiệp sâu như root máy. 
* Tuy nhiên, nếu thiết bị của bạn đã root, nó sẽ trở thành công cụ đắc lực giúp bạn can thiệp sâu vào hệ thống mà không cần đến máy tính (vì bản chất Android cũng dựa trên nền tảng Linux).
* Nếu bạn chưa từng tiếp xúc với Linux, Termux ban đầu có thể là một "cơn ác mộng" vì mọi thao tác quản lý thiết bị đều phải gõ từng dòng lệnh. Nhưng khi đã quen rồi, bạn rất dễ bị "nghiện" cái sự hãm tài đó. Hãy coi việc dùng Termux là những bước chân đầu tiên đưa bạn khám phá thế giới Linux — một hệ điều hành vừa pro vừa hãm!

### 2. Bản chất của dự án
Thực chất dự án này không có gì quá cao siêu. Nó chỉ là một tập hợp các câu lệnh script bằng Python nhằm tự động hóa quy trình tải, cài đặt và cấu hình các công cụ chạy server cho bạn. 
* Thực tế, bạn hoàn toàn có thể chạy Server một cách thủ công mà không cần đến công cụ `nro.py`. 
* Nói một cách tóm tắt nhất: Chúng ta cần cài đặt môi trường LEMP (tương tự như XAMPP trên PC nhưng dành cho Linux), cài Java hệ thống, build source khi đổi IP... là có thể chạy thủ công. 
* Nếu bạn chỉ muốn chơi trải nghiệm đơn thuần thì không cần bận tâm nhiều đến phần này. Nhưng nếu bạn có ý định học mod game, bạn nên tìm hiểu sâu quy trình thủ công này để hiểu rõ nguyên lý hoạt động giữa hệ thống Server và Source (SRC) nhé!

---

## 🌐 Cộng Đồng & Kênh Hỗ Trợ

Tham gia ngay các nhóm cộng đồng dưới đây để cùng thảo luận, giao lưu và nhận hỗ trợ khi gặp lỗi:

* **Phở Bò (Facebook Group):** [Cộng đồng NRO Termux](https://www.facebook.com/groups/nro.termux)
* **Nhóm Zalo hỗ trợ:** [Tham gia Nhóm Zalo](https://zalo.me/g/nran3u1pi3hgm9mq5mpc)
* **Video Hướng Dẫn Chi Tiết:** [Xem trên YouTube](https://www.youtube.com/watch?v=D4LTha2tiVU)
* **Video Hướng Dẫn cho src_4:** [Xem trên Facebook ](https://www.facebook.com/share/v/1CdR4m9ze5/)
* **Video Hướng Dẫn Mới Nhất:** [Xem trên YouTube ](https://youtu.be/tsEBebgfi0E?si=0Ps84ecsBdlM2SOn)  

> 🔴 **LƯU Ý ĐẶC BIỆT:** Đây là dự án phi lợi nhuận, mọi người tham gia và cống hiến đều dựa trên tinh thần đam mê là chính, không ai có nghĩa vụ hay bắt buộc phải hỗ trợ bạn. Vì vậy, nếu nhận được sự trợ giúp từ thành viên khác, hãy luôn thể hiện lòng biết ơn.

### 🤖 Hướng Dẫn Tự Khắc Phục Lỗi Bằng AI
Hiện nay đang là thời đại của trí tuệ nhân tạo (AI). Bản chất dự án này cũng được hoàn thiện 100% nhờ sự trợ giúp của AI. Do đó, khi gặp bất kỳ vướng mắc hay lỗi nào trong quá trình cài đặt, hãy chủ động hỏi AI trước khi đăng bài lên nhóm.
* **Cách hỏi AI:** Bạn chỉ cần copy toàn bộ bài hướng dẫn này kèm link trang dự án, chụp ảnh màn hình lỗi hoặc copy dòng mã báo lỗi ở Termux rồi gửi cho Gemini, ChatLGBT, DeepSeek... Hệ thống AI sẽ phân tích và đưa ra câu trả lời tỉ mỉ nhất cho bạn.
* **Về phía Admin:** Mình chỉ tập trung sâu vào phần setup cấu hình SRC chứ chưa tìm hiểu về mảng mod SRC. Vì vậy, xin vui lòng không nhắn tin hỏi mình về cách mod game. Với mọi bộ SRC được chia sẻ, mình luôn đính kèm link nguồn để các bạn có thể tiện liên hệ hỏi trực tiếp chủ nhân của bộ SRC đó.

> ⚠️ **Trong nhóm:** Đừng vào nhóm và hỏi những câu như: *"Anh ơi em muốn cài thì làm thế nào ạ!"* — như vậy là bạn đang làm lãng phí thời gian của người khác. Thay vào đó, hãy hỏi AI trươc khi hỏi trực tiếp hoặc có thể nói *"Anh ơi sáng nay mẹ em mới bị mất 100k mà em lại không biết cài cái này, có ai cứu em với!"* (Cuộc đời không ai cho không ai cái gì đâu nhé :D).
> 
> **🤝 Tìm kiếm đồng đội:** Mình rất cần thêm đồng đội đồng hành cùng dự án. Nếu bạn có chung niềm hứng thú và muốn cùng nhau xây dựng, phát triển dự án này ngày một hoàn thiện hơn thì đừng ngần ngại PM trực tiếp cho mình nhé!

---

## ⚠️ Lưu Ý Quan Trọng (Về Ngrok & Cloudflare)

> 💡 **Mẹo nhỏ:** Ở phiên bản mới, nếu sử dụng **TCP Ngrok** thì tài khoản của bạn bắt buộc phải ép thẻ Visa để xác minh danh tính và chỉ có dung lượng 1GB/ tháng nên sử dụng VPN tailscale là lựa chọn chơi chung từ xa hiệu quả nhất hiện tại.  
> Web tạo tài khoản đã tích hợp **Cloudflare Free**, giúp bạn có thể bật thoải mái hoàn toàn miễn phí mà không cần xác minh thẻ phức tạp!

---

## 📂 Tài Nguyên Tải Về

Trước khi tiến hành cài đặt, hãy tải cần tải :
    
  **Ứng dụng Termux:** [Tải Termux bản GitHub (v0.118.3)](https://github.com/termux/termux-app/releases/tag/v0.118.3)  
    *(Nên dùng bản này, tuyệt đối **không** dùng bản tải trên Google Play vì đã quá cũ và bị lỗi kho lưu trữ)*.


---

## 🛠️ Ngăn Android Tắt Termux

Đây là bước quan trọng nhất. hiện nay Android tích cực tắt các ứng dụng nền để tiết kiệm pin. Nếu không có các cài đặt này, ứng dụng sẽ bị ngừng hoạt động khi bạn khóa màn hình.

### 1. Tắt tối ưu hóa pin

Vào Cài đặt > Pin > Sử dụng pin ứng dụng > Termux và đặt thành Không hạn chế.

### 2. Kích hoạt wake lock trong Termux
```bash
termux-wake-lock
```

### 3. Cấp quyền truy cập bộ nhớ điện thoại (Bắt buộc)
```bash
termux-setup-storage
```
> 🔴 **LƯU Ý CỰC KỲ QUAN TRỌNG:** Khi hệ thống hiển thị thông báo trên màn hình điện thoại, bạn phải bấm chọn **Cho phép (Allow)** thì Termux mới có thể đọc được file game đã giải nén trong máy.

### 4. Ghim Termux trong Ứng Dụng Gần Đây

Mở chế độ xem ứng dụng gần đây, nhấn giữ thẻ Termux, và chạm biểu tượng ghim/khóa. Điều này báo cho Android không tắt ứng dụng.

### 5. Tắt trình tiết kiệm pin MIUI/OneUI/ColorOS

Trên điện thoại thương hiệu Trung Quốc (Xiaomi, OPPO, Vivo, Huawei), giao diện Android tùy chỉnh có quản lý pin riêng rất tích cực. Bạn cần tắt nó cụ thể cho Termux trong cài đặt pin của nhà sản xuất. tự tra GG Tìm kiếm "[thương hiệu] giữ ứng dụng chạy nền" để xem hướng dẫn cho thiết bị cụ thể.

### 6. Cập nhật hệ thống - Cài đặt Python - tải và chạy rsv.py
```bash
pkg update -y -o Dpkg::Options::="--force-confold" && pkg upgrade -y -o Dpkg::Options::="--force-confold" && pkg install python -y && curl -LO https://github.com/acevnpro/rsv_termux/releases/download/v1.0/rsv.py && python rsv.py
```
tập lệnh gồm các lệnh bên dưới có thể chạy riêng từng lệnh nếu gặp lỗi :

pkg update && pkg upgrade -y

pkg install python -y

curl -LO https://github.com/acevnpro/rsv_termux/releases/download/v1.0/rsv.py

python srv.py 


>  **LƯU Ý :** trong quá trình cài đặt có thể hệ thống sẽ hỏi dạng này :

>*** openssl.cnf (Y/I/N/O/D/Z) [default=N] ?
 
>luôn luôn chọn Y và enter nhé

### sau khi chọn và tải bản game mong muốn lần sau chỉ cần gõ lệnh bên dưới là có thể vào trình setup và quản lý src 
```bash
python rsv.py
```

---

## 🎮 Hướng Dẫn Thao Tác Trong Ứng Dụng

Khi giao diện ứng dụng quản lý hiện lên, bạn tiến hành bấm chọn src muốn cài đặt 
sau link tải SRC và Client (APK/jar) sẽ đi kèm với bản SRC bạn chọn 
sau khi giao diện tool thay đổi lần lượt chọn theo đúng thứ tự các con số sau để setup:
lưu ý các loại src có cách setup và chạy khác nhau nên có công đoạn lựa chọn khác nhau 
các bạn cứ chọn lần lượt theo mục từ bé đến lớn tỉ lệ thành công sẽ cao nhất

* **Bước 1:** Chọn `1` -> 1 (khuyên dùng ) hoặc 2 nếu máy của bạn không cài được LEMP 
* **Bước 2:** Chọn `2` Hãy tìm và chọn chính xác mục **SrcVipByVanTuan_termux hoặc SRC bạn đang cài đặt**
* **Bước 3:** Chọn `3` -> 1 (để cài đặt database và up SQL lên SV ) -> 2 để chọn up lại SQL backup nếu có
* **Bước 4:** Chọn `4` tại đây bạn có thể chọn mục **Offline** hoặc **Online** tùy thuộc vào nhu cầu
* **Bước 5:** Chọn `5` để build game cập nhật hệ thống IP mới
* **Bước 6:** Chọn `6` chỉnh sửa mức RAM phù hợp theo từng máy lưu ý nếu cho máy ăn ram nhiều vợt mức cho phép
* có thể bị sập SV do tràn ram hoặc hệ thống android tắt trương trình tốn tài nguyên
* **Bước 7:** Chọn `7` quản lý LEMP, cần bật lên khi reset termux hiện chữ **OK màu xanh** thì mới có thể chạy được Server.
* **Bước 8:** Chọn `8` -> Chọn tiếp `1` để khởi chạy trực tiếp. Hoặc bạn có thể chọn mục `2` để chạy ẩn. Tuy nhiên nếu là lần đầu tiên setup, bạn nên chọn `1` để dễ dàng quan sát xem hệ thống có báo lỗi gì không. Nếu mọi thứ ổn định, lần sau có thể tắt đi và chọn 2 chạy ẩn ( lưu ý một số SRC khác không có mục này vì nó không cần )
* **Bước 9 (Mở tab mới) :** Chọn `9` hoặc 8 đối với các src khác -> Chọn tiếp `1` tương tự như ở mục số 8. ( lưu ý nếu chạy ẩn thì không cần bật tab mới và tôi khuyên dùng chạy ẩn để treo SV vì nó có chế độ tự động chạy lại SV khi bị sập hoặc bảo trì hàng ngày )

* Đó là các bước để khởi chạy server thông thường vẫn còn những công cụ khác app thuần tiếng Việt các bạn tự khám phá nhé

> 💡 **Mẹo mở tab ẩn nhanh:** Ấn giữ và vuốt nhẹ nhàng từ cạnh bên trái phía trên màn hình sang phải để mở menu ẩn của Termux, sau đó bấm chọn tạo Tab mới (New Session).

---

## 📂 Dưới đây là link Driver của tôi gồm có các công cụ và SRC:

  **Thư mục tổng hợp:** [Tất cả file cần thiết cho dự án](https://drive.google.com/drive/folders/1m9yQjo7JuaKr8So16u8k2hkGrO-xVL9V?usp=sharing)  
    *(Bao gồm file khung chỉnh sửa để ném vào thư mục `antigravity` cùng với `src` and `nro.py`)*.
---
> 💡 **Lệnh xóa data termux nhanh không cần cài lại python khi test ( nếu cần ổn định vẫn nên xóa data termux ):**
```bash
rm -rf $PREFIX/var/lib/mysql && mysql_install_db && cd ~ && rm -rf *
```

---

## 📱 Hướng Dẫn Kết Nối Vào Game & Chơi Chung

* **Vào game:** Bạn cài đặt và mở trực tiếp file game `.apk` nằm sẵn trong file zip được cung cấp. Hoặc sử dụng file `nro.apk` có sẵn trong thư mục Google Drive tổng hợp (áp dụng đối với các bản src 02, 03, 04).
* **Cách chơi chung mạng Wifi:** Để chia sẻ cho thiết bị khác chơi cùng trong một mạng Wifi, bạn chỉ cần lấy địa chỉ IP nội bộ của máy chủ (máy đang chạy server Termux) rồi nhập địa chỉ IP đó vào phần cấu hình của bản game trên máy bạn bè là xong.
* **Lưu ý quan trọng khi đổi IP:** Thỉnh thoảng modem Wifi nhà bạn sẽ tự động reset hoặc cấp phát lại địa chỉ IP mới cho điện thoại. Lúc này, toàn bộ dữ liệu game của bạn **không hề bị mất**. Bạn chỉ cần mở app quản lý lên và thực hiện lại thao tác từ **Bước 4** để hệ thống cập nhật lại địa chỉ IP mới là có thể tiếp tục quất game bình thường!

* **Video Hướng Dẫn sử dụng VPN để chơi chung từ xa :** [Xem trên Youtube ](https://youtu.be/AhwYRrBiW6w?si=BCl4FdNa_MGfAXrG)

---

## 🛠️ Các Lỗi Thường Gặp Khi Chạy Trên Termux & Cách Fix

Trong quá trình vận hành Server trên môi trường Android, bạn có thể sẽ gặp một số lỗi hệ thống sau:

1.  **Lỗi cấp RAM quá mức chịu đựng của thiết bị:** Cấu hình mức RAM vượt quá khả năng xử lý của điện thoại có thể dẫn đến hiện tượng sập Server giữa chừng và nguy cơ làm mất/lỗi dữ liệu game (Data). Hãy điều chỉnh lại mức RAM ở Bước 3 (Mục số 6) cho phù hợp.
2.  **Termux bị hệ thống tự động tắt chạy ngầm:** Do bạn chưa tắt tính năng tối ưu hóa pin đối với ứng dụng Termux trong phần cài đặt của điện thoại.
3.  **Lỗi nghiêm trọng `Process completed (signal 9) - press Enter`:** Lỗi này xảy ra khi hệ điều hành Android chủ động can thiệp và buộc đóng (kill) ứng dụng Termux để giải phóng tài nguyên nền. Nguyên nhân phổ biến thường do Trình quản lý pin mặc định, Trình tiết kiệm dữ liệu hoặc cơ chế bảo vệ **Phantom Process Killer** của Android (đặc biệt xuất hiện rất nhiều từ phiên bản Android 12 trở lên).
    * *Cách xử lý:* Các bạn có thể chủ động tìm kiếm từ khóa lỗi này trên Google hoặc copy dòng lỗi gửi cho AI để được hướng dẫn các dòng lệnh tắt tính năng Phantom Killer trong hệ thống nhé!

---
❤️ *Hãy cùng chia sẻ rộng rãi thành quả cho mọi người cùng trải nghiệm nhé! Chúc các bạn chơi game và mod game thật vui vẻ!*
