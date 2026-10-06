import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_logic = """            terminalInput.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    const fullCmd = this.value.trim();
                    const cmdLower = fullCmd.toLowerCase();
                    const args = cmdLower.split(' ').slice(1);
                    const cmd = cmdLower.split(' ')[0];
                    this.value = '';
                    
                    if (fullCmd === '') return;
                    
                    const cmdEcho = document.createElement('div');
                    cmdEcho.innerHTML = `<span class="text-green-400">guest@farrel:~$</span> <span class="escape-text"></span>`;
                    cmdEcho.querySelector('.escape-text').textContent = fullCmd;
                    terminalOutput.appendChild(cmdEcho);
                    
                    const response = document.createElement('div');
                    response.className = 'text-gray-300 mb-2 leading-relaxed';
                    
                    if(cmd === 'help') {
                        response.innerHTML = `<table class="w-full text-left border-collapse">
                        <tr><td class="text-purple-400 font-bold w-24">whoami</td><td>About me</td></tr>
                        <tr><td class="text-purple-400 font-bold">skills</td><td>My tech stack</td></tr>
                        <tr><td class="text-purple-400 font-bold">projects</td><td>List key projects</td></tr>
                        <tr><td class="text-purple-400 font-bold">socials</td><td>My online profiles</td></tr>
                        <tr><td class="text-purple-400 font-bold">neofetch</td><td>System info</td></tr>
                        <tr><td class="text-purple-400 font-bold">music</td><td>Toggle background music</td></tr>
                        <tr><td class="text-purple-400 font-bold">date</td><td>Show current time</td></tr>
                        <tr><td class="text-purple-400 font-bold">echo</td><td>Print a message</td></tr>
                        <tr><td class="text-purple-400 font-bold">clear</td><td>Clear terminal</td></tr>
                        </table>`;
                    } else if(cmd === 'whoami') {
                        response.innerHTML = `I'm Farrel, a Software Engineer from Batam, Indonesia. I build scalable mobile apps and web platforms.`;
                    } else if(cmd === 'skills') {
                        response.innerHTML = `Mobile: Kotlin, Jetpack Compose<br>Backend: PHP, Laravel, MySQL<br>AI: Python, OpenCV<br>Design: Figma`;
                    } else if(cmd === 'projects') {
                        response.innerHTML = `<span class="text-orange-400">1. CraveIt</span> - Food delivery app (Kotlin)<br><span class="text-orange-400">2. E-Voting</span> - Secure voting platform (Laravel)<br>Type <span class="italic">cd projects</span> to explore (just kidding).`;
                    } else if(cmd === 'socials') {
                        response.innerHTML = `<a href="https://github.com/farrel1234" target="_blank" class="text-blue-400 hover:underline">GitHub</a> | <a href="#" class="text-blue-400 hover:underline">LinkedIn</a> | <a href="#" class="text-blue-400 hover:underline">Instagram</a>`;
                    } else if(cmd === 'sudo') {
                        response.innerHTML = `guest is not in the sudoers file. <span class="text-red-500 font-bold">This incident will be reported.</span>`;
                    } else if(cmd === 'date') {
                        response.innerHTML = new Date().toString();
                    } else if(cmd === 'neofetch') {
                        response.innerHTML = `<div class="flex gap-4 items-center">
                            <div class="text-blue-500 font-bold leading-none text-xs sm:text-sm">
                             /\\_/<\\<br>
                            ( o.o )<br>
                             > ^ <
                            </div>
                            <div class="text-xs sm:text-sm">
                                <span class="text-purple-400 font-bold">OS:</span> FarrelOS v1.0<br>
                                <span class="text-purple-400 font-bold">Host:</span> Batam, Indonesia<br>
                                <span class="text-purple-400 font-bold">Uptime:</span> 2002 - Present<br>
                                <span class="text-purple-400 font-bold">Shell:</span> bash 5.1.16<br>
                            </div>
                        </div>`;
                    } else if(cmd === 'music') {
                        const bgMusic = document.getElementById('bgMusic');
                        const musicToggle = document.getElementById('musicToggle');
                        if(bgMusic) {
                            musicToggle.click();
                            response.innerHTML = bgMusic.paused ? "Music paused." : "Playing Lofi Beats... ?";
                        } else {
                            response.innerHTML = "Audio not found.";
                        }
                    } else if(cmd === 'echo') {
                        response.textContent = args.join(' ');
                    } else if(cmd === 'ls' || cmd === 'dir') {
                        response.innerHTML = `<span class="text-blue-400 font-bold">projects/</span> &nbsp; <span class="text-blue-400 font-bold">designs/</span> &nbsp; resume.pdf &nbsp; readme.md`;
                    } else if(cmd === 'cd') {
                        response.innerHTML = `bash: cd: ${args[0] || ''}: Permission denied`;
                    } else if(cmd === 'cat') {
                        if(args[0] === 'readme.md') response.innerHTML = `Hello world! Thanks for visiting my portfolio.`;
                        else response.innerHTML = `cat: ${args[0] || ''}: No such file or directory`;
                    } else if(cmd === 'clear') {
                        terminalOutput.innerHTML = '';
                        response.innerHTML = '';
                    } else {
                        response.innerHTML = `<span class="text-red-400">Command not found:</span> <span class="escape-cmd"></span>. Type 'help' for available commands.`;
                        response.querySelector('.escape-cmd').textContent = cmd;
                    }
                    
                    if(response.innerHTML) terminalOutput.appendChild(response);
                    terminalBody.scrollTop = terminalBody.scrollHeight;
                }
            });"""

old_logic = """            terminalInput.addEventListener('keydown', function(e) {
                if(e.key === 'Enter') {
                    const cmd = this.value.trim().toLowerCase();
                    this.value = '';
                    
                    const cmdEcho = document.createElement('div');
                    cmdEcho.innerHTML = `<span class="text-green-400">guest@farrel:~$</span> ${cmd}`;
                    terminalOutput.appendChild(cmdEcho);
                    
                    const response = document.createElement('div');
                    response.className = 'text-gray-300 mb-2';
                    
                    if(cmd === 'help') {
                        response.innerHTML = `Available commands:<br>
                        <span class="text-purple-400">whoami</span> - About me<br>
                        <span class="text-purple-400">skills</span> - My tech stack<br>
                        <span class="text-purple-400">clear</span>  - Clear terminal`;
                    } else if(cmd === 'whoami') {
                        response.innerHTML = `I'm Farrel, a Software Engineer from Batam, Indonesia. I build scalable mobile apps and web platforms.`;
                    } else if(cmd === 'skills') {
                        response.innerHTML = `Mobile: Kotlin, Jetpack Compose<br>Backend: PHP, Laravel, MySQL<br>AI: Python, OpenCV<br>Design: Figma`;
                    } else if(cmd === 'clear') {
                        terminalOutput.innerHTML = '';
                        response.innerHTML = '';
                    } else if(cmd === '') {
                        response.innerHTML = '';
                    } else {
                        response.innerHTML = `<span class="text-red-400">Command not found: ${cmd}</span>. Type 'help' for available commands.`;
                    }
                    
                    if(response.innerHTML) terminalOutput.appendChild(response);
                    terminalBody.scrollTop = terminalBody.scrollHeight;
                }
            });"""

# Because indentation might not be exact, I'll use regex or substring index to replace it.
start_idx = html.find("terminalInput.addEventListener('keydown', function(e) {")
end_idx = html.find("        }", start_idx) + 9

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + new_logic + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Terminal logic replaced successfully.")
else:
    print("Could not find the target code to replace.")
