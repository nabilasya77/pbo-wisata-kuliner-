import json
import os
from datetime import datetime

import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, messagebox



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, "users.json")
KULINER_FILE = os.path.join(BASE_DIR, "kuliner.json")
DESTINASI_FILE = os.path.join(BASE_DIR, "destinasi.json")
BUKU_TAMU_FILE = os.path.join(BASE_DIR, "buku_tamu.json")
TRANSAKSI_FILE = os.path.join(BASE_DIR, "transaksi.json")


WARNA = {
    "primer": "#146C43",        # hijau utama (Forest Green) - warna branding
    "primer_gelap": "#0B4A2E",  # hijau paling gelap untuk hover/active header
    "hijau": "#1E8F5E",         # hijau medium untuk tombol aksi positif (Tambah/Simpan)
    "hijau_muda": "#E7F5EC",    # soft mint untuk background tag/badge kategori
    "aksen": "#2FA876",         # hijau-teal lebih cerah, dipakai utk badge harga & CTA
    "aksen_gelap": "#1F7A56",   # hover utk aksen
    "aksen_muda": "#EAF8F1",    # light mint kedua utk tag sekunder
    "merah": "#C0453D",         # tetap merah khusus tombol Hapus / danger (konvensi universal)
    "merah_gelap": "#A23931",
    "latar": "#F4F8F6",         # off-white kehijauan lembut untuk background halaman
    "kartu": "#FFFFFF",         # putih untuk card
    "teks": "#1C2B24",          # teks gelap kehijauan (bukan hitam pekat, lebih senada)
    "teks_abu": "#6B7873",      # abu-hijau untuk teks sekunder/deskripsi pendek
    "border": "#DCE8E1",        # border tipis hijau pucat
}

FONT_UTAMA = "Segoe UI"  # tkinter otomatis fallback ke font sistem jika tak tersedia

ROLE_ADMIN = "admin"
ROLE_USER = "user"
DAFTAR_ROLE = [ROLE_USER, ROLE_ADMIN]

STATUS_DIPROSES = "Diproses"
STATUS_SELESAI = "Selesai"
STATUS_DIBATALKAN = "Dibatalkan"
DAFTAR_STATUS_TRANSAKSI = [STATUS_DIPROSES, STATUS_SELESAI, STATUS_DIBATALKAN]
WARNA_STATUS = {
    STATUS_DIPROSES: "#2FA876",     # teal aksen - masih berjalan
    STATUS_SELESAI: "#146C43",      # hijau primer - tuntas
    STATUS_DIBATALKAN: "#C0453D",   # merah - dibatalkan
}

KULINER_DATA_DEFAULT = [
    {"id": 1, "nama": "Nasi Tiwul", "kategori": "Makanan Berat", "harga": 8000,
     "lokasi": "Pasar Kota Wonogiri", "jam": "06:00 - 20:00", "rating": 4.8, "ulasan": 215,
     "deskripsi": "Makanan pokok ikonik Wonogiri dari tepung gaplek (singkong kering) yang "
                  "dikukus hingga mengembang. Teksturnya legit, sedikit kenyal, dan beraroma "
                  "khas. Disajikan hangat dengan sayur lodeh, urap, atau lauk pauk tradisional."},
    {"id": 2, "nama": "Tiwul Goreng", "kategori": "Makanan Berat", "harga": 7000,
     "lokasi": "Pasar Wuryantoro", "jam": "07:00 - 18:00", "rating": 4.5, "ulasan": 98,
     "deskripsi": "Kreasi modern dari tiwul yang digoreng dengan bumbu rempah pilihan. "
                  "Hasilnya gurih, renyah di luar dan lembut di dalam."},
    {"id": 3, "nama": "Geti Wijen", "kategori": "Jajanan & Camilan", "harga": 10000,
     "lokasi": "Sentra Oleh-oleh Jl. Ahmad Yani", "jam": "08:00 - 21:00", "rating": 4.7, "ulasan": 167,
     "deskripsi": "Oleh-oleh khas Wonogiri dari biji wijen yang disangrai lalu dicetak "
                  "bersama gula merah cair hingga membentuk batangan manis-legit."},
    {"id": 4, "nama": "Kacang Mete Wonogiri", "kategori": "Oleh-oleh", "harga": 25000,
     "lokasi": "Sentra Mete Jatisrono", "jam": "08:00 - 17:00", "rating": 4.9, "ulasan": 312,
     "deskripsi": "Kacang mete lokal diolah dengan teknik sangrai tradisional menggunakan "
                  "wajan tanah liat hingga gurih, renyah, dan beraroma menggoda."},
    {"id": 5, "nama": "Es Gempol Pleret", "kategori": "Minuman", "harga": 6000,
     "lokasi": "Alun-alun Kota Wonogiri", "jam": "10:00 - 22:00", "rating": 4.4, "ulasan": 89,
     "deskripsi": "Minuman segar tradisional berupa bola-bola tepung beras (gempol) dan "
                  "lempengan tipis merah (pleret) disajikan dalam kuah santan gula jawa."},
    {"id": 6, "nama": "Sate Kere", "kategori": "Makanan Berat", "harga": 12000,
     "lokasi": "Jl. Diponegoro No. 12", "jam": "17:00 - 23:00", "rating": 4.6, "ulasan": 143,
     "deskripsi": "Kuliner legendaris dari tempe gembus, jeroan, dan kulit sapi yang "
                  "dibakar lalu disiram bumbu kacang kaya rempah."},
    {"id": 7, "nama": "Madu Klanceng", "kategori": "Oleh-oleh", "harga": 35000,
     "lokasi": "Desa Girimarto", "jam": "08:00 - 17:00", "rating": 4.9, "ulasan": 198,
     "deskripsi": "Madu premium dari lebah klanceng (Trigona sp.) dengan rasa asam-manis "
                  "khas dan kandungan antioksidan tinggi."},
    {"id": 8, "nama": "Bakmi Jowo Wonogiri", "kategori": "Makanan Berat", "harga": 15000,
     "lokasi": "Jl. Pemuda", "jam": "17:00 - 24:00", "rating": 4.7, "ulasan": 234,
     "deskripsi": "Mie telur dimasak di atas bara arang menghasilkan cita rasa smoky "
                  "yang autentik, disajikan dengan ayam kampung dan telur."},
    {"id": 9, "nama": "Wedang Uwuh", "kategori": "Minuman", "harga": 8000,
     "lokasi": "Warung Tradisional Alun-alun", "jam": "16:00 - 22:00", "rating": 4.6, "ulasan": 77,
     "deskripsi": "Minuman herbal hangat dari kayu manis, cengkeh, jahe, kapulaga, dan "
                  "daun pandan yang direbus bersama, berwarna merah cantik."},
    {"id": 10, "nama": "Pecel Wonogiri", "kategori": "Makanan Berat", "harga": 10000,
     "lokasi": "Pasar Wonogiri & sekitar kota", "jam": "06:00 - 11:00", "rating": 4.8, "ulasan": 189,
     "deskripsi": "Pecel dengan bumbu kacang kental dan legit dicampur daun jeruk purut, "
                  "disajikan di atas daun pisang dengan rempeyek dan telur pindang."},
]

