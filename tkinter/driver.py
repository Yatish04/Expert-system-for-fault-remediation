# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:42:25 2017

@author: Tanmay
"""
#Check if git
import sys
from pyke import knowledge_engine, krb_traceback
remedy_list=[]
# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)
class REMEDY(object):
    
    def __init__(self,name,cost,time):
        self.name=name
        self.time=time
        self.cost=cost
        self.prod=time*cost
    def __str__(self):
        return '{ '+str(self.name)+' '+str(self.cost)+' '+str(self.prod)+' '+str(self.time)+' }'        

#Do heap insert and delete and create class accordingly
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
                        #print('hello')
#            for i in remedy_list:
#                print(i)
            return remedy_list.pop(0)
    except:
        print('No more remedies left')


class hashtable(object):
    """docstring for ."""
    def __init__(self):
        self.list1 = [0,0,0,0,0,0]
hashobbjects=[]


for i in range(100):
    new=hashtable()
    hashobbjects.append(new)



def scale(value):
    if value<50:
        return 'low'
    elif 50<value<=70:
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
#        print(temp,'hello')
        for value in temp:
            if(fault==value[0]):
                return (value[1],value[2])

                
                
def insert(key,curr):#curr is a list= [fault,[remedies],[faults]]
    primary_key=key%100
    sec_key=key//100
    if(hashobbjects[primary_key-1].list1[sec_key-1]==0):
        hashobbjects[primary_key-1].list1[sec_key-1]=[curr]
    else:
        for i in range(len(hashobbjects[primary_key-1].list1[sec_key-1])):
            if(hashobbjects[primary_key-1].list1[sec_key-1][i][0]==curr[0]):
                hashobbjects[primary_key-1].list1[sec_key-1][i][-2]+=curr[1]
                hashobbjects[primary_key-1].list1[sec_key-1][i][-1]+=curr[2]
                return
        hashobbjects[primary_key-1].list1[sec_key-1].append(curr)

def getremedy():
    engine.reset()
    i=-1
    global remedy_list
    try:
        engine.activate('Remedyrule')
        a_time=input("Enter application response time is less than or greater than 15[less\greater]")
        print("Virtual Machine Paramaeters")
        storage1=int(input("Enter Storage percentage:[0-100]"))
        memory1=int(input("Enter Memory percentage:[0-100]"))
        network1=int(input("Enter Network level:[0-100]"))
        cpu1=int(input("Enter CPU level:[0-100]"))
        storage11=scale(storage1)
        memory11=scale(memory1)
        network11=scale(network1)
        cpu11=scale(cpu1)
        print("\nPhysical Machine Parameters")
        storage2=int(input("Enter Storage percentage:[0-100]"))
        memory2=int(input("Enter Memory percentage:[0-100]"))
        network2=int(input("Enter Network level:[0-100]"))
        cpu2=int(input("Enter CPU level:[0-100]"))
        storage22=scale(storage2)
        memory22=scale(memory2)
        network22=scale(network2)
        cpu22=scale(cpu2)
        fault=(a_time,(storage11,memory11,network11,cpu11),(storage22,memory22,network22,cpu22))
#        print(fault,'hello')
        sum1=int(storage1)+int(cpu1)+int(network1)+int(memory1)+int(storage2)+int(cpu2)+int(network2)+int(memory2)
        try:
            remedy_list=[]
            op=search(sum1,fault)
            #op=[(('Regular_checkpointing', (20, 10)), ('application_rejuvination', (25, 8)), ('application_migration', (9, 20)))(('Regular_cg', (20, 10)), ('application', (25, 8)), ('applicattion', (9, 20)))]
#            print(op[1])
            temp=op[1]
            print('The following are the faults\n')
            for i in temp:
                for k in range(len(i)):
                    print(i[k])
            for k in op[0]:
                for j in k:
#                    print(j)
                    ob=REMEDY(j[0],j[1][0],j[1][1])
                    remedy_list.append(ob)
            while (True):    
                    c_check=input('Do you want to check based on cost\n')
                    t_check=input('Do you want to check based on time\n')
                    if (c_check=="y" and t_check=="y"):
                        ob=min_heap("prod")
                    elif (c_check=="y"):
                        ob=min_heap("cost")
                    elif (t_check=="y"):
                        ob=min_heap("time")
#                        print(ob,'dssd')
                    else: 
                        for i in remedy_list:
                            print(i)
                        break
                    try:
                        print("Remedy:",ob.cost,ob.name,ob.time)
                    except:
                        pass
        except:
            remedy_list=[]
            temp=[]
            with engine.prove_goal('Remedyrule.get($fault,$actualfault,$remedy)',fault=fault) as gen:
                for  i,(vars, no_plan) in enumerate(gen):
                    remedy=vars['remedy']
                    temp.append(vars['actualfault'])
                    insert(sum1,[fault,[vars['remedy']],[vars['actualfault']]])
                    for j in remedy:
#                        print(j)
                        ob=REMEDY(j[0],j[1][0],j[1][1])
#                        print(ob)
                        remedy_list.append(ob)
                print("The following faults were diagonised\n")
#                print(temp)
                for i in temp:
                    for k in range(len(i)):
                        print(i[k])
                while (True):    
                    c_check=input('Do you want to check based on cost\n')
                    t_check=input('Do you want to check based on time\n')
                    if (c_check=="y" and t_check=="y"):
                        ob=min_heap("prod")
                    elif (c_check=="y"):
                        ob=min_heap("cost")
                    elif (t_check=="y"):
                        ob=min_heap("time")
                    else: 
                        print ("Remedy:",vars['remedy'])
                        break
                    try:
                        
                        print("Remedy:",ob.name,"Cost is",ob.cost,"Time is",ob.time)
                    except:
                        pass

                    
                if i==-1:
                    print("No remedy available")
                    insert(sum1,[fault,['No Remedy Availaible']])
                #elif (c_check=="y" or t_check=="y"):
                    #print ("\nRemedy:",remedy_list[0].name,"Cost:",remedy_list[0].cost,"Time:",remedy_list[0].time,"is the best solution")
                    #print("All solutions: ")
                    #for i in remedy_list:
                        #print(i.name,i.cost,i.time)

                    #print("The remedy to the fault: ",fault,"; is ", vars['remedy'])
                    #print (vars)
    except:
        krb_traceback.print_exc()

        sys.exit(1)
while (True):
    check=input("Enter 1 to find remedy;any other key to quit\n")
    if (check!="1"):
        break
   
    #fault=input("Enter the fault:")
    getremedy()
