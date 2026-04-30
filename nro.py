import os, json, socket, subprocess, time, re

# ==========================================
# MÀU SẮC & GIAO DIỆN
# ==========================================
class C:
    H = '\033[95m'; B = '\033[94m'; CY = '\033[96m'; G = '\033[92m'
    Y = '\033[93m'; R = '\033[91m'; E = '\033[0m'; BOLD = '\033[1m'

def p_h(t): print(f"\n{C.H}{C.BOLD}=== {t} ==={C.E}")
def p_ok(t): print(f"{C.G}[✓] {t}{C.E}")
def p_err(t): print(f"{C.R}[✗] {t}{C.E}")
def p_info(t): print(f"{C.CY}[i] {t}{C.E}")

# ==========================================
# CẤU HÌNH
# ==========================================
HOME = os.path.expanduser("~")
CONFIG_FILE = os.path.join(HOME, "nro_config.json")

def load_config():
    defaults = {
        "base_dir": os.path.join(HOME, "SrcVipByVanTuan"),
        "db_user": "root", "db_pass": "", "db_name": "nrovip",
        "tcp_domain": "127.0.0.1", "tcp_port": 14445,
        "local_login_port": 8888, "local_game_port": 14445,
        "mode": "offline", "pma_port": 8081, "jvm_xmx": "512m",
        "status": {"env": False, "source": False, "db_web": False, "build": False}
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f: cfg = json.load(f)
            for k, v in defaults.items():
                if k not in cfg: cfg[k] = v
                elif isinstance(v, dict) and isinstance(cfg.get(k), dict):
                    for sk, sv in v.items():
                        if sk not in cfg[k]: cfg[k][sk] = sv
            cfg['tcp_port'] = int(cfg.get('tcp_port', 14445))
            cfg['local_login_port'] = int(cfg.get('local_login_port', 8888))
            cfg['local_game_port'] = int(cfg.get('local_game_port', 14445))
            return cfg
        except: pass
    return dict(defaults)

def save_config(cfg):
    with open(CONFIG_FILE, 'w') as f: json.dump(cfg, f, indent=4)

def get_paths(cfg):
    b = cfg["base_dir"]
    return {
        "BASE": b,
        "LOGIN_DIR": os.path.join(b, "ServerLogin"),
        "GAME_DIR": os.path.join(b, "SrcVIP"),
        "LOGIN_INI": os.path.join(b, "ServerLogin/server.ini"),
        "GAME_PROPS": os.path.join(b, "SrcVIP/config/server.properties"),
        "DB_SERVICE": os.path.join(b, "SrcVIP/src/main/java/nro/jdbc/DBService.java"),
        "DATA_GAME": os.path.join(b, "SrcVIP/src/main/java/nro/data/DataGame.java"),
        "SQL_FILE": os.path.join(b, "NroVIP.sql"),
    }

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)); ip = s.getsockname()[0]; s.close(); return ip
    except: return "127.0.0.1"

def resolve_ip(domain):
    try:
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain): return domain
        return socket.gethostbyname(domain)
    except: return domain

def kill_port(port):
    os.system(f"lsof -t -i:{port} 2>/dev/null | xargs kill -9 2>/dev/null")

def get_st(pattern):
    try:
        subprocess.check_output(["pgrep", "-f", pattern], stderr=subprocess.DEVNULL)
        return f"{C.G}ON{C.E}"
    except: return f"{C.R}OFF{C.E}"

def check_status():
    login = get_st("ServerLogin")
    game = f"{C.R}OFF{C.E}"
    for p in ["0337766460_VanTuan", "nro.server.ServerManager"]:
        if "ON" in get_st(p): game = f"{C.G}ON{C.E}"; break
    db = get_st("mariadbd")
    return login, game, db

def get_stat(cfg, key):
    return f" {C.G}(OK){C.E}" if cfg.get("status", {}).get(key) else ""

