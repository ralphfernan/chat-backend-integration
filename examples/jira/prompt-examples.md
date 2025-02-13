# Examples of LLM Outputs
## The problem: LLMs do not properly interpret prompts with date and math comparisons.
### Example 1
```
prompt = "Find tickets that contain case number 123xyz, and was updated within the last week."
result["search_text"] # Output: "case number 123xyz"
result["project"] # Output: None
result["issue_key"] # Output: None
result["search_date"] # Output: None
result["search_date_delta"] # Output: "last week"
```

### Example 2
```commandline
query = "Find tickets that were updated in the prior month, and contain case number 123xyz, for project TECH."
params = parse_natural_language_query(query)
params["search_text"] # Output: "case number 123xyz"
params["project"] # Output: "TECH"
params["issue_key"] # Output: None
params["search_date"] # Output: None
params["search_date_delta"] # Output: 30
```

### Example 3 (longer.  Note result does not include date delta)
```commandline
Find tickets that were updated in the prior month,
and contain case number 123xyz,
for project TECH and issue TECH-10012.

result["search_text"] # Output: "case number 123xyz"
result["project"] # Output: "TECH"
result["issue_key"] # Output: "TECH-10012"
```

### Improved examples showing the LLM output:
```commandline
search_text = "Find tickets that contain case number 123xyz, for project TECH and issue TECH-12006, and was updated last week."
text_to_match = "case number 123xyz"
project = "TECH"
issue = "TECH-12006"
search_date = "last week"
search_date_delta = 7 (since "last week" is a delta of 7 days)
```
```commandline
Search Text: What is the status of cases that contain case number 123xyz, for project TECH and issue TECH-12006, and was updated on 01-20-2025.
Text to Match: 123xyz
Filenames to Match: None
Project: TECH
Issue: TECH-12006
Search Date: (2025, 1, 20)
Search Date Delta: None
```
### This example outputs a sign to indicate the date-delta is to be subtracted.
```commandline
Search Text: What is the status of cases that contain case number 123xyz, for project TECH and issue TECH-12006, and was updated last month.
Text to Match: case number 123xyz
Filenames to Match: None
Project: TECH
Issue: TECH-12006
Search Date: Last Month
Search Date Delta: -30 days
```


```commandline
1. Extract the name of the entity in the conversation.
2. Analyze the sentiment of the conversation.
3. Summarize the conversation.  The summary includes the above 2 analyses.
```

### System Prompt
```commandline
You are an AI assistant that answers user's questions.
Answer ONLY based on the provided documentation.
If the answer is not in the documentation, say "I don't know".
```