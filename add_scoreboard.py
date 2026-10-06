import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject HTML
scoreboard_html = """
    <!-- ESPORTS SCOREBOARD OVERLAY -->
    <div id="tabScoreboard" class="fixed inset-0 z-[9999] backdrop-blur-md bg-black/70 flex items-center justify-center opacity-0 pointer-events-none transition-opacity duration-150 p-4">
        <div class="relative bg-gray-900/80 border border-purple-500/30 rounded-xl p-6 sm:p-8 max-w-md w-full shadow-[0_0_40px_rgba(124,58,237,0.2)] overflow-hidden transform transition-all">
            <!-- Glow Accent -->
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-orange-400 to-purple-500"></div>
            
            <div class="flex items-center gap-4 border-b border-gray-700 pb-4 mb-6">
                <div class="w-16 h-16 rounded-full bg-gradient-to-br from-orange-500 to-purple-600 flex items-center justify-center text-white font-bold text-xl shadow-[0_0_15px_rgba(249,115,22,0.4)]">
                    FN
                </div>
                <div>
                    <h2 class="text-2xl font-black text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-purple-500 tracking-wider">FARREL_NADHIL</h2>
                    <p class="text-green-400 text-sm font-mono flex items-center gap-2">
                        <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> ONLINE
                    </p>
                </div>
            </div>
            
            <div class="space-y-4 font-mono text-sm">
                <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center bg-gray-800/50 p-3 rounded-lg border border-gray-700/50 gap-1 sm:gap-0">
                    <span class="text-gray-400">Class:</span>
                    <span class="text-white font-bold tracking-wide">Software Engineer</span>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center bg-gray-800/50 p-3 rounded-lg border border-gray-700/50 gap-1 sm:gap-0">
                    <span class="text-gray-400">Base Camp:</span>
                    <span class="text-orange-400 font-bold tracking-wide">Batam, ID</span>
                </div>
                <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center bg-gray-800/50 p-3 rounded-lg border border-gray-700/50 gap-1 sm:gap-0">
                    <span class="text-gray-400">Guild:</span>
                    <span class="text-purple-400 font-bold tracking-wide text-right sm:text-left">Politeknik Negeri Batam</span>
                </div>
                <div class="mt-6 pt-4 border-t border-gray-700">
                    <p class="text-gray-500 text-xs uppercase mb-2">Current Quest</p>
                    <p class="text-yellow-400 font-bold animate-pulse text-sm sm:text-base border-l-2 border-yellow-500 pl-3">Seeking Project-Based / Internship Opportunities</p>
                </div>
            </div>
        </div>
    </div>
"""

if 'ESPORTS SCOREBOARD OVERLAY' not in html:
    html = html.replace('    <!-- TERMINAL TOAST NOTIFICATION -->', scoreboard_html + '\n    <!-- TERMINAL TOAST NOTIFICATION -->')

# 2. Inject JS
scoreboard_js = """
        // 15. ESPORTS SCOREBOARD (HOLD TAB)
        const tabScoreboard = document.getElementById('tabScoreboard');
        let isScoreboardOpen = false;

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                e.preventDefault(); // Mencegah navigasi fokus ke link lain
                if (!isScoreboardOpen) {
                    isScoreboardOpen = true;
                    if(tabScoreboard) {
                        tabScoreboard.classList.remove('opacity-0', 'pointer-events-none');
                        tabScoreboard.classList.add('opacity-100', 'pointer-events-auto');
                    }
                }
            }
        });

        document.addEventListener('keyup', (e) => {
            if (e.key === 'Tab') {
                isScoreboardOpen = false;
                if(tabScoreboard) {
                    tabScoreboard.classList.remove('opacity-100', 'pointer-events-auto');
                    tabScoreboard.classList.add('opacity-0', 'pointer-events-none');
                }
            }
        });
"""

if 'ESPORTS SCOREBOARD (HOLD TAB)' not in html:
    html = html.replace('</script>\n</body>', scoreboard_js + '\n    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Scoreboard injected successfully.")
