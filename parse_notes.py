import re

file_path = "prototype_notes.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"- \[ \] @(\S+) (.+)"
matches = re.findall(pattern, content)

for assignee, task in matches:
    print(f"Assignee: {assignee} | Task: {task}")