## Categories
- file system

## Query
write "hello world" to help.txt  

## Query code
```
write(
    value="hello world",
    to="help.txt",
)
```

## Thoughts
Agent needs to parse string "help.txt" to find that is matches patter of Filename concept.  
And so agent will call a function that writes a value to a file.  
This query implies that agent should append "hello world" to the file in case it exists.  
Also agent should add newline before printing if the file does not end with it already.  
This is something that needs to be generalised, but to generalise this agent also needs content of the file to see
if it ends with '\n' or not and agent needs to know did the file exist when function was called.  
So generalisation process depends on a set of function realisations with context.  
Functions themselves are not enough.  Hierarchical