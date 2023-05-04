import mysql.connector as con
import csv

def addstud(dabase,tab,cls,sec):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()
    admno=int(input("Enter Addmission number: "))
    cur.execute("select * from A")
    rec=cur.fetchall()
    cur.execute("select * from B")
    rec=rec+cur.fetchall()
    cur.execute("select * from C")
    rec=rec+cur.fetchall()
    f=0
    for i in rec:
        for j in i:
            if i[0]==admno:
                f=1
    if f==0:
        name=input("Enter name: ")
        fname=input("Enter father's name: ")
        sql="insert into {}(admno,name,fname,class,section) values({},'{}','{}',{},'{}')"
        cur.execute(sql.format(tab,admno,name,fname,cls,sec))
        db.commit()
        print("Record Successfully Added")
    else:
        print("Record Already exists")

def addmarks(dabase,tab,cls,sec):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()
    admno=int(input("Enter Addmission number: "))
    sql="select * from {}"
    cur.execute(sql.format(tab))
    f=0
    rec=cur.fetchall()
    for i in rec:
        if i[0]==admno:
            phy=int(input("Enter Physics marks: "))
            chem=int(input("Enter CHemistry marks: "))
            maths=int(input("Enter Maths marks: "))
            eng=int(input("Enter English marks: "))
            opt=int(input("Enter Optional marks: "))
            sql="update {} set Physics={},Chemistry={},Maths={},English={},Optional={} where admno={}"
            cur.execute(sql.format(tab,phy,chem,maths,eng,opt,i[0]))
            f=1
            db.commit()
            print("Marks Successfully Added")
    if f==0:
        print("Record not found")



def deldata(dabase,tab):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()
    print("1.Delete Record by Admno","2.Delete Record by Name",sep='\n')
    x=int(input("Enter choice: "))
    if x==1:
        admno=int(input("Enter Addmission number: "))
        sql="select * from {}"
        cur.execute(sql.format(tab))
        f=0
        rec=cur.fetchall()
        for i in rec:
            if i[0]==admno:
                sql="delete from {} where admno={}"
                cur.execute(sql.format(tab,admno))
                f=1
                db.commit()
                print("Record Successfully Deleted")
        if f==0:
            print("Record not found")

    elif x==2:
        name=input("Enter Student's Name: ")
        sql="select * from {}"
        cur.execute(sql.format(tab))
        f=0
        rec=cur.fetchall()
        for i in rec:
            if i[1]==name:
                sql="delete from {} where name='{}'"
                cur.execute(sql.format(tab,name))
                f=1
                db.commit()
                print("Record Successfully Deleted")
        if f==0:
            print("Record not found")


def update(dabase,tab,cls,sec):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()
    print("1.Change Personal information","2.Change Marks",sep='\n')
    s=int(input("Enter choice: "))
    admno=int(input("Enter Addmission number to modify: "))
    sql="select * from {}"
    cur.execute(sql.format(tab))
    f=0
    rec=cur.fetchall()
    for i in rec:
        if i[0]==admno:
            if s==1:
                admno1=int(input("Enter New Addmission number: "))
                name=input("Enter Student's name: ")
                fname=input("Enter Father's name: ")
                sql="update {} set admno={},name='{}',fname='{}',class={},section='{}' where admno={}"
                cur.execute(sql.format(tab,admno1,name,fname,cls,sec,i[0]))
                f=1
                db.commit()
                print("Successfully Updated")
            elif s==2:
                print("1.Physics","2.Chemistry","3.Maths","4.English","5.Optional",sep='\n')
                h=int(input("Which subject's marks do you want to change: "))
                if h==1:
                    phy=int(input("Enter Physics marks: "))
                    sql="update {} set Physics={} where admno={}"
                    cur.execute(sql.format(tab,phy,i[0]))
                    f=1
                    db.commit()
                    print("Record Successfully Updated")
                elif h==2:
                    chem=int(input("Enter Chemistry marks: "))
                    sql="update {} set Chemistry={} where admno={}"
                    cur.execute(sql.format(tab,chem,i[0]))
                    f=1
                    db.commit()
                    print("Record Successfully Updated")
                elif h==3:
                    maths=int(input("Enter Maths marks: "))
                    sql="update {} set Maths={} where admno={}"
                    cur.execute(sql.format(tab,maths,i[0]))
                    f=1
                    db.commit()
                    print("Record Successfully Updated")
                elif h==4:
                    eng=int(input("Enter English marks: "))
                    sql="update {} set English={} where admno={}"
                    cur.execute(sql.format(tab,eng,i[0]))
                    f=1
                    db.commit()
                    print("Record Successfully Updated")
                elif h==5:
                    opt=int(input("Enter Optional subject marks: "))
                    sql="update {} set Optional={} where admno={}"
                    cur.execute(sql.format(tab,opt,i[0]))
                    f=1
                    db.commit()
                    print("Record Successfully Updated")
                else:
                    print("Invalid Input")
                    
            else:
                print("Invalid Input")
    if f==0:
        print("Record not found")


