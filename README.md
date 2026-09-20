Nama: Muhammad Hafidz Muazzam

NPM: 2506621812

Kelas: PBP C

Semangat!

Pertanyaan Reflektif:
### Tugas 1
1. iya, saya menggunakan elemen semantik HTML5 seperti <header>, <nav>, <main>, <section>, <article>, dan <footer>. elemen tersebut membantu saya untuk membuat struktur informasi yang jelas dan rapi. hal tersebut juga memudahkan dalam pembacaan kode. penggunaan <article> pada bagian education dan projects juga sangat pas karena sangat sesuai untuk digunakan pada konten yang sifatnya mandiri.

2. tantangan utamanya terletak pada menjaga tata letak agar tetap rapi dan tidak berantakan di layar mobile. evaluasi yang saya lakukan adalah mengubah elemen yang berjejer horizontal di desktop contohnya seperti grid pada hero, education, dan projects menjadi berjejer vertikal di mobile, selain itu saya juga menyesuaikan ukuran font dan paddingnya agar tetap nyaman untuk dibaca.

3. batasannya adalah kontennya atau informasinya bersifat statis dan tidak bisa menyimpan atau memproses data secara langsung (dinamis). untuk iterasi selanjutnya, fungsi dinamis yang terbayang oleh saya adalah menambah fitur pengganti tampilan untuk diubah ke tampilan dark mode agar pengguna bisa mengubah tampilan website menjadi mode gelap atau terang sesuai keinginan.

dalam pengerjaan tugas ini, saya memanfaatkan bantuan dari AI untuk mengetahui fitur atau fungsi krusial apa saja yang harus diperhatikan saat merancang website agar terlihat proper secara visual, seperti header yang dijadikan sticky agar tetap berada di atas pada saat halamannya discroll.

### Tugas 2
1. pengguna mengakses URL di browser. permintaan ini diterima oleh urls.py utama proyek untuk diteruskan ke urls.py milik aplikasi main. kemudian urls.py aplikasi akan mengarah ke fungsi view yang sesuai, yaitu show_project. di dalam view, aplikasi meminta data dari model project yang bertugas untuk mengambilnya dari database. setelah data diterima, view memasukkan data tersebut ke dalam context dan merendernya ke template projects.html. sehingga menghasilkan tampilan HTML yang kemudian dikirimkan kembali untuk ditampilkan di browser pengguna.

2. agar pengelolaan data dan tampilan HTML terpisah dengan jelas. hal ini membuat pemeliharaan aplikasi ke depannya jadi lebih praktis karena penambahan, perubahan, atau penghapusan data bisa dilakukan langsung dari database tanpa mengotak-atik berkas HTML. selain itu tampilan web juga menjadi lebih dinamis dan fleksibel saat menyajikan data.

3. perbedaan utamanya ada pada alur eksekusi: makemigrations bertugas mendeteksi perubahan di models.py dan membuat berkas rancangan migrasi, sedangkan migrate bertugas mengaplikasikan rancangan tersebut ke database.

contohnya saat membuat model Project baru atau menambah field baru. kita wajib menjalankan makemigrations untuk mencatat perubahannya, lalu migrate untuk memperbarui tabel database.

dalam pengerjaan tugas ini, saya memanfaatkan AI untuk membantu menganalisis dan menjelaskan penyebab kesalahan atau error pada kode program yang saya buat  sehingga keseluruhan fiturnya dapat berjalan dengan baik. selain itu, saya juga meminta saran dan panduan dalam menyamakan elemen desain antar halaman agar tampilannya terlihat konsisten dengan halaman yang lain.

### Tugas 3
1. pemanfaatan ModelForm yaitu karena bisa mengotomatisasi pembuatan form HTML berdasarkan kelas model yang sudah ada. Hal ini jadi sangat efektif untuk mempersingkat waktu penulisan kode berulang sekaligus memastikan validasi data langsung sinkron dengan skema basis data.

pemanfaatan {%% csrf_token %%} adalah sebagai pengaman dari server untuk memastikan bahwa data yang dikirim melalui formulir benar-benar berasal dari halaman web kita.

2. JSON dipilih karena memiliki bentuk yang jauh lebih ringkas, tidak membutuhkan banyak tanda baca atau tag yang panjang, dan lebih cepat dan ringan saat diproses.

3. Saat URL diakses, sistem mengambil data dari basis data, mengubahnya ke format standar, lalu mengirimkannya sebagai respons ke pengguna.

Proses serialization diperlukan untuk mengubah data internal Django agar dapat dibaca dan dikirim dengan mudah melalui jaringan web.

dalam pengerjaan tugas ini, saya memanfaatkan AI sebagai teman diskusi untuk membantu dalam memahami konsep ModelForm dan JSON serta membantu dalam mendebug error pada program di tengah pengerjaan disertai dengan penjelasan agar saya dapat memahami error yang terjadi.