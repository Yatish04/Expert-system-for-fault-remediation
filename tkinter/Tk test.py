# -*- coding: utf-8 -*-
import sys,datetime
from pyke import knowledge_engine, krb_traceback

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

class REMEDY:
    
    def __init__(self,name,cost,time):
        self.name=name
        self.time=time
        self.cost=cost
        self.prod=time*cost
    def __str__(self):
        return '{ '+str(self.name)+' '+str(self.cost)+' '+str(self.prod)+' '+str(self.time)+' }'  

class queue:
    def __init__(self):
        self.list=[None for x in range(10000)]
        self.front=0
        self.rear=-1
    
    def enqueue(self,ob):
        self.rear=self.rear+1
        self.list[self.rear]=ob
    
    def dequeue(self):
        self.list[self.front]=None
        self.front=self.front+1
    
    def queuelength(self):
        return (self.rear-self.front+1)
class log_object:
    
    def __init__(self,timestamp,fault,remedy):
        self.time=timestamp
        self.fault=fault
        self.remedy=remedy
    
    def __str__(self):
        return ("Time:"+str(self.time)+"\nFault: "+str(self.fault)+"\nRemedy: "+self.remedy)


def compare(ob1,ob2,criteria):
    if (criteria=="cost"):
        return ob1.cost>ob2.cost
    elif (criteria=="time"):
        return ob1.time>ob2.time
    else:
        return ob1.prod>ob2.prod

