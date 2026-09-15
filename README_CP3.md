# Checkpoint 3

# Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
## Jawab
Django AuthenticationForm adalah form Object bawaan Django agar kita sebagai developer bisa membuat flow login autentikasi hanya dengan library. Dengan ini, data user login bisa digunakan yaitu username dan password.

Kelebihannya: siap pakai sehingga tidak perlu membuat form login dari nol, otomatis menangani validasi dan proses autentikasi user, serta sudah terintegrasi dengan sistem autentikasi dan model User milik Django sehingga aman dan menghemat waktu pengembangan.

Kekurangannya: field yang disediakan default terbatas (hanya username dan password), sehingga kurang fleksibel apabila kita ingin melakukan kustomisasi seperti login menggunakan email, menambah field lain, atau styling khusus. Untuk kebutuhan seperti itu kita perlu meng-override atau membuat form sendiri.


# Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
## Jawab
Autentikasi adalah proses memverifikasi identitas user ("siapa kamu?"), misalnya dengan mengecek username dan password saat login. Sedangkan otorisasi adalah proses menentukan hak akses user ("kamu boleh mengakses atau melakukan apa?"), misalnya membatasi halaman tertentu hanya untuk user yang berhak.

Django mengimplementasikan autentikasi menggunakan fungsi seperti `authenticate()`, `login()`, `logout()`, dan `AuthenticationForm`. Sedangkan otorisasi diimplementasikan menggunakan sistem permissions (`@permission_required`, `user.has_perm()`, groups) serta decorator `@login_required` yang membatasi suatu halaman agar hanya bisa diakses oleh user yang sudah login.

# Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
## Jawab
Session memiliki kelebihan dimana web app cukup men-track session id-nya saja di sisi client, sementara data aslinya disimpan di server sehingga lebih aman. Akan tetapi, kekurangannya adalah session membebani penyimpanan di server (server harus menyimpan data setiap session), sehingga lebih boros resource dan butuh penanganan khusus ketika aplikasi di-scale.

Kelebihan dari cookies adalah data disimpan di sisi client sehingga tidak membebani server dan bisa persist (diberi masa berlaku tertentu). Akan tetapi, kekurangannya adalah kapasitas data yang bisa ditampung sangat kecil (sekitar 4KB) dan kurang aman karena data di sisi client bisa dibaca atau dimanipulasi oleh user maupun penyerang.

# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
## Jawab
Penggunaan cookies TIDAK sepenuhnya aman secara default dalam pengembangan web. Ada beberapa risiko potensial yang harus diwaspadai, seperti pencurian cookie (session hijacking), cookie dibaca oleh script berbahaya lewat serangan XSS, data cookie dimanipulasi, atau cookie bocor apabila dikirim lewat koneksi HTTP (bukan HTTPS).

Django menangani risiko-risiko tersebut dengan beberapa mekanisme, antara lain: signed cookies (cookie ditandatangani secara kriptografis agar tidak bisa dipalsukan atau dimanipulasi), flag `SESSION_COOKIE_HTTPONLY` (agar cookie tidak bisa dibaca oleh JavaScript sehingga mencegah XSS), flag `SESSION_COOKIE_SECURE` (agar cookie hanya dikirim lewat HTTPS), flag `SESSION_COOKIE_SAMESITE` (untuk mencegah serangan CSRF), serta penggunaan CSRF token pada form.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Jawab
1. Pertama-tama, saya membuat kedua function `register` dan juga `login_user` di `views.py` menggunakan library bawaan Django, seperti UserCreationForm dan AuthenticationForm. UserCreationForm ini berguna untuk membuat form yang menjadi user dengan username dan password, sedangkan AuthenticationForm berguna untuk form yang meng-autentikasikan user yang ingin login.
2. Kemudian, saya membuat routing pathnya di `main/urls.py` dan juga templatenya dengan form pada `register.html`.
3. Setelah itu, saya menambahkan fuction `logout` agar user bisa logout dan juga membuat routing pathnya di `main/urls.py`.
4. Selanjutnya, saya menambahkan decorator pada beberapa function di `views.py` agar hanya user yang sudah login dapat mengakses halaman tersebut, yaitu function `show_main` dan `create_product` yang artinya user yang belum login tidak bisa mengakses halaman utama dan juga tidak bisa membuat product.
5. Kemudian, saya menghubungkan model `Product` dengan `User` dengan menambahkan field `ForeignKey` ke `User` pada `models.py`, lalu menjalankan `makemigrations` dan `migrate`. Pada function `create_product`, saya menggunakan `form.save(commit=False)` lalu mengisi `product_entry.user = request.user` sebelum menyimpan, agar setiap product terhubung dengan user yang membuatnya. Saya juga menambahkan filter pada `show_main` agar user bisa melihat semua product atau hanya product miliknya sendiri.
6. Terakhir, saya menerapkan cookies dengan menyimpan `last_login` menggunakan `response.set_cookie("last_login", ...)` saat user berhasil login, menampilkannya di halaman utama melalui `request.COOKIES.get("last_login")` pada `context`, dan menghapusnya dengan `response.delete_cookie("last_login")` saat user logout. Saya juga membuat dua akun pengguna dengan masing-masing tiga dummy data product di lokal.