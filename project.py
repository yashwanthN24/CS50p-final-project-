import sys
import os
import time
class Node :
    def __init__(self , data):
        self.data = data
        self.status = 'P'
        self.link = None

def main():
    first = None
    while True :
        print("***************************************")
        print("1.Add Task")
        print("2.Remove Task")
        print("3.View All pending Tasks")
        print("4.View All completed Tasks")
        print("5.View All Tasks in the To do List")
        print("6.Mark Task as Completed")
        print("Press 0 to exit")
        while True :
            try :
                choice=int(input("Choice:"))
                if choice >= 0 :
                    break
            except ValueError :
                pass
        match(choice):
            case 1 :
                while True :
                    Task = input("Enter the task you want to add:")
                    if Task:
                        break
                first = inserttask(Task, first)

            case 2:
                while True :
                    Task = input("Enter the task You want to delete:")
                    if Task:
                        break
                first = deletetask(Task , first)

            case 3:
                PendingTasks = viewAllPendingTasks(first)
                if PendingTasks:
                    for Task in PendingTasks:
                        print(Task.strip())
                print("--------")
                time.sleep(5)

            case 4:
                CompletedTasks = viewAllCompletedTasks(first)
                if CompletedTasks:
                    for Task in CompletedTasks:
                        print(Task.strip())
                print("--------")
                time.sleep(5)

            case 5:
                Tasks= viewAllTasks(first)
                if Tasks:
                    for Task in Tasks:
                        print(Task.strip())
                time.sleep(5)
            case 6:
                while True :
                    Task = input("Enter the task you want to mark as complete:")
                    if Task:
                        break
                first = marktaskcompleted(Task , first)

            case _ :
                if choice == 0:
                    while True :
                        while True :
                            confirm = input("Do you want to really exit?\n(Yes)/(y) or (No)/(n) :")
                            if confirm:
                                break
                        if confirm.lower() in ["yes"  , "y", "no" , "n"]:
                            break
                    if confirm.lower() in ['yes' , 'y']:
                        print("\nThank You :) !!")
                        break
                if choice >=7 :
                    print("\nInvalid Choice\nProgram Exiting\nThank You :)!!")
                    break
        time.sleep(1)
        os.system('clear')

def inserttask(Task , first):
    temp = Node(Task)
    if first is None :
        return temp
    temp.link = first
    return temp


def deletetask(Task , first):
    if first is None :
        print("No Task present in the To Do list")
        return first
    cur = first
    prev = None
    while cur is not None :
        if cur.data.lower() == Task.lower().strip() and cur == first:
            first = cur.link
            return first
        elif cur.data.lower() == Task.lower().strip():
            prev.link = cur.link
            return first
        prev = cur
        cur = cur.link
    print("Task not Found Check out for a typo ")
    return first

def viewAllTasks(first):
    if first is None :
        print("List is empty!! No Tasks")
        return
    cur = first
    no = 1
    li = []
    while cur is not None:
        li.append(f"{no}.{cur.data} | Status : {cur.status}")
        cur = cur.link
        no+=1
    return li

def viewAllPendingTasks(first):
    if first is None :
        print("List is empty!! No Tasks")
        return
    cur = first
    no = 1
    li = []
    while cur is not None:
        if cur.status == 'P':
            li.append(f"{no}.{cur.data}")
            no+=1
        cur = cur.link
    return li



def viewAllCompletedTasks(first):
    if first is None :
        print("List is empty!! No Tasks")
        return
    cur = first
    no = 1
    li = []
    while cur is not None:
        if cur.status == 'C':
            li.append(f"{no}.{cur.data}")
            no+=1
        cur = cur.link
    return li


def marktaskcompleted(Task , first):
    if first is None :
        print("No Tasks in list. Add them")
        return first
    cur = first
    while cur is not None :
        if cur.data.lower() == Task.lower().strip():
            cur.status = 'C'
            return first
        cur = cur.link
    print("Task not found check out for typos")
    return first


if __name__ == "__main__":
    main()

