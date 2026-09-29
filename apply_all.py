import os
import json
import re
import glob

# 1. READ ALL DATA.JS
with open('data.js', 'r', encoding='utf-8') as f:
    # Check if data.js exists
    pass

# 2. GENERATE NEW HTML ARTICLES
books = [
    ("reminders-of-him", "Reminders of Him", "Colleen Hoover", "romance", "Saking populernya, saat ini terdapat 94% pengguna Google yang menyukai novel romantis dengan judul R..."),
    ("remarkably-bright-creatures", "Remarkably Bright Creatures", "Shelby Van Pelt", "mystery", "Novel ini bercerita mengenai kehidupan Tova Sullivan. Setelah suaminya meninggal, Tova memulai ruti..."),
    ("every-summer-after", "Every Summer After", "Carley Fortune", "fiction", "Pernahkah kamu merasa bahwa kesalahan yang pernah dilakukan bisa membatasi masa depanmu? Kalau perna..."),
    ("charlottes-web", "Charlotte’s Web", "E.B. White", "fiction", "Kalau kamu termasuk orang yang menyukai buku dari visual, coba deh baca buku ini. Sebab, di di dala..."),
    ("the-sense-of-an-ending", "The Sense of an Ending", "Julian Barnes", "fiction", "The Sense of an Ending menceritakan tentang seorang pria bernama Tony Webster yang mencoba memahami ..."),
    ("our-souls-at-night", "Our Souls at Night", "Kent Haruf", "fiction", "Our Souls at Night bercerita tentang dua orang tetangga tua, Addie Moore dan Louis Waters, yang mem..."),
    ("happy-place", "Happy Place", "Emily Henry", "romance", "Happy Place memuat cerita romantis dari pasangan Harriet dan Wyn. yang telah menjalin hubungan seja..."),
    ("love-on-the-brain", "Love on the Brain", "Ali Hazelwood", "romance", "Melalui buku ini, sang penulis menceritakan Bee Königswasser yang tertarik dengan pemuda bernama Le..."),
    ("things-we-never-got-over", "Things We Never Got Over", "Lucy Score", "romance", "Ringkasnya, novel ini mengisahkan tentang Naomi yang berusaha untuk hidup dengan keponakannya, yait..."),
    ("the-fault-in-our-stars", "The Fault in Our Stars", "John Green", "romance", "The Fault in Our Stars menuliskan kisah tentang Hazel Grace Lancaster, seorang remaja yang menderit..."),
    ("eleanor-and-park", "Eleanor & Park", "Rainbow Rowell", "romance", "Nantinya, kamu akan mengenal tokoh Eleanor, yaitu seorang gadis penuh warna-warni yang memiliki ban..."),
    ("cinder", "Cinder", "Marissa Meyer", "fantasy", "Nah, tokoh utama dalam novel ini adalah Cinder, yaitu seorang remaja yang hidup di kota futuristik ..."),
    ("the-no-1-ladies-detective-agency", "The No. 1 Ladies’ Detective Agency", "Alexander McCall Smith", "mystery", "Singkatnya, Precious Ramotswe adalah wanita cerdas dan penuh semangat yang memutuskan untuk membuka..."),
    ("and-then-there-were-none", "And Then There Were None", "Agatha Christie", "mystery", "Sinopsis singkatnya, sepuluh orang asing diundang ke sebuah pulau misterius oleh seorang tuan rumah..."),
    ("the-cuckoos-calling", "The Cuckoo’s Calling", "J.K. Rowling", "mystery", "Ceritanya tentang detektif swasta bernama Cormoran Strike yang sedang kesulitan secara finansial ke..."),
    ("coraline", "Coraline", "Neil Gaiman", "fantasy", "Coraline adalah gadis muda yang merasa bosan dengan hidupnya dan orang tuanya yang sibuk. Suatu har..."),
    ("the-graveyard-book", "The Graveyard Book", "Neil Gaiman", "fantasy", "Novel ini menceritakan tentang seorang bayi laki-laki yang selamat dari pembunuhan keluarganya dan ...")
]

