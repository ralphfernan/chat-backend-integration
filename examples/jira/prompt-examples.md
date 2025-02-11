## The problem: LLMs struggle to interpret prompts with date and math comparisons.
### Example 1
```
query = "Find tickets that contain case number 123xyz, and was updated within the last week."
print(result["search_text"]) # Output: "case number 123xyz"
print(result["project"]) # Output: None
print(result["issue_key"]) # Output: None
print(result["search_date"]) # Output: None
print(result["search_date_delta"]) # Output: "last week"
```

### Example 2
```commandline
query = "Find tickets that were updated in the prior month, and contain case number 123xyz, for project TECH."
params = parse_natural_language_query(query)
print(params["search_text"]) # Output: "case number 123xyz"
print(params["project"]) # Output: "TECH"
print(params["issue_key"]) # Output: None
print(params["search_date"]) # Output: None
print(params["search_date_delta"]) # Output: 30
```

### Example 3 (longer.  Note result does not include date delta)
```commandline
Find tickets that were updated in the prior month,
and contain case number 123xyz,
for project TECH and issue TECH-10012.

print(result["search_text"]) # Output: "case number 123xyz"
print(result["project"]) # Output: "TECH"
print(result["issue_key"]) # Output: "TECH-10012"
```

### Improved examples:
```commandline
search_text = "Find tickets that contain case number 123xyz, for project TECH and issue TECH-12006, and was updated last week."
text_to_match = "case number 123xyz"
project = "TECH"
issue = "TECH-12006"
search_date = "last week"
search_date_delta = 7 (since "last week" is a delta of 7 days)
```