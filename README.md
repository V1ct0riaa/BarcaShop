# Checkpoint 1
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
# Jawab
1. Proyek Django baru dibuat dengan menginisiasi melakukan pembuatan virtual environment, menambahkan requirements,
dan kemudian pada direktori utama membuat django project dengan perintah `django-admin startproject <nama app>`
2. Routing dilakukan dengan menambahkan path pada urls.py milik project dan juga pada app main.
3. Model dibuat dengan nama Product dengan atribut `name`, `price`, `description`, `thumbnail`. `category`, `is_featured`, dll
pada models.py di app main.
4. Fungsi pada views dibuat untuk menampilkan data yang dipass ke urls agar bisa ditampilkan di template html.
5. Routing pada urls.py pada aplikasi main agar routing dari urls.py project bisa masuk ke app main.
6. Deployment TBA.

## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
# 