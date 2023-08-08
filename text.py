import tkinter

def gettext():
    print(text.get("1.0","end"))

def inserttext():
    text.insert("1.0","hii")

def deletetext():
    text.delete("1.0","1.1")

window=tkinter.Tk()
window.title("Text")
window.geometry('500x500')
text=tkinter.Text(window,width=40,height=10,font=("Arial",20))
button_get=tkinter.Button(window,text="Get text",command=gettext)
button_insert=tkinter.Button(window,text="Insert text",command=inserttext)
button_delete=tkinter.Button(window,text="Delete text",command=deletetext)
text.pack()
button_get.pack()
button_insert.pack()
button_delete.pack()
window.mainloop()