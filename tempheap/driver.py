# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:42:25 2017

@author: Yatish H R
"""
import sys
from pyke import knowledge_engine, krb_traceback

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
                    print('hello')
                    remedy_list[i]=remedy_list[2*i+2]
                    remedy_list[2*i+2]=temp
            except:
                if(compare(remedy_list[i],remedy_list[2*i+1],criteria)):
                    temp=remedy_list[i]
                    remedy_list[i]=remedy_list[2*i+1]
                    remedy_list[2*i+1]=temp
                    print('hello')
        for i in remedy_list:
            print(i)
     
     
#    for i in remedy_list:
#        print(i)
#        
    

def getremedy(fault):
    engine.reset()
    i=-1
    try:
        engine.activate('remedyget')
        c_check=input("Is cost an issue?:[y/n]")
        c_check=c_check[0].lower()
        t_check=input("Is time an issue?;[y/n]")
        t_check=t_check[0].lower()
        with engine.prove_goal('remedyget.get($fault,$remedy)',fault=fault) as gen:
            for  i,(vars, no_plan) in enumerate(gen):
                remedy=tuple(vars['remedy'])
                ob=REMEDY(remedy[0],remedy[1],remedy[2])
                remedy_list.append(ob)
            if (c_check=="y" and t_check=="y"):
                min_heap("prod")
            elif (c_check=="y"):
                min_heap("cost")
            elif (t_check=="y"):
                min_heap("time")
            else: #No priority to solution...displaying all
                print("Remedy:",remedy[0])
            if i==-1:
                print("No remedy available")
            elif (c_check=="y" or t_check=="y"):
                print ("\nRemedy:",remedy_list[0].name,"Cost:",remedy_list[0].cost,"Time:",remedy_list[0].time,"is the best solution")
                print("All solutions: ")
                
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
    fault=input("Enter the fault:")
    getremedy(fault)