import tkinter as tk


root = tk.Tk()
root.title("Люблю Python!")
root.geometry("300x200")  


root.configure(bg='lightblue')

label = tk.Label(root, text="Я люблю Python!", font=("Helvetica", 24, "bold"), bg='lightblue', fg='darkblue')
label.pack(expand=True)  

root.mainloop()