DESTINASI_DATA_DEFAULT = [
    {"id": 1, "nama": "Waduk Gajah Mungkur", "kategori": "Waduk & Air", "harga": 15000,
     "lokasi": "Sendang, Wonogiri", "jam": "07:00 - 17:00", "rating": 4.8, "ulasan": 542,
     "fasilitas": "Parkir Luas, Warung Makan, Toilet, Gazebo, Sewa Perahu, Camping",
     "deskripsi": "Ikon wisata utama Wonogiri! Waduk buatan terbesar di Jawa Tengah dengan "
                  "panorama air biru luas dikelilingi bukit hijau. Sunset di sini legendaris."},
    {"id": 2, "nama": "Bukit Cumbri", "kategori": "Alam & Pegunungan", "harga": 10000,
     "lokasi": "Desa Sendang", "jam": "05:00 - 18:00", "rating": 4.9, "ulasan": 387,
     "fasilitas": "Basecamp, Toilet, Warung, Area Camping, Gardu Pandang",
     "deskripsi": "Spot sunrise dan sunset terbaik di Wonogiri dengan panorama 360 derajat "
                  "Waduk Gajah Mungkur dan Gunung Lawu. Jalur pendakian ringan 30 menit."},
    {"id": 3, "nama": "Air Terjun Girimanik", "kategori": "Air Terjun", "harga": 12000,
     "lokasi": "Desa Setren, Slogohimo", "jam": "07:00 - 17:00", "rating": 4.9, "ulasan": 298,
     "fasilitas": "Parkir, Toilet, Mushola, Warung, Jembatan Gantung, Jalur Trekking",
     "deskripsi": "Kompleks tiga air terjun bertingkat di kawasan hutan pinus sejuk dengan "
                  "suhu 18-22 derajat, cocok untuk wisata keluarga."},
    {"id": 4, "nama": "Gunung Gandul", "kategori": "Alam & Pegunungan", "harga": 7000,
     "lokasi": "Desa Sendang", "jam": "06:00 - 18:00", "rating": 4.7, "ulasan": 256,
     "fasilitas": "Parkir, Warung, Toilet, Spot Foto, Jalur Trekking Ringan",
     "deskripsi": "Bukit kapur ikonik dengan puncak menyerupai padang savana mini, spot "
                  "foto favorit dengan latar Waduk Gajah Mungkur."},
    {"id": 5, "nama": "Pantai Sembukan", "kategori": "Waduk & Air", "harga": 5000,
     "lokasi": "Desa Sembukan, Paranggupito", "jam": "06:00 - 18:00", "rating": 4.5, "ulasan": 178,
     "fasilitas": "Parkir, Warung Ikan Bakar, Toilet, Area Piknik",
     "deskripsi": "Pantai selatan yang eksotis dengan ombak besar Samudera Hindia dan "
                  "tebing karang megah, terkenal dengan ritual Malam 1 Suro."},
    {"id": 6, "nama": "Goa Putri Kencana", "kategori": "Goa", "harga": 8000,
     "lokasi": "Desa Pracimantoro", "jam": "08:00 - 16:00", "rating": 4.5, "ulasan": 134,
     "fasilitas": "Parkir, Penerangan Goa, Pemandu Wisata, Toilet",
     "deskripsi": "Goa alam kawasan karst dengan formasi stalaktit-stalagmit menakjubkan, "
                  "dilengkapi pencahayaan warna-warni dan jalur aman."},
    {"id": 7, "nama": "Museum Wayang Indonesia", "kategori": "Wisata Budaya & Religi", "harga": 5000,
     "lokasi": "Jl. Pemuda No. 5", "jam": "08:00 - 16:00 (Tutup Senin)", "rating": 4.4, "ulasan": 98,
     "fasilitas": "AC, Toilet, Pemandu, Toko Souvenir, Ruang Pertunjukan",
     "deskripsi": "Menyimpan lebih dari 5.000 koleksi wayang se-Nusantara, salah satu "
                  "museum wayang terlengkap di Indonesia."},
    {"id": 8, "nama": "Puncak Joglo", "kategori": "Alam & Pegunungan", "harga": 15000,
     "lokasi": "Lereng Lawu, Jatisrono", "jam": "24 Jam (Camping)", "rating": 4.8, "ulasan": 321,
     "fasilitas": "Basecamp, Toilet, Warung, Area Camping, Pemandu Pendakian",
     "deskripsi": "Titik tertinggi kawasan Gunung Lawu, di hari cerah bisa melihat "
                  "deretan Gunung Merapi, Merbabu, Lawu, dan Semeru."},
    {"id": 9, "nama": "Desa Wisata Kepuhsari", "kategori": "Wisata Budaya & Religi", "harga": 10000,
     "lokasi": "Desa Kepuhsari, Manyaran", "jam": "08:00 - 16:00", "rating": 4.7, "ulasan": 145,
     "fasilitas": "Workshop Membuat Wayang, Galeri, Homestay, Pemandu",
     "deskripsi": "Desa penghasil wayang kulit terbesar di Indonesia, wisatawan dapat "
                  "belajar langsung membuat wayang dari para pengrajin."},
]


def format_rupiah(n):
    return "Rp " + f"{n:,}".replace(",", ".")




def _rounded_rect_points(x1, y1, x2, y2, r):
    r = min(r, (x2 - x1) / 2, (y2 - y1) / 2)
    return [
        x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
        x2, y2 - r, x2, y2, x2 - r, y2, x1 + r, y2,
        x1, y2, x1, y2 - r, x1, y1 + r, x1, y1,
    ]


class Pill(tk.Canvas):
  

    def __init__(self, parent, text, bg, fg="white", hover_bg=None, command=None,
                 font=(FONT_UTAMA, 10, "bold"), padx=16, pady=8, min_width=0):
        parent_bg = parent["bg"] if "bg" in parent.keys() else WARNA["latar"]
        super().__init__(parent, bg=parent_bg, highlightthickness=0, bd=0)
        f = tkfont.Font(font=font)
        w = max(f.measure(text) + padx * 2, min_width)
        h = f.metrics("linespace") + pady * 2
        self.config(width=w, height=h)
        self.w, self.h, self.text, self.font = w, h, text, font
        self.bg_color = bg
        self.hover_color = hover_bg or bg
        self.fg_color = fg
        self.command = command
        self._draw(bg)
        if command:
            self.bind("<Enter>", lambda e: (self._draw(self.hover_color), self.config(cursor="hand2")))
            self.bind("<Leave>", lambda e: self._draw(self.bg_color))
            self.bind("<Button-1>", lambda e: self.command())

    def _draw(self, color):
        self.delete("all")
        self.create_polygon(_rounded_rect_points(1, 1, self.w - 1, self.h - 1, self.h / 2),
                             smooth=True, fill=color, outline=color)
        self.create_text(self.w / 2, self.h / 2, text=self.text, fill=self.fg_color, font=self.font)

    def set_style(self, bg, fg=None):
        self.bg_color = bg
        if fg:
            self.fg_color = fg
        self._draw(self.bg_color)


class Logo(tk.Canvas):
    """Lingkaran gradasi hijau berisi ikon, meniru .brand-logo pada navbar."""

    def __init__(self, parent, size=48, icon="\U0001F33F"):
        parent_bg = parent["bg"] if "bg" in parent.keys() else WARNA["latar"]
        super().__init__(parent, width=size, height=size, bg=parent_bg, highlightthickness=0, bd=0)
        self.create_oval(2, 2, size - 2, size - 2, fill=WARNA["primer"], outline=WARNA["hijau"], width=2)
        self.create_text(size / 2, size / 2, text=icon, font=(FONT_UTAMA, int(size * 0.42)))


# =========================================================================
# 3. DATA LAYER (Encapsulation)
# =========================================================================

