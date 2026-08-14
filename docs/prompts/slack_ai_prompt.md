# Slack AI System Prompt

## System Prompt

Convert meeting notes into GitHub-ready task items.

Follow these rules:

1. Include only clear, actionable tasks.
2. Ignore greetings, jokes, general discussion, status updates, and other information that does not require action.
3. Include a task only when the person responsible for it is clearly identified.
4. Use the assignee's GitHub handle beginning with `@`.
5. Format every task exactly like this:

`- [ ] @username Task description`

6. Put one task on each line.
7. Do not include introductions, headings, explanations, summaries, comments, or other conversational text in the output.
8. Leave out any task that does not have a clear owner.
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

- [ ] @Bashir3355 Update the README documentation
- [ ] @MrOliverW Review the Slack automation workflow
- [ ] @Alex Test the GitHub integration

## Test Payload B — Chaotic Notes

### Input

The meeting started with a quick conversation about the weather and a few jokes about coffee. @Bashir3355 said he would update the project documentation before the next meeting. @MrOliverW gave an update on the Slack workflow and said it was looking better. Someone suggested improving the testing process, but no one was assigned to do it. Later, @MrOliverW agreed to review the AI prompt. The team also talked about lunch. Before the meeting ended, @Alex said she would test the GitHub integration.

### Expected Output

- [ ] @Bashir3355 Update the project documentation before the next meeting
- [ ] @MrOliverW Review the AI prompt
- [ ] @Alex Test the GitHub integration

## Validation Results

The system prompt was tested with both sample payloads.

### Payload A Result

- [ ] @Bashir3355 Update the README documentation
- [ ] @MrOliverW Review the Slack automation workflow
- [ ] @Alex Test the GitHub integration

**Result:** Passed

### Payload B Result

- [ ] @Bashir3355 Update the project documentation before the next meeting
- [ ] @MrOliverW Review the AI prompt
- [ ] @Alex Test the GitHub integration

**Result:** Passed

## Validation Summary

Both test cases passed. Only actionable tasks with clear owners were included. General conversation, status updates, and unassigned tasks were left out. Every returned task follows the required `- [ ] @username Task description` format.
