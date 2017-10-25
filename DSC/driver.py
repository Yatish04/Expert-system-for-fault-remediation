# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:42:25 2017

@author: Tanmay
"""
#Check if git 
import sys
from pyke import knowledge_engine, krb_traceback

# Compile and load .krb files in same directory that I'm in (recursively).
engine = knowledge_engine.engine(__file__)

class REMEDY:
    
    def __init__(self,name,cost,time):
        self.name=name
        self.time=time
        self.cost=cost
        self.prod=time*cost
        

#Do heap insert and delete and create class accordingly
def compare(ob1,ob2,criteria):
    if (criteria=="cost"):
        return ob1.cost>ob2.cost
    elif (criteria=="time"):
        return ob1.time>ob2.time
    else:
        return ob1.prod>ob2.prod

def min_heap(ob,criteria):
    global remedy_list
    remedy_list.append(ob)
    if len(remedy_list)!=1:
        pos=len(remedy_list)-1
        while (compare(remedy_list[int(pos/2)],remedy_list[pos],criteria)):
            remedy_list[pos]=remedy_list[int(pos/2)]
            pos=int(pos/2)
        remedy_list[pos]=ob
        
def scale(value):
    if value<50:
        return 'low'
    elif 50<value<=70:
        return 'mid'
    else:
        return 'high'

def getremedy():
    engine.reset()
    i=-1
    try:
        engine.activate('Remedyrule')
        a_time=input("Enter application response time is less than or greater than 15[less\greater]")
        print("Virtual Machine Paramaeters")
        storage1=int(input("Enter Storage percentage:[0-100]"))
        memory1=int(input("Enter Memory percentage:[0-100]"))
        network1=int(input("Enter Network level:[0-100]"))
        cpu1=int(input("Enter CPU level:[0-100]"))
        storage1=scale(storage1)
        memory1=scale(memory1)
        network1=scale(network1)
        cpu1=scale(cpu1)
        print("\nPhysical Machine Parameters")
        storage2=int(input("Enter Storage percentage:[0-100]"))
        memory2=int(input("Enter Memory percentage:[0-100]"))
        network2=int(input("Enter Network level:[0-100]"))
        cpu2=int(input("Enter CPU level:[0-100]"))
        storage2=scale(storage2)
        memory2=scale(memory2)
        network2=scale(network2)
        cpu2=scale(cpu2)
        fault=(a_time,(storage1,memory1,network1,cpu1),(storage2,memory2,network2,cpu2))
        print(fault)
        with engine.prove_goal('Remedyrule.get($fault,$remedy)',fault=fault) as gen:
            for  i,(vars, no_plan) in enumerate(gen):
                #remedy=tuple(vars['remedy'])
                #ob=REMEDY(remedy[0],remedy[1],remedy[2])
                #if (c_check=="y" and t_check=="y"):
                    #min_heap(ob,"prod")
                #elif (c_check=="y"):
                    #min_heap(ob,"cost")
                #elif (t_check=="y"):
                    #min_heap(ob,"time")
                #else: #No priority to solution...displaying all
                #print("Remedy:",ob.cost,ob.name,ob.time)
                print ("Remedy:",vars['remedy'])
            if i==-1:
                print("No remedy available")
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
    check=input("Enter 1 to find remedy;any other key to quit")
    if (check!="1"):
        break
    remedy_list=[]
    #fault=input("Enter the fault:")
    getremedy()