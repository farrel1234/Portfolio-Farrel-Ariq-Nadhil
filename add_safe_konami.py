import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS
css_code = """
    <style>
        @keyframes matrix-glitch {
            0% { transform: translate(1px, 1px); filter: hue-rotate(0deg); }
            20% { transform: translate(-1px, -2px); filter: hue-rotate(90deg) brightness(1.2); }
            40% { transform: translate(-3px, 0px); filter: hue-rotate(180deg) brightness(1.5); }
            60% { transform: translate(3px, 2px); filter: hue-rotate(270deg) brightness(1.2); }
            80% { transform: translate(1px, -1px); filter: hue-rotate(360deg) brightness(1.5); }
            100% { transform: translate(1px, -2px); filter: hue-rotate(0deg); }
        }
        .matrix-hacked {
            animation: matrix-glitch 0.5s infinite;
        }
    </style>
</head>"""

if 'matrix-glitch' not in html:
    html = html.replace('</head>', css_code)

# 2. Inject HTML Toast
html_toast = """
    <!-- KONAMI EASTER EGG TOAST -->
    <div id="achievement-toast" class="fixed top-24 left-1/2 -translate-x-1/2 -translate-y-40 opacity-0 pointer-events-none z-[100] bg-gray-900/90 backdrop-blur-md border-2 border-[#22c55e] p-5 rounded-2xl shadow-[0_0_30px_rgba(34,197,94,0.5)] flex items-center gap-4 transition-all duration-500 max-w-sm text-center">
        <i class="fas fa-gamepad text-[#22c55e] text-3xl animate-pulse"></i>
        <p class="text-gray-200 text-sm font-mono font-semibold">
            Achievement Unlocked!<br>
            <span class="text-[#22c55e]">Gamer Architect</span><br>
            <span class="text-xs font-normal opacity-80 leading-relaxed mt-1 block">From clutching in Valorant & PUBG, building in Minecraft & Roblox, surviving GTA V, to architecting flawless code.</span>
        </p>
    </div>
"""
if 'id="achievement-toast"' not in html:
    html = html.replace('    <!-- TERMINAL TOAST NOTIFICATION -->', html_toast + '\n    <!-- TERMINAL TOAST NOTIFICATION -->')

# 3. Inject JS Logic
js_logic = """
        // 11. KONAMI CODE EASTER EGG (SAFE MODE)
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

            const toast = document.getElementById('achievement-toast');
            if(toast) {
                toast.classList.remove('-translate-y-40', 'opacity-0');
                toast.classList.add('translate-y-0', 'opacity-100');
            }

            const canvas = document.getElementById('vanilla-canvas');
            if(canvas) {
                canvas.classList.add('matrix-hacked');
            }

            // Save old colors and modify
            const oldColors = [...colors];
            colors.length = 0;
            colors.push('#22c55e', '#4ade80', '#16a34a');

            particles.forEach(p => {
                p.konamiSpeedX = p.speedX;
                p.konamiSpeedY = p.speedY;
                p.konamiColor = p.color;

                p.speedX = 0;
                p.speedY = Math.random() * 5 + 3;
                p.color = colors[Math.floor(Math.random() * colors.length)];
            });

            setTimeout(() => {
                if(toast) {
                    toast.classList.remove('translate-y-0', 'opacity-100');
                    toast.classList.add('-translate-y-40', 'opacity-0');
                }

                if(canvas) {
                    canvas.classList.remove('matrix-hacked');
                }

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
print("Safe Konami Easter Egg injected!")