# ==========================================
# [1] CÀI ĐẶT MÔI TRƯỜNG
# ==========================================
def install_env(cfg):
    p_h("CÀI ĐẶT MÔI TRƯỜNG")
    pkgs = ["openjdk-17", "mariadb", "nginx", "php", "php-fpm", "maven",
            "wget", "unzip", "unrar", "tar", "git", "tmux", "psmisc", "lsof"]
    subprocess.run(["pkg", "update", "-y"])
    for pkg in pkgs:
        p_info(f"Đang cài {pkg}...")
        subprocess.run(["pkg", "install", pkg, "-y"])
    p_ok("Cài đặt hoàn tất!")
    cfg["status"]["env"] = True; save_config(cfg)

# ==========================================
# [2] GIẢI NÉN SOURCE
# ==========================================
def extract_source(cfg):
    p_h("GIẢI NÉN SOURCE")
    # Các thư mục cần quét file nén
    scan_paths = [HOME, "/sdcard/Download"]
    
    all_files = []
    for path in scan_paths:
        if os.path.exists(path):
            try:
                files = [(f, path) for f in os.listdir(path) if any(f.endswith(e) for e in [".zip", ".rar", ".tar.gz"])]
                all_files.extend(files)
            except: continue

    if not all_files:
        p_err("Không tìm thấy file nén trong ~/ hoặc /sdcard/Download")
        p_info("Mẹo: Hãy đảm bảo bạn đã chạy 'termux-setup-storage' để script có quyền truy cập bộ nhớ.")
        return
    
    for i, (f, p) in enumerate(all_files):
        loc = "Download" if "Download" in p else "Home"
        print(f"[{i+1}] {f} ({loc})")
        
    c = input("\nChọn file để giải nén (0=hủy): ")
    if not c or c == "0": return
    
    sel_file, sel_path = all_files[int(c)-1]
    full_path = os.path.join(sel_path, sel_file)
    
    target = os.path.join(HOME, "SrcVipByVanTuan")
    os.makedirs(target, exist_ok=True)
    
    p_info(f"Đang giải nén: {sel_file}...")
    if sel_file.endswith(".zip"):
        subprocess.run(["unzip", "-o", full_path, "-d", target])
    elif sel_file.endswith(".rar"):
        subprocess.run(["unrar", "x", "-o+", full_path, target + "/"])
    elif sel_file.endswith(".tar.gz"):
        subprocess.run(["tar", "-xf", full_path, "-C", target])

    # Xử lý thư mục lồng nhau
    inner = os.path.join(target, "SrcVipByVanTuan")
    if os.path.isdir(inner):
        p_info("Sửa lỗi thư mục lồng nhau...")
        os.system(f"mv {inner}/* {target}/ 2>/dev/null; rm -rf {inner}")
        
    os.system(f"chmod -R 777 {target}")
    p_ok("Giải nén & Phân quyền thành công!")
    cfg["base_dir"] = target; cfg["status"]["source"] = True; save_config(cfg)
    input("\nNhấn Enter để tiếp tục...")

