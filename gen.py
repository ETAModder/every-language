import json
import os

with open("languages.json","r",encoding="utf-8") as f:
    data=json.load(f)

os.makedirs("files",exist_ok=True)

exts=set()
for lang in data:
    for e in lang.get("extensions",[]):
        exts.add(e.lstrip("."))

for e in exts:
    open(os.path.join("files",f"file.{e}"),"w").close()