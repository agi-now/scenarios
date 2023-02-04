## Categories
- file system

## Query
open help.co

## Query code
```
open(
    value="help.co",
)
```

## Thoughts
Agent will parse "help.co" and will find that it corresponds to website domain and file name.  
Agent needs to decide what is it - file or domain.  
Fallback will be to ask the user.  

Context is definetly very helpful in this situation, but what if agent doesn't have context.  
'.co' domains are not as frequent, but are valid nontheless.  
Agent can check if this file exists, if it does, then it's very like a refernce to that file.  

Such situations show why pattern recognition can't be fully done with traditional ML approaches (different types of NNs).  
Agent can incorporate custom actions when making decisions, and this can't be done with current ML algos.
