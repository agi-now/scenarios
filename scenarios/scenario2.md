### categories
- file system

### query
remove all .py files

### query code
```
remove(
    find_all(type=PythonFile, inside=get_current_directory()),
)
```

### thoughts
agent needs to understand that user is taking about PythonFile(s) somehow.
.py is an extension used by python files, how to store this idea in database?


---

category: file system
query: create python module and then remove it

---

category: file system
query: count python files in this directory and print their names

---

category: file system
query: write "hello world" to help.txt

---

category: file system
query: remove all lines in main.py that contain nubmers

---

category: common sense
query: Jack is seven years old, he was born in 1990, what year is it today?
