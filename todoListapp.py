import tkinter 
from tkinter import *

root=Tk() # Root là cứa sổ của tkinter trong Python
root.title("To-Do-List")
root.geometry("400x650+400+400")
root.resizable(False, False) #=>thay đổi kích thước theo chiều ngang và dọc hay không?

task_list= []
 
def addTask():
   task = task_entry.get()
   task_entry.delete(0, END)

   if task:
      with open("tasklist.txt",'a') as taskfile:
         taskfile.write(f"\n{task}")
      task_list.append(task)
      listbox.insert(END, task)


def deltask():
     global task_list
     task= str(listbox.get(ANCHOR))
     if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
           for task in task_list:
              taskfile.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():
  
 try:  
    global task_list 
    with open("tasklist.txt","r") as taskfile: # Mở tệp văn bản để đọc
        tasks= taskfile.readlines()   # Đọc tất cả các dòng từ tệp
    
    
    for task in tasks: 
        if task != "\n":
            task_list.append(task)
            listbox.insert(END, task)

 except: 
    file=open("tasklist.txt", "w")  
    file.close()
            
#heading:

heading=Label(root,text="All Task", font="arial 20 bold", fg="white", bg="black")
heading.place(x=130, y=20)

#main:
frame= Frame(root, width=400, height=50, bg="grey")
frame.place(x=0, y=180)

task= StringVar() #=> lưu trữ dữ liệu giá trị của một chuổi trong biến task
task_entry= Entry(frame, width= 16, font="arial 20", bd=0)  #=> tạo ra con trỏ điền thông tin vào
task_entry.place(x=10, y =10)  
task_entry.focus() #=> tự động nhập dữ liệu người dùng mà không cần bấm chuột vô


button= Button(frame, text="ADD", font=" arial 20 bold", width=6, bg="black", fg="white", command=addTask)
button.place(x= 300, y = 0 )

#listbox:
frame1= Frame(root, bd=3, width=700, height= 280, bg="black")
frame1.pack(pady= (160,0)) #=> đặt khoảng cách dọc giữ widget và widget trên nó với một khoảng là 160px
# và không có khoảng dọc.
frame1.place(x=2, y = 300)
listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="black", fg="white",
                   cursor="hand2", selectbackground= "grey"  )
listbox.pack(side=LEFT, fill=BOTH,padx=2  )
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=  scrollbar.set ) #=> đặt cấu hình là thanh cuộn dọc liên két với listbox
scrollbar.config(command=listbox.yview)

openTaskFile()
#delete
Delete_button = Button(root, text="Delete" , font=" arial 10 bold", width=6, bg="black", fg="white", command=deltask  )
Delete_button.pack(side=BOTTOM, pady=5 )

root.mainloop()



