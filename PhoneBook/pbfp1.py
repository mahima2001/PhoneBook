try:
    from Tkinter import*
except:
    from tkinter import*
root1=Tk()
root1.geometry("1000x600")
Label(root1,text="Project Title: PHONEBOOK",font="times 25 bold").grid(row=0,column=0,sticky=E)
Label(root1,text="Project of Python and Database",font="times 18 bold").grid(row=1,column=1,sticky=W)
Label(root1,text="Developed by:Mahima Pandey(181B116)",font="times 18 bold",fg="Blue").grid(row=2,column=1)
Label(root1,text="--------------------------------------------------------",fg="Blue").grid(row=3,column=1)
Label(root1,text="Make mouse movement over this screen to close",font="times 12 bold",fg="Red").grid(row=4,column=1,sticky=W)
def close(e=1):
    root1.destroy()
root1.bind('<Motion>',close)
root1.mainloop()
