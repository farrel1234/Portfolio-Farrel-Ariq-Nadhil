import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject HTML
afk_html = """
    <!-- AFK DVD SCREENSAVER -->
    <div id="afkOverlay" class="fixed inset-0 bg-black/95 z-[9999] opacity-0 pointer-events-none transition-opacity duration-500 overflow-hidden">
        <div id="afkLogo" class="absolute top-0 left-0 font-mono font-bold text-3xl sm:text-4xl text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-purple-500 whitespace-nowrap tracking-wider" style="will-change: transform;">
            &lt; FN /&gt;
        </div>
    </div>
"""

if 'AFK DVD SCREENSAVER' not in html:
    html = html.replace('    <!-- TERMINAL TOAST NOTIFICATION -->', afk_html + '\n    <!-- TERMINAL TOAST NOTIFICATION -->')

# 2. Inject JS
afk_js = """
        // 13. DYNAMIC TAB TITLE
        const originalTitle = document.title;
        document.addEventListener("visibilitychange", () => {
            if (document.visibilityState === "hidden") {
                document.title = "Hey, I'm compiling! ⚙️";
            } else {
                document.title = originalTitle;
            }
        });

        // 14. AFK MODE / DVD BOUNCE LOGO
        let idleTimeout;
        const afkOverlay = document.getElementById('afkOverlay');
        const afkLogo = document.getElementById('afkLogo');
        let isAfk = false;
        let afkReq;

        let logoX = 0;
        let logoY = 0;
        let speedX = 2;
        let speedY = 2;

        function resetIdleTimer() {
            if (isAfk) {
                isAfk = false;
                if(afkOverlay) {
                    afkOverlay.classList.remove('opacity-100', 'pointer-events-auto');
                    afkOverlay.classList.add('opacity-0', 'pointer-events-none');
                }
                cancelAnimationFrame(afkReq);
            }
            clearTimeout(idleTimeout);
            idleTimeout = setTimeout(triggerAfkMode, 60000);
        }

        function triggerAfkMode() {
            if(!afkOverlay || !afkLogo) return;
            isAfk = true;
            afkOverlay.classList.remove('opacity-0', 'pointer-events-none');
            afkOverlay.classList.add('opacity-100', 'pointer-events-auto');
            
            logoX = Math.random() * (window.innerWidth - 150);
            logoY = Math.random() * (window.innerHeight - 50);
            speedX = Math.random() > 0.5 ? 2.5 : -2.5;
            speedY = Math.random() > 0.5 ? 2.5 : -2.5;
            
            animateBounce();
        }

        function animateBounce() {
            if (!isAfk) return;
            
            const rect = afkLogo.getBoundingClientRect();
            
            logoX += speedX;
            logoY += speedY;
            
            if (logoX <= 0 || logoX + rect.width >= window.innerWidth) {
                speedX *= -1;
            }
            if (logoY <= 0 || logoY + rect.height >= window.innerHeight) {
                speedY *= -1;
            }
            
            if(logoX < 0) logoX = 0;
            if(logoY < 0) logoY = 0;
            if(logoX + rect.width > window.innerWidth) logoX = window.innerWidth - rect.width;
            if(logoY + rect.height > window.innerHeight) logoY = window.innerHeight - rect.height;

            afkLogo.style.transform = `translate(${logoX}px, ${logoY}px)`;
            
            afkReq = requestAnimationFrame(animateBounce);
        }

        ['mousemove', 'keydown', 'scroll', 'touchstart', 'click'].forEach(evt => {
            window.addEventListener(evt, resetIdleTimer, {passive: true});
        });
        resetIdleTimer();
"""

if 'AFK MODE / DVD BOUNCE LOGO' not in html:
    html = html.replace('</script>\n</body>', afk_js + '\n    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("AFK and Dynamic Title injected successfully.")
