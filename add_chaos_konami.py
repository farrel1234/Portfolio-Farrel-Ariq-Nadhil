import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS
css_code = """
    <style>
        @keyframes earthquake {
            0% { transform: translate(2px, 1px) rotate(0deg) skew(0deg); color: inherit; }
            10% { transform: translate(-5px, -2px) rotate(-5deg) skew(5deg); color: #ff0000; }
            20% { transform: translate(-10px, 0px) rotate(10deg) skew(-5deg); color: #00ff00; }
            30% { transform: translate(10px, 5px) rotate(0deg) skew(10deg); color: inherit; }
            40% { transform: translate(1px, -10px) rotate(5deg) skew(-10deg); color: #ff0000; }
            50% { transform: translate(-10px, 5px) rotate(-10deg) skew(5deg); color: #00ff00; }
            60% { transform: translate(-5px, 1px) rotate(0deg) skew(0deg); color: inherit; }
            70% { transform: translate(10px, 1px) rotate(-5deg) skew(-5deg); color: #ff0000; }
            80% { transform: translate(-2px, -5px) rotate(10deg) skew(5deg); color: #00ff00; }
            90% { transform: translate(5px, 10px) rotate(0deg) skew(0deg); color: inherit; }
            100% { transform: translate(2px, -2px) rotate(-5deg) skew(-5deg); color: #ff0000; }
        }
        .chaos-mode p:not(#chaosToast p), 
        .chaos-mode h1, 
        .chaos-mode h2, 
        .chaos-mode h3, 
        .chaos-mode a, 
        .chaos-mode button:not(#chaosToast button), 
        .chaos-mode nav,
        .chaos-mode img {
            animation: earthquake 0.3s infinite;
        }
    </style>
</head>"""

if 'earthquake' not in html:
    html = html.replace('</head>', css_code)

# 2. Inject HTML Toast
html_toast = """
    <!-- CHAOS EASTER EGG TOAST -->
    <div id="chaosToast" class="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 opacity-0 pointer-events-none z-[9999] bg-black/90 backdrop-blur-xl border-2 border-red-500 p-8 rounded-2xl shadow-[0_0_50px_rgba(255,0,0,0.8)] flex flex-col items-center gap-4 transition-all duration-500 max-w-md text-center scale-50">
        <i class="fas fa-biohazard text-red-500 text-5xl animate-pulse"></i>
        <p class="text-white text-lg font-mono font-bold" style="animation: none !important; transform: none !important;">
            Achievement Unlocked!<br>
            <span class="text-red-500 text-2xl">Gamer Architect</span><br>
            <span class="text-sm font-normal text-gray-300 leading-relaxed mt-3 block">You broke the Matrix! (GTA V, Valorant, Minecraft, Roblox)<br>Now fixing the code...</span>
        </p>
    </div>
"""
if 'id="chaosToast"' not in html:
    html = html.replace('    <!-- TERMINAL TOAST NOTIFICATION -->', html_toast + '\n    <!-- TERMINAL TOAST NOTIFICATION -->')

# 3. Inject JS Logic
js_logic = """
        // 11. KONAMI CODE EASTER EGG (CHAOS MODE)
        const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
        let konamiIndex = 0;
        let isHackingMode = false;

        document.addEventListener('keydown', (e) => {
            if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
                return;
            }

            if (e.key === konamiCode[konamiIndex]) {
                konamiIndex++;
                if (konamiIndex === konamiCode.length) {
                    activateHackingMode();
                    konamiIndex = 0;
                }
            } else {
                konamiIndex = 0;
            }
        });

        function activateHackingMode() {
            if (isHackingMode) return;
            isHackingMode = true;

            const toast = document.getElementById('chaosToast');
            if(toast) {
                toast.classList.remove('opacity-0', 'scale-50');
                toast.classList.add('opacity-100', 'scale-100');
            }

            document.body.classList.add('chaos-mode');

            // Save old colors and modify
            const oldColors = [...colors];
            colors.length = 0;
            colors.push('#00FF00', '#39FF14');

            particles.forEach(p => {
                p.konamiSpeedX = p.speedX;
                p.konamiSpeedY = p.speedY;
                p.konamiColor = p.color;

                p.speedX = 0;
                p.speedY = Math.random() * 8 + 5; // Very fast
                p.color = colors[Math.floor(Math.random() * colors.length)];
            });

            setTimeout(() => {
                if(toast) {
                    toast.classList.remove('opacity-100', 'scale-100');
                    toast.classList.add('opacity-0', 'scale-50');
                }

                document.body.classList.remove('chaos-mode');

                colors.length = 0;
                oldColors.forEach(c => colors.push(c));

                particles.forEach(p => {
                    p.speedX = p.konamiSpeedX;
                    p.speedY = p.konamiSpeedY;
                    p.color = p.konamiColor;
                });

                isHackingMode = false;
            }, 6000);
        }
"""
if 'KONAMI CODE EASTER EGG' not in html:
    html = html.replace('</script>\n</body>', js_logic + '\n    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Chaos Konami Easter Egg injected!")