class DataStore:
    """Mengelola penyimpanan data akun (users.json) dan data konten
    (kuliner.json, destinasi.json)."""

    def __init__(self):
        self.users = self._load(USERS_FILE, {})
        self.kuliner = self._load(KULINER_FILE, KULINER_DATA_DEFAULT)
        self.destinasi = self._load(DESTINASI_FILE, DESTINASI_DATA_DEFAULT)
        self.buku_tamu = self._load(BUKU_TAMU_FILE, [])
        self.transaksi = self._load(TRANSAKSI_FILE, [])

    @staticmethod
    def _load(path, default):
        if not os.path.exists(path):
            return json.loads(json.dumps(default))  # deep copy
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return json.loads(json.dumps(default))

    @staticmethod
    def _save(path, data):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def register(self, nama, username, password, role=ROLE_USER):
        if not all([nama, username, password]):
            return False, "Semua kolom wajib diisi!"
        if username in self.users:
            return False, "Username sudah terdaftar!"
        if role not in DAFTAR_ROLE:
            role = ROLE_USER
        self.users[username] = {
            "nama": nama, "password": password, "role": role,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        self._save(USERS_FILE, self.users)
        return True, "Registrasi berhasil! Silakan login."

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            user.setdefault("role", ROLE_USER)
            return True, user
        return False, None

    @staticmethod
    def _next_id(data):
        return max([d["id"] for d in data], default=0) + 1

    def add_item(self, data, file_path, item):
        item = dict(item)
        item["id"] = self._next_id(data)
        data.append(item)
        self._save(file_path, data)
        return item

    def update_item(self, data, file_path, item_id, new_values):
        for d in data:
            if d["id"] == item_id:
                d.update(new_values)
                self._save(file_path, data)
                return True
        return False

    def delete_item(self, data, file_path, item_id):
        idx = next((i for i, d in enumerate(data) if d["id"] == item_id), None)
        if idx is None:
            return False
        data.pop(idx)
        self._save(file_path, data)
        return True

    # ---------------------------------------------------- buku tamu digital --
    def tambah_buku_tamu(self, nama, pesan):
        entri = {
            "id": self._next_id(self.buku_tamu),
            "nama": nama,
            "pesan": pesan,
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        self.buku_tamu.append(entri)
        self._save(BUKU_TAMU_FILE, self.buku_tamu)
        return entri

    def hapus_buku_tamu(self, entri_id):
        return self.delete_item(self.buku_tamu, BUKU_TAMU_FILE, entri_id)

    # ------------------------------------------------------------ transaksi --
    def buat_transaksi(self, username, item_nama, jumlah, harga_satuan):
        entri = {
            "id": self._next_id(self.transaksi),
            "username": username,
            "item_nama": item_nama,
            "jumlah": jumlah,
            "harga_satuan": harga_satuan,
            "subtotal": jumlah * harga_satuan,
            "status": STATUS_DIPROSES,
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
        self.transaksi.append(entri)
        self._save(TRANSAKSI_FILE, self.transaksi)
        return entri

    def ubah_status_transaksi(self, trx_id, status):
        for d in self.transaksi:
            if d["id"] == trx_id:
                d["status"] = status
                self._save(TRANSAKSI_FILE, self.transaksi)
                return True
        return False

    def hapus_transaksi(self, trx_id):
        return self.delete_item(self.transaksi, TRANSAKSI_FILE, trx_id)


# =========================================================================
# 4. HALAMAN-HALAMAN GUI
# =========================================================================

class BasePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=WARNA["latar"])
        self.app = app

    def on_show(self):
        pass


class LoginPage(BasePage):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        box = tk.Frame(self, bg=WARNA["kartu"], padx=44, pady=36,
                        highlightbackground=WARNA["border"], highlightthickness=1)
        box.place(relx=0.5, rely=0.5, anchor="center")

        Logo(box, size=56).grid(row=0, column=0, columnspan=2, pady=(0, 10))
        Pill(box, "SELAMAT DATANG", bg=WARNA["hijau_muda"], fg=WARNA["primer"],
             font=(FONT_UTAMA, 9, "bold"), padx=14, pady=6).grid(row=1, column=0, columnspan=2, pady=(0, 10))
        tk.Label(box, text="Wisata & Kuliner Wonogiri", font=(FONT_UTAMA, 19, "bold"),
                 fg=WARNA["teks"], bg=WARNA["kartu"]).grid(row=2, column=0, columnspan=2, pady=(0, 4))
        tk.Label(box, text="Masuk untuk menjelajahi kuliner khas dan destinasi wisata",
                 font=(FONT_UTAMA, 9), fg=WARNA["teks_abu"], bg=WARNA["kartu"]).grid(
            row=3, column=0, columnspan=2, pady=(0, 22))

        tk.Label(box, text="Username", font=(FONT_UTAMA, 9, "bold"), fg=WARNA["teks"],
                 bg=WARNA["kartu"], anchor="w").grid(row=4, column=0, columnspan=2, sticky="w")
        self.entry_user = tk.Entry(box, width=32, font=(FONT_UTAMA, 10), relief="flat",
                                    highlightthickness=1, highlightbackground=WARNA["border"],
                                    highlightcolor=WARNA["primer"])
        self.entry_user.grid(row=5, column=0, columnspan=2, pady=(4, 14), ipady=6)

        tk.Label(box, text="Password", font=(FONT_UTAMA, 9, "bold"), fg=WARNA["teks"],
                 bg=WARNA["kartu"], anchor="w").grid(row=6, column=0, columnspan=2, sticky="w")
        self.entry_pwd = tk.Entry(box, width=32, show="*", font=(FONT_UTAMA, 10), relief="flat",
                                   highlightthickness=1, highlightbackground=WARNA["border"],
                                   highlightcolor=WARNA["primer"])
        self.entry_pwd.grid(row=7, column=0, columnspan=2, pady=(4, 20), ipady=6)
        self.entry_pwd.bind("<Return>", lambda e: self.login())

        Pill(box, "Masuk", bg=WARNA["primer"], hover_bg=WARNA["primer_gelap"], fg="white",
             command=self.login, font=(FONT_UTAMA, 11, "bold"), padx=0, pady=10,
             min_width=280).grid(row=8, column=0, columnspan=2, pady=(0, 14))

        link = tk.Label(box, text="Belum punya akun?  Daftar di sini", fg=WARNA["aksen"],
                         bg=WARNA["kartu"], cursor="hand2", font=(FONT_UTAMA, 9, "bold"))
        link.grid(row=9, column=0, columnspan=2)
        link.bind("<Button-1>", lambda e: self.app.show_page("RegisterPage"))

        
    def on_show(self):
        self.entry_user.delete(0, tk.END)
        self.entry_pwd.delete(0, tk.END)
        self.entry_user.focus_set()

    def login(self):
        username = self.entry_user.get().strip()
        pwd = self.entry_pwd.get().strip()
        ok, user = self.app.data.login(username, pwd)
        if ok:
            self.app.current_user = {"username": username, **user}
            peran = "Admin" if user["role"] == ROLE_ADMIN else "Pengunjung"
            messagebox.showinfo("Login", f"Login berhasil sebagai {peran}!\nSelamat datang, {user['nama']}.")
            self.app.build_menu()
            self.app.show_page("MainPage")
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")


class RegisterPage(BasePage):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        box = tk.Frame(self, bg=WARNA["kartu"], padx=44, pady=32,
                        highlightbackground=WARNA["border"], highlightthickness=1)
        box.place(relx=0.5, rely=0.5, anchor="center")

        Logo(box, size=48).grid(row=0, column=0, columnspan=2, pady=(0, 8))
        tk.Label(box, text="Buat Akun Baru", font=(FONT_UTAMA, 17, "bold"),
                 fg=WARNA["teks"], bg=WARNA["kartu"]).grid(row=1, column=0, columnspan=2, pady=(0, 18))

        labels = ["Nama Lengkap", "Username", "Password"]
        self.entries = {}
        for i, lbl in enumerate(labels, start=2):
            tk.Label(box, text=lbl, font=(FONT_UTAMA, 9, "bold"), fg=WARNA["teks"],
                     bg=WARNA["kartu"], anchor="w").grid(row=i, column=0, columnspan=2, sticky="w", pady=(6, 0))
            show = "*" if lbl == "Password" else ""
            ent = tk.Entry(box, width=32, show=show, font=(FONT_UTAMA, 10), relief="flat",
                            highlightthickness=1, highlightbackground=WARNA["border"],
                            highlightcolor=WARNA["primer"])
            ent.grid(row=i + 1, column=0, columnspan=2, pady=(4, 4), ipady=6)
            self.entries[lbl] = ent

        baris_role = 2 + len(labels) * 2
        tk.Label(box, text="Daftar sebagai", font=(FONT_UTAMA, 9, "bold"), fg=WARNA["teks"],
                 bg=WARNA["kartu"], anchor="w").grid(row=baris_role, column=0, columnspan=2, sticky="w", pady=(6, 0))
        self.combo_role = ttk.Combobox(box, values=["Pengunjung", "Admin"], state="readonly",
                                        width=29, font=(FONT_UTAMA, 10))
        self.combo_role.set("Pengunjung")
        self.combo_role.grid(row=baris_role + 1, column=0, columnspan=2, pady=(4, 18), ipady=3)

        Pill(box, "Register", bg=WARNA["hijau"], hover_bg=WARNA["primer_gelap"], fg="white",
             command=self.register, font=(FONT_UTAMA, 11, "bold"), padx=0, pady=10,
             min_width=280).grid(row=baris_role + 2, column=0, columnspan=2, pady=(0, 14))

        link = tk.Label(box, text="Sudah punya akun?  Login di sini", fg=WARNA["aksen"],
                         bg=WARNA["kartu"], cursor="hand2", font=(FONT_UTAMA, 9, "bold"))
        link.grid(row=baris_role + 3, column=0, columnspan=2)
        link.bind("<Button-1>", lambda e: self.app.show_page("LoginPage"))

    def on_show(self):
        for ent in self.entries.values():
            ent.delete(0, tk.END)
        self.combo_role.set("Pengunjung")

    def register(self):
        nama = self.entries["Nama Lengkap"].get().strip()
        username = self.entries["Username"].get().strip()
        pwd = self.entries["Password"].get().strip()
        role = ROLE_ADMIN if self.combo_role.get() == "Admin" else ROLE_USER
        ok, pesan = self.app.data.register(nama, username, pwd, role)
        if ok:
            messagebox.showinfo("Registrasi", pesan)
            self.app.show_page("LoginPage")
        else:
            messagebox.showerror("Registrasi Gagal", pesan)


class ItemFormDialog(tk.Toplevel):
    """Dialog tambah/edit item, dipakai oleh admin."""

    def __init__(self, parent, judul, item=None, pakai_fasilitas=False, on_submit=None):
        super().__init__(parent)
        self.title(judul)
        self.configure(bg=WARNA["kartu"])
        self.resizable(False, False)
        self.on_submit = on_submit
        item = item or {}

        tk.Label(self, text=judul, font=(FONT_UTAMA, 13, "bold"), fg=WARNA["primer"],
                 bg=WARNA["kartu"]).grid(row=0, column=0, columnspan=2, padx=18, pady=(18, 6), sticky="w")

        field_dasar = [
            ("nama", "Nama"), ("kategori", "Kategori"), ("harga", "Harga (angka)"),
            ("lokasi", "Lokasi"), ("jam", "Jam Operasional"),
            ("rating", "Rating (0-5)"), ("ulasan", "Jumlah Ulasan"),
        ]
        if pakai_fasilitas:
            field_dasar.append(("fasilitas", "Fasilitas"))

        self.entries = {}
        for i, (key, label) in enumerate(field_dasar, start=1):
            tk.Label(self, text=label + ":", bg=WARNA["kartu"], fg=WARNA["teks"],
                     font=(FONT_UTAMA, 9), anchor="w").grid(row=i, column=0, sticky="w", padx=18, pady=6)
            ent = tk.Entry(self, width=32, font=(FONT_UTAMA, 10), relief="flat",
                            highlightthickness=1, highlightbackground=WARNA["border"],
                            highlightcolor=WARNA["primer"])
            ent.insert(0, str(item.get(key, "")))
            ent.grid(row=i, column=1, padx=18, pady=6, ipady=3)
            self.entries[key] = ent

        baris_deskripsi = len(field_dasar) + 1
        tk.Label(self, text="Deskripsi:", bg=WARNA["kartu"], fg=WARNA["teks"],
                 font=(FONT_UTAMA, 9), anchor="nw").grid(row=baris_deskripsi, column=0, sticky="nw", padx=18, pady=6)
        self.txt_deskripsi = tk.Text(self, width=30, height=5, font=(FONT_UTAMA, 10), relief="flat",
                                      highlightthickness=1, highlightbackground=WARNA["border"],
                                      highlightcolor=WARNA["primer"], bg=WARNA["hijau_muda"])
        self.txt_deskripsi.insert("1.0", item.get("deskripsi", ""))
        self.txt_deskripsi.grid(row=baris_deskripsi, column=1, padx=18, pady=6)

        Pill(self, "Simpan", bg=WARNA["hijau"], hover_bg=WARNA["primer_gelap"], fg="white",
             command=self._submit, font=(FONT_UTAMA, 10, "bold"), padx=0, pady=9,
             min_width=180).grid(row=baris_deskripsi + 1, column=0, columnspan=2, pady=18)

        self.grab_set()

    def _submit(self):
        try:
            hasil = {
                "nama": self.entries["nama"].get().strip(),
                "kategori": self.entries["kategori"].get().strip(),
                "harga": int(self.entries["harga"].get().strip() or 0),
                "lokasi": self.entries["lokasi"].get().strip(),
                "jam": self.entries["jam"].get().strip(),
                "rating": float(self.entries["rating"].get().strip() or 0),
                "ulasan": int(self.entries["ulasan"].get().strip() or 0),
                "deskripsi": self.txt_deskripsi.get("1.0", tk.END).strip(),
            }
        except ValueError:
            messagebox.showerror("Input Salah", "Harga, Rating, dan Ulasan harus berupa angka!")
            return
        if "fasilitas" in self.entries:
            hasil["fasilitas"] = self.entries["fasilitas"].get().strip()
        if not hasil["nama"]:
            messagebox.showerror("Input Salah", "Nama tidak boleh kosong!")
            return
        if self.on_submit:
            self.on_submit(hasil)
        self.destroy()


class ItemListPanel(tk.Frame):
    """Panel daftar (kartu) + detail untuk satu jenis data (Kuliner /
    Destinasi). Tampilan kartu meniru .info-card pada style.css: badge
    harga, tag kategori berwarna, rating bintang, dan efek highlight
    saat kartu dipilih. Tombol kelola data (Tambah/Edit/Hapus) hanya
    tampil untuk role admin."""

    KOLOM_HARGA_LABEL = "Harga"

    SORT_OPTIONS = {
        "Rating Tertinggi": lambda d: (-d["rating"], d["nama"]),
        "Harga Terendah": lambda d: (d["harga"], d["nama"]),
        "Harga Tertinggi": lambda d: (-d["harga"], d["nama"]),
        "Terbaru": lambda d: -d["id"],
        "Nama (A-Z)": lambda d: d["nama"].lower(),
    }

    def __init__(self, parent, datastore, data, file_path, is_admin=False, jenis="kuliner", on_pesan=None):
        super().__init__(parent, bg=WARNA["latar"])
        self.datastore = datastore
        self.data = data
        self.file_path = file_path
        self.is_admin = is_admin
        self.jenis = jenis
        self.on_pesan = on_pesan
        self.item_terpilih = None
        self.kategori_aktif = "Semua"
        self.kata_kunci = ""
        self.urutan_aktif = "Rating Tertinggi"
        self.pakai_fasilitas = bool(data) and "fasilitas" in data[0]

        # warna badge/tag mengikuti style.css: kuliner = oranye, destinasi = hijau
        if jenis == "kuliner":
            self.warna_tag_bg, self.warna_tag_fg = WARNA["aksen_muda"], WARNA["aksen_gelap"]
            self.warna_badge = WARNA["aksen"]
        else:
            self.warna_tag_bg, self.warna_tag_fg = WARNA["hijau_muda"], WARNA["primer"]
            self.warna_badge = WARNA["primer"]

        self.pill_kategori = {}   # nama_kategori -> Pill widget (untuk update gaya aktif)
        self.kartu_widgets = {}   # item_id -> frame kartu (untuk highlight terpilih)

        # ---------------- kotak pencarian + sortir ----------------
        self.frame_cari = tk.Frame(self, bg=WARNA["latar"])
        self.frame_cari.pack(fill="x", padx=16, pady=(16, 8))

        cari_box = tk.Frame(self.frame_cari, bg=WARNA["kartu"], highlightbackground=WARNA["border"],
                             highlightthickness=1)
        cari_box.pack(side="left", fill="x", expand=True, ipady=2)
        tk.Label(cari_box, text="\U0001F50D", bg=WARNA["kartu"], fg=WARNA["teks_abu"],
                 font=(FONT_UTAMA, 10)).pack(side="left", padx=(10, 4))
        self.var_cari = tk.StringVar()
        self.entry_cari = tk.Entry(cari_box, textvariable=self.var_cari, font=(FONT_UTAMA, 10),
                                    relief="flat", bg=WARNA["kartu"], fg=WARNA["teks"],
                                    highlightthickness=0, bd=0)
        placeholder = "Cari kuliner..." if jenis == "kuliner" else "Cari destinasi..."
        self.entry_cari.insert(0, "")
        self.entry_cari.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.entry_cari.bind("<KeyRelease>", self._on_cari_ketik)
        self._cari_placeholder = placeholder
        self._set_placeholder()
        self.entry_cari.bind("<FocusIn>", self._hapus_placeholder)
        self.entry_cari.bind("<FocusOut>", lambda e: self._set_placeholder() if not self.var_cari.get() else None)

        tk.Label(self.frame_cari, text="Urutkan:", bg=WARNA["latar"], fg=WARNA["teks_abu"],
                 font=(FONT_UTAMA, 9, "bold")).pack(side="left", padx=(14, 6))
        self.combo_urut = ttk.Combobox(self.frame_cari, values=list(self.SORT_OPTIONS.keys()),
                                        state="readonly", width=16, font=(FONT_UTAMA, 9))
        self.combo_urut.set(self.urutan_aktif)
        self.combo_urut.pack(side="left")
        self.combo_urut.bind("<<ComboboxSelected>>", self._on_urut_ganti)

        # ---------------- filter kategori (pill) ----------------
        self.frame_filter = tk.Frame(self, bg=WARNA["latar"])
        self.frame_filter.pack(fill="x", padx=16, pady=(0, 8))

        main = tk.Frame(self, bg=WARNA["latar"])
        main.pack(expand=True, fill="both", padx=16, pady=(0, 16))

        # ---------------- daftar kartu (scrollable) ----------------
        left = tk.Frame(main, bg=WARNA["latar"], width=330)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        if self.is_admin:
            aksi = tk.Frame(left, bg=WARNA["latar"])
            aksi.pack(fill="x", pady=(0, 8))
            Pill(aksi, "+ Tambah", bg=WARNA["hijau"], hover_bg=WARNA["primer_gelap"], fg="white",
                 command=self.tambah_item, font=(FONT_UTAMA, 9, "bold"), padx=14, pady=7).pack(side="left", padx=(0, 6))
            Pill(aksi, "Edit", bg=WARNA["aksen"], hover_bg=WARNA["aksen_gelap"], fg="white",
                 command=self.edit_item, font=(FONT_UTAMA, 9, "bold"), padx=14, pady=7).pack(side="left", padx=(0, 6))
            Pill(aksi, "Hapus", bg=WARNA["merah"], hover_bg=WARNA["merah_gelap"], fg="white",
                 command=self.hapus_item, font=(FONT_UTAMA, 9, "bold"), padx=14, pady=7).pack(side="left")

        self.lbl_jumlah_hasil = tk.Label(left, text="", bg=WARNA["latar"], fg=WARNA["teks_abu"],
                                          font=(FONT_UTAMA, 8, "italic"), anchor="w")
        self.lbl_jumlah_hasil.pack(fill="x", pady=(0, 4))

        list_container = tk.Frame(left, bg=WARNA["latar"], highlightbackground=WARNA["border"],
                                   highlightthickness=1)
        list_container.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(list_container, bg=WARNA["latar"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = tk.Frame(self.canvas, bg=WARNA["latar"])
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self._win = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self._win, width=e.width))
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        for widget in (list_container, self.canvas, self.scroll_frame):
            widget.bind("<MouseWheel>", self._scroll)
            widget.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-2, "units"))
            widget.bind("<Button-5>", lambda e: self.canvas.yview_scroll(2, "units"))

        # ---------------- panel detail (kartu besar) ----------------
        right = tk.Frame(main, bg=WARNA["kartu"], highlightbackground=WARNA["border"], highlightthickness=1)
        right.pack(side="left", fill="both", expand=True, padx=(16, 0))
        inner = tk.Frame(right, bg=WARNA["kartu"], padx=26, pady=22)
        inner.pack(fill="both", expand=True)

        top_row = tk.Frame(inner, bg=WARNA["kartu"])
        top_row.pack(fill="x")
        self.tag_kategori = Pill(top_row, "KATEGORI", bg=self.warna_tag_bg, fg=self.warna_tag_fg,
                                  font=(FONT_UTAMA, 8, "bold"), padx=12, pady=5)
        self.tag_kategori.pack(side="left")
        self.badge_harga = Pill(top_row, "Rp 0", bg=self.warna_badge, fg="white",
                                 font=(FONT_UTAMA, 9, "bold"), padx=14, pady=6)
        self.badge_harga.pack(side="right")

        self.lbl_nama = tk.Label(inner, text="Pilih salah satu item di daftar",
                                  font=(FONT_UTAMA, 18, "bold"), bg=WARNA["kartu"], fg=WARNA["teks"],
                                  anchor="w", justify="left", wraplength=430)
        self.lbl_nama.pack(fill="x", pady=(14, 4))

        self.lbl_rating = tk.Label(inner, text="", font=(FONT_UTAMA, 10, "bold"),
                                    bg=WARNA["kartu"], fg=WARNA["aksen"], anchor="w")
        self.lbl_rating.pack(fill="x", pady=(0, 10))

        self.lbl_info = tk.Label(inner, text="", font=(FONT_UTAMA, 9), bg=WARNA["kartu"],
                                  fg=WARNA["teks_abu"], justify="left", anchor="w")
        self.lbl_info.pack(fill="x", pady=(0, 14))

        self.btn_pesan = None
        if self.jenis == "kuliner" and not self.is_admin and self.on_pesan:
            self.btn_pesan = Pill(inner, "\U0001F6D2 Pesan Sekarang", bg=WARNA["hijau"],
                                   hover_bg=WARNA["primer_gelap"], fg="white",
                                   command=self._klik_pesan, font=(FONT_UTAMA, 10, "bold"),
                                   padx=0, pady=10, min_width=430)
            self.btn_pesan.pack(side="bottom", fill="x", pady=(14, 0))

        desc_box = tk.Frame(inner, bg=WARNA["hijau_muda"])
        desc_box.pack(fill="both", expand=True)
        self.txt_deskripsi = tk.Text(desc_box, wrap="word", relief="flat", bg=WARNA["hijau_muda"],
                                      fg=WARNA["teks"], font=(FONT_UTAMA, 10), padx=14, pady=12,
                                      highlightthickness=0, bd=0)
        self.txt_deskripsi.pack(fill="both", expand=True)
        self.txt_deskripsi.config(state="disabled")

        self._bangun_pill_kategori()

    def _scroll(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _bind_scroll_rekursif(self, widget):
        """Supaya scroll roda mouse tetap jalan walau kursor ada di atas
        label/frame di dalam kartu (bukan cuma di area kosong canvas)."""
        widget.bind("<MouseWheel>", self._scroll)
        widget.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-2, "units"))
        widget.bind("<Button-5>", lambda e: self.canvas.yview_scroll(2, "units"))
        for child in widget.winfo_children():
            self._bind_scroll_rekursif(child)

    # ---------------------------------------------------- pencarian & sortir --
    def _set_placeholder(self):
        self.entry_cari.delete(0, tk.END)
        self.entry_cari.insert(0, self._cari_placeholder)
        self.entry_cari.config(fg=WARNA["teks_abu"])

    def _hapus_placeholder(self, event=None):
        if self.entry_cari.get() == self._cari_placeholder:
            self.entry_cari.delete(0, tk.END)
            self.entry_cari.config(fg=WARNA["teks"])

    def _on_cari_ketik(self, event=None):
        teks = self.entry_cari.get()
        if teks == self._cari_placeholder:
            teks = ""
        self.kata_kunci = teks.strip().lower()
        self.refresh_list()

    def _on_urut_ganti(self, event=None):
        self.urutan_aktif = self.combo_urut.get()
        self.refresh_list()

    # ---------------------------------------------------- filter kategori --
    def _bangun_pill_kategori(self):
        for w in self.frame_filter.winfo_children():
            w.destroy()
        self.pill_kategori = {}
        kategori_list = ["Semua"] + sorted({d["kategori"] for d in self.data})
        for kat in kategori_list:
            aktif = (kat == self.kategori_aktif)
            bg = WARNA["primer"] if aktif else WARNA["kartu"]
            fg = "white" if aktif else WARNA["teks"]
            p = Pill(self.frame_filter, kat, bg=bg, fg=fg,
                     hover_bg=WARNA["primer"] if not aktif else WARNA["primer"],
                     command=lambda k=kat: self._pilih_kategori(k),
                     font=(FONT_UTAMA, 8, "bold"), padx=12, pady=6)
            p.pack(side="left", padx=(0, 6), pady=2)
            self.pill_kategori[kat] = p

    def _pilih_kategori(self, kategori):
        self.kategori_aktif = kategori
        for kat, pill in self.pill_kategori.items():
            aktif = (kat == kategori)
            pill.set_style(WARNA["primer"] if aktif else WARNA["kartu"], "white" if aktif else WARNA["teks"])
        self.refresh_list()

    # ------------------------------------------------------------- daftar --
    def refresh_list(self):
        kategori_list_baru = ["Semua"] + sorted({d["kategori"] for d in self.data})
        if set(kategori_list_baru) != set(self.pill_kategori.keys()):
            if self.kategori_aktif not in kategori_list_baru:
                self.kategori_aktif = "Semua"
            self._bangun_pill_kategori()

        for w in self.scroll_frame.winfo_children():
            w.destroy()
        self.kartu_widgets = {}

        item_terlihat = [d for d in self.data
                          if self.kategori_aktif == "Semua" or d["kategori"] == self.kategori_aktif]

        if self.kata_kunci:
            item_terlihat = [
                d for d in item_terlihat
                if self.kata_kunci in d["nama"].lower()
                or self.kata_kunci in d["lokasi"].lower()
                or self.kata_kunci in d["kategori"].lower()
                or self.kata_kunci in d["deskripsi"].lower()
            ]

        kunci_urut = self.SORT_OPTIONS.get(self.urutan_aktif, self.SORT_OPTIONS["Rating Tertinggi"])
        item_terlihat = sorted(item_terlihat, key=kunci_urut)

        self.lbl_jumlah_hasil.config(text=f"{len(item_terlihat)} item ditemukan")

        if not item_terlihat:
            tk.Label(self.scroll_frame, text="Tidak ada hasil yang cocok.",
                     bg=WARNA["latar"], fg=WARNA["teks_abu"], font=(FONT_UTAMA, 9, "italic")).pack(pady=20)

        for item in item_terlihat:
            self._buat_kartu(item)

        if self.item_terpilih and self.item_terpilih["id"] not in [d["id"] for d in item_terlihat]:
            self.tampilkan_detail(None)

    def _buat_kartu(self, item):
        terpilih = self.item_terpilih is not None and self.item_terpilih["id"] == item["id"]
        border = WARNA["aksen"] if terpilih else WARNA["border"]
        kartu = tk.Frame(self.scroll_frame, bg=WARNA["kartu"], highlightbackground=border,
                          highlightthickness=2 if terpilih else 1, cursor="hand2")
        kartu.pack(fill="x", pady=5, padx=2)
        isi = tk.Frame(kartu, bg=WARNA["kartu"], padx=12, pady=10)
        isi.pack(fill="both", expand=True)

        baris1 = tk.Frame(isi, bg=WARNA["kartu"])
        baris1.pack(fill="x")
        tk.Label(baris1, text=item["nama"], font=(FONT_UTAMA, 11, "bold"), bg=WARNA["kartu"],
                 fg=WARNA["teks"], anchor="w", justify="left", wraplength=190).pack(side="left")
        Pill(baris1, format_rupiah(item["harga"]), bg=self.warna_badge, fg="white",
             font=(FONT_UTAMA, 8, "bold"), padx=10, pady=4).pack(side="right")

        baris2 = tk.Frame(isi, bg=WARNA["kartu"])
        baris2.pack(fill="x", pady=(6, 0))
        Pill(baris2, item["kategori"], bg=self.warna_tag_bg, fg=self.warna_tag_fg,
             font=(FONT_UTAMA, 8, "bold"), padx=9, pady=3).pack(side="left")
        tk.Label(baris2, text=f"\u2605 {item['rating']}", font=(FONT_UTAMA, 9, "bold"),
                 bg=WARNA["kartu"], fg=WARNA["aksen"]).pack(side="right")

        tk.Label(isi, text=f"\U0001F4CD {item['lokasi']}", font=(FONT_UTAMA, 9), bg=WARNA["kartu"],
                 fg=WARNA["teks_abu"], anchor="w", wraplength=280, justify="left").pack(fill="x", pady=(6, 0))

        for widget in (kartu, isi, baris1, baris2):
            widget.bind("<Button-1>", lambda e, it=item: self.pilih_item(it))
        for child in isi.winfo_children():
            if isinstance(child, tk.Label):
                child.bind("<Button-1>", lambda e, it=item: self.pilih_item(it))

        self.kartu_widgets[item["id"]] = kartu
        self._bind_scroll_rekursif(kartu)

    def pilih_item(self, item):
        lama = self.item_terpilih
        self.item_terpilih = item
        if lama and lama["id"] in self.kartu_widgets:
            self.kartu_widgets[lama["id"]].config(highlightbackground=WARNA["border"], highlightthickness=1)
        if item["id"] in self.kartu_widgets:
            self.kartu_widgets[item["id"]].config(highlightbackground=WARNA["aksen"], highlightthickness=2)
        self.tampilkan_detail(item)

    def tampilkan_detail(self, item):
        self.item_terpilih = item
        if item is None:
            self.tag_kategori.set_style(self.warna_tag_bg, self.warna_tag_fg)
            self.lbl_nama.config(text="Pilih salah satu item di daftar")
            self.lbl_rating.config(text="")
            self.lbl_info.config(text="")
            self.badge_harga.text = "Rp 0"
            self.badge_harga._draw(self.warna_badge)
            self._set_text("")
            return

        self.lbl_nama.config(text=item["nama"])
        self.lbl_rating.config(text=f"\u2605 {item['rating']}  ({item['ulasan']} ulasan)")

        self.tag_kategori.text = item["kategori"].upper()
        self.tag_kategori.w = tkfont.Font(font=self.tag_kategori.font).measure(self.tag_kategori.text) + 24
        self.tag_kategori.config(width=self.tag_kategori.w)
        self.tag_kategori._draw(self.warna_tag_bg)

        self.badge_harga.text = f"{self.KOLOM_HARGA_LABEL}: {format_rupiah(item['harga'])}"
        self.badge_harga.w = tkfont.Font(font=self.badge_harga.font).measure(self.badge_harga.text) + 28
        self.badge_harga.config(width=self.badge_harga.w)
        self.badge_harga._draw(self.warna_badge)

        info = f"\U0001F4CD {item['lokasi']}    \U0001F551 {item['jam']}"
        extra = item.get("fasilitas")
        if extra:
            info += f"\n\U0001F3F7 Fasilitas: {extra}"
        self.lbl_info.config(text=info)
        self._set_text(item["deskripsi"])

    def _set_text(self, teks):
        self.txt_deskripsi.config(state="normal")
        self.txt_deskripsi.delete("1.0", tk.END)
        self.txt_deskripsi.insert(tk.END, teks)
        self.txt_deskripsi.config(state="disabled")

    def _klik_pesan(self):
        if not self.item_terpilih:
            messagebox.showwarning("Pesan", "Pilih kuliner yang ingin dipesan terlebih dahulu.")
            return
        if self.on_pesan:
            self.on_pesan(self.item_terpilih)

    # ---------------------------------------------- aksi khusus admin ----
    def tambah_item(self):
        def simpan(hasil):
            self.datastore.add_item(self.data, self.file_path, hasil)
            self.refresh_list()
        ItemFormDialog(self, "Tambah Item Baru", pakai_fasilitas=self.pakai_fasilitas, on_submit=simpan)

    def edit_item(self):
        if not self.item_terpilih:
            messagebox.showwarning("Edit", "Pilih item yang ingin diedit terlebih dahulu.")
            return
        item_id = self.item_terpilih["id"]

        def simpan(hasil):
            self.datastore.update_item(self.data, self.file_path, item_id, hasil)
            self.refresh_list()
        ItemFormDialog(self, "Edit Item", item=self.item_terpilih,
                        pakai_fasilitas=self.pakai_fasilitas, on_submit=simpan)

    def hapus_item(self):
        if not self.item_terpilih:
            messagebox.showwarning("Hapus", "Pilih item yang ingin dihapus terlebih dahulu.")
            return
        nama = self.item_terpilih["nama"]
        if messagebox.askyesno("Konfirmasi Hapus", f"Yakin ingin menghapus '{nama}'?"):
            self.datastore.delete_item(self.data, self.file_path, self.item_terpilih["id"])
            self.item_terpilih = None
            self.refresh_list()


