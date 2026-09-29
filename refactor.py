import os
import json
import glob
import re

json_files = glob.glob('data/stories/*.json')
db = {}
for f in json_files:
    if os.path.basename(f) == 'index.json':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        story_id = os.path.basename(f).replace('.json', '')
        db[story_id] = data

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const STORY_DB = ' + json.dumps(db, indent=2) + ';\n')

with open('insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

if '<script src="data.js"></script>' not in html:
    html = html.replace('<script>', '<script src="data.js"></script>\n    <script>')

old_fetch_logic = """        async function openStoryReader(storyId) {
            let story;
            try {
                const res = await fetch("data/stories/" + storyId + ".json");
                if (!res.ok) throw new Error("Not found");
                story = await res.json();
            } catch(e) {
                console.error("Failed to lazy load story", e);
                return;
            }"""

new_fetch_logic = """        async function openStoryReader(storyId) {
            let story = STORY_DB[storyId];
            if (!story) {
                console.error("Failed to lazy load story: Not found in STORY_DB");
                return;
            }"""

if old_fetch_logic in html:
    html = html.replace(old_fetch_logic, new_fetch_logic)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(html)