html_articles = []
for idx, (b_id, title, author, cat, snippet) in enumerate(books):
    color = "orange" if cat == "romance" else "blue" if cat == "mystery" else "purple" if cat == "fantasy" else "teal"
    icon = "fa-heart" if cat == "romance" else "fa-search" if cat == "mystery" else "fa-magic" if cat == "fantasy" else "fa-book"
    
    article = f'''
            <!-- Story {26+idx}: {title} -->
            <article data-id="{b_id}" data-category="{cat}" class="story-card bg-galaxy-card/70 backdrop-blur-md border border-gray-800/70 rounded-3xl overflow-hidden hover:border-{color}-500/60 hover:shadow-[0_15px_35px_rgba(0,0,0,0.5)] hover:-translate-y-2.5 transition-all duration-300 group reveal delay-100 flex flex-col cursor-pointer" onclick="openStoryReader('{b_id}')">
                <div class="h-48 relative overflow-hidden flex items-center justify-center border-b border-gray-800/50 bg-black/40">
                    <img src="images/stories/{b_id}.jpg" alt="{title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    <div class="absolute inset-0 bg-gradient-to-t from-gray-950 via-transparent to-black/30"></div>
                </div>
                <div class="p-6 flex flex-col flex-grow relative">
                    <div class="mb-3 flex items-center gap-2">
                        <span class="text-{color}-400 text-xs font-bold tracking-wider uppercase">{cat}</span>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2 group-hover:text-{color}-400 transition-colors line-clamp-2">{title}</h3>
                    <p class="text-sm text-gray-400 mb-6 flex-grow line-clamp-3">{snippet}</p>
                    
                    <div class="mt-auto pt-5 border-t border-gray-800/60 flex items-center justify-between text-xs font-semibold">
                        <span class="text-gray-500"><i class="fas {icon} mr-1"></i> {author}</span>
                        <span class="text-white group-hover:text-{color}-400 transition-colors flex items-center gap-1.5">Read <i class="fas fa-arrow-right"></i></span>
                    </div>
                </div>
            </article>'''
    html_articles.append(article)

# 3. APPLY TO HTML
with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix All Stories Count
html = html.replace('All Stories <span class="ml-1 text-xs opacity-80">(25)</span>', 'All Stories <span class="ml-1 text-xs opacity-80">(42)</span>')
html = html.replace('placeholder="Search 25 stories by title, character, or keyword..."', 'placeholder="Search 42 stories by title, character, or keyword..."')

# Insert filters
if 'data-filter="romance"' not in html:
    new_filters = """
                <button data-filter="romance" class="filter-btn px-5 sm:px-6 py-2 bg-gray-800/50 text-gray-400 border border-gray-700/50 rounded-full font-semibold text-xs sm:text-sm transition-all duration-300 hover:text-white hover:border-gray-500">
                    <i class="fas fa-heart mr-1 text-xs"></i> Romance <span class="ml-1 text-xs opacity-75">(6)</span>
                </button>
                <button data-filter="mystery" class="filter-btn px-5 sm:px-6 py-2 bg-gray-800/50 text-gray-400 border border-gray-700/50 rounded-full font-semibold text-xs sm:text-sm transition-all duration-300 hover:text-white hover:border-gray-500">
                    <i class="fas fa-search mr-1 text-xs"></i> Mystery <span class="ml-1 text-xs opacity-75">(4)</span>
                </button>
"""
    # Find the filterTabs div end
    idx = html.find('</div>', html.find('id="filterTabs"'))
    html = html[:idx] + new_filters + html[idx:]

# Insert Articles
articles_str = "\n".join(html_articles) + "\n"
html = html.replace('        </div>\n        \n        <!-- PAGINATION CONTROLS -->', articles_str + '        </div>\n        \n        <!-- PAGINATION CONTROLS -->')

# Refactor JS
if '<script src="data.js"></script>' not in html:
    html = html.replace('</body>', '    <script src="data.js"></script>\n</body>')

old_fetch_logic = """        async function openStoryReader(storyId) {
            let story;
            try {
                const res = await fetch("data/stories/" + storyId + ".json");
                if (!res.ok) throw new Error("Not found");
                story = await res.json();
            } catch(e) {
                console.error("Failed to lazy load story", e);
                return;
            }"""

new_fetch_logic = """        async function openStoryReader(storyId) {
            let story = STORY_DB[storyId];
            if (!story) {
                console.error("Failed to lazy load story: Not found in STORY_DB");
                return;
            }"""

html = html.replace(old_fetch_logic, new_fetch_logic)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Applied successfully.")
