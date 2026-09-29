import os
import json
import re
import shutil

raw_text = """
1. Reminders of Him by Colleen Hoover
Saking populernya, saat ini terdapat 94% pengguna Google yang menyukai novel romantis dengan judul Reminders of Him (2022) karya Colleen Hoover. Keren ya? Nah, masih di tahun yang sama, novel ini sempat masuk jadi nominasi buku paling romantis, loh.
Melalui novel ini, Colleen Cover mengisahkan Kenna Rowan, seorang ibu muda yang menjalani lima tahun penjara karena kesalahan tragis. Kemudian, Kenna kembali ke kota tempat ia mengacaukan semuanya, dengan harapan bersatu lagi bersama putrinya yang berusia empat tahun.
Sayangnya, untuk memperbaiki hubungan dengan orang-orang di sekitarnya terhalang oleh masa lalu yang kelam. Sampai akhirnya Kenna bertemu Ledger yang perlahan-lahan menjadi bagian penting dalam kehidupan Kenna.

2. Remarkably Bright Creatures by Shelby Van Pelt
Rekomendasi novel bahasa Inggris populer yang ditulis oleh Shelby Van Pelt dan terbit pada tahun 2022 ini pernah menjadi nominasi buku fiksi terbaik, plus nominasi untuk novel debut terbaik.
Novel ini bercerita mengenai kehidupan Tova Sullivan. Setelah suaminya meninggal, Tova memulai rutinitas baru dengan bekerja shift malam di Sowell Bay Aquarium.
Menyibukkan diri bisa membantunya untuk berpaling dari ingatan mengenai Erik, yakni putranya yang berusia delapan belas tahun yang menghilang secara misterius di atas kapal di Puget Sound lebih dari tiga puluh tahun yang lalu.
Di tempatnya bekerja, Tova berkenalan dan akhirnya bersahabat dengan Marcellus, yaitu seekor gurita Pasifik raksasa yang tinggal di akuarium. Karena pernah jadi detektif, akhirnya Marcellus membantu Tova untuk mengungkap fakta mengenai kematian putranya.

3. Every Summer After by Carley Fortune
Lagi-lagi, rekomendasi novel bahasa Inggris terpopuler selanjutnya terpilih juga sebagai nominasi buku fiksi dan buku debut terbaik pada tahun 2022. Nah, novelnya berjudul Every Summer After yang ditulis oleh Carley Fortune.
Pernahkah kamu merasa bahwa kesalahan yang pernah dilakukan bisa membatasi masa depanmu? Kalau pernah, mungkin sinopsis dari novel ini cukup relate untukmu.
Novel Every Summer After menceritakan tokoh bernama Persephone Fraser yang selalu dihantui rasa khawatir akan masa depan sejak ia melakukan kesalahan besar pada 10 tahun lalu.
Saat musim panas, ia menjalani hari-hari di sebuah apartemen modern tengah kota dan kerap menghabiskan waktu bersama teman-temannya.
Sampai akhirnya, hidup Persephone berubah ketika ia menerima telepon yang mengirimnya kembali ke Barry’s Bay, dan juga kembali ke kehidupan Sam Florek.

4. Charlotte’s Web by E.B. White
E.B White menuliskan novel Charlotte’s Web dengan total 184 halaman, dan terbit pertama kali pada tahun 1952. Sampai saat ini, novel tersebut sudah mengalami 5 kali penerbitan (yang terakhir pada tahun 2015).
Kalau kamu termasuk orang yang menyukai buku dari visual, coba deh baca buku ini. Sebab, di di dalamnya terdapat banyak ilustrasi berkualitas tinggi yang diwarnai oleh Rosemary Wells dan Garth Williams.
Selain itu, novel ini cocok juga untuk jadi bacaan usia kanak-kanak, loh. Pasalnya, ini mengisahkan Charlotte, yakni seekor laba-laba yang mengungkapkan perasaannya terhadap seekor babi kecil bernama Wilbur. Kisah tokoh dalam novel tersebut memberi banyak kesan baik soal cinta, kehidupan, dan persahabatan.

5. The Sense of an Ending by Julian Barnes
Siapa, sih, yang nggak tau Julian Barnes? Itu lho, penulis kontemporer bahasa Inggris yang sudah menerbitkan hampir 150 buku, salah satunya The Sense of an Ending yang masuk sebagai nominasi buku fiksi terbaik (2011).
The Sense of an Ending menceritakan tentang seorang pria bernama Tony Webster yang mencoba memahami kembali masa lalunya setelah menerima warisan tak terduga pada masa remaja.
Ketika dia menyelidiki kembali hubungan dengan teman sekolahnya yang misterius, Adrian Finn, Tony menyadari bahwa kenangan masa lalunya mungkin tidak sejelas yang dia ingat.

6. Our Souls at Night by Kent Haruf
Terakhir, English Academy memilih novel berjudul Our Souls at Night by Kent Haruf (2015) sebagai salah satu rekomendasi novel singkat bahasa Inggris. Tenang, buku ini hanya ditulis dalam 179 halaman.
Our Souls at Night bercerita tentang dua orang tetangga tua, Addie Moore dan Louis Waters, yang memutuskan untuk menjalin hubungan platonic pada malam hari untuk mengatasi kesepian mereka.
Platonik itu apa, sih? Platonik adalah istilah yang mengacu pada hubungan atau cinta yang bersifat tidak romantis atau tidak seksual, yha, misal hanya saling mengobrol satu sama lain.

7. Happy Place by Emily Henry
Kalau punya hobi membaca, buku Happy Place harusnya sudah kamu tamatkan sejak 2023 lalu. Sebab, buku ini cukup populer untuk kategori novel romantis. Tak heran kalau Emily Henry berhasil menjadikannya sebagai Winner for Best Romance (2023).
Happy Place memuat cerita romantis dari pasangan Harriet dan Wyn. yang telah menjalin hubungan sejak masa perguruan tinggi. Sayangnya, hubungan mereka kandas di tengah perjalanan tanpa alasan yang jelas.
Setelah berpisah, Harriet dan Wyn membuat perjanjian untuk tetap terlihat masih bersama, supaya acara berlibur bersama para sahabatnya tetap berjalan lancar. But, ternyata rencana keduanya tidak berjalan dengan mulus, guys.

8. Love on the Brain by Ali Hazelwood
Kali ini, salah satu rekomendasi novel romantis bahasa Inggris yang bisa kamu baca adalah Love on the Brain (2022). Melalui buku ini, sang penulis menceritakan Bee Königswasser yang tertarik dengan pemuda bernama Levi.
Tapi sayang, Levi dengan jelas menunjukkan ketidaksukaannya terhadap Bee, padahal keduanya harus terlibat dalam proyek yang sama.
Eits, ternyata kisah mereka baru dimulai ketika banyak staf lain yang mengabaikan Bee, sehingga ia mulai melihat Levi sebagai sosok yang bisa diandalkan untuk mendukung ide-idenya. 

9. Things We Never Got Over by Lucy Score
Guys, novel Things We Never Got Over karya Lucy Score (2022) ini nggak boleh dilewatkan, terutama bagi kamu yang menggemari bacaan bertema romantis.
Soalnya, perlu kamu tau kalau genre romantis pun tak luput dari konflik. Selain itu, romantis tak melulu berbicara soal hubungan antar pasangan, tapi bisa juga antar saudara.
Ringkasnya, novel ini mengisahkan tentang Naomi yang berusaha untuk hidup dengan keponakannya, yaitu Waylay yang berseteru dengan kembarannya bernama Tina. Ditambah lagi, ibu dari Waylay dan Tina tega meninggalkan kedua anaknya ini.

10. The Fault in Our Stars by John Green
Novel bahasa Inggris yang memiliki judul The Fault in Our Stars by John Green terbitan tahun 2012 ini merupakan pemenang novel fiksi remaja terbaik.
The Fault in Our Stars menuliskan kisah tentang Hazel Grace Lancaster, seorang remaja yang menderita kanker paru-paru. Kondisinya membuat Hazel harus bepergian dengan tabung oksigen untuk membantunya bernafas.
Kemudian, Hazel diarahkan sang ibu untuk menghadiri kelompok pendukung kanker. Di sana, ia bertemu dengan Augustus Waters.

11. Eleanor & Park by Rainbow Rowell
Kamu tertarik dengan cerita-cerita tentang cinta? Yuk, coba luangkan waktu untuk membaca novel bahasa Inggris berjudul Eleanor & Park dari Rainbow Rowell yang memiliki latar belakang sekolahan pada tahun 1986.
Nantinya, kamu akan mengenal tokoh Eleanor, yaitu seorang gadis penuh warna-warni yang memiliki banyak masalah keluarga, beserta Park, seorang anak laki-laki introvert yang menyukai komik.
Apakah hubungan keduanya berjalan dengan mulus? Tentunya nggak, ya. Sebab, Eleanor kerap mendapat banyak tekanan dari pihak keluarga dan teman sebayanya.

12. Cinder by Marissa Meyer
Buat kamu yang menyukai dunia science, merapat! Nih, ada rekomendasi novel bahasa Inggris berjudul Cinder by Marissa Meyer yang wajib masuk ke daftar bacaanmu.
Terbit pada tahun 2012, novel Cinder berhasil meraup prestasi sebagai Nominee for Best Goodreads Author (2012) dan Nominee for Best Young Adult Fantasy & Science Fiction (2012).
Nah, tokoh utama dalam novel ini adalah Cinder, yaitu seorang remaja yang hidup di kota futuristik New Beijing. Cinder memiliki skill cyborg, tetapi ia bekerja sebagai montir dan dianggap rendah oleh masyarakat karena statusnya yang berbeda.

13. The No. 1 Ladies’ Detective Agency – Alexander McCall Smith
Novel ini bergenre mystery crime, dan mengisahkan tentang Precious Ramostwe. Novel ini cocok untuk yang suka misteri ringan dan tokoh utama yang unik.
Singkatnya, Precious Ramotswe adalah wanita cerdas dan penuh semangat yang memutuskan untuk membuka agen detektif pertama yang dikelola wanita di Botswana. Dengan logika, hati yang baik, dan teh rooibos favoritnya, ia menyelesaikan berbagai kasus kecil – dari suami yang berselingkuh hingga anak hilang – sambil menunjukkan sisi kemanusiaan dan budaya Afrika yang hangat.

14. And Then There Were None – Agatha Christie
Penyuka Agatha Christie gak mungkin melewatkan novel populer yang satu ini, nih! And Then There Were None adalah sebuah novel bergenre psychological thriller. Sebuah cerita detektif klasik dengan twist yang sangat terkenal.
Sinopsis singkatnya, sepuluh orang asing diundang ke sebuah pulau misterius oleh seorang tuan rumah yang tidak mereka kenal. Satu per satu, mereka mulai mati sesuai bait lagu anak-anak yang tergantung di dinding. Tidak ada jalan keluar, dan pembunuhnya bisa jadi salah satu dari mereka.

15. The Cuckoo’s Calling – Robert Galbraith (J.K. Rowling)
Novel bergenre crime dan private detective ini ditulis oleh J.K. Rowling, loh!
Ceritanya tentang detektif swasta bernama Cormoran Strike yang sedang kesulitan secara finansial ketika ia ditawari kasus untuk menyelidiki kematian seorang supermodel terkenal yang jatuh dari balkon. Polisi menyebutnya bunuh diri, tapi keluarganya tidak percaya. Bersama asistennya Robin, Strike menelusuri dunia mode, ketenaran, dan kebohongan.

16. Coraline – Neil Gaiman
Novel yang ditulis oleh Neil Gaiman ini bergenre horror fantasy, dan menceritakan tentang Coraline Jones.
Coraline adalah gadis muda yang merasa bosan dengan hidupnya dan orang tuanya yang sibuk. Suatu hari, dia menemukan pintu rahasia ke dunia lain yang terlihat sempurna – di sana ada versi “orang tuanya” yang sangat perhatian. Tapi ada sesuatu yang salah. Dunia itu makin menyeramkan, dan Coraline harus menyelamatkan dirinya (dan orang tuanya) dari ibu lain yang jahat.

17. The Graveyard Book – Neil Gaiman
Rekomendasi novel terakhir juga ditulis oleh Neil Gaiman, dan masih di genre yang sama, yaitu horror fantasy. Novel ini menceritakan tentang seorang bayi laki=laki yang selamat dari pembunuhan keluarganya dan dibesarkan oleh hantu di pemakaman.
Ia diberi nama “Nobody Owens” atau “Bod”. Selama tumbuh besar, ia belajar dari berbagai makhluk gaib dan menghadapi banyak bahaya – termasuk si pembunuh yang masih mencarinya.
"""