# [3] THIẾT LẬP DATABASE & WEB (LEMP)
# ==========================================
def setup_db(cfg):
    p_h("THIẾT LẬP DATABASE & WEB (LEMP)")
    
    # 1. Cài đặt các gói (Theo nro_cu.py)
    p_info("Đang đảm bảo các gói hệ thống...")
    os.system("pkg install nginx mariadb php php-fpm wget tar -y")

    # 2. Khởi tạo MariaDB (Theo nro_cu.py)
    p_info("Đang cấu hình MariaDB...")
    if not os.path.exists(os.path.join(os.environ['PREFIX'], "var/lib/mysql")):
        os.system("mysql_install_db")
    
    # Khởi động MariaDB an toàn
    os.system("mariadbd-safe > /dev/null 2>&1 &")
    time.sleep(4)

    # Cấu hình quyền truy cập (Theo nro_cu.py - root no pass)
    sql_cmds = [
        "ALTER USER 'root'@'localhost' IDENTIFIED BY '';",
        "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;",
        "FLUSH PRIVILEGES;"
    ]
    for cmd in sql_cmds:
        os.system(f"mariadb -u root -e \"{cmd}\"")
    p_ok("Đã cấu hình MariaDB (User: root / No Pass)")

    # 3. Import SQL
    paths = get_paths(cfg)
    db_name = cfg.get('db_name', 'nro')
    if os.path.exists(paths['SQL_FILE']):
        p_info(f"Đang import database: {os.path.basename(paths['SQL_FILE'])}...")
        os.system(f"mariadb -u root -e 'CREATE DATABASE IF NOT EXISTS {db_name};'")
        os.system(f"mariadb -u root {db_name} < {paths['SQL_FILE']}")
        p_ok(f"Import {db_name} thành công!")

    # 4. Thiết lập phpMyAdmin (Theo nro_cu.py)
    web_dir = os.path.join(HOME, "phpmyadmin")
    if not os.path.exists(os.path.join(web_dir, "index.php")):
        p_info("Đang tải và giải nén phpMyAdmin mới nhất...")
        pma_url = "https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-languages.tar.gz"
        pma_tar = os.path.join(HOME, "pma.tar.gz")
        os.system(f"wget {pma_url} -O {pma_tar}")
        os.system(f"tar -xf {pma_tar} -C {HOME}")
        # Tìm thư mục vừa giải nén
        extracted = [d for d in os.listdir(HOME) if d.startswith("phpMyAdmin-") and os.path.isdir(os.path.join(HOME, d))]
        if extracted:
            os.system(f"rm -rf {web_dir}")
            os.system(f"mv {os.path.join(HOME, extracted[0])} {web_dir}")
        os.system(f"rm -f {pma_tar}")
    
    # Cấu hình config.inc.php (Kết nối qua 127.0.0.1 để ổn định)
    pma_config = os.path.join(web_dir, "config.inc.php")
    pma_sample = os.path.join(web_dir, "config.sample.inc.php")
    if not os.path.exists(pma_config) and os.path.exists(pma_sample):
        os.system(f"cp {pma_sample} {pma_config}")
    
    if os.path.exists(pma_config):
        with open(pma_config, 'r') as f: content = f.read()
        content = content.replace("'localhost'", "'127.0.0.1'")
        content = content.replace("AllowNoPassword'] = false", "AllowNoPassword'] = true")
        if "$cfg['blowfish_secret'] = '';" in content:
            content = content.replace("$cfg['blowfish_secret'] = '';", "$cfg['blowfish_secret'] = 'vantuannro2026_super_secret_key';")
        with open(pma_config, 'w') as f: f.write(content)
        p_ok("Đã cấu hình config.inc.php (127.0.0.1)")

    # 5. Cấu hình Nginx & PHP-FPM (Theo nro_cu.py nhưng chuẩn hóa Port 8081)
    nginx_conf = os.path.join(os.environ['PREFIX'], "etc/nginx/nginx.conf")
    nginx_template = f"""
worker_processes  1;
events {{
    worker_connections  1024;
}}
http {{
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {{
        listen       8081;
        server_name  localhost;
        root         {web_dir};
        index        index.php index.html index.htm;

        location / {{
            try_files $uri $uri/ =404;
        }}

        location ~ \.php$ {{
            try_files $uri =404;
            fastcgi_pass   127.0.0.1:9000;
            fastcgi_index  index.php;
            fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
            include        fastcgi_params;
        }}
    }}
}}
"""
    with open(nginx_conf, 'w') as f: f.write(nginx_template)
    
    # Đảm bảo php-fpm lắng nghe cổng 9000
    fpm_conf = os.path.join(os.environ['PREFIX'], "etc/php-fpm.d/www.conf")
    if os.path.exists(fpm_conf):
        with open(fpm_conf, 'r') as f: c = f.read()
        c = re.sub(r'^listen\s*=.*', 'listen = 127.0.0.1:9000', c, flags=re.M)
        with open(fpm_conf, 'w') as f: f.write(c)

    # Vá lỗi PHP 8.4 cho phpMyAdmin (Vị trí siêu an toàn)
    pma_idx = os.path.join(web_dir, "index.php")
    if os.path.exists(pma_idx):
        with open(pma_idx, 'r') as f: lines = f.readlines()
        
        # Kiểm tra xem file có dùng strict_types không
        has_declare = any("declare(strict_types=1)" in l for l in lines)
        new_lines = []
        inserted = False
        fix_code = "error_reporting(0); ini_set('display_errors', 0); // Fix PHP 8.4 by VanTuan\n"
        
        for line in lines:
            # Xóa các dòng fix cũ nếu có để tránh bị lặp
            if "Fix PHP 8.4 by VanTuan" in line:
                continue
                
            new_lines.append(line)
            
            if not inserted:
                if has_declare:
                    if "declare(strict_types=1)" in line:
                        new_lines.append(fix_code)
                        inserted = True
                elif "<?php" in line:
                    new_lines.append(fix_code)
                    inserted = True
        
        with open(pma_idx, 'w') as f: f.writelines(new_lines)
        p_ok("Đã vá lỗi tương thích PHP 8.4 (Vị trí an toàn)")

    # 6. Khởi động lại toàn bộ
    p_info("Đang khởi động lại dịch vụ...")
    os.system("pkill -9 nginx; pkill -9 php-fpm")
    time.sleep(1)
    os.system("php-fpm")
    os.system("nginx")
    
    cfg["status"]["db_web"] = True; save_config(cfg)
    p_ok(f"Hệ thống Database & Web đã SẴN SÀNG!")
    p_info(f"Truy cập: http://{get_local_ip()}:8081")
    p_info("User: root | Pass: (Trống)")
    input("\nEnter...")

