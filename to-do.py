#project_Todo list

class Todo_list:#declaing a class
    def __init__(self):
        self.tasks=[] #initializing a empty list to do tasks
    def add(self,task):
        #adding the task to the list
        self.tasks.append(task)
        print(f"the {task} added successfully to the Todo list")

    def remove(self,task):
        #removing the task from the todo list    
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"The {task} removed successfully from the Todo list")
        else:
            print(f"the {task} is not in the Todo list")

    def view(self):
        #viewing the task in the todo list
        if not self.tasks:
            print("your Todo list is empty!!")
        else:
            print("your Todo list is:")
            for index,task in enumerate(self.tasks,start=1):
                print(f"{index}:{task}")

#defining the main function
def main():
    todo=Todo_list()
    Name=input("enter your name:")       
    print(f"hello {Name} ,welcome to the Todo list app!!") 
    
    while True:
        #declaring the menu of the task that can do
        print("The following tasks you can perform are:")
        print("1.adding")
        print("2.deleting")
        print("3.viewing")
        print("4.Exit")

        #getting the choice of the user
        choice=int(input("enter the choice to perform the task (1-4):"))
        if choice==1:
            task=input("enter the task to add to Todo list:")
            todo.add(task)
        elif choice==2:
            task=input("enter the task to delete from the Todo list:")
            todo.remove(task)
        elif choice==3:
            todo.view()
        elif choice==4:
            print("Exiting from the Todo list,Thanks for using!!")
            break
        else:
            print("it is an invalid choice!,please enter the correct choice from the menu!!")

#calling the main function
if __name__=="__main__":
    main()


