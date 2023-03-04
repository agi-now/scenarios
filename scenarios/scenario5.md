## Categories
- file system

## Query
create help.txt  

## Query code
```python
create("help.txt")
```

## Steps

### Input Observation
for every input the agent calls
```python
observe(value="help.txt")
```

The agent does pattern matching and phonetic associations.  
There may be multiple patterns that will match this string on its own but with outside context the agent will be able to understand that this is a file name.  
Also `".txt"` is a lot more associated with `FileName` and `File` concepts than with anything else.  

### Function Resolution
The agent is looking for tasks that are associated with word `"create"` and concepts `FileName`, `File`, `TextFile`.  
There will likely be multiple functions that match, somehow we need to select one.  
In case of an error we will be able to select the next one, although it's not quite clear what is an indication of an error.

### Interpreter
The agent selected the function to execute and starts executing it.  
For example function may be something like this:  
```python
def function1234(filename: FileName):
  execute('touch ' + filename.value)
```

This code might have been provided by a user and it doesn't have proper escaping.  
It's not a problem if it works but if there is a problem, then user should explain that filename should be escaped.  

