import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

toast_html = """
    <!-- TERMINAL TOAST NOTIFICATION -->
    <div id="terminalToast" class="fixed top-24 right-0 translate-x-full opacity-0 z-50 bg-gray-900/90 backdrop-blur-md border border-gray-700 p-4 rounded-l-xl shadow-[0_0_20px_rgba(37,99,235,0.4)] flex items-center gap-3 transition-all duration-700 max-w-xs sm:max-w-sm pointer-events-none">
        <i class="fas fa-terminal text-blue-400"></i>
        <p id="toastMessage" class="text-gray-200 text-sm font-mono truncate"></p>
    </div>
"""

# Insert toast HTML
if 'id="terminalToast"' not in html:
    html = html.replace('    <!-- AUDIO TOGGLE -->', toast_html + '    <!-- AUDIO TOGGLE -->')

toast_js = """        // Terminal Toast Logic
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
                
                // Reset styles instantly
                toast.style.transition = 'none';
                toast.classList.add('translate-x-full', 'opacity-0');
                toast.classList.remove('-translate-x-10');
                
                // Animate in from right
                setTimeout(() => {
                    toast.style.transition = 'all 0.7s cubic-bezier(0.4, 0, 0.2, 1)';
                    toast.classList.remove('translate-x-full', 'opacity-0');
                }, 50);
                
                // Animate out to left after 3 seconds
                toastTimeout = setTimeout(() => {
                    toast.classList.add('-translate-x-10', 'opacity-0');
                    
                    // Reset to default hidden state after fade out completes
                    toastResetTimeout = setTimeout(() => {
                        toast.style.transition = 'none';
                        toast.classList.remove('-translate-x-10');
                        toast.classList.add('translate-x-full');
                    }, 700);
                }, 3500);
            }
        }
"""

# Insert toast JS
if 'function showTerminalToast' not in html:
    html = html.replace('// 10. INTERACTIVE TERMINAL', toast_js + '\n        // 10. INTERACTIVE TERMINAL')

# Update echo logic
old_echo = "} else if(cmd === 'echo') {\n                        response.textContent = args.join(' ');"
new_echo = """} else if(cmd === 'echo') {
                        const text = args.join(' ');
                        response.textContent = `Echoing: ${text}`;
                        if(text) showTerminalToast(text);"""

if old_echo in html:
    html = html.replace(old_echo, new_echo)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Toast feature added successfully!")
