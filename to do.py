import tkinter as tk
from tkinter import messagebox as mg

roof=tk.Tk()
roof.state("zoomed")
roof.title("To Do List")

label = tk.Label(
    roof,
    text="\"Small steps every day lead to big results.\n Start with one task and keep moving forward.\"",
    font=("Helvetica", 18, "bold"))
label.pack(pady=30)

task_input = tk.Entry(roof, width=40)
task_input.bind("<Return>", lambda event: add_task())
task_input.pack(pady=20)
task_input.focus()                                                                               
    



def add_task():
    task = task_input.get()
    if task == "":
        return

    task_row=tk.Frame(task_frame,width=5)

    def mark_change():
        c=task_label.cget("fg")
        if c=="dark red":
            task_label.config(fg="dark green")
        else:
            task_label.config(fg="dark red")
            
    def ask_user():
        res=mg.askyesno("confirmation","Do you want to remove this task")
        if res:
            task_row.pack_forget()    

        
    
    task_label = tk.Label(task_row, text=task, font=("Arial", 14,"normal"),fg="dark red")
    task_label.pack(side="left", fill="x", expand=True)

    mark_button=tk.Button(task_row,text="✅",fg="green",command=mark_change)
    mark_button.pack(side="left")

    
            
    
    
    close_button=tk.Button(task_row,text="X",bg="white",fg="red",font=("Arial",10, "bold"),anchor="w",command=ask_user)
    close_button.pack(side="right")
    
    
    task_row.pack(pady=10)

    task_input.delete(0, tk.END)
     

button = tk.Button(roof, text="Add Task ➕",fg="blue",font=("Arial", 10, "bold"), command=add_task)
button.pack()


task_frame = tk.Frame(roof, width=960, height=540)
task_frame.pack()


roof.mainloop()




