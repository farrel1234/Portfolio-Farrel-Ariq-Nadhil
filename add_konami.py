import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject CSS
css_code = """
    <style>
        @keyframes konamiShake {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            70% { transform: translate(3px, 1px) rotate(-1deg); }
            80% { transform: translate(-1px, -1px) rotate(1deg); }
            90% { transform: translate(1px, 2px) rotate(0deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }
        .konami-shake {
            animation: konamiShake 0.5s infinite;
        }
    </style>
</head>"""

if 'konamiShake' not in html:
    html = html.replace('</head>', css_code)

# 2. Inject HTML Toast
html_toast = """
    <!-- KONAMI EASTER EGG TOAST -->
    <div id="konamiToast" class="fixed top-24 left-1/2 -translate-x-1/2 -translate-y-10 opacity-0 pointer-events-none z-[100] bg-gray-900/90 backdrop-blur-md border-2 border-[#39FF14] p-5 rounded-2xl shadow-[0_0_30px_rgba(57,255,20,0.5)] flex items-center gap-4 transition-all duration-500 max-w-sm text-center">
        <i class="fas fa-gamepad text-[#39FF14] text-2xl animate-pulse"></i>
        <p class="text-gray-200 text-sm font-mono font-semibold">
            Achievement Unlocked!<br>
            <span class="text-[#39FF14]">Gamer Architect</span><br>
            <span class="text-xs font-normal opacity-80 leading-relaxed mt-1 block">From clutching in Valorant & PUBG, building in Minecraft & Roblox, surviving GTA V, to architecting flawless code.</span>
        </p>
    </div>
"""
if 'id="konamiToast"' not in html:
    html = html.replace('    <!-- TERMINAL TOAST NOTIFICATION -->', html_toast + '\n    <!-- TERMINAL TOAST NOTIFICATION -->')

# 3. Inject JS Logic
js_logic = """
        // 11. KONAMI CODE EASTER EGG
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

            const toast = document.getElementById('konamiToast');
            if(toast) {
                toast.classList.remove('-translate-y-10', 'opacity-0');
                toast.classList.add('translate-y-0', 'opacity-100');
            }

            document.body.classList.add('konami-shake');

            // Save old colors and modify
            const oldColors = [...colors];
            colors.length = 0;
            colors.push('#00FF00', '#39FF14');

            particles.forEach(p => {
                p.konamiSpeedX = p.speedX;
                p.konamiSpeedY = p.speedY;
                p.konamiColor = p.color;

                p.speedX = 0;
                p.speedY = Math.random() * 4 + 3;
                p.color = colors[Math.floor(Math.random() * colors.length)];
            });

            setTimeout(() => {
                if(toast) {
                    toast.classList.remove('translate-y-0', 'opacity-100');
                    toast.classList.add('-translate-y-10', 'opacity-0');
                }

                document.body.classList.remove('konami-shake');

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
print("Konami Easter Egg injected!")
