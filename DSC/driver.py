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

class hashtable(object):
    """docstring for ."""
    def __init__(self):
        self.list1 = [0,0,0,0,0,0,0,0,0,0]
hashobbjects=[]
for i in range(100):
    new=hashtable()
    hashobbjects.append(new)

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
        
def search(key,curr):#curr is a tuple(fault,remedy)
    primary_key=key%100
    sec_key=key//100
    if(hashobbjects[primary_key-1].list1[sec_key-1]==0):
        raise KeyError('key not found') 
    else:
        temp=hashobbjects[primary_key-1].list1[sec_key-1]
#        print(temp)
        for value in temp:
            if(curr==value[0]):
                return value[1]
def insert(key,curr):
    primary_key=key%100
    sec_key=key//100
    if(hashobbjects[primary_key-1].list1[sec_key-1]==0):
        hashobbjects[primary_key-1].list1[sec_key-1]=[curr]
    else:
        hashobbjects[primary_key-1].list1[sec_key-1].append(curr)

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
            op=search(sum1,fault)
            print(op)
        except:
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
                    insert(sum1,(fault,('Insert the fault here','Insert best possible remedy here')))
                if i==-1:
                    print("No remedy available")
                    insert(sum1,(fault,'No Remedy Availaible'))
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