import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

js_logic = """
        // 12. SECRET CONSOLE MESSAGE
        setTimeout(() => {
            console.log(
                "%c< FN />\\n%cLooking under the hood?\\nI see you're a developer of culture. You found the secret console.\\n\\n%c Let's talk: farrelariq3@gmail.com ",
                "font-size: 45px; font-family: monospace; font-weight: bold; color: #f97316; text-shadow: 2px 2px 0px #7c3aed, 4px 4px 0px #4c1d95;",
                "font-size: 14px; font-family: sans-serif; color: #cbd5e1; line-height: 1.8;",
                "font-size: 14px; font-family: monospace; font-weight: bold; color: #39FF14; background-color: #064e3b; padding: 6px 12px; border-radius: 4px;"
            );
        }, 2000);
"""

if 'SECRET CONSOLE MESSAGE' not in html:
    html = html.replace('</body>', js_logic + '</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Secret console message injected successfully.")
else:
    print("Secret console message already exists.")