def min_heap(criteria):
    global remedy_list
    try:
        if len(remedy_list)==1:
            return remedy_list.pop(0)
        if len(remedy_list)!=1:
            length=len(remedy_list)
            for i in range(length//2-1,-1,-1):
                try:
                    if(compare(remedy_list[i],remedy_list[2*i+1],criteria)):
                        temp=remedy_list[i]
                        remedy_list[i]=remedy_list[2*i+1]
                        remedy_list[2*i+1]=temp
                    if(compare(remedy_list[i],remedy_list[2*i+2],criteria)):
                        temp=remedy_list[i]
                        remedy_list[i]=remedy_list[2*i+2]
                        remedy_list[2*i+2]=temp
                except:
                    if(compare(remedy_list[i],remedy_list[2*i+1],criteria)):
                        temp=remedy_list[i]
                        remedy_list[i]=remedy_list[2*i+1]
                        remedy_list[2*i+1]=temp
            return remedy_list.pop(0)
    except:
        return REMEDY("No remedies available",0,0)
        
class hashtable(object):
    """docstring for ."""
    def __init__(self):
        self.list1 = [0,0,0,0,0,0,0,0,0,0]



def scale(value):
    if int(value)<50:
        return 'low'
    elif 50<=int(value)<=70:
        return 'mid'
    else:
        return 'high'

def search(key,fault):#curr is a tuple(fault,remedy)
    primary_key=key%100
    sec_key=key//100
    if(hashobbjects[primary_key-1].list1[sec_key-1]==0):
        raise KeyError('key not found')
    else:
        temp=hashobbjects[primary_key-1].list1[sec_key-1]
        for value in temp:
            if(fault==value[0]):
                return (value[1],value[2])
            
def insert(key,curr):
    primary_key=key%100
    sec_key=key//100
    if(hashobbjects[primary_key-1].list1[sec_key-1]==0):
        hashobbjects[primary_key-1].list1[sec_key-1]=[curr]
    else:
        for i in range(len(hashobbjects[primary_key-1].list1[sec_key-1])):
            if(hashobbjects[primary_key-1].list1[sec_key-1][i][0]==curr[0]):
                hashobbjects[primary_key-1].list1[sec_key-1][i][-1]+=curr[1]
                hashobbjects[primary_key-1].list1[sec_key-1][i][-1]+=curr[2]
                return
        hashobbjects[primary_key-1].list1[sec_key-1].append(curr)
        
def FaultLog():

    def backpage():
        global ctr
        ctr=ctr-5
        frame=tkinter.Frame(root,bg="Blue")
        frame.place(x=0,y=0,height=650,width=800)
        button=tkinter.Button(frame,text="Go Back to main",command=mainpage,font=("Times New Roman","12"))
        button.place(x=10,y=510,height=100,width=150)
        
        button2=tkinter.Button(frame,text="Next",command=nextpage,font=("Times New Roman","12"))
        button2.place(x=600,y=510,height=100,width=100)
        button3=tkinter.Button(frame,text="Back",command=backpage,font=("Times New Roman","12"))
        button3.place(x=500,y=510,height=100,width=100)
        try:
            if (fault_queue.list[ctr]!=None):
                Label1=tkinter.Label(frame,text=str(fault_queue.list[ctr]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label1.place(x=30,y=(ctr%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+1]!=None):    
                Label2=tkinter.Label(frame,text=str(fault_queue.list[ctr+1]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label2.place(x=30,y=((ctr+1)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+2]!=None):
                Label3=tkinter.Label(frame,text=str(fault_queue.list[ctr+2]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label3.place(x=30,y=((ctr+2)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+3]!=None):
                Label4=tkinter.Label(frame,text=str(fault_queue.list[ctr+3]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label4.place(x=30,y=((ctr+3)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+4]!=None):
                Label5=tkinter.Label(frame,text=str(fault_queue.list[ctr+4]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label5.place(x=30,y=((ctr+4)%5)*100,width=700,height=100)
        except:
            pass
        if (ctr<5):
            button3.configure(state=tkinter.DISABLED)
        button2.configure(state=tkinter.NORMAL)
    
    def nextpage():
        global ctr
        ctr=ctr+5
        frame=tkinter.Frame(root,bg="Blue")
        frame.place(x=0,y=0,height=650,width=800)
        button=tkinter.Button(frame,text="Go Back to main",command=mainpage,font=("Times New Roman","12"))
        button.place(x=10,y=510,height=100,width=150)
        
        button2=tkinter.Button(frame,text="Next",command=nextpage,font=("Times New Roman","12"))
        button2.place(x=600,y=510,height=100,width=100)
        button3=tkinter.Button(frame,text="Back",command=backpage,font=("Times New Roman","12"))
        button3.place(x=500,y=510,height=100,width=100)
        
        if (length-ctr<=5):
            button2.configure(state=tkinter.DISABLED)
        try:
            if (fault_queue.list[ctr]!=None):
                Label1=tkinter.Label(frame,text=str(fault_queue.list[ctr]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label1.place(x=30,y=(ctr%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+1]!=None):    
                Label2=tkinter.Label(frame,text=str(fault_queue.list[ctr+1]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label2.place(x=30,y=((ctr+1)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+2]!=None):
                Label3=tkinter.Label(frame,text=str(fault_queue.list[ctr+2]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label3.place(x=30,y=((ctr+2)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+3]!=None):
                Label4=tkinter.Label(frame,text=str(fault_queue.list[ctr+3]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label4.place(x=30,y=((ctr+3)%5)*100,width=700,height=100)
            if (fault_queue.list[ctr+4]!=None):
                Label5=tkinter.Label(frame,text=str(fault_queue.list[ctr+4]),relief=tkinter.GROOVE,font=("Helvetica","12"))
                Label5.place(x=30,y=((ctr+4)%5)*100,width=700,height=100)
        except:
            pass
    global fault_queue
    frame=tkinter.Frame(root,bg="Blue")
    frame.place(x=0,y=0,height=650,width=800)
    button=tkinter.Button(frame,text="Go Back to main",command=mainpage,font=("Times New Roman","12"))
    button.place(x=10,y=510,height=100,width=150)
    
    length=fault_queue.queuelength()
    
    button2=tkinter.Button(frame,text="Next",command=nextpage,font=("Times New Roman","12"))
    button2.place(x=600,y=510,height=100,width=100)
    button3=tkinter.Button(frame,text="Back",command=backpage,font=("Times New Roman","12"))
    button3.place(x=500,y=510,height=100,width=100)
    
    if length<5:
        button2.configure(state=tkinter.DISABLED)
    button3.configure(state=tkinter.DISABLED)
    try:
        if (fault_queue.list[ctr]!=None):
            Label1=tkinter.Label(frame,text=str(fault_queue.list[ctr]),relief=tkinter.GROOVE,font=("Helvetica","12"))
            Label1.place(x=30,y=(ctr%5)*100,width=700,height=100)
        if (fault_queue.list[ctr+1]!=None):    
            Label2=tkinter.Label(frame,text=str(fault_queue.list[ctr+1]),relief=tkinter.GROOVE,font=("Helvetica","12"))
            Label2.place(x=30,y=((ctr+1)%5)*100,width=700,height=100)
        if (fault_queue.list[ctr+2]!=None):
            Label3=tkinter.Label(frame,text=str(fault_queue.list[ctr+2]),relief=tkinter.GROOVE,font=("Helvetica","12"))
            Label3.place(x=30,y=((ctr+2)%5)*100,width=700,height=100)
        if (fault_queue.list[ctr+3]!=None):
            Label4=tkinter.Label(frame,text=str(fault_queue.list[ctr+3]),relief=tkinter.GROOVE,font=("Helvetica","12"))
            Label4.place(x=30,y=((ctr+3)%5)*100,width=700,height=100)
        if (fault_queue.list[ctr+4]!=None):
            Label5=tkinter.Label(frame,text=str(fault_queue.list[ctr+4]),relief=tkinter.GROOVE,font=("Helvetica","12"))
            Label5.place(x=30,y=((ctr+4)%5)*100,width=700,height=100)
    except:
        pass




def solve():
    global e6,e7,e8,e9,c_check,t_check,remedy_remain,cur_fault,sumy,sumx,sum1,fault_queue
    if remedy_remain==[]:
        sumy=0
        t2=(e6.get(),e7.get(),e8.get(),e9.get())
        if ("" in t2):
            return
        for i in t2:
            if int(i)<0 or int(i)>100:
                return 
        l2=list(t2)
        for i in range(4):
            sumy+=int(l2[i])
            l2[i]=scale(l2[i])
        tup=tuple(l2)
        ft[2]=tup
        #remedy_frame=tkinter.Frame(root)
        #remedy_frame.place(x=0,y=0,height=650,width=800)
        print(tuple(ft))
        fault=tuple(ft)
        sum1=sumx+sumy
        engine.reset()
        i=-1
        try:
            engine.activate('Remedyrule')
            global remedy_list
            try:
                #To see if remedy is present in hash only.
                remedy_list=[]
                op=search(sum1,fault)
                temp=op[1][0]
                print(temp)
                print('The following are the faults\n')
                for i in range(len(temp)):
                        print(temp[i])
                print("\n",op[0][0],"\n")
                for k in op[0]:
                    for j in k:
                        print(j)
                        ob=REMEDY(j[0],j[1][0],j[1][1])
                        remedy_list.append(ob)   
                if (c_check=="y" and t_check=="y"):
                    ob=min_heap("prod")
                elif (c_check=="y"):
                    ob=min_heap("cost")
                elif (t_check=="y"):
                    ob=min_heap("time")
                    
            except: #Not found in hash map
                temp=[]
                remedy_list=[]
                with engine.prove_goal('Remedyrule.get($fault,$actualfault,$remedy)',fault=fault) as gen:
                    for  i,(vars, no_plan) in enumerate(gen):
                        remedy=vars['remedy']
                        temp=vars['actualfault']
                        insert(sum1,[fault,[vars['remedy']],[vars['actualfault']]])
                        for j in remedy:
                            ob=REMEDY(j[0],j[1][0],j[1][1])
                            remedy_list.append(ob)
                    print("The following faults were diagonised\n")
                    print (temp)
                    for i in range(len(temp)):
                            print(temp[i])
                    if (c_check=="y" and t_check=="y"):
                        ob=min_heap("prod")
                    elif (c_check=="y"):
                        ob=min_heap("cost")
                    elif (t_check=="y"):
                        ob=min_heap("time")
        
            if i==-1:
                    print("No remedy available")
                    insert(sum1,[fault,['No Remedy Availaible'],['Undefined Fault']])
        except:
            krb_traceback.print_exc()
            sys.exit(1)
    else:
        remedy_list=remedy_remain
        temp=cur_fault
        if (c_check=="y" and t_check=="y"):
            ob=min_heap("prod")
        elif (c_check=="y"):
            ob=min_heap("cost")
        elif (t_check=="y"):
            ob=min_heap("time")
            
    remedy_remain=remedy_list
    cur_fault=temp
    remedy_frame=tkinter.Frame(root,bg="Blue")
    remedy_frame.place(x=0,y=0,height=650,width=800)
    back=tkinter.Button(remedy_frame,text="Back to Main Page",command=mainpage,font=("Times New Roman","12"))
    back.place(x=20,y=530,height=80,width=150)
    f1=tkinter.Label(remedy_frame,text="The Faults are:",font=("Helvetica","16"),relief=tkinter.GROOVE)
    f1.place(x=300,y=40,height=50,width=200)
    xpos=150
    ypos=100
    for i in temp:
        tkinter.Label(remedy_frame,text=i,relief=tkinter.GROOVE,font=("Helvetica","12")).place(x=xpos,y=ypos,height=100,width=250)
        if (xpos==400):
            xpos=150
            ypos=200
        else:
            xpos=400
    if len(temp)==0:
        tkinter.Label(remedy_frame,text="Undefined fault",relief=tkinter.GROOVE,font=("Helvetica","16")).place(x=300,y=100,height=100,width=200)
    fl=[]
    for i in temp:
        fl.append(i)
    if fl==[]:
        fl=["Undefined Fault"]
    remedy_string=ob.name
    logobj=log_object(datetime.datetime.now(),fl,remedy_string)
    fault_queue.enqueue(logobj)
    print (logobj)
    if fl!=["Undefined Fault"]:
        f2=tkinter.Label(remedy_frame,text="The best possible remedy is:",relief=tkinter.GROOVE,font=("Helvetica","16"))
        f2.place(x=250,y=310,height=50,width=300)
        f3=tkinter.Label(remedy_frame,text=ob.name+"\nCost:"+str(ob.cost)+"\nTime:"+str(ob.time),relief=tkinter.GROOVE,font=("Helvetica","12"))
        f3.place(x=150,y=370,height=150,width=500)
        buttonback=tkinter.Button(remedy_frame,text="Remedy Not working..suggest next best",command=solve_cond,font=("Times New Roman","12"))
        buttonback.place(x=450,y=530,height=80,width=300)
    else:
        f2=tkinter.Label(remedy_frame,text="No remedy found in database.",relief=tkinter.GROOVE,font=("Helvetica","16"))
        f2.place(x=250,y=400,height=100,width=300)

def cost_only():
    global c_check
    c_check="y"
    solve()
    
def time_only():
    global t_check
    t_check="y"
    solve()
    
def both():
    global c_check,t_check
    c_check="y"
    t_check="y"
    solve()

def solve_cond():
    t2=(e6.get(),e7.get(),e8.get(),e9.get())
    if ("" in t2):
        return
    cond_frame=tkinter.Frame(root,bg="Blue")
    cond_frame.place(x=0,y=0,height=650,width=800)
    try:
        PMf.destroy()
    except:
        pass
    Label1=tkinter.Label(cond_frame,text="PRIORITY:",font=("Helvetica","16"),relief=tkinter.GROOVE)
    Label1.place(x=270,y=50,height=100,width=200)
    Button1=tkinter.Button(cond_frame,text="Cost only",command=cost_only,font=("Times New Roman","12"))
    Button1.place(x=50,y=200,height=100,width=150)
    
    Button2=tkinter.Button(cond_frame,text="Time only",command=time_only,font=("Times New Roman","12"))
    Button2.place(x=550,y=200,height=100,width=150)
    
    Button3=tkinter.Button(cond_frame,text="Cost and Time",command=both,font=("Times New Roman","12"))
    Button3.place(x=300,y=450,height=100,width=150)

def PM():
    global e2,e3,e4,e5,e6,e7,e8,e9,sumx,sumy
    sumx=0
    t2=(e2.get(),e3.get(),e4.get(),e5.get())
    if ("" in t2):
        return
    for i in t2:
        if int(i)<0 or int(i)>100:
            return
    l2=list(t2)
    for i in range(4):
        sumx=sumx+int(l2[i])
        l2[i]=scale(l2[i])
    tup=tuple(l2)
    ft[1]=tup
    PMf=tkinter.Frame(root,bg="Blue")
    PMf.place(x=0,y=0,height=650,width=800)
    #PMf.lift()
    tkinter.Label(PMf,text="PM PARAMETERS",font=("Helvetica","16"),relief=tkinter.GROOVE).place(x=300,y=20)
    storage=tkinter.Label(PMf,text="Storage(%used)",font=("Helvetica","12"))
    storage.place(x=10,y=120)
    e6=tkinter.Entry(PMf)
    e6.place(x=200,y=100,height=70,width=150)
    
    memory=tkinter.Label(PMf,text="Memory(%used)",font=("Helvetica","12"))
    memory.place(x=10,y=220)
    e7=tkinter.Entry(PMf)
    e7.place(x=200,y=200,height=70,width=150)
    
    network=tkinter.Label(PMf,text="Network(%used)",font=("Helvetica","12"))
    network.place(x=10,y=320)
    e8=tkinter.Entry(PMf)
    e8.place(x=200,y=300,height=70,width=150)
    
    cpu=tkinter.Label(PMf,text="CPU(%used)",font=("Helvetica","12"))
    cpu.place(x=10,y=420)
    e9=tkinter.Entry(PMf)
    e9.place(x=200,y=400,height=70,width=150)
    
    back=tkinter.Button(PMf,text="Back",command=VM,font=("Times New Roman","12"))
    back.place(x=50,y=500,height=80,width=150)
    
    next=tkinter.Button(PMf,text="Next",command=solve_cond,font=("Times New Roman","12"))
    next.place(x=580,y=500,height=80,width=150)


def VM():
    global e1,e2,e3,e4,e5
    str=e1.get()
    if (str.lower() not in ["less","more"]):
        return
    ft[0]=str
    VMf=tkinter.Frame(root,bg="Blue")
    VMf.place(x=0,y=0,height=650,width=800)
    try:
        PMf.destroy()
    except:
        pass
    tkinter.Label(VMf,text="VM PARAMETERS",font=("Helvetica","16"),relief=tkinter.GROOVE).place(x=300,y=20)
    storage=tkinter.Label(VMf,text="Storage(%used)",font=("Helvetica","12"))
    storage.place(x=10,y=120)
    e2=tkinter.Entry(VMf)
    e2.place(x=200,y=100,height=70,width=150)
    
    memory=tkinter.Label(VMf,text="Memory(%used)",font=("Helvetica","12"))
    memory.place(x=10,y=220)
    e3=tkinter.Entry(VMf)
    e3.place(x=200,y=200,height=70,width=150)
    
    network=tkinter.Label(VMf,text="Network(%used)",font=("Helvetica","12"))
    network.place(x=10,y=320)
    e4=tkinter.Entry(VMf)
    e4.place(x=200,y=300,height=70,width=150)
    
    cpu=tkinter.Label(VMf,text="CPU(%used)",font=("Helvetica","12"))
    cpu.place(x=10,y=420)
    e5=tkinter.Entry(VMf)
    e5.place(x=200,y=400,height=70,width=150)
    
    back=tkinter.Button(VMf,text="Back",command=application,font=("Times New Roman","12"))
    back.place(x=50,y=500,height=80,width=150)
    
    next=tkinter.Button(VMf,text="Next",command=PM,font=("Times New Roman","12"))
    next.place(x=580,y=500,height=80,width=150)
    
def application():
    aplt=tkinter.Frame(root,bg="Blue")
    aplt.place(x=0,y=0,height=650,width=800)
    try:
        VMf.destroy()
    except:
        pass
    art=tkinter.Label(aplt,text="Enter application response time as greater than or less than 15 seconds[less/more]",font=("Helvetica","12"))
    art.place(x=40,y=10,width=700,height=100)
    global e1
    e1=tkinter.Entry(aplt)
    e1.place(x=300,y=200,height=50,width=200)
    back=tkinter.Button(aplt,text="Back",command=mainpage,font=("Times New Roman","12"))
    back.place(x=50,y=500,height=80,width=150)
    next=tkinter.Button(aplt,text="Next",command=VM,font=("Times New Roman","12"))
    next.place(x=580,y=500,height=80,width=150)

def mainpage():
    mainframe=tkinter.Frame(root,bg="Blue")
    mainframe.place(x=0,y=0,height=650,width=800)
    global ctr,remedy_remain,cur_fault
    remedy_remain=[]
    cur_fault=[]
    ctr=0
    try:
        aplt.destroy()
        remedy_frame.destroy()
    except:
        pass
    welcome=tkinter.Label(mainframe,text="EXPERT SYSTEM",relief=tkinter.GROOVE,font=("Times New Roman","20"))
    welcome.place(x=250,y=100,height=300,width=300)
    
    start=tkinter.Button(mainframe,text="Remedy Fault",font=("Times New Roman","12"),command=application)
    start.place(x=10,y=500,height=100,width=200)
    
    log=tkinter.Button(mainframe,text="Show Fault Log",font=("Times New Roman","12"),command=FaultLog)
    log.place(x=550,y=500,height=100,width=200)


import tkinter,pickle
#predecalring entry vars:
e1,e2,e3,e4,e5,e6,e7,e8,e9=[None for i in range(9)]
ft=["","",""]
try:
    file1=open("Faultlog.log","rb")
    fault_queue=pickle.load(file1)
    file1.close()
except:
    fault_queue=queue()
    
ctr=sum1=sumx=sumy=0
c_check=t_check=""
aplt=VMf=PMf=remedy_frame=cond_frame=None
root=tkinter.Tk()
root.minsize(width=800, height=650)
root.maxsize(width=800, height=650)

hashobbjects=[]
remedy_list=[]
remedy_remain=[]
cur_fault=[]

for i in range(100):
    new=hashtable()
    hashobbjects.append(new)

mainpage()
root.mainloop()
file1=open("Faultlog.log","wb")
pickle.dump(fault_queue,file1)
file1.close()

