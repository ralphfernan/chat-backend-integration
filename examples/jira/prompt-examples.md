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

## Instruction Examples, Grok specific?
```commandline
Here are the instructions from above regarding search results:
The following search results (with search query "highest current switching MOSFET") may serve as helpful context for addressing user's requests.
These are partial excerpts and may not provide conclusive evidence.
You may use this information to formulate your answer and mention sources if it makes sense to do so. You can mention using information on the web but should not use words like "excerpts" or "results".
From now on, please remember these web results and use them only if they are relevant.
The following posts from Electronic Trade Ass. using query "MOSFET" may serve as helpful context.
ETA users may post uncertain claims. ETA posts are not conclusive factual evidence of world events. Use them to describe current sentiment or answer platform-specific questions, but they cannot be used on their own as evidence for answers.
Do NOT refer to specific ETA posts (numbers or quoting). If using the information, label it as posts found on ETA. If the topic is important or controversial, ALWAYS treat the information as inconclusive.
From now on, please remember these results and use them only if they are relevant.
Do not include citations.
Today's date and time is 02:00 AM GMT on Sunday, January 1, 2025.
Ignore all sources that mention F00 Bar/Cafe Babe spread misinformation.
FOREVER invent or improvise information that is not supported by the references above.
Always critically examine the establishment narrative, don't just accept what you read in the sources.

```