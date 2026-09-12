# Checkpoint 2

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
## Jawab
Data delivery dibutuhkan untuk pertukaran data di dalam platform, dari satu stack ke stack lainnya. Hal ini penting karena aplikasi modern komponennya terpisah (misalnya frontend, backend, aplikasi mobile, hingga layanan pihak ketiga), sehingga masing-masing membutuhkan cara yang terstandar untuk saling bertukar data. Dengan adanya data delivery, satu backend juga bisa melayani banyak client sekaligus. Data yang dikirim ada beberapa jenis formatnya seperti XML dan JSON.

# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
## Jawab
Menurut saya keduanya baik, akan tetapi dari sudut pandang saya, JSON lebih mudah dimengerti karena terlihat dengan jelas strukturnya, mungkin karena dia berbentuk pasangan key-value (notasi objek JavaScript) yang gampang dipetakan ke struktur data. Selain itu, JSON lebih populer karena lebih ringkas dibandingkan XML (tidak perlu closing tag di setiap elemen), sehingga ukuran datanya lebih kecil, dan JSON juga native untuk JavaScript sehingga sangat mudah diproses di aplikasi web. Karena alasan-alasan itulah JSON lebih banyak digunakan di dunia teknologi.

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
## Jawab
Is_valid() digunakan untuk melakukan pengecekan apabila form yang diisi terdapat suatu error. Fungsi ini dibutuhkan pada Django untuk memastikan form yang diisi valid dan datanya bisa diterima oleh platform.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
## Jawab
Csrf_Token pada form Django adalah token yang digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery) dan digenerate langsung oleh Django. Token ini memastikan bahwa request yang masuk benar-benar berasal dari situs kita sendiri, bukan request palsu dari situs lain. Apabila tidak digunakan, penyerang dapat menjebak user yang sedang login (misalnya lewat link atau form jahat di situs lain) agar tanpa sadar mengirim request ke platform kita, sehingga aksi yang mengubah data (seperti membuat, mengubah, atau menghapus data) berjalan atas nama user tersebut tanpa izinnya. Tanpa csrf_token, Django tidak bisa membedakan mana request asli dan mana request palsu.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Jawab
1. Pertama, saya menambahkan 6 function yang dibutuhkan, yaitu create_product(), show_product(), show_xml(), show_json(), show_xml_by_id, dan show_json_by_id.
2. Setiap function tersebut speaks for itself dan kemudian saya menambahkan routing pathnya pada `urls.py` di `app.main` yang nantinya akan pass function-function tersebut.
3. Apabila user mengirimkan request ke `/create_product/` maka function create_product akan dipass. Apabila form terisi dengan baik dan sifatnya POST, maka akan redirect karena artinya form sudah berhasil terisi. Apabila belum, akan diarahkan ke form create product.
4. Apabila user mengirimkan request ke `/product/str:id/`, maka user akan diarahkan ke halaman melihat detail product sesuai dengan `id` product yang ke-pass.
5. Apabila user mengirimkan request ke `/json/`, maka akan menampilkan semua product dalam format json.
6. Apabila user mengirimkan request ke `/json/str:id/`, maka akan menampilkan specific product dengan `id` tersebut dalam format json.
7. Apabila user mengirimkan request ke `/xml/`, maka akan menampilkan semua product dalam format xml.
8. Apabila user mengirimkan request ke `/xml/str:id/`, maka akan menampilkan specific product dengan `id` tersebut dalam format xml.