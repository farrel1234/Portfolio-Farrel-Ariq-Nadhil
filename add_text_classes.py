import re

with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# readerTitle -> reader-text
html = html.replace(
    'id="readerTitle" class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#E0E0E0] leading-tight mb-4 tracking-tight font-serif"',
    'id="readerTitle" class="reader-text text-3xl sm:text-4xl lg:text-5xl font-extrabold text-[#E0E0E0] leading-tight mb-4 tracking-tight font-serif"'
)

# readerSubtitle -> reader-subtext
html = html.replace(
    'id="readerSubtitle" class="text-sm sm:text-base text-[#AAAAAA] italic mb-6"',
    'id="readerSubtitle" class="reader-subtext text-sm sm:text-base text-[#AAAAAA] italic mb-6"'
)

# readerDate -> reader-subtext
html = html.replace(
    'id="readerDate" class="font-medium"',
    'id="readerDate" class="reader-subtext font-medium"'
)

# readerEpigraph -> reader-quote
html = html.replace(
    'id="readerEpigraph" class="font-serif italic text-[#CCCCCC] text-sm sm:text-base leading-relaxed"',
    'id="readerEpigraph" class="reader-quote font-serif italic text-[#CCCCCC] text-sm sm:text-base leading-relaxed"'
)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)