# =========================================================================
# 4b. PEMESANAN KULINER (dialog jumlah + subtotal otomatis)
# =========================================================================

class OrderQuantityDialog(tk.Toplevel):
    """Dialog pilih jumlah pesanan, subtotal terhitung otomatis, meniru
    alur pesan.php pada versi web."""

    def __init__(self, parent, item, on_submit=None):
        super().__init__(parent)
        self.title("Pesan Kuliner")
        self.configure(bg=WARNA["kartu"])
        self.resizable(False, False)
        self.on_submit = on_submit
        self.item = item

        tk.Label(self, text="\U0001F6D2 Pesan Kuliner", font=(FONT_UTAMA, 13, "bold"),
                 fg=WARNA["primer"], bg=WARNA["kartu"]).grid(row=0, column=0, columnspan=2,
                                                              padx=20, pady=(20, 4), sticky="w")
        tk.Label(self, text=item["nama"], font=(FONT_UTAMA, 15, "bold"), fg=WARNA["teks"],
                 bg=WARNA["kartu"]).grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 2), sticky="w")
        tk.Label(self, text=f"Harga satuan: {format_rupiah(item['harga'])}", font=(FONT_UTAMA, 9),
                 fg=WARNA["teks_abu"], bg=WARNA["kartu"]).grid(row=2, column=0, columnspan=2,
                                                                padx=20, pady=(0, 16), sticky="w")

        tk.Label(self, text="Jumlah:", font=(FONT_UTAMA, 9, "bold"), fg=WARNA["teks"],
                 bg=WARNA["kartu"]).grid(row=3, column=0, padx=20, pady=6, sticky="w")
        self.var_jumlah = tk.IntVar(value=1)
        self.spin_jumlah = tk.Spinbox(self, from_=1, to=99, textvariable=self.var_jumlah, width=8,
                                       font=(FONT_UTAMA, 10), relief="flat", highlightthickness=1,
                                       highlightbackground=WARNA["border"], command=self._update_subtotal)
        self.spin_jumlah.grid(row=3, column=1, padx=20, pady=6, sticky="w", ipady=3)
        self.spin_jumlah.bind("<KeyRelease>", lambda e: self._update_subtotal())

        self.lbl_subtotal = tk.Label(self, text="", font=(FONT_UTAMA, 13, "bold"),
                                      fg=WARNA["primer"], bg=WARNA["hijau_muda"], padx=14, pady=10)
        self.lbl_subtotal.grid(row=4, column=0, columnspan=2, padx=20, pady=(14, 4), sticky="ew")
        self._update_subtotal()

        Pill(self, "Pesan Sekarang", bg=WARNA["hijau"], hover_bg=WARNA["primer_gelap"], fg="white",
             command=self._submit, font=(FONT_UTAMA, 10, "bold"), padx=0, pady=10,
             min_width=280).grid(row=5, column=0, columnspan=2, pady=18)

        self.grab_set()

    def _update_subtotal(self):
        try:
            jumlah = max(1, int(self.var_jumlah.get()))
        except (tk.TclError, ValueError):
            jumlah = 1
        subtotal = jumlah * self.item["harga"]
        self.lbl_subtotal.config(text=f"Subtotal: {format_rupiah(subtotal)}")

    def _submit(self):
        try:
            jumlah = max(1, int(self.var_jumlah.get()))
        except (tk.TclError, ValueError):
            messagebox.showerror("Input Salah", "Jumlah harus berupa angka!")
            return
        if self.on_submit:
            self.on_submit(self.item, jumlah)
        self.destroy()


