from pbfp1 import *
try:
    from Tkinter import*
except:
    from tkinter import*
try:
    from tkMessageBox import *
except:
    import tkinter.messagebox
import re
root=Tk()
import sqlite3
#Made by Mahima Pandey(181B116)
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
root.title("Phonebook")
root.geometry("550x800")
root.config(background="gray35")
con=sqlite3.Connection('phonbook')
cur=con.cursor()
cur.execute("create table if not exists contac_det(ContactID INTEGER primary key AUTOINCREMENT,firstname varchar(30),lastname varchar(30),company varchar(30),address varchar(50),city varchar(20),pin number(6),websiteurl varchar(30),Birthdate date)")
cur.execute("create table if not exists mobile(cid INTEGER references contac_det(ContactID) on delete cascade,contacttype varchar(10),phonenumber INTEGER(10),primary key(cid,phonenumber))")
cur.execute("create table if not exists email(coid INTEGER references contac_det(ContactID) on delete cascade ,emailid_type varchar(10),eid varchar(30),primary key(coid,eid))")
img=PhotoImage(file="photo.gif")
Label(root,image=img,bg="gray35").grid(row=0,columnspan=2,sticky=E)
Label(root,text="PhoneBook",fg="navy",font="times 30 bold",bg="Hot Pink").grid(row=1,columnspan=2,sticky=E)
Label(root,text="First Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=2,column=0)
e1=Entry(root,bd=3)
e1.grid(row=2,column=1)
Label(root,text="Last Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=4,column=0)
e3=Entry(root,bd=3)
e3.grid(row=4,column=1)
Label(root,text="Company Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=5,column=0)
e4=Entry(root,bd=3)
e4.grid(row=5,column=1)
Label(root,text="Address",font="Comic 15",bg="gray35",fg="cyan").grid(row=6,column=0)
e5=Entry(root,bd=3)
e5.grid(row=6,column=1)
Label(root,text="City",font="Comic 15",bg="gray35",fg="cyan").grid(row=7,column=0)
e6=Entry(root,bd=3)
e6.grid(row=7,column=1)
Label(root,text="Pin Code",font="Comic 15",bg="gray35",fg="cyan").grid(row=8,column=0)
e7=Entry(root,bd=3)
e7.grid(row=8,column=1)
Label(root,text="Website URL",font="Comic 15",bg="gray35",fg="cyan").grid(row=9,column=0)
e8=Entry(root,bd=3)
e8.grid(row=9,column=1)
Label(root,text="Date of Birth(yyyy-mm-dd)",font="Comic 15",bg="gray35",fg="cyan").grid(row=10,column=0)
e9=Entry(root,bd=3)
e9.grid(row=10,column=1)
v1=IntVar()
v01=IntVar()
v2=IntVar()
v02=IntVar()

v7=IntVar()
Label(root,text="Select Phone Type:",fg="Blue",font="times 15",bg="Hot Pink").grid(row=11,column=0)
Radiobutton(root,text="Office",variable=v1,value=1,bg="light Pink",highlightcolor="maroon1").grid(row=11,column=1)
Radiobutton(root,text="Home",variable=v1,value=2,bg="light Pink",highlightcolor="maroon1").grid(row=11,column=2)
Radiobutton(root,text="Mobile",variable=v1,value=3,bg="light Pink",highlightcolor="maroon1").grid(row=11,column=3)
Label(root,text="Phone Number ",font="Comic 15",bg="gray35",fg="cyan").grid(row=12,column=0)
Label(root,text="(Without Dashes or brackets) ",font="Comic 13",bg="gray35",fg="DarkOrchid1").grid(row=13,column=0,sticky=W)
e10=Entry(root,bd=3)
e10.grid(row=12,column=1)
e2=Entry(root,bd=3)
e12=Entry(root,bd=3)

def insertp():
    showwarning('Warning','Do not save the same Contact Type as the previous One')
    Radiobutton(root,text="Office",variable=v01,value=41,bg="light Pink",highlightcolor="maroon1").grid(row=13,column=1)
    Radiobutton(root,text="Home",variable=v01,value=42,bg="light Pink",highlightcolor="maroon1").grid(row=13,column=2)
    Radiobutton(root,text="Mobile",variable=v01,value=43,bg="light Pink",highlightcolor="maroon1").grid(row=13,column=3)
    
    e2.grid(row=14,column=1)

Label(root,text="Select Email Type:",fg="Blue",font="times 15",bg="Hot Pink").grid(row=15,column=0)
Radiobutton(root,text="Office",variable=v2,value=4,bg="light Pink",highlightcolor="maroon1").grid(row=15,column=1)
Radiobutton(root,text="Personal",variable=v2,value=5,bg="light Pink",highlightcolor="maroon1").grid(row=15,column=2)
Label(root,text="Email id ",font="Comic 15",bg="gray35",fg="cyan").grid(row=16,column=0)
e11=Entry(root,bd=3)
e11.grid(row=16,column=1)

Button(root,text="+",command=insertp,bg="plum1").grid(row=12,column=2)
def inserte():
    showwarning('Warning','Do not save the same Email Type as the previous One')
    Radiobutton(root,text="Office",variable=v02,value=44,bg="light Pink",highlightcolor="maroon1").grid(row=17,column=1)
    Radiobutton(root,text="Personal",variable=v02,value=45,bg="light Pink",highlightcolor="maroon1").grid(row=17,column=2)
    
    e12.grid(row=18,column=1)
Button(root,text="+",command=inserte,bg="plum1").grid(row=16,column=2)
def phno():
    if v1.get()==1:
        jk="Office"
    elif v1.get()==2:
        jk="Home"
    elif v1.get()==3:
        jk="mobile"
    return jk
def phno1():
    if v01.get()==41:
        jjk="Office"
    elif v01.get()==42:
        jjk="Home"
    elif v01.get()==43:
        jjk="mobile"
    return jjk
def emid():
    
    if v2.get()==4:
        lk1="Office"
    elif v2.get()==5:
        lk1="Personal"
    return lk1
def emid1():
    if v02.get()==44:
        ljk="Office"
    elif v02.get()==45:
        ljk="Personal"
    return ljk
def save():
    j=phno()
    l=emid()
    dt=str(e9.get())
    gs=str(e10.get())
    gt=str(e10.get())
    em=str(e11.get())
    if(str(e1.get())=='' and str(e3.get())=='' ):
        showerror('Error','Please Enter contact name')
        return
    if(gt==''):
        showerror('Error','Please Enter contact number')
        return
    try:
        gs=int(gs)
    except ValueError:
        showerror('Error','Not a valid mobile number')
        return
    if len(gt)>15:
        showerror('Error','Not a valid mobile number')
        return
    if(str(e1.get())==str(e3.get())):
        showerror('Error','First name cannot be equal to last name')
        return
    if(dt!=''):
        cur.execute("SELECT cast(( julianday('now') - julianday(?))/365 As Integer) ",(dt,))
        hh=cur.fetchall()
        if(hh[0][0]!='None' and (hh[0][0]<18 or hh[0][0]>100 )):
            showerror('Error','The Date of Birth is invalid')
            return
    if(em==''):
        showerror('Error','Please Enter Email ID')
        return
    
    if (not(re.search(regex,em))):  
        showinfo('Error','Invalid Email')
        return
    a,b,c,d,e,f,g,h,i,kp=e1.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()
    cur.execute("insert into contac_det (firstname,lastname,company,address,city,pin,websiteurl,Birthdate)  values (?,?,?,?,?,?,?,?)",(a,b,c,d,e,f,g,h))
    cur.execute("Select ContactID from contac_det where firstname= ? and lastname= ?  and Birthdate=?",(a,b,h))
    lm=cur.fetchall()
    k=int(lm[0][0])
    if(e2.get()):
        hs=str(e2.get())
        ht=str(e2.get())
        if(ht==''):
            showerror('Error','Please Enter contact number')
            return
        try:
            hs=int(hs)
        except ValueError:
            showerror('Error','Not a valid mobile number')
            return
        if len(ht)!=10 :
            showerror('Error','Not a valid mobile number')
            return
        
        jkk=phno1()
        if(jkk==j):
            showerror('Error','Contact Type same as the previous one')
            return
        lll=e2.get()
        try:
            
            cur.execute("Insert into mobile values (?,?,?)",(k,j,i))
            cur.execute("Insert into mobile values (?,?,?)",(k,jkk,lll))
        except sqlite3.IntegrityError:
            showerror('Error','Same Phone Numbers')
            return
    else:
        cur.execute("Insert into mobile values (?,?,?)",(k,j,i))
    
    if(e12.get()):
        eml=str(e12.get())
        if(eml==''):
            showerror('Error','Please Enter Email ID')
            return
        if (not(re.search(regex,eml))):  
            showinfo('Error','Invalid Email')
            return
        jkm=emid1()
        if(jkm==l):
            showerror('Error','Email Type same as the previous one')
            return
        
        ljl=e12.get()
        try:
            cur.execute("Insert into email values (?,?,?)",(k,l,kp))
            cur.execute("Insert into email values (?,?,?)",(k,jkm,ljl))
        except sqlite3.IntegrityError:
            showerror('Error','Same EmailIds')
            return
    else:
        cur.execute("Insert into email values (?,?,?)",(k,l,kp))
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e4.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e10.delete(0,END)
    e9.delete(0,END)
    e11.delete(0,END)
    e12.delete(0,END)
    
    showinfo('save','Record Successfully Saved')
def close(e=1):
        root.destroy()

def search():
    root1=Tk()
    root1.geometry("480x600")
    root1.title("Search")
    root1.attributes("-topmost", True)
    root1.config(background="light sea green")
    Label(root1,text="Searching Phonebook",font="times 20 bold",bg="magenta3").grid(row=0,column=1,sticky=W);
    Label(root1,text="Enter Name:",bg="magenta3",relief=RAISED).grid(row=1,column=0,)
    et=Entry(root1,relief=SUNKEN)
    et.grid(row=1,column=1,sticky=W)
    lb=Listbox(root1,width=60,height=25,font="times 12 bold" ,fg='midnight Blue',bg="powder blue")
    lb.grid(row=2,column=0,columnspan=3)
    def close(e=1):
        root1.destroy()
    Button(root1,text="Close",command=close,bg="magenta3").grid(row=3,column=1)
    cur.execute("Select firstname,lastname from contac_det order by firstname")
    u= cur.fetchall()
    for il in u:
        lb.insert(END,il)
    
    def onselect(e=0):
        list_item=lb.curselection()
        if not list_item:
            return
        v=lb.get(list_item)
        #print v
        cur.execute("Select ContactId from contac_det where firstname=? and lastname=? order by firstname",(v[0],v[1]))
        xz=cur.fetchall()
        #print xz
        def delete():
            cur.execute("Delete from contac_det where ContactID=(?)",(xz[0][0],))
            con.commit()
            lb.delete(0,END)
            lb1.destroy()
            
            showinfo('Removed','Record Deleted from Phone Book')
      
        def back():
            et.delete(0,END)
            lb1.destroy()
        lb1=Listbox(root1,width=60,height=25,font="times 15 bold" ,fg='gray25',bg="LightSteelBlue1")
        lb1.grid(row=2,column=0,columnspan=3)
        Button(lb1,text="Delete",command=delete,bg="magenta3").place(x=270,y=500)
        Button(lb1,text="Back",command=back,bg="magenta3").place(x=130,y=500)
        lb.delete(0,END)
        cur.execute("Select * from contac_det inner join mobile on ContactID=cid inner join email on ContactID=coid and ContactID=(?)",(xz[0][0],))
        xx=cur.fetchall()
        lb1.insert(END,"First Name:"+xx[0][1])
        lb1.insert(END,"Last Name: "+xx[0][2])
        lb1.insert(END,"Company: "+xx[0][3])
        lb1.insert(END,"Address: "+xx[0][4])
        lb1.insert(END,"City: "+xx[0][5])
        lb1.insert(END,"Pincode: "+str(xx[0][6]))
        lb1.insert(END,"Website URL: "+xx[0][7])
        lb1.insert(END,"Date of Birth: "+xx[0][8])
        
        lb1.insert(END,"Phone Details..... ")
        lb1.insert(END,xx[0][10]+" : "+str(xx[0][11]))
        if(len(xx)==2and xx[0][11]!=xx[1][11]):
            lb1.insert(END,xx[1][10]+" : "+str(xx[1][11]))
        elif(len(xx)==4):
            lb1.insert(END,xx[3][10]+" : "+str(xx[3][11]))
        lb1.insert(END,"Email Addresses... ")
        lb1.insert(END,xx[0][13]+" : "+xx[0][14])
        if(len(xx)==2 and xx[0][14]!=xx[1][14]):
            lb1.insert(END,xx[1][13]+" : "+xx[1][14])
        elif(len(xx)==4):
            lb1.insert(END,xx[3][13]+" : "+xx[3][14])
            
       
            
        def edit():
            root2=Tk()
            root2.config(background="plum1")
            root2.geometry("500x550")
            root2.attributes("-topmost", True)
            
            Label(root2,text="First Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=2,column=0,sticky=W,columnspan=3)
            e21=Entry(root2,bd=3)
            e21.grid(row=2,column=3)
            e21.insert(END,xx[0][1])
            Label(root2,text="Last Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=4,column=0,sticky=W,columnspan=3)
            e23=Entry(root2,bd=3)
            e23.grid(row=4,column=3)
            e23.insert(END,xx[0][2])
            Label(root2,text="Company Name",font="Comic 15",bg="gray35",fg="cyan").grid(row=5,column=0,sticky=W,columnspan=3)
            e24=Entry(root2,bd=3)
            e24.grid(row=5,column=3)
            e24.insert(END,xx[0][3])
            Label(root2,text="Address",font="Comic 15",bg="gray35",fg="cyan").grid(row=6,column=0,sticky=W,columnspan=3)
            e25=Entry(root2,bd=3)
            e25.grid(row=6,column=3)
            e25.insert(END,xx[0][4])
            Label(root2,text="City",font="Comic 15",bg="gray35",fg="cyan").grid(row=7,column=0,sticky=W,columnspan=3)
            e26=Entry(root2,bd=3)
            e26.grid(row=7,column=3)
            e26.insert(END,xx[0][5])
            Label(root2,text="Pin Code",font="Comic 15",bg="gray35",fg="cyan").grid(row=8,column=0,sticky=W,columnspan=3)
            e27=Entry(root2,bd=3)
            e27.grid(row=8,column=3)
            e27.insert(END,xx[0][6])
            Label(root2,text="Website URL",font="Comic 15",bg="gray35",fg="cyan").grid(row=9,column=0,sticky=W,columnspan=3)
            e28=Entry(root2,bd=3)
            e28.grid(row=9,column=3)
            e28.insert(END,xx[0][7])
            Label(root2,text="Date of Birth",font="Comic 15",bg="gray35",fg="cyan").grid(row=10,column=0,sticky=W,columnspan=3)
            e29=Entry(root2,bd=3)
            e29.grid(row=10,column=3)
            e29.insert(END,xx[0][8])
            Label(root2,text="Phone Number "+"("+xx[0][10]+"): ",font="Comic 15",bg="gray35",fg="cyan").grid(row=12,column=0,sticky=W,columnspan=3)
            OptionList = ["Contact_Type","Office","Home","mobilele",]
            OptionList1 = ["Email_Type","Office","Personal"]
            e30=Entry(root2,bd=3)
            e30.grid(row=12,column=3)
            e30.insert(END,str(xx[0][11]))
            v= StringVar()
            v.set(OptionList[0])
            va= StringVar()
            va.set(OptionList1[0])
            e32=Entry(root2,bd=3)
            def ins():
                Label(root2,text="Do not save same contact type as the previous one",fg="Red").grid(row=14,column=0,columnspan=4)
                opt = OptionMenu(root2, v,*OptionList)
                opt.configure(width=10,font=('Times', 12),bg="purple1")
                opt.grid(row=13,column=0)
                e32.grid(row=13,column=3)
                Label(root2,text="(Select Contact Type)", font=('Helvetica', 12), fg='red').grid(row=13,column=1,columnspan=2)
            if(len(xx)==2 and xx[0][11]==xx[1][11]) or len(xx)==1:
                
                Button(root2,text="+",command=ins,bg="lavenderBlush").grid(row=12,column=4)
            elif(len(xx)==2 and xx[0][11]!=xx[1][11]):
                Label(root2,text=xx[1][10]+": ",font="Comic 15",bg="gray35",fg="cyan").grid(row=13,column=0,sticky=W,columnspan=3)
                e32.grid(row=13,column=3)
                e32.insert(END,xx[1][11])
            elif(len(xx)==4):
                Label(root2,text=xx[3][10]+": ",font="Comic 15",bg="gray35",fg="cyan").grid(row=13,column=0,sticky=W,columnspan=3)
                e32.grid(row=13,column=3)
                e32.insert(END,xx[3][11])
            Label(root2,text="Email id "+"("+xx[0][13]+"): ",font="Comic 15",bg="gray35",fg="cyan").grid(row=15,column=0,sticky=W,columnspan=3)
            e31=Entry(root2,bd=3)
            e31.grid(row=15,column=3)
            e31.insert(END,xx[0][14])
            e33=Entry(root2,bd=3)
            def inse():
                Label(root2,text="Do not save same email type as the previous one",fg="Red").grid(row=18,column=0,columnspan=4)
                opt1 = OptionMenu(root2, va,*OptionList1)
                opt1.config(width=10, font=('Helvetica', 12),fg="Black",bg="purple1")
                opt1.grid(row=17,column=0)
                e33.grid(row=17,column=3)
                Label(root2,text="(Email Type)", font=('Helvetica', 12), fg='red').grid(row=17,column=1,columnspan=2)
            if(len(xx)==2 and xx[0][14]==xx[1][14]) or len(xx)==1:
                Button(root2,text="+",command=inse,bg="lavenderBlush").grid(row=15,column=3,sticky=E)
                
            elif(len(xx)==2 and xx[0][14]!=xx[1][14]):
                Label(root2,text=xx[1][13]+": ",font="Comic 15",bg="gray35",fg="cyan").grid(row=16,column=0,sticky=W,columnspan=3)
                e33.grid(row=16,column=3)
                e33.insert(END,xx[1][14])
            elif(len(xx)==4):
                Label(root2,text=xx[3][13]+": ",font="Comic 15",bg="gray35",fg="cyan").grid(row=16,column=0,sticky=W,columnspan=3)
                e33.grid(row=16,column=3)
                e33.insert(END,xx[3][14])
            def closep(e=0):
                root2.destroy()
                lb1.destroy()
            def saveit():
                cfd=xz[0][0]
                aa=e21.get()
                cur.execute("Update  contac_det set firstname=? where ContactID= ? ",(aa,cfd))
                cur.execute("Update contac_det set lastname=? where ContactID= ? ",(e23.get(),cfd))
                cur.execute("Update contac_det set company=? where ContactID= ? ",(e24.get(),cfd))
                cur.execute("Update contac_det set address=? where ContactID= ? ",(e25.get(),cfd))
                cur.execute("Update contac_det set city=? where ContactID= ? ",(e26.get(),cfd))
                cur.execute("Update contac_det set pin=? where ContactID= ? ",(e27.get(),cfd))
                cur.execute("Update contac_det set websiteurl=? where ContactID= ? ",(e28.get(),cfd))
                cur.execute("Update contac_det set Birthdate=? where ContactID= ? ",(e29.get(),cfd))
                try:
                    tt=str(e30.get())
                    ts=str(e30.get())
                    es=str(e31.get())
                    try:
                        ts=int(ts)
                    except ValueError:
                        showerror('Error','Not a valid mobile number')
                        return
                    if len(tt)>15 :
                        showerror('Error','Not a valid mobile number')
                        return
                    if (not(re.search(regex,es))):  
                        showinfo('Error','Invalid Email')
                        return
                    if (e32.get()):
                        dd=str(e32.get())
                        ds=str(e32.get())
                        
                        try:
                            ds=int(ds)
                        except ValueError:
                            showerror('Error','Not a valid mobile number')
                            return
                        if len(dd)>15:
                            showerror('Error','Not a valid mobile number')
                            return
                        
        
                        if(v.get()!=OptionList[0]):
                            
                            if str(v.get())==str(xx[0][10]):
                                showerror('Error','Contact Type is Same as the previous one')
                                return
                            cur.execute("Update mobile set phonenumber=? where cid= ? and contacttype=? ",(e30.get(),cfd,xx[0][10]))
                            cur.execute("Insert into  mobile values(?,?,?)",(cfd,v.get(),e32.get()))
                        else:
                            cur.execute("Update mobile set phonenumber=? where cid= ? and contacttype=? ",(e30.get(),cfd,xx[0][10]))
                            if(len(xx)==4):
                                cur.execute("Update  mobile set phonenumber=? where cid= ? and contacttype=? ",(e32.get(),cfd,xx[3][10]))
                            else:
                                cur.execute("Update  mobile set phonenumber=? where cid= ? and contacttype=? ",(e32.get(),cfd,xx[1][10]))
                    else:
                        cur.execute("Update mobile set phonenumber=? where cid= ? and contacttype=? ",(e30.get(),cfd,xx[0][10]))
                    
                    if (e33.get()):
                        es1=str(e33.get())
                        if (not(re.search(regex,es1))):
                            showinfo('Error','Invalid Email')
                            return
                        if(va.get()!=OptionList1[0]):
                            if str(va.get())==str(xx[0][13]):
                                showerror('Error','Email Type is Same as the previous one')
                                return
                            cur.execute("Insert into  email values(?,?,?)",(cfd,va.get(),e33.get()))
                            cur.execute("Update email set eid=? where coid= ? and emailid_type=? ",(e31.get(),cfd,xx[0][13]))
                        else:
                            
                            cur.execute("Update email set eid=? where coid= ? and emailid_type=? ",(e31.get(),cfd,xx[0][13]))
                            cur.execute("Update email set eid=? where coid= ? and emailid_type=? ",(e33.get(),cfd,xx[1][13]))
                    else:
                        cur.execute("Update email set eid=? where coid= ? and emailid_type=? ",(e31.get(),cfd,xx[0][13]))
                except sqlite3.IntegrityError:
                    showerror('Error','Same Phone number or EmailId not allowed')
                    return
                con.commit()
                showinfo('Edit','Changes Saved in the Phone Book')
                
            Button(root2,text="Save Changes",command=saveit,bg="cyan").grid(row=19,column=1,columnspan=2)
            Button(root2,text="Back",command=closep,bg="cyan").grid(row=19,column=3,columnspan=2)
            root2.mainloop()
        Button(lb1,text="Edit",command=edit,bg="magenta3").place(x=360,y=500)       
    def inp(e=0):
        lb.delete(0,END)
        gt=str(et.get())
        pt=['%'+et.get()+'%']
        cur.execute("Select firstname,lastname from contac_det  where firstname like (?)  order by firstname",pt)
        xu=cur.fetchall()
        for ij in xu:
            lb.insert(END,ij)
        
        lb.bind('<<ListboxSelect>>', onselect)
        
    lb.bind('<<ListboxSelect>>', onselect)    
    root1.bind('<Key>',inp)
    root1.mainloop()    
Button(root,text="Save",command=save,bg="magenta2").grid(row=19,column=0)
Button(root,text="Search",command=search,bg="magenta2").grid(row=19,column=1)
Button(root,text="Close",command=close,bg="magenta2").grid(row=19,column=2)
Button(root,text="Edit",command=search,bg="magenta2").grid(row=19,column=3)
con.commit()
root.mainloop()