# Extract books
blocks = re.split(r'\n(?=\d+\.\s)', "\n" + raw_text.strip())[1:]
books = []

generated_images = {
    "reminders-of-him": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\reminders_of_him_1790673871674.jpg",
    "remarkably-bright-creatures": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\remarkably_bright_1790673886320.jpg",
    "every-summer-after": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\every_summer_after_1790673899355.jpg",
    "charlottes-web": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\charlottes_web_1790673914947.jpg",
    "the-sense-of-an-ending": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\sense_of_an_ending_1790673928752.jpg",
    "our-souls-at-night": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\our_souls_at_night_1790673947707.jpg",
    "happy-place": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\happy_place_1790673968594.jpg",
    "love-on-the-brain": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\love_on_the_brain_1790673984357.jpg",
    "things-we-never-got-over": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\things_we_never_got_over_1790674000109.jpg",
    "the-fault-in-our-stars": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\fault_in_our_stars_1790674013722.jpg",
    "eleanor-and-park": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\eleanor_and_park_1790674029199.jpg",
    "cinder": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\cinder_1790674044740.jpg",
    "the-no-1-ladies-detective-agency": r"C:\Users\farre\.gemini\antigravity\brain\917dda74-d615-4985-9214-bf6e5c1686fc\no1_ladies_detective_1790674061967.jpg"
}