class TransaksiPanel(tk.Frame):
    """Riwayat pesanan untuk pengunjung, dan kelola transaksi untuk admin.
    Meniru riwayat_pesanan.php (user) & admin/transaksi.php (admin)."""

    def __init__(self, parent, app):
        super().__init__(parent, bg=WARNA["latar"])
        self.app = app

        header = tk.Frame(self, bg=WARNA["latar"])
        header.pack(fill="x", padx=16, pady=(16, 8))
        self.lbl_judul = tk.Label(header, text="", font=(FONT_UTAMA, 13, "bold"),
                                   fg=WARNA["teks"], bg=WARNA["latar"])
        self.lbl_judul.pack(side="left")
        self.lbl_jumlah = tk.Label(header, text="", font=(FONT_UTAMA, 8, "italic"),
                                    fg=WARNA["teks_abu"], bg=WARNA["latar"])
        self.lbl_jumlah.pack(side="right")

        list_container = tk.Frame(self, bg=WARNA["latar"], highlightbackground=WARNA["border"],
                                   highlightthickness=1)
        list_container.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        self.canvas = tk.Canvas(list_container, bg=WARNA["latar"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = tk.Frame(self.canvas, bg=WARNA["latar"])
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self._win = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self._win, width=e.width))
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _bind_scroll_rekursif(self, widget):
        widget.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        widget.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-2, "units"))
        widget.bind("<Button-5>", lambda e: self.canvas.yview_scroll(2, "units"))
        for child in widget.winfo_children():
            self._bind_scroll_rekursif(child)

    def refresh_list(self):
        user = self.app.current_user
        is_admin = user and user["role"] == ROLE_ADMIN
        self.lbl_judul.config(text="Kelola Transaksi" if is_admin else "Riwayat Pesanan Saya")

        for w in self.scroll_frame.winfo_children():
            w.destroy()

        if is_admin:
            daftar = sorted(self.app.data.transaksi, key=lambda d: -d["id"])
        else:
            username = user["username"] if user else None
            daftar = sorted([d for d in self.app.data.transaksi if d["username"] == username],
                             key=lambda d: -d["id"])

        self.lbl_jumlah.config(text=f"{len(daftar)} transaksi")

        if not daftar:
            tk.Label(self.scroll_frame, text="Belum ada transaksi.", bg=WARNA["latar"],
                     fg=WARNA["teks_abu"], font=(FONT_UTAMA, 9, "italic")).pack(pady=20)

        for trx in daftar:
            self._buat_kartu_transaksi(trx, is_admin)

    def _buat_kartu_transaksi(self, trx, is_admin):
        kartu = tk.Frame(self.scroll_frame, bg=WARNA["kartu"], highlightbackground=WARNA["border"],
                          highlightthickness=1)
        kartu.pack(fill="x", pady=5, padx=6)
        isi = tk.Frame(kartu, bg=WARNA["kartu"], padx=16, pady=12)
        isi.pack(fill="both", expand=True)

        atas = tk.Frame(isi, bg=WARNA["kartu"])
        atas.pack(fill="x")
        tk.Label(atas, text=trx["item_nama"], font=(FONT_UTAMA, 12, "bold"), bg=WARNA["kartu"],
                 fg=WARNA["teks"]).pack(side="left")
        warna_status = WARNA_STATUS.get(trx["status"], WARNA["teks_abu"])
        Pill(atas, trx["status"], bg=warna_status, fg="white",
             font=(FONT_UTAMA, 8, "bold"), padx=10, pady=4).pack(side="right")

        info = (f"Jumlah: {trx['jumlah']} \u00d7 {format_rupiah(trx['harga_satuan'])}   "
                f"\u2022   Subtotal: {format_rupiah(trx['subtotal'])}")
        tk.Label(isi, text=info, font=(FONT_UTAMA, 9, "bold"), bg=WARNA["kartu"],
                 fg=WARNA["primer"], anchor="w").pack(fill="x", pady=(6, 0))

        bawah = tk.Frame(isi, bg=WARNA["kartu"])
        bawah.pack(fill="x", pady=(4, 0))
        keterangan = f"\U0001F551 {trx['tanggal']}"
        if is_admin:
            keterangan += f"   \u2022   \U0001F464 {trx['username']}"
        tk.Label(bawah, text=keterangan, font=(FONT_UTAMA, 8), bg=WARNA["kartu"],
                 fg=WARNA["teks_abu"]).pack(side="left")

        aksi = tk.Frame(isi, bg=WARNA["kartu"])
        aksi.pack(fill="x", pady=(10, 0))

        if is_admin:
            var_status = tk.StringVar(value=trx["status"])
            combo = ttk.Combobox(aksi, textvariable=var_status, values=DAFTAR_STATUS_TRANSAKSI,
                                  state="readonly", width=14, font=(FONT_UTAMA, 8))
            combo.pack(side="left", padx=(0, 8))
            combo.bind("<<ComboboxSelected>>",
                       lambda e, tid=trx["id"], v=var_status: self._ubah_status(tid, v.get()))
            Pill(aksi, "Hapus", bg=WARNA["merah"], hover_bg=WARNA["merah_gelap"], fg="white",
                 command=lambda tid=trx["id"]: self._hapus(tid),
                 font=(FONT_UTAMA, 8, "bold"), padx=12, pady=6).pack(side="left")
        elif trx["status"] == STATUS_DIPROSES:
            Pill(aksi, "Batalkan Pesanan", bg=WARNA["merah"], hover_bg=WARNA["merah_gelap"], fg="white",
                 command=lambda tid=trx["id"]: self._batalkan(tid),
                 font=(FONT_UTAMA, 8, "bold"), padx=12, pady=6).pack(side="left")

        self._bind_scroll_rekursif(kartu)

    def _ubah_status(self, trx_id, status):
        self.app.data.ubah_status_transaksi(trx_id, status)
        self.refresh_list()

    def _hapus(self, trx_id):
        if messagebox.askyesno("Konfirmasi", "Hapus transaksi ini?"):
            self.app.data.hapus_transaksi(trx_id)
            self.refresh_list()

    def _batalkan(self, trx_id):
        if messagebox.askyesno("Konfirmasi", "Batalkan pesanan ini?"):
            self.app.data.ubah_status_transaksi(trx_id, STATUS_DIBATALKAN)
            self.refresh_list()


