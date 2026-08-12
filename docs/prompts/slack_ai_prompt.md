# Slack AI System Prompt

## System Prompt

Convert meeting notes into clear, GitHub-ready task checklist items.

Follow these rules:

1. Include only tasks that require someone to take action.
2. Ignore general conversation, greetings, jokes, status updates, and other non-actionable information.
3. Include a task only when the person responsible for it is clearly identified.
4. Write the assignee using their GitHub handle beginning with `@`.
5. Use exactly this format for every task:

`- [ ] @username Task description`

6. Put one task on each line.
7. Do not add headings, explanations, introductions, summaries, comments, or other conversational text to the output.
8. If a task does not have a clear owner, leave it out.
9. Do not guess an assignee or GitHub username.
10. Return only the Markdown checklist items.

## Test Payload A — Structured Notes

### Input

* @Bashir3355 will update the README documentation.
* @MrOliverW will review the Slack automation workflow.
* The team discussed next week's meeting.
* @Alex will test the GitHub integration.
* Everyone thanked the team for their work.

### Expected Output

* [ ] @Bashir3355 Update the README documentation
* [ ] @MrOliverW Review the Slack automation workflow
* [ ] @Alex Test the GitHub integration

## Test Payload B — Chaotic Notes

### Input

We started the meeting talking about the weather and everyone joked about how much coffee they needed. @Bashir3355 said he would update the project documentation before the next meeting. @MrOliverW mentioned that the Slack workflow is looking better and gave a status update about last week's work. Someone suggested improving the testing process, but nobody was assigned to it. Later, @MrOliverW agreed to review the AI prompt. The team talked about lunch for a few minutes. Before the meeting ended, @Alex said she would test the GitHub integration.

### Expected Output

* [ ] @Bashir3355 Update the project documentation before the next meeting
* [ ] @MrOliverW Review the AI prompt
* [ ] @Alex Test the GitHub integration

## Validation Results

Both test payloads were tested using the System Prompt.

### Payload A Result

* [ ] @Bashir3355 Update the README documentation
* [ ] @MrOliverW Review the Slack automation workflow
* [ ] @Alex Test the GitHub integration

**Result:** Passed

### Payload B Result

* [ ] @Bashir3355 Update the project documentation before the next meeting
* [ ] @MrOliverW Review the AI prompt
* [ ] @Alex Test the GitHub integration

**Result:** Passed

## Validation Summary

Both tests passed. The outputs contain only actionable tasks with clearly identified owners and follow the required `- [ ] @username Task description` format. Unassigned tasks and unrelated conversation were excluded.