# ==========================================
# [4] CẤU HÌNH KẾT NỐI (Online/Offline)
# ==========================================
def manage_tcp(cfg):
    p_h("CẤU HÌNH KẾT NỐI")
    mode_str = cfg.get('mode', 'offline').upper()
    print(f"Chế độ hiện tại: {C.H}{mode_str}{C.E}")
    print(f"Địa chỉ hiện tại: {C.Y}{cfg['tcp_domain']}:{cfg['tcp_port']}{C.E}")
    
    print(f"\n[1] Online: Tự động lấy từ Ngrok API")
    print(f"[2] Online: Nhập thủ công (Playit/Bore/Bungou/CF)")
    print(f"[3] Offline: Chế độ LAN/WiFi (Dùng IP máy)")
    print(f"[0] Quay lại")
    ch = input(f"\n{C.BOLD}Chọn: {C.E}")

    if ch == "1":
        try:
            import urllib.request
            with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels") as r:
                tunnels = json.loads(r.read().decode()).get('tunnels', [])
                if not tunnels: p_err("Không thấy tunnel!"); return
                for i, t in enumerate(tunnels):
                    print(f"[{i+1}] {t.get('name')}: {C.Y}{t.get('public_url')}{C.E}")
                sel = input("\nChọn: ")
                if not sel: return
                url = tunnels[int(sel)-1].get('public_url', '').replace('tcp://', '')
                if ':' in url:
                    d, p = url.rsplit(':', 1)
                    cfg['mode'] = 'online'
                    cfg['tcp_domain'] = d; cfg['tcp_port'] = int(p)
                    save_config(cfg); p_ok(f"Đã chuyển ONLINE: {d}:{p}")
                    p_info("Lưu ý: Hãy chạy mục [5] để áp dụng IP mới.")
        except Exception as e: p_err(f"Lỗi Ngrok API: {e}")

    elif ch == "2":
        p_info("VD: bore.pub:6489 | 0.tcp.ap.ngrok.io:12345 | abc.at.playit.gg:30000")
        link = input("Nhập địa chỉ: ").strip().replace("tcp://", "")
        if ':' in link:
            d, p = link.rsplit(':', 1)
            cfg['mode'] = 'online'
            cfg['tcp_domain'] = d; cfg['tcp_port'] = int(p)
            save_config(cfg); p_ok(f"Đã chuyển ONLINE: {d}:{p}")
            p_info("Lưu ý: Hãy chạy mục [5] để áp dụng IP mới.")
        else: p_err("Sai format! Cần Domain:Port")

    elif ch == "3":
        cfg["mode"] = "offline"
        cfg["tcp_domain"] = get_local_ip()
        cfg["tcp_port"] = cfg['local_game_port']
        save_config(cfg)
        p_ok("Đã chuyển sang chế độ OFFLINE")
        p_info("Lưu ý: Hãy chạy mục [5] để áp dụng IP mới.")

