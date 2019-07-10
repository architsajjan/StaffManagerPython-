
"""
@author: architsajjan
"""
####################   Import necessary modules   #######################

import mysql.connector
import os.path
import json
import time as t

########################   Global Variables   ###########################

db_val={'dbas':'','usr':'','pswd':'',}                 # database data dict
db=0                                                   # database variable
cur=0                                                  # cursor variable
flag=1                                    # flag variable <flag 1 indicates program's first run on machine>
prog_run=True                             # decides when to exit program loop
############################   FUNCTIONS   ##############################

def get_db_val():
    global db_val
    db_val['dbas']=input("\n\n\n\n\n\t\tEnter database name:")
    db_val['usr']=input("\t\tEnter user name:")
    db_val['pswd']=input("\t\tEnter password:")
    
def cnct_db():
    global db_val,db,cur
    db=mysql.connector.connect(database=db_val['dbas'],user=db_val['usr'],password=db_val['pswd'],host='127.0.0.1')
    cur=db.cursor()
    
def add_staff():
        global cur,db
        fn=input("\n\n\n\t\tEnter first name: ")
        ln=input("\t\tEnter last name: ")
        mob=int(input("\t\tEnter Mobile no.: "))
        eml=input("\t\tEnter Email address: ")
        des=input("\t\tEnter designation: ")
        cur.execute("insert into staff_list(`fname`,`lname`,`mob`,`email`,`des`) values('{}','{}',{},'{}','{}')".format(fn,ln,mob,eml,des))
        db.commit()
    
#def welcome_screen():
    #input("Press Enter to continue..")
    
    
######################################################################### 
def main():
  global flag,prog_run
  if(flag==1):
      cur.execute("create table staff_list (id int NOT NULL PRIMARY KEY AUTO_INCREMENT, fname char(50) NOT NULL, lname char(50) NOT NULL, mob int NOT NULL, email char(50) NOT NULL, des char(20) NOT NULL)")
      flag=flag-1
  try: 
    #welcome_screen()
    
    print("\n\n#############################################################\n")
    print("##\n")
    print("##   A. Add Staff Member\n")
    print("##   B. Retrive Data\n")
    print("##   C. Run a complete sql command\n")
    print("##   E. Exit Program\n")
    print("##\n")      
    print("#############################################################\n")
    ch=input("\n\t\tEnter your choice: ")
    if (ch=='a' or ch=='A'):
        add_staff()
    elif (ch=='b' or ch=='B'):
        print("\n\n\tThis option under construction, try after some time. ")
        t.sleep(1)
    elif (ch=='c' or ch=='C'):
        print("\n\n\tThis option under construction, try after some time. ")
        t.sleep(1)
    elif (ch=='e' or ch=='E'):
        prog_run=False
        db.close()
    else:
        print("Invalid Input")
          
  except(ValueError):
      print("Invalid Input")  
    
#########################################################################    


###############################   MAIN   ################################    


"""
This piece of code is only gonna be
executed at program's first run.
"""

if(os.path.isfile("db_this_sys")):
    with open('db_this_sys','r') as f_db:
         db_val=json.load(f_db)
    f_db.close()
    flag=flag-1
    
else:
    get_db_val()
    with open('db_this_sys', 'w') as f_db:
            json.dump(db_val , f_db)
    f_db.close()
    print("\n\n\tFile Created")
    



# connect to database and create a cursor

input("\n\tPress enter to connect: ")
cnct_db()
input("\n\tConnected.. Press enter to proceed to menu: ")

# main

while(prog_run):
    main()



