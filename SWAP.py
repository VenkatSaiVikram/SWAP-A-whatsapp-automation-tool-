# importing required modules

from tkinter import * # importing tkinter
import pywhatkit as kit # importing pywhatkit
import time # importing time
import csv # importing csv

# configuring main login window

login=Tk() # creating a main login window
login.title("SWAP") # adding a title
login.iconbitmap("swap.ico") # adding icon to the login window
login.configure(bg="#cd853f") # adding a background
login.geometry("400x400") # setting login window size
login.resizable(width=False,height=False) # making the window non-resizable

# creating login window's widgets

heading=Label(login,text="SWAP",bg="#cd853f",fg="black",font=("Comic Sans MS",24),padx=40)
heading.pack(pady=10) # creating a heading

line1=Label(login,text="-------------------------------------",bg="#cd853f",fg="black",font=("Comic Sans MS",18))
line1.place(x=11,y=67.5) # creating a line

user_name=Label(login,text="USERNAME  :",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
user_name.place(x=50,y=125) # creating username label

user_name_entry=Entry(login,width=16,bd=2,selectbackground="#cd853f",relief=SOLID,font=("Comic Sans MS",12),justify=CENTER)
user_name_entry.place(x=175,y=125) # creating username entry

password=Label(login,text="PASSWORD  :",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
password.place(x=50,y=175) # creating password label

password_entry=Entry(login,width=16,bd=2,selectbackground="#cd853f",relief=SOLID,font=("Comic Sans MS",12),show="*",justify=CENTER)
password_entry.place(x=175,y=175) # creating password entry

line2=Label(login,text="-------------------------------------",bg="#cd853f",fg="black",font=("Comic Sans MS",18))
line2.place(x=11,y=214.5) #creating a line 

# defining the button command functions between the widgets and the buttons

def LOGIN(): # defining login button's command
    
    Username=user_name_entry.get() # getting the input of
    Password=password_entry.get()  # login window
    
    if Username =='SPSUSER' and Password == 'SPS@123': # checking the parameters
        
        login.destroy()
        
        # configuring main window
        main=Tk() # creating a new window (main) if the login credentials are correct
        main.title("SWAP") # addind title to main window
        main.iconbitmap("swap.ico") # adding icon to the main window
        main.configure(bg="#cd853f") # adding background colour to main window
        main.geometry("400x400") # setting the main window size
        
        # creating widgets for main window
        
        heading=Label(main,text="ENTER THE BELOW ASKED DETAILS..",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
        heading.place(x=45,y=25) # creating a heading
        line1=Label(main,text="-------------------------------------",bg="#cd853f",fg="black",font=("Comic Sans MS",18))
        line1.place(x=11,y=50) # creating a line
        exam_name=Label(main,text="EXAM NAME   :",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
        exam_name.place(x=20,y=100) # creating a label exam name
        exam_name_entry=Entry(main,width=20,bd=2,selectbackground="#cd853f",relief=SOLID,font=("Comic Sans MS",12),justify=CENTER)
        exam_name_entry.place(x=160,y=100) # creating a exam_name_entry
        class_sec=Label(main,text="CLASS & SEC   :",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
        class_sec.place(x=20,y=150) # creating a label class_sec
        class_sec_entry=Entry(main,width=20,bd=2,selectbackground="#cd853f",relief=SOLID,font=("Comic Sans MS",12),justify=CENTER)
        class_sec_entry.place(x=160,y=150) # creating a class_sec_entry
        location=Label(main,text="LOCATION      :",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
        location.place(x=20,y=200) # creating a label location
        location_entry=Entry(main,width=20,bd=2,selectbackground="#cd853f",relief=SOLID,font=("Comic Sans MS",12),justify=CENTER)
        location_entry.place(x=160,y=200) # creating a label_entry
        line2=Label(main,text="-------------------------------------",bg="#cd853f",fg="black",font=("Comic Sans MS",18))
        line2.place(x=11,y=230) #creating a line 
        
        # defining the functions of START and BACK buttons
        
        def START(): # defining a function for start button
            exam=exam_name_entry.get()
            Class_sec=class_sec_entry.get()
            Location=location_entry.get()+".csv"

            file=open(Location,"r")
            reader=csv.reader(file)
            
            a=2
            n=[]
            ch=[]
            av=[]
            subjects=[]
            
            for i in range(1,101):
                i=str(i)
                n.append(i)
            
            for i in reader:
                
                if len(i)==16:
                    
                    if i[2].lower()=="english":
                        
                        for y in i:
                            subjects.append(i[a])
                            
                            if a==10:
                                break
                            
                            else:
                                a+=2
                    
                    elif i[1].lower()=="highest mark":
                        ch.append(i[3])
                        ch.append(i[5])
                        ch.append(i[7])
                        ch.append(i[9])
                        ch.append(i[11])
                    
                    elif i[1].lower()=="average":
                        av.append(i[3])
                        av.append(i[5])
                        av.append(i[7])
                        av.append(i[9])
                        av.append(i[11])
                
                elif len(i)==18:

                    if i[2].lower()=="english":
                        
                        for z in i:
                            subjects.append(i[a])
                            
                            if a==14:
                                break
                            
                            else:
                                a+=2
                    
                    elif i[1]=="Highest Mark":
                        ch.append(i[3])
                        ch.append(i[5])
                        ch.append(i[7])
                        ch.append(i[9])
                        ch.append(i[11])
                        ch.append(i[13])
                    
                    elif i[1].lower()=="average":
                        av.append(i[3])
                        av.append(i[5])
                        av.append(i[7])
                        av.append(i[9])
                        av.append(i[11])
                        av.append(i[13])
            
            file=open(Location,"r")
            reader=csv.reader(file)
            
            for j in reader:

                if len(j)==16:
                    
                    if j[0] in n:
                        ph="+91"+j[15]
                        msg="--------------------------\n"+exam+" RESULTS\n--------------------------\nNAME : "+j[1]+"\n"+Class_sec+"\n--------------------------\n"+subjects[0]+": "+j[3]+" | C.H: "+ch[0]+" |C.A: "+av[0]+"\n"+subjects[1]+": "+j[5]+" | "+"C.H: "+ch[1]+" | C.A: "+av[1]+"\n"+subjects[2]+": "+j[7]+" | "+" C.H: "+ch[2]+" | C.A: "+av[2]+"\n"+subjects[3]+": "+j[9]+" | C.H: "+ch[3]+" | C.A: "+av[3]+"\n"+subjects[4]+": "+j[11]+" | "+"C.H: "+ch[4]+" | C.A: "+av[4]+"\n--------------------------\nTOTAL : "+j[12]+"\nAVERAGE : "+j[13]+"\nRANK : "+j[14]+"\n--------------------------"
                        kit.sendwhatmsg_instantly(ph,msg)
                        kit.close_tab(wait_time=5)
                        
                        time.sleep(1)
                
                elif len(j)==18:

                    if j[0] in n:
                        ph="+91"+j[17]

                        if j[5]=="":
                            msg="--------------------------\n"+exam+" RESULTS\n--------------------------\nNAME : "+j[1]+"\n"+Class_sec+"\n--------------------------\n"+subjects[0]+": "+j[3]+" | C.H: "+ch[0]+" |C.A: "+av[0]+"\n"+subjects[2]+": "+j[7]+" | "+"C.H: "+ch[2]+" | C.A: "+av[2]+"\n"+subjects[3]+": "+j[9]+" | "+" C.H: "+ch[3]+" | C.A: "+av[3]+"\n"+subjects[4]+": "+j[11]+" | C.H: "+ch[4]+" | C.A: "+av[4]+"\n"+subjects[5]+": "+j[13]+" | C.H: "+ch[5]+" | C.A: "+av[5]+"\n--------------------------\nTOTAL : "+j[14]+"\nAVERAGE : "+j[15]+"\nRANK : "+j[16]+"\n--------------------------"
                        
                        elif j[7]=="":
                            msg="--------------------------\n"+exam+" RESULTS\n--------------------------\nNAME : "+j[1]+"\n"+Class_sec+"\n--------------------------\n"+subjects[0]+": "+j[3]+" | C.H: "+ch[0]+" |C.A: "+av[0]+"\n"+subjects[1]+": "+j[5]+" | "+"C.H: "+ch[1]+" | C.A: "+av[1]+"\n"+subjects[3]+": "+j[9]+" | "+" C.H: "+ch[3]+" | C.A: "+av[3]+"\n"+subjects[4]+": "+j[11]+" | C.H: "+ch[4]+" | C.A: "+av[4]+"\n"+subjects[5]+": "+j[13]+" | C.H: "+ch[5]+" | C.A: "+av[5]+"\n--------------------------\nTOTAL : "+j[14]+"\nAVERAGE : "+j[15]+"\nRANK : "+j[16]+"\n--------------------------"
                        
                        kit.sendwhatmsg_instantly(ph,msg)
                        kit.close_tab(wait_time=5)
                        
                        time.sleep(1)

            file.close()

            main.destroy()

            result=Tk() # creating a new window (main) if the login credentials are correct
            result.title("SWAP") #adding icon to the result window
            result.iconbitmap("E:\EDUCATION\COMPUTER\SWAP\Source code\swap.ico") # adding icon to main window
            result.configure(bg="#cd853f") # adding background colour to main window
            result.geometry("400x400") # setting the main window size
            result.resizable(width=False,height=False) # making the result window non-resizable
            
            # creating widgets for result window
            
            heading=Label(result,text="MARKS OF STUDENTS ARE\nSENT SUCCESFULLY\nTO THEIR WHATSAPP NUMBER...",bg="#cd853f",fg="black",font=("Comic Sans MS",12))
            heading.place(x=65,y=100) # creating a heading
            def EXIT():
                result.destroy() # destroying the result window
                
            Exit_button=Button(result,text="EXIT",relief=SOLID,bd=2,bg="#cd853f",padx=25,pady=5,font=("Comic Sans MS",8),command=EXIT)
            Exit_button.place(x=157,y=250) # creating a exit button for result window
            
            vsv=Label(result,text="© developed by VSV",bg="#cd853f",fg="black",font=("Comic Sans MS",10))
            vsv.place(x=134,y=373) # creating a footnote
            
            result.mainloop() # entering the mainloop of result window

        def EXIT(): # defining function for exit button
            main.destroy() # destroying the main window

        # creating a START and EXIT  button for main window
        
        start_button=Button(main,text="START",relief=SOLID,bd=2,bg="#cd853f",padx=20,pady=5,font=("Comic Sans MS",8),command=START)
        start_button.place(x=157,y=275) # creating a START button for main window
        
        exit_button=Button(main,text="EXIT",relief=SOLID,bd=2,bg="#cd853f",padx=25,pady=5,font=("Comic Sans MS",8),command=EXIT)
        exit_button.place(x=157,y=325) # creating a EXIT button for main window
        
        vsv=Label(main,text="© developed by VSV",bg="#cd853f",fg="black",font=("Comic Sans MS",10))
        vsv.place(x=134,y=373) # adding a footnote
        
        main.resizable(width=False,height=False) # making the window non-resizable
        
        main.mainloop() # entering the infinite loop of main window
        
    else:    
        user_name_entry.delete(0,END) # deleting the entered login credentials
        password_entry.delete(0,END) # if it is invalid
        error=Label(login,text="INVALID LOGIN CREDENTIALS",bg="#cd853f",fg="black",font=("Comic Sans MS",8)) # creating an error label
        error.place(x=105,y=250) # creating a error label to display a text if login credentials is invalid

def EXIT(): # defining exit button's command
    login.destroy() # destroying the login window if exit is clicked

Login_button=Button(login,text="LOGIN",relief=SOLID,bd=2,bg="#cd853f",padx=20,pady=5,font=("Comic Sans MS",8),command=LOGIN)
Login_button.place(x=157,y=275) # creating a login button for login window

Exit_button=Button(login,text="EXIT",relief=SOLID,bd=2,bg="#cd853f",padx=25,pady=5,font=("Comic Sans MS",8),command=EXIT)
Exit_button.place(x=157,y=325) # creating a exit button for login window

development_label=Label(login,text="© developed by VSV",bg="#cd853f",fg="black",font=("Comic Sans MS",10))
development_label.place(x=134,y=373) # adding footnotes

login.mainloop() # entering the infinte loop of login window