def get_ram_bar():
    try:
        res = subprocess.check_output("free -m", shell=True).decode()
        lines = res.split('\n')
        mem = lines[1].split()
        total, used = int(mem[1]), int(mem[2])
        percent = int(used * 100 / total)
        bar_len = 20
        filled = int(percent * bar_len / 100)
        bar = "█" * filled + "░" * (bar_len - filled)
        color = C.G if percent < 70 else (C.Y if percent < 90 else C.R)
        return f"{color}[{bar}] {percent}% ({used}MB/{total}MB){C.E}"
    except: return "[N/A]"

def check_lemp_status():
    nginx = subprocess.run(["pgrep", "nginx"], stdout=subprocess.DEVNULL).returncode == 0
    mysql = subprocess.run(["pgrep", "mariadbd"], stdout=subprocess.DEVNULL).returncode == 0
    php = subprocess.run(["pgrep", "php-fpm"], stdout=subprocess.DEVNULL).returncode == 0
    if nginx and mysql and php: return f"{C.G}OK{C.E}"
    if not nginx and not mysql and not php: return f"{C.R}OFF{C.E}"
    return f"{C.Y}PARTIAL{C.E}"

def manage_lemp(cfg):
    p_h("QUẢN LÝ DỊCH VỤ LEMP")
    print(f"Trạng thái hiện tại: LEMP: {check_lemp_status()}")
    print("-" * 30)
    print("[1] Bật dịch vụ (Start)")
    print("[2] Tắt dịch vụ (Stop)")
    print("[3] Xóa sạch môi trường (Wipe/Reset)")
    print("[0] Quay lại")
    c = input(f"\n{C.BOLD}Lựa chọn: {C.E}").upper()
    if c == "1":
        os.system("php-fpm > /dev/null 2>&1; nginx > /dev/null 2>&1; mariadbd-safe > /dev/null 2>&1 &")
        p_ok("Đã khởi động!")
    elif c == "2":
        os.system("pkill -9 nginx; pkill -9 php-fpm; pkill -9 mariadbd")
        p_ok("Đã tắt!")
    elif c == "3":
        confirm = input(f"{C.R}Xóa sạch Database & Config (Y/N)? {C.E}").upper()
        if confirm == "Y":
            os.system("pkill -9 nginx; pkill -9 php-fpm; pkill -9 mariadbd; pkill -9 mysqld")
            os.system(f"rm -rf {os.environ['PREFIX']}/var/lib/mysql")
            os.system(f"rm -rf {os.environ['PREFIX']}/etc/nginx/nginx.conf")
            os.system(f"rm -rf {HOME}/phpmyadmin")
            p_ok("Đã dọn dẹp sạch sẽ!")
    time.sleep(1)

