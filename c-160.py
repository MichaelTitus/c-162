from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("NOTEPAD")

name=""


open_image=ImageTk.PhotoImage(Image.open("openfile.png"))
close_image=ImageTk.PhotoImage(Image.open("close.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))

label_file_name=Label(root,text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.58,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)


def open_file():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name=os.path.basename(text_file)
    formattedname=name.split('.')[0]
    root.title(formattedname)
    text_file=open(name,'r')
    para=text_file.read()
    my_text.insert(END,para)
    text_file.close()
    
def close():
    root.destroy()
    
def save():
    input_name=input_file_name.get()
    file=open(input_name+".txt",'w')
    data=my_text.get(1.0,END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","success")
    


open_button=Button(root,image=open_image,text="Open File",command=open_file)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

close_button=Button(root,image=close_image,text="Close",command=close)
close_button.place(relx=0.09,rely=0.03,anchor=CENTER)

save_button=Button(root,image=save_image,text="Save",command=save)
save_button.place(relx=0.13,rely=0.03,anchor=CENTER)



root.mainloop()