def search(dabase,tab):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()   
    admno=int(input("Enter Addmission number to search: "))
    sql="select * from {}"
    cur.execute(sql.format(tab))
    f=0
    rec=cur.fetchall()
    for i in rec:
        if i[0]==admno:
            print("\t\t\t\t\t\t\t\t\t-----------REPORT CARD-----------")
            print("\t\t\t\t\t\t\t\t\tCh. Chhabil Dass Public School")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Addmission Number: ",i[0])
            print("Student's Name: ",i[1])
            print("Father's Name: ",i[2])
            print("Class section-",i[3],"-",i[4])
            print()
            print("Subject","Marks",sep='\t\t')
            print("Physics\t\t",i[5])
            print("Chemistry\t",i[6])
            print("Maths\t\t",i[7])
            print("English\t\t",i[8])
            print("Optional\t",i[9])
            print('\n')
            total=i[5]+i[6]+i[7]+i[8]+i[9]
            print("Total Marks: ",total,"/","500")
            per=total*100/500
            print("Percentage: ",per)
            if per > 33:
                print("Result:Pass")
            elif per < 33:
                print("Result:Fail")
            print()
            print("---------------------------------")
            f=1
    if f==0:
        print("Record not found")

def disp(dabase,tab):
    db=con.connect(host="localhost",user="root",passwd="pranav",database=dabase)
    cur=db.cursor()   
    sql="select * from {}"
    cur.execute(sql.format(tab))
    rec=cur.fetchall()
    print("Admno","Name","Class","Section","Physics","Chemistry","Maths","English","Optional",sep='\t')
    for i in rec:
        print(i[0],i[1],i[3],i[4],i[5],i[6],i[7],i[8],i[9],sep='\t')
        print()

def high(dabase):
    db=con.connect(host="localhost",user='root',passwd='pranav',database=dabase)
    cur=db.cursor()
    cur.execute("select * from A")
    rec=cur.fetchall()
    cur.execute("select * from B")
    rec=rec+cur.fetchall()
    cur.execute("select * from C")
    rec=rec+cur.fetchall()
    print("---------------Student's scoring above 90%---------------")
    print("Admno","Name","Class","Section","Percentage",sep='\t')
    for i in rec:
        marks=i[5:10]
        try:
                s=sum(marks)
                per=s*100/500
                if per>90:
                    print(i[0],i[1],i[3],i[4],per,sep='\t')
        except:
                continue
    print('\n\n')
def low(dabase):
    db=con.connect(host="localhost",user='root',passwd='pranav',database=dabase)
    cur=db.cursor()
    cur.execute("select * from A")
    rec=cur.fetchall()
    cur.execute("select * from B")
    rec=rec+cur.fetchall()
    cur.execute("select * from C")
    rec=rec+cur.fetchall()
    for i in rec:
        marks=i[5:10]
        print("---------------Student's scoring below 40%---------------")
        print("Admno","Name","Class","Section","Percentage",sep='\t')
        try:
                s=sum(marks)
                per=s*100/500
                if per<40:
                    print(i[0],i[1],i[3],i[4],per,sep='\t')
        except:
                continue
    print('\n\n')
        
print("-----------Student Report Card Managment-----------")