# ==========================================
# [6] VÁ IP & BUILD
# ==========================================
def apply_and_build(cfg):
    p_h("VÁ MÃ NGUỒN & BUILD")
    paths = get_paths(cfg)
    if cfg.get('mode') == 'online':
        ip = resolve_ip(cfg['tcp_domain']); port = cfg['tcp_port']
    else:
        ip = get_local_ip(); port = cfg['local_game_port']
    l_port = cfg['local_login_port']; g_port = cfg['local_game_port']
    db_u = cfg['db_user']; db_p = cfg['db_pass']; db_name = cfg['db_name']
    sv1 = f"Buffalo:{ip}:{port}"

    p_info(f"Mode: {cfg.get('mode','offline').upper()} | Online: {ip}:{port}")
    p_info(f"Local: Login={l_port}, Game={g_port}")

    # 1. server.ini
    if os.path.exists(paths["LOGIN_INI"]):
        with open(paths["LOGIN_INI"], 'w') as f:
            f.write(f"# Config\nserver.port={l_port}\ndb.port=3306\ndb.host=127.0.0.1\n")
            f.write(f"db.user={db_u}\ndb.password={db_p}\ndb.name={db_name}\n")
            f.write("db.driver=com.mysql.cj.jdbc.Driver\nadmin.mode=0\n")
        p_ok(f"server.ini → port={l_port}")

    # 2. server.properties (GHI ĐẦY ĐỦ)
    props_dir = os.path.dirname(paths["GAME_PROPS"])
    if os.path.exists(props_dir):
        with open(paths["GAME_PROPS"], 'w') as f:
            f.write(f"""##config db
server.db.ip=localhost
server.db.port=3306
server.db.name={db_name}
server.db.us={db_u}
server.db.pw={db_p}
server.db.maxactive=99999

##config server
server.sv=1
server.port={g_port}
server.sv1={sv1}

login.host=127.0.0.1
login.port={l_port}

server.waitlogin=5
server.maxperip=50
server.maxplayer=1500
server.expserver=4
server.debug=false
server.name=buffalo
server.domain=https://nro-buffalo.com/

api.port=8080
api.key=abcdef

#hikariCP
server.hikari.minIdle=5
server.hikari.poolSize=200
server.hikari.cachePre=true
server.hikari.cacheSize=250
server.hikari.cacheSqlLimit=2048

execute.command=java -Djava.awt.headless=true -jar target/0337766460_VanTuan-1.0-RELEASE-jar-with-dependencies.jar

server.event=6
##config server 1 = halloween, 2 = 20/11 nha giao , 3 noel, 4 tet, 5 sk8/3
""")
        p_ok(f"server.properties → sv1={sv1}")

    # 3. DBService.java
    if os.path.exists(paths["DB_SERVICE"]):
        with open(paths["DB_SERVICE"], 'r', encoding='utf-8') as f: content = f.read()
        content = re.sub(r'DB_HOST\s*=\s*".*?"', 'DB_HOST = "127.0.0.1"', content)
        content = re.sub(r'DB_NAME\s*=\s*".*?"', f'DB_NAME = "{db_name}"', content)
        content = re.sub(r'DB_USER\s*=\s*".*?"', f'DB_USER = "{db_u}"', content)
        content = re.sub(r'DB_PASSWORD\s*=\s*".*?"', f'DB_PASSWORD = "{db_p}"', content)
        with open(paths["DB_SERVICE"], 'w', encoding='utf-8') as f: f.write(content)
        p_ok("DBService.java → DB config")

    # 4. DataGame.java
    if os.path.exists(paths["DATA_GAME"]):
        with open(paths["DATA_GAME"], 'r', encoding='utf-8') as f: content = f.read()
        content = re.sub(r'LINK_IP_PORT\s*=\s*".*?"', f'LINK_IP_PORT = "Buffalo:{ip}:{port}:0"', content)
        with open(paths["DATA_GAME"], 'w', encoding='utf-8') as f: f.write(content)
        p_ok(f"DataGame.java → LINK_IP_PORT")

    # 5. Build
    p_info("Đang build Maven (1-3 phút)...")
    game_dir = paths["GAME_DIR"]
    target_dir = os.path.join(game_dir, "target")
    if os.path.exists(target_dir): os.system(f"rm -rf {target_dir}")
    res = subprocess.run(["mvn", "clean", "package", "-DskipTests"], cwd=game_dir)
    if res.returncode == 0:
        p_ok("BUILD THÀNH CÔNG!"); cfg["status"]["build"] = True
    else: p_err("BUILD THẤT BẠI!")
    save_config(cfg); input("\nEnter...")

