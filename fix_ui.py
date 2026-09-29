import re

with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix readerBackdrop
html = html.replace(
    'id="readerBackdrop" class="reader-backdrop-hidden fixed inset-0 z-50 bg-black/90 backdrop-blur-xl',
    'id="readerBackdrop" class="reader-backdrop-hidden fixed inset-0 z-50 bg-transparent backdrop-blur-md'
)

# 2. Fix readerModal
html = html.replace(
    'id="readerModal" class="reader-modal-hidden bg-[#1E1E1E] rounded-md sm:rounded-xl w-full max-w-5xl h-[85vh] sm:h-[90vh] shadow-[0_30px_60px_rgba(0,0,0,0.8)]',
    'id="readerModal" class="reader-modal-hidden bg-[#1E1E1E]/80 backdrop-blur-3xl border border-white/5 reader-surface rounded-md sm:rounded-xl w-full max-w-2xl h-[85vh] sm:h-[90vh] shadow-[0_30px_60px_rgba(0,0,0,0.8)]'
)

# 3. Remove book crease
html = html.replace(
    '<div class="hidden md:block absolute top-0 left-1/2 -translate-x-1/2 w-20 h-full pointer-events-none z-20 bg-gradient-to-r from-transparent via-black/60 to-transparent"></div>',
    ''
)

# 4. Fix Sticky Top Bar background
html = html.replace(
    'class="border-b border-[#2A2A2A] bg-[#1E1E1E]/95 backdrop-blur-md px-4 sm:px-8 py-3.5 flex items-center justify-between z-30 flex-shrink-0 relative"',
    'class="border-b border-white/5 bg-transparent px-4 sm:px-8 py-3.5 flex items-center justify-between z-30 flex-shrink-0 relative"'
)

# 5. Fix multiColumnWrapper layout to 1 column
html = html.replace(
    'id="multiColumnWrapper" class="md:columns-2 md:gap-[80px] md:h-[calc(90vh-140px)] h-auto"',
    'id="multiColumnWrapper" class="md:columns-1 md:gap-[96px] md:h-[calc(90vh-140px)] h-auto"'
)

# 6. Re-add Theme Toggle Button
theme_btn = """
                    <!-- THEME TOGGLE -->
                    <button id="themeToggleBtn" onclick="toggleReaderTheme()" title="Warm Theme" class="p-2 rounded-lg bg-[#2A2A2A] hover:bg-orange-500/20 text-[#888888] hover:text-orange-400 transition text-sm flex items-center gap-2 border border-transparent">
                        <i class="fas fa-mug-hot"></i>
                    </button>
                    """
if 'id="themeToggleBtn"' not in html:
    html = html.replace(
        '<!-- CLOSE BUTTON -->',
        theme_btn + '\n                    <!-- CLOSE BUTTON -->'
    )

# 7. Fix theme-sepia CSS
old_css = """        body.theme-sepia .reader-surface {
            background-color: #17130f !important;
            border-color: #3d2e20 !important;
        }"""
new_css = """        body.theme-sepia .reader-surface {
            background-color: rgba(23, 19, 15, 0.8) !important;
            border-color: rgba(61, 46, 32, 0.5) !important;
        }"""
if old_css in html:
    html = html.replace(old_css, new_css)
else:
    # try regex
    html = re.sub(r'body\.theme-sepia\s*\.reader-surface\s*\{[^}]+\}', new_css, html)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)