while True:
    print("1)11th","2)12th","3)Create CSV file","4)Exit",sep='\n')
    a=int(input("Enter class: "))
    if a==1:
        print("1.Section A","2.Section B","3.Section C","4.Show high Achievers","5.Show low achievers",sep='\n')
        b=int(input("Enter choice: "))
        if b==1:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to back menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('eleventh','A',11,'A')
                elif c==2:
                    addmarks('eleventh','A',11,'A')
                elif c==3:
                    update('eleventh','A',11,'A')
                elif c==4:
                    deldata('eleventh','A')
                elif c==5:
                    search('eleventh','A')
                elif c==6:
                    disp('eleventh','A')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break
        elif b==2:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to back menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('eleventh','B',11,'B')
                elif c==2:
                    addmarks('eleventh','B',11,'B')
                elif c==3:
                    update('eleventh','B',11,'B')
                elif c==4:
                    deldata('eleventh','B')
                elif c==5:
                    search('eleventh','B')
                elif c==6:
                    disp('eleventh','B')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break
        elif b==3:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to back menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('eleventh','C',11,'C')
                elif c==2:
                    addmarks('eleventh','C',11,'C')
                elif c==3:
                    update('eleventh','C',11,'C')
                elif c==4:
                    deldata('eleventh','C')
                elif c==5:
                    search('eleventh','C')
                elif c==6:
                    disp('eleventh','C')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break
        elif b==4:
            high('eleventh')
        elif b==5:
            low('eleventh')
        else:
            print("Incorrect Input Try Again")
    elif a==2:
        print("1.Section A","2.Section B","3.Section C",sep='\n')
        b=int(input("Enter choice: "))
        if b==1:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to back menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('twelfth','A',12,'A')
                elif c==2:
                    addmarks('twelfth','A',12,'A')
                elif c==3:
                    update('twelfth','A',12,'A')
                elif c==4:
                    deldata('twelfth','A')
                elif c==5:
                    search('twelfth','A')
                elif c==6:
                    disp('twelfth','A')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break
        elif b==2:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to back menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('twelfth','B',12,'B')
                elif c==2:
                    addmarks('twelfth','B',12,'B')
                elif c==3:
                    update('twelfth','B',12,'B')
                elif c==4:
                    deldata('twelfth','B')
                elif c==5:
                    search('twelfth','B')
                elif c==6:
                    disp('twelfth','B')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break

        elif b==3:
            while True:
                print("1.Add Student","2.Add Marks","3.Update record","4.Delete record","5.Search record","6.Display all","7.Go to Home menu",sep='\n')
                c=int(input("Enter choice: "))
                if c==1:
                    addstud('twelfth','C',12,'C')
                elif c==2:
                    addmarks('twelfth','C',12,'C')
                elif c==3:
                    update('twelfth','C',12,'C')
                elif c==4:
                    deldata('twelfth','C')
                elif c==5:
                    search('twelfth','C')
                elif c==6:
                    disp('twelfth','C')
                elif c==7:
                    break
                else:
                    print("Invalid Input Try Again")
                    print()
                k=input("Do you want to Continue(y/n): ")
                if k=='y' or k=='Y':
                    continue
                else:
                    break
        elif b==4:
            high('twelfth')
        elif b==5:
            low('twelfth')


    elif a==3:
        db=con.connect(host="localhost",user='root',passwd='pranav',database='twelfth')
        cur=db.cursor()
        cur.execute("select * from A")
        rec=cur.fetchall()
        cur.execute("select * from B")
        rec=rec+cur.fetchall()
        cur.execute("select * from C")
        rec=rec+cur.fetchall()
        db=con.connect(host="localhost",user='root',passwd='pranav',database='eleventh')
        cur=db.cursor()
        cur.execute("select * from A")
        rec=rec+cur.fetchall()
        cur.execute("select * from B")
        rec=rec+cur.fetchall()
        cur.execute("select * from C")
        rec=rec+cur.fetchall()
        j=open('Student.csv','w',newline='')
        csv_w=csv.writer(j)
        csv_w.writerow(["Admno","Name","Class","Section","Physics","Chemistry","Maths","English","Optional"])
        csv_w.writerows(rec)
        j.close()
        print("CSV file Student.csv created")
        
    elif a==4:
        break
    
    else:
        print("Invalid Input Try Again")
        print()