# ==========================================
# [6] CẤU HÌNH RAM & SWAP (HYBRID)
# ==========================================
def config_ram(cfg):
    p_h("CẤU HÌNH RAM & SWAP")
    try:
        mem = subprocess.check_output(["cat", "/proc/meminfo"]).decode()
        total = int(re.search(r"MemTotal:\s+(\d+)", mem).group(1)) // 1024
        avail = int(re.search(r"MemAvailable:\s+(\d+)", mem).group(1)) // 1024
        swap_total = int(re.search(r"SwapTotal:\s+(\d+)", mem).group(1)) // 1024
        swap_free = int(re.search(r"SwapFree:\s+(\d+)", mem).group(1)) // 1024
        
        used = total - avail; pct = int(used * 20 / total)
        print(f"  RAM Thật: [{'█' * pct}{'░' * (20-pct)}] {used}MB / {total}MB")
        print(f"  RAM Ảo (Swap): {swap_total - swap_free}MB / {swap_total}MB")
        
        if swap_total > 0:
            suggest = max(total - 150, 512)
            p_info(f"Phát hiện Swap: Gợi ý chế độ Hybrid {suggest}MB (Chạy gần full RAM thật)")
        else:
            suggest = max(min(avail - 200, 1024), 256)
            p_info(f"Gợi ý an toàn: {suggest}MB")
    except: suggest = 512

    print(f"\n[1] Cấu hình RAM cho Server (Hiện: {cfg.get('jvm_xmx','512m')})")
    print(f"[2] Tạo/Cập nhật RAM ảo - Swap (Yêu cầu ROOT)")
    print(f"[0] Quay lại")
    
    ch = input(f"\n{C.BOLD}Chọn: {C.E}")
    
    if ch == "1":
        val = input(f"Nhập RAM (VD: 512m, 1g) [{suggest}m]: ").strip()
        if not val: val = f"{suggest}m"
        if not val.endswith(('m','g')): val += 'm'
        cfg['jvm_xmx'] = val
        save_config(cfg); p_ok(f"Đã thiết lập JVM RAM = {val}")
        
    elif ch == "2":
        if subprocess.run(["which", "su"], stdout=subprocess.DEVNULL).returncode != 0:
            p_err("Máy bạn chưa ROOT hoặc chưa cài 'su'!"); return
        
        size_gb = input("Nhập dung lượng Swap muốn tạo (GB) [2]: ").strip()
        if not size_gb: size_gb = "2"
        
        swap_file = os.path.join(HOME, "swapfile")
        p_info(f"Đang tạo {size_gb}GB Swap tại {swap_file}...")
        
        # Các lệnh Root để tạo Swap
        cmds = [
            f"su -c 'swapoff {swap_file}'",
            f"su -c 'dd if=/dev/zero of={swap_file} bs=1M count={int(size_gb)*1024}'",
            f"su -c 'chmod 600 {swap_file}'",
            f"su -c 'mkswap {swap_file}'",
            f"su -c 'swapon {swap_file}'"
        ]
        
        for cmd in cmds:
            p_info(f"Đang chạy: {cmd}")
            os.system(cmd)
            
        p_ok("Đã kích hoạt RAM ảo Hybrid thành công!")
    
    input("\nEnter...")