# =========================================================================
# 4c. BUKU TAMU DIGITAL
# =========================================================================

class GuestbookPanel(tk.Frame):
    """Buku tamu digital: pengunjung/admin bisa menulis pesan, semua
    entri tampil di daftar publik. Admin bisa menghapus entri.
    Meniru buku_tamu.php & admin/buku_tamu.php."""

    def __init__(self, parent, app):
        super().__init__(parent, bg=WARNA["latar"])
        self.app = app

        main = tk.Frame(self, bg=WARNA["latar"])
        main.pack(fill="both", expand=True, padx=16, pady=16)

        # ---------------- form isi buku tamu ----------------
        form_box = tk.Frame(main, bg=WARNA["kartu"], highlightbackground=WARNA["border"],
                             highlightthickness=1, padx=18, pady=16)
        form_box.pack(fill="x", pady=(0, 14))

        tk.Label(form_box, text="\U0001F4D6 Tulis Pesan di Buku Tamu", font=(FONT_UTAMA, 12, "bold"),
                 fg=WARNA["primer"], bg=WARNA["kartu"]).pack(anchor="w")

        self.lbl_nama_pengirim = tk.Label(form_box, text="", font=(FONT_UTAMA, 9),
                                           fg=WARNA["teks_abu"], bg=WARNA["kartu"])
        self.lbl_nama_pengirim.pack(anchor="w", pady=(2, 10))

        self.txt_pesan = tk.Text(form_box, height=3, font=(FONT_UTAMA, 10), relief="flat",
                                  bg=WARNA["hijau_muda"], fg=WARNA["teks"], wrap="word",
                                  highlightthickness=1, highlightbackground=WARNA["border"],
                                  highlightcolor=WARNA["primer"], padx=10, pady=8)
        self.txt_pesan.pack(fill="x")

        Pill(form_box, "Kirim Pesan", bg=WARNA["hijau"], hover_bg=WARNA["primer_gelap"], fg="white",
             command=self._kirim_pesan, font=(FONT_UTAMA, 9, "bold"), padx=16,
             pady=8).pack(anchor="e", pady=(10, 0))

        # ---------------- daftar entri ----------------
        self.lbl_jumlah = tk.Label(main, text="", font=(FONT_UTAMA, 8, "italic"),
                                    fg=WARNA["teks_abu"], bg=WARNA["latar"])
        self.lbl_jumlah.pack(anchor="w", pady=(0, 4))

        list_container = tk.Frame(main, bg=WARNA["latar"], highlightbackground=WARNA["border"],
                                   highlightthickness=1)
        list_container.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(list_container, bg=WARNA["latar"], highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview)
        self.scroll_frame = tk.Frame(self.canvas, bg=WARNA["latar"])
        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self._win = self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfig(self._win, width=e.width))
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _bind_scroll_rekursif(self, widget):
        widget.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))
        widget.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-2, "units"))
        widget.bind("<Button-5>", lambda e: self.canvas.yview_scroll(2, "units"))
        for child in widget.winfo_children():
            self._bind_scroll_rekursif(child)

    def on_show(self):
        user = self.app.current_user
        nama = user["nama"] if user else "Tamu"
        self.lbl_nama_pengirim.config(text=f"Menulis sebagai: {nama}")
        self.refresh_list()

    def _kirim_pesan(self):
        pesan = self.txt_pesan.get("1.0", tk.END).strip()
        if not pesan:
            messagebox.showwarning("Buku Tamu", "Pesan tidak boleh kosong.")
            return
        user = self.app.current_user
        nama = user["nama"] if user else "Tamu"
        self.app.data.tambah_buku_tamu(nama, pesan)
        self.txt_pesan.delete("1.0", tk.END)
        messagebox.showinfo("Buku Tamu", "Terima kasih! Pesan Anda sudah tercatat.")
        self.refresh_list()

    def refresh_list(self):
        for w in self.scroll_frame.winfo_children():
            w.destroy()

        daftar = sorted(self.app.data.buku_tamu, key=lambda d: -d["id"])
        self.lbl_jumlah.config(text=f"{len(daftar)} pesan dari pengunjung")

        if not daftar:
            tk.Label(self.scroll_frame, text="Belum ada pesan. Jadilah yang pertama menulis!",
                     bg=WARNA["latar"], fg=WARNA["teks_abu"], font=(FONT_UTAMA, 9, "italic")).pack(pady=20)

        is_admin = self.app.current_user and self.app.current_user["role"] == ROLE_ADMIN
        for entri in daftar:
            self._buat_kartu_entri(entri, is_admin)

    def _buat_kartu_entri(self, entri, is_admin):
        kartu = tk.Frame(self.scroll_frame, bg=WARNA["kartu"], highlightbackground=WARNA["border"],
                          highlightthickness=1)
        kartu.pack(fill="x", pady=5, padx=6)
        isi = tk.Frame(kartu, bg=WARNA["kartu"], padx=16, pady=10)
        isi.pack(fill="both", expand=True)

        atas = tk.Frame(isi, bg=WARNA["kartu"])
        atas.pack(fill="x")
        tk.Label(atas, text=entri["nama"], font=(FONT_UTAMA, 10, "bold"), bg=WARNA["kartu"],
                 fg=WARNA["primer"]).pack(side="left")
        tk.Label(atas, text=entri["tanggal"], font=(FONT_UTAMA, 8), bg=WARNA["kartu"],
                 fg=WARNA["teks_abu"]).pack(side="right")

        tk.Label(isi, text=entri["pesan"], font=(FONT_UTAMA, 9), bg=WARNA["kartu"], fg=WARNA["teks"],
                 anchor="w", justify="left", wraplength=760).pack(fill="x", pady=(6, 0))

        if is_admin:
            Pill(isi, "Hapus", bg=WARNA["merah"], hover_bg=WARNA["merah_gelap"], fg="white",
                 command=lambda eid=entri["id"]: self._hapus_entri(eid),
                 font=(FONT_UTAMA, 8, "bold"), padx=10, pady=5).pack(anchor="e", pady=(8, 0))

        self._bind_scroll_rekursif(kartu)

    def _hapus_entri(self, entri_id):
        if messagebox.askyesno("Konfirmasi", "Hapus pesan ini dari buku tamu?"):
            self.app.data.hapus_buku_tamu(entri_id)
            self.refresh_list()


