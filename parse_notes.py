import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(description="Extract tasks from meeting notes.")
parser.add_argument("notes_file", nargs="?", default="prototype_notes.md", type=Path)
args = parser.parse_args()

content = args.notes_file.read_text(encoding="utf-8-sig")
pattern = r"- \[ \] @(\S+) (.+)"

for assignee, task in re.findall(pattern, content):
    print(f"Assignee: {assignee} | Task: {task}")