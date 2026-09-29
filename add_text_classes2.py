import re

with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<span id="readerDate">Date</span>',
    '<span id="readerDate" class="reader-subtext">Date</span>'
)

html = html.replace(
    '<div id="readerEpigraph" class="p-4 sm:p-5 rounded-lg bg-[#252525] border-l-4 border-orange-500 text-[#CCCCCC] italic text-sm font-serif mb-6">',
    '<div id="readerEpigraph" class="reader-quote p-4 sm:p-5 rounded-lg bg-[#252525] border-l-4 border-orange-500 text-[#CCCCCC] italic text-sm font-serif mb-6">'
)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)
