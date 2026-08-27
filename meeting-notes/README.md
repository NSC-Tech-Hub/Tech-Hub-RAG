# meeting-notes/

This directory is the inbound target path for automated meeting-notes commits.

Files here are created by the Slack → Zapier/Make automation pipeline (see issues #1, #2, #4).
Each file corresponds to one processed meeting, containing a clean Markdown task checklist in the format:

- [ ] @username Task description

Do not manually edit files in this directory — they are overwritten/appended by the automation pipeline.