for block in blocks:
    lines = block.strip().split('\n')
    title_line = lines[0]
    m = re.match(r'\d+\.\s*(.+?)\s*(?:by|–|-)\s*(.+)', title_line, re.IGNORECASE)
    if m:
        title = m.group(1).strip()
        author = m.group(2).strip()
    else:
        title = title_line
        author = "Unknown"
    
    body = "\n".join(lines[1:]).strip()
    book_id = title.lower().replace(' ', '-').replace("’", "").replace("'", "").replace(".", "").replace("&", "and")
    
    # Categorize
    cat = "fiction"
    if "romantis" in body.lower() or "cinta" in body.lower() or "romance" in body.lower():
        cat = "romance"
    elif "misteri" in body.lower() or "detective" in body.lower() or "thriller" in body.lower() or "crime" in body.lower():
        cat = "mystery"
    elif "horror" in body.lower() or "fantasy" in body.lower() or "fiksi remaja" in body.lower() or "cyborg" in body.lower():
        cat = "fantasy"
        
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "category": cat,
        "body": body,
        "date": "2023"
    })

os.makedirs('data/stories', exist_ok=True)
os.makedirs('images/stories', exist_ok=True)

html_articles = []
for b in books:
    # write json
    json_path = f"data/stories/{b['id']}.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            "id": b['id'],
            "title": b['title'],
            "category": b['category'],
            "body": "<p class=\"mb-5 leading-[1.8] text-[#CCCCCC]\">" + b['body'].replace('\n', '</p><p class=\"mb-5 leading-[1.8] text-[#CCCCCC]\">') + "</p>"
        }, f, indent=4)
        
    # Copy images or create dummy
    img_dest = f"images/stories/{b['id']}.jpg"
    if b['id'] in generated_images and os.path.exists(generated_images[b['id']]):
        shutil.copy(generated_images[b['id']], img_dest)
    else:
        # Create dummy colored image
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (800, 450), color = (40, 40, 50))
        d = ImageDraw.Draw(img)
        d.text((400, 225), b['title'], fill=(255,255,255), anchor="mm")
        img.save(img_dest)

    # HTML markup
    color = "orange" if b['category'] == "romance" else "blue" if b['category'] == "mystery" else "purple" if b['category'] == "fantasy" else "teal"
    icon = "fa-heart" if b['category'] == "romance" else "fa-search" if b['category'] == "mystery" else "fa-magic" if b['category'] == "fantasy" else "fa-book"
    
    html_articles.append(f'''
            <article data-id="{b['id']}" data-category="{b['category']}" class="story-card bg-galaxy-card/70 backdrop-blur-md border border-gray-800/70 rounded-3xl overflow-hidden hover:border-{color}-500/60 hover:shadow-[0_15px_35px_rgba(0,0,0,0.5)] hover:-translate-y-2.5 transition-all duration-300 group reveal delay-100 flex flex-col cursor-pointer" onclick="openStoryReader('{b['id']}')">
                <div class="h-48 relative overflow-hidden flex items-center justify-center border-b border-gray-800/50 bg-black/40">
                    <img src="images/stories/{b['id']}.jpg" alt="{b['title']}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute inset-0 bg-gradient-to-t from-gray-950 via-transparent to-black/30"></div>
                </div>
                <div class="p-6 flex flex-col flex-grow relative">
                    <div class="mb-3 flex items-center gap-2">
                        <span class="text-{color}-400 text-xs font-bold tracking-wider uppercase">{b['category']}</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2 group-hover:text-{color}-400 transition-colors line-clamp-2">{b['title']}</h3>
                    <p class="text-sm text-gray-400 mb-6 flex-grow line-clamp-3">{b['body'][:100]}...</p>
                    
                    <div class="mt-auto pt-5 border-t border-gray-800/60 flex items-center justify-between text-xs font-semibold">
                        <span class="text-gray-500"><i class="fas {icon} mr-1"></i> {b['author']}</span>
                        <span class="text-white group-hover:text-{color}-400 transition-colors flex items-center gap-1.5">Read <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
            </article>
''')

