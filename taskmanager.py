# main Function
def main():
  message="""1- Add Task To a List
2- Mark Task As Completed
3- View Tasks
4- Quit\n"""
  global tasks
  tasks=[]
  while True:
   print (message)
   choice=input("Enter Your Choice : ")
   if choice == "1":
    add_tasks()
   elif choice == "2":
    mark_task_completed()  
   elif choice == "3":
    view_tasks()
   elif choice=="4":
    break
   else:
    print("Please Enter Number From 1 To 4")

# Function To add a task
def add_tasks():
  # take the task  Fro the user
  task=input("Enter Your Task : ")
  # define task status
  task_info={"task":task,"completed":False}
  # add  the task to the list
  tasks.append(task_info)
  print("task added successfully to the list...")

# Function to mark task completed
def mark_task_completed():
  # get incompleted task
  incompleted_tasks=[task for task in tasks if task["completed"]==False]
  # if there is tasks to mark, print message and return
  if len(incompleted_tasks)==0:
    print("No Tasks To Mark As Completed...") 
    return
  # show incompleted to the user
  for i,task in enumerate(incompleted_tasks):
    print(f"{i+1}- {task['task']}")
    print("-"*40)
  # get the task from the user
  task_number=int(input("Choose the task to complete : "))
  # mark the task as completed
  incompleted_tasks[task_number-1]["completed"]=True
  # print a message to the user  
  print("Your Task mark Completed ")  

# Function To Viwe Tasks
def view_tasks():
  # if there is no tasks to viwe, print message an return 
  if len(tasks)==0:
    print("There is No Tasks To Viwe..")
    return 
  # if there is tasks to viwe
  else:
    for i,task in enumerate(tasks):
      status="✅" if task["completed"] else "❎"
      print(f"{i+1}. {task['task']} {status}")

main()
  
