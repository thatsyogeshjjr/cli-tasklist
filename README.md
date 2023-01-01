# CLI tasklist
created in python
This is a todo list, designed to be used in a terminal.

#### How to use:

    python ./app.py [command]

#### Commands:
[nothing\]: displays the list
add [task value]  : adds the [task value] to the list
did [taskid]      : marks the task complete
undid [taskid]    : marks the task uncomplete
flush             : clears the entire list
del [taskid]      : deletes the task mentioned 
 
**TaskID**: Index of the task selected.(count from zero) [int]

### How this works:
We use sys to get the command line argument, and standard python file operations to store, add, and delete date from a txt file (log.txt).