with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace filters if not present
if 'data-filter="romance"' not in html:
    new_filters = """
                <button data-filter="romance" class="filter-btn px-5 sm:px-6 py-2 bg-gray-800/50 text-gray-400 border border-gray-700/50 rounded-full font-semibold text-xs sm:text-sm transition-all duration-300 hover:text-white hover:border-gray-500">
                    <i class="fas fa-heart mr-1 text-xs"></i> Romance <span class="ml-1 text-xs opacity-75">(6)</span>
                </button>
                <button data-filter="mystery" class="filter-btn px-5 sm:px-6 py-2 bg-gray-800/50 text-gray-400 border border-gray-700/50 rounded-full font-semibold text-xs sm:text-sm transition-all duration-300 hover:text-white hover:border-gray-500">
                    <i class="fas fa-search mr-1 text-xs"></i> Mystery <span class="ml-1 text-xs opacity-75">(2)</span>
                </button>
"""
    html = html.replace('</button>\n            </div>', '</button>\n' + new_filters + '            </div>')

# Find the end of storiesGrid and append new articles
grid_end = html.find('</div>', html.find('id="storiesGrid"'))
if grid_end != -1:
    html = html[:grid_end] + "\n".join(html_articles) + "\n" + html[grid_end:]

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done generating 17 stories!")