# ==========================================
# [9/10] QUẢN LÝ SERVER
# ==========================================
def launch_server(cfg, stype):
    paths = get_paths(cfg)
    xmx = cfg.get('jvm_xmx', '512m')
    if stype == "login":
        path = paths["LOGIN_DIR"]; port = cfg['local_login_port']
        jar_cmd = f"java -Djava.awt.headless=true -jar ServerLogin.jar"
        session = "nro_login"
    else:
        path = paths["GAME_DIR"]; port = cfg['local_game_port']
        jar_cmd = f"java -Djava.awt.headless=true -server -Xms{xmx} -Xmx{xmx} -jar target/*.jar"
        session = "nro_game"

    p_h(f"VẬN HÀNH {stype.upper()} (port {port})")
    print(f"[1] Chạy trực tiếp (thấy log)")
    print(f"[2] Chạy ngầm (tmux)")
    print(f"[0] TẮT server (kill port {port})")
    ch = input(f"\n{C.BOLD}Chọn: {C.E}")
    if ch == "1":
        kill_port(port); time.sleep(1)
        os.chdir(path); os.system(jar_cmd)
    elif ch == "2":
        kill_port(port); time.sleep(1)
        os.system(f"tmux kill-session -t {session} 2>/dev/null")
        os.system(f"tmux new-session -d -s {session} 'cd {path} && {jar_cmd}'")
        p_ok(f"{stype} đang chạy trong tmux ({session})")
        p_info(f"Xem log: tmux attach -t {session}")
    elif ch == "0":
        kill_port(port)
        os.system(f"tmux kill-session -t {session} 2>/dev/null")
        p_ok(f"Đã tắt {stype} (port {port})")

def get_stat(cfg, key):
    return f" {C.G}(OK){C.E}" if cfg.get("status", {}).get(key) else ""

def main():
    cfg = load_config()
    while True:
        os.system("clear")
        lemp_st = check_lemp_status()
        ram_bar = get_ram_bar()
        ip = get_local_ip()
        mode = cfg.get('mode', 'offline').upper()
        
        print(f"""{C.CY}{C.BOLD}
==========================================
        NRO SERVER MANAGER - PRO
=========================================={C.E}
 {C.G}tôi tạo ra app này để mod những game này thành game pvp 
 hoặc các chế độ khác tương tự mà không cần cày quốc 
 ae ai có chung ý tưởng nhớ share cho mọi người để 
 chúng ta cùng vui vẻ nhé hiện tại tôi chưa thể mod 
 nó chạy online được ai có tâm thì mod lại và chia sẻ nhé{C.E}
------------------------------------------
 {C.BOLD}RAM: {ram_bar}
 {C.BOLD}IP:  {C.G}{ip}{C.E} | {C.BOLD}PMA: {C.Y}http://{ip}:8081{C.E} | {C.BOLD}MODE:{C.E} {C.H}{mode}{C.E}
------------------------------------------
 [1] Cài đặt môi trường hệ thống{get_stat(cfg,'env')}
 [2] Giải nén Source game (Scan Download){get_stat(cfg,'source')}
 [3] Thiết lập Database & Web (Auto Fix){get_stat(cfg,'db_web')}
 [4] Cấu hình Kết nối (Online/Offline)
 [5] Vá IP & Build Game{get_stat(cfg,'build')}
 [6] Cấu hình RAM & Swap (Hybrid)
 [7] Quản lý Dịch vụ LEMP: {lemp_st}
 [8] VẬN HÀNH LOGIN SERVER
 [9] VẬN HÀNH GAME SERVER
 [D] LÀM MỚI KẾT NỐI NHANH
 [0] THOÁT CHƯƠNG TRÌNH
------------------------------------------""")
        ch = input(f"{C.BOLD}Lựa chọn của bạn: {C.E}").upper()

        if ch == "1": install_env(cfg)
        elif ch == "2": extract_source(cfg)
        elif ch == "3": setup_db(cfg)
        elif ch == "4": manage_tcp(cfg)
        elif ch == "5": apply_and_build(cfg)
        elif ch == "6": config_ram(cfg)
        elif ch == "7": manage_lemp(cfg)
        elif ch == "8": launch_server(cfg, "login")
        elif ch == "9": launch_server(cfg, "game")
        elif ch == "D":
            kill_port(cfg['local_login_port'])
            kill_port(cfg['local_game_port'])
            time.sleep(2)
            if cfg.get("mode") != "online":
                cfg["tcp_domain"] = get_local_ip()
                cfg["tcp_port"] = cfg['local_game_port']
                save_config(cfg)
            apply_and_build(cfg)
        elif ch == "0": break
        time.sleep(0.3)

if __name__ == "__main__":
    main()
