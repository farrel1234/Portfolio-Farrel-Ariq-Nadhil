import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_toast_logic = """        // Terminal Toast Logic
        let toastTimeout;
        let toastResetTimeout;
        function showTerminalToast(msg) {
            const toast = document.getElementById('terminalToast');
            const toastMsg = document.getElementById('toastMessage');
            if(toast && toastMsg) {
                toastMsg.textContent = msg;
                
                // Clear any existing timeouts to prevent overlapping animations
                clearTimeout(toastTimeout);
                clearTimeout(toastResetTimeout);
                
                // 1. Initial State: Snug off-screen to the right.
                toast.style.transition = 'none';
                toast.style.transform = 'translateX(100%)';
                toast.style.opacity = '1';
                toast.classList.remove('translate-x-full', 'opacity-0', '-translate-x-10');
                
                // Force a browser reflow to apply the reset instantly
                void toast.offsetWidth;
                
                // 2. Running State: Move leftwards slowly and fade out.
                // transform moves it across the screen, opacity fades it out in the last 2 seconds of the 6-second journey.
                toast.style.transition = 'transform 6s linear, opacity 2s ease-out 4s';
                toast.style.transform = 'translateX(calc(-100vw + 100px))';
                toast.style.opacity = '0';
                
                // 3. Reset State: Hide it back to the start.
                toastTimeout = setTimeout(() => {
                    toast.style.transition = 'none';
                    toast.style.transform = 'translateX(100%)';
                }, 6500);
            }
        }"""

pattern = re.compile(r"// Terminal Toast Logic.*?\}\n\s*\}", re.DOTALL)
match = pattern.search(html)
if match:
    html = html[:match.start()] + new_toast_logic + html[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced successfully")
else:
    print("Not found")
