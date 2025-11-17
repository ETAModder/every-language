import json
import os

with open("languages.json","r",encoding="utf-8") as f:
    data=json.load(f)

exts=set()
for lang in data:
    for e in lang.get("extensions",[]):
        exts.add(e.lstrip("."))

for e in exts:
    open(f"file.{e}","w").close()