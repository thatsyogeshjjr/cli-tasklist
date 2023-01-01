#!/Users/shekh/AppData/Local/Programs/Python/Python310/python.exe
import sys # to get command line parameters
import os

if os.path.exists('log.txt'):
    read_tasks = open('log.txt','r')

def add_task(task):
    with open('log.txt','a') as task_list:
        task_list.write("[ ]\t"+task+"\n")

def complete_task(taskid: int):
    data = open('log.txt','r').readlines()
    # print(data)
    #    if '[*]' in data[taskid]:
    #        print("[~] Task already completed.")
    # else:
    data[taskid] = data[taskid].replace("[ ]","[*]")
    with open('log.txt','w') as task_list:
        task_list.writelines(data)
        task_list.close()

def uncomplete_task(taskid: int):

    data = open('log.txt','r').readlines()
    data[taskid] = data[taskid].replace("[*]","[ ]")
    with open('log.txt','w') as task_list:
        task_list.writelines(data)

def check_arg():
    #    print(sys.argv[2])
    if int(sys.argv[2])-1 > len(open('log.txt','r').readlines()):
        print("[-] Task ID is greater than the list size")
        print("[~] Remember to count from zero.")
        exit()

def clear_data():
    confirm = input("Do you really want to clear all of the list? [Y/N]: ")
    if confirm.lower() == 'n':
        exit()
    file = open('log.txt','w')
    file.writelines('')

def delete_tast(itemid:int):
    data = open('log.txt','r').readlines()
    del data[itemid]
    open('log.txt','w').writelines(data)

def display_help():
    print('''
    ===============================================================
    =               Displaying help for task-list                 =
    ===============================================================
    = Commands:                                                   =
    = add [task value]  : adds the [task value] to the list       =
    = did [taskid]      : marks the task complete                 =
    = undid [taskid]    : marks the task uncomplete               =
    = flush             : clears the entire list                  =
    = del [taskid]      : deletes the task mentioned              =
    =                                                             =
    = TaskID: Index of the task selected.(count from zero) [int]  =
    ===============================================================
    ''')

def main():
    title = "Task List"
    if len(open('log.txt','r').readlines()) == 0:
        longest_str = len(title)+4
    else:
        longest_str = len(max(open('log.txt','r').readlines(), key=len)) + 4

    # print("longest string: ",longest_str)
    # len(title)
    longest_str+=4
    x = int(round((longest_str-len(title)-4)/2)+2)
    print("="*longest_str+"=")
    printing_str = "="+" "*x + title+" "*x +"="

    if len(printing_str) != longest_str:
        y=x-1
        print("="+" "*y + title+" "*x +"=")
    else:
        print(printing_str)

    print("="*longest_str+"=")
    with open('log.txt','r') as tasks:
        txt = read_tasks.readlines()
    index = 0
    for i in txt:
        x = longest_str-len(i)-7
        i = i.replace("\n","")
        #index_str = "\t("+index+")"
        i = i.replace("\t","\t("+str(index)+")")
        print("= "+i+" "*x+" =")
        index+=1

    print("="*longest_str+"=")






if len(sys.argv) == 1:
    main()
# TODO: Add try-catch block to show error if sys.argv[2] is absent

else: 
    param = sys.argv[1]
    match param:
        case 'add':
            add_task(sys.argv[2])
        case 'did':
            check_arg()
            complete_task(int(sys.argv[2]))
            #print("params :",sys.argv))
        case 'undid':
            check_arg()
            uncomplete_task(int(sys.argv[2]))
        case 'flush':
            clear_data()
        case 'del':
            check_arg()
            delete_tast(int(sys.argv[2]))
        case 'help':
            display_help()