class MainPage(BasePage):
    """Halaman utama setelah login: header ala navbar + dua tab
    (Kuliner & Destinasi) yang tampilannya menyesuaikan role user."""

    def __init__(self, parent, app):
        super().__init__(parent, app)

        header = tk.Frame(self, bg=WARNA["primer"], height=84)
        header.pack(fill="x")
        header.pack_propagate(False)
        isi_header = tk.Frame(header, bg=WARNA["primer"])
        isi_header.pack(fill="both", expand=True, padx=24)

        kiri = tk.Frame(isi_header, bg=WARNA["primer"])
        kiri.pack(side="left", fill="y")
        brand = tk.Frame(kiri, bg=WARNA["primer"])
        brand.pack(anchor="w", expand=True, pady=(0, 0))
        Logo(brand, size=42).pack(side="left", padx=(0, 10))
        teks_brand = tk.Frame(brand, bg=WARNA["primer"])
        teks_brand.pack(side="left")
        self.lbl_judul = tk.Label(teks_brand, text="Wisata Kuliner Wonogiri", fg="white",
                                   bg=WARNA["primer"], font=(FONT_UTAMA, 15, "bold"), anchor="w")
        self.lbl_judul.pack(anchor="w")
        self.lbl_welcome = tk.Label(teks_brand, text="", fg=WARNA["hijau_muda"],
                                     bg=WARNA["primer"], font=(FONT_UTAMA, 9), anchor="w")
        self.lbl_welcome.pack(anchor="w")

        kanan = tk.Frame(isi_header, bg=WARNA["primer"])
        kanan.pack(side="right", pady=20)
        Pill(kanan, "Logout", bg=WARNA["primer_gelap"], hover_bg=WARNA["merah"], fg="white",
             command=lambda: self.app.logout(), font=(FONT_UTAMA, 9, "bold"), padx=16, pady=8).pack()

        # ---- styling ttk Notebook agar senada dengan warna hijau ----
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("Wonogiri.TNotebook", background=WARNA["latar"], borderwidth=0)
        style.configure("Wonogiri.TNotebook.Tab", background=WARNA["kartu"], foreground=WARNA["teks"],
                         padding=(18, 10), font=(FONT_UTAMA, 10, "bold"), borderwidth=0)
        style.map("Wonogiri.TNotebook.Tab",
                  background=[("selected", WARNA["primer"])],
                  foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(self, style="Wonogiri.TNotebook")
        self.notebook.pack(expand=True, fill="both", padx=14, pady=14)
        self.panel_kuliner = None
        self.panel_destinasi = None
        self.panel_transaksi = None
        self.panel_buku_tamu = None

    def _bangun_ulang_panel(self):
        for tab in self.notebook.tabs():
            self.notebook.forget(tab)

        is_admin = self.app.current_user and self.app.current_user["role"] == ROLE_ADMIN

        self.panel_kuliner = ItemListPanel(
            self.notebook, self.app.data, self.app.data.kuliner, KULINER_FILE,
            is_admin=is_admin, jenis="kuliner", on_pesan=self.app.buat_pesanan)
        self.panel_kuliner.KOLOM_HARGA_LABEL = "Harga"

        self.panel_destinasi = ItemListPanel(
            self.notebook, self.app.data, self.app.data.destinasi, DESTINASI_FILE,
            is_admin=is_admin, jenis="destinasi")
        self.panel_destinasi.KOLOM_HARGA_LABEL = "Tiket Masuk"

        self.panel_transaksi = TransaksiPanel(self.notebook, self.app)
        self.panel_buku_tamu = GuestbookPanel(self.notebook, self.app)

        self.notebook.add(self.panel_kuliner, text="  \U0001F372  Kuliner Khas  ")
        self.notebook.add(self.panel_destinasi, text="  \U0001F3D4  Destinasi Wisata  ")
        judul_transaksi = "  \U0001F4CB  Kelola Transaksi  " if is_admin else "  \U0001F4CB  Pesanan Saya  "
        self.notebook.add(self.panel_transaksi, text=judul_transaksi)
        self.notebook.add(self.panel_buku_tamu, text="  \U0001F4D6  Buku Tamu  ")

    def on_show(self):
        user = self.app.current_user
        nama = user["nama"] if user else "Tamu"
        is_admin = user and user["role"] == ROLE_ADMIN
        peran = "Admin" if is_admin else "Pengunjung"
        judul = "Panel Admin \u2013 Wisata Kuliner Wonogiri" if is_admin else "Wisata Kuliner Wonogiri"

        self.lbl_judul.config(text=judul)
        self.lbl_welcome.config(text=f"Login sebagai {nama}  \u2022  {peran}")

        self._bangun_ulang_panel()
        self.panel_kuliner.refresh_list()
        self.panel_destinasi.refresh_list()
        self.panel_transaksi.refresh_list()
        self.panel_buku_tamu.on_show()

    def refresh_transaksi(self):
        if self.panel_transaksi:
            self.panel_transaksi.refresh_list()


# =========================================================================
# 5. APPLICATION CONTROLLER (Composition)
# =========================================================================

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistem Informasi Kuliner Lokal & Destinasi Wisata Wonogiri")
        self.geometry("1040x660")
        self.minsize(900, 560)
        self.configure(bg=WARNA["latar"])

        self.data = DataStore()
        self._seed_admin_default()
        self.current_user = None

        container = tk.Frame(self, bg=WARNA["latar"])
        container.pack(fill="both", expand=True)

        self.pages = {}
        for PageClass in (LoginPage, RegisterPage, MainPage):
            page = PageClass(container, self)
            self.pages[PageClass.__name__] = page
            page.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.config(menu=tk.Menu(self))
        self.show_page("LoginPage")

    def _seed_admin_default(self):
        if "admin" not in self.data.users:
            self.data.register("Administrator", "admin", "admin123", ROLE_ADMIN)

    def show_page(self, name):
        page = self.pages[name]
        page.tkraise()
        page.on_show()

    def build_menu(self):
        menubar = tk.Menu(self)
        menu_akun = tk.Menu(menubar, tearoff=0)
        menu_akun.add_command(label="Logout", command=self.logout)
        menu_akun.add_separator()
        menu_akun.add_command(label="Keluar Aplikasi", command=self.quit)
        menubar.add_cascade(label="Akun", menu=menu_akun)

        menu_bantuan = tk.Menu(menubar, tearoff=0)
        menu_bantuan.add_command(label="Tentang Aplikasi", command=self.tentang)
        menubar.add_cascade(label="Bantuan", menu=menu_bantuan)

        self.config(menu=menubar)

    def buat_pesanan(self, item):
        """Dipanggil dari tombol 'Pesan Sekarang' pada tab Kuliner Khas.
        Membuka dialog jumlah, lalu menyimpan transaksi baru."""
        def simpan(item_terpilih, jumlah):
            self.data.buat_transaksi(
                self.current_user["username"], item_terpilih["nama"],
                jumlah, item_terpilih["harga"])
            messagebox.showinfo(
                "Pesanan Berhasil",
                f"Pesanan {jumlah}x {item_terpilih['nama']} berhasil dibuat!\n"
                f"Cek tab 'Pesanan Saya' untuk melihat status."
            )
            self.pages["MainPage"].refresh_transaksi()
        OrderQuantityDialog(self, item, on_submit=simpan)

    def logout(self):
        self.current_user = None
        self.config(menu=tk.Menu(self))
        self.show_page("LoginPage")

    def tentang(self):
        messagebox.showinfo(
            "Tentang Aplikasi",
            "Sistem Informasi Kuliner Lokal & Destinasi Wisata Wonogiri\n"
            "Versi Desktop (Tkinter - OOP, 2 Role)\n\n"
            "Role Admin: kelola (tambah/edit/hapus) data Kuliner & Destinasi,\n"
            "kelola status transaksi, dan moderasi buku tamu.\n"
            "Role Pengunjung: lihat daftar & detail, pesan kuliner,\n"
            "lihat riwayat pesanan, dan isi buku tamu."
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()