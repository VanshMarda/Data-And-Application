import subprocess as sp
import pymysql
import pymysql.cursors
import datetime

def search():
    try:
        # letter = input(First letter)
        query = "select H.sport_name from equipment as H where H.quantity in (select max(quantity) from equipment); "
        print(query)
        cur.execute(query)
        con.commit()

        print("Sports with max equipment fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return
def maxEquip():
    try:
        query = "select H.sport_name from equipment as H where H.quantity in (select max(quantity) from equipment); "
        print(query)
        cur.execute(query)
        con.commit()

        print("Sports with max equipment fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return

def lhostel():
    try:
        query = "select H.hostel_name from hostel as H where H.no_of_students in (select min(no_of_students) from hostel);"
        print(query)
        cur.execute(query)
        con.commit()

        print("Least populated hostel fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return

def amount():
    try:
        query = "select sum(P.salary) from professors;"
        print(query)
        cur.execute(query)
        con.commit()

        print("Total salary fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return
    
def avgStd():
    try:
        query = "select avg(S.no_of_students) from subjects as S;"
        print(query)
        cur.execute(query)
        con.commit()

        print("Avg no. of fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return

def labSub():
    try:
        query = "select count(*) from subjects as S where S.labs = 'Y';"
        print(query)
        cur.execute(query)
        con.commit()

        print("Subjects having lab fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return

def studgt30():
    try:
        query = "select course_id, subject_name from subjects where subjects.no_of_students > 30;"
        print(query)
        cur.execute(query)
        con.commit()

        print("Subjects having more than 30 students fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to get required details")
        print(">>>>>>>>>>>>>>",e)

    return

def nonEquipSports():
    try:
        query = "select S.sport_name from sports as S left join equipment as E on S.sport_name = E.sport_name where E.quantity is not NULL and E.quantity > 0;"
        print(query)
        cur.execute(query)
        con.commit()

        print("Sports with no equipment fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch sport details")
        print(">>>>>>>>>>>>>>",e)

    return

def deptBuilding():
    try:
        building_no = int(input("Buildin No: "))
        query = "select * form department as D where D.building_no = %d;" % (building_no)
        print(query)
        cur.execute(query)
        con.commit()

        print("Department Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch department details")
        print(">>>>>>>>>>>>>>",e)

    return

def profDetails():
    try:
        prof_id = int(input("Professor ID: "))
        query = "select * form professors as P where P.prof_id = %d;" % (prof_id)
        print(query)
        cur.execute(query)
        con.commit()

        print("Professor Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch professor details")
        print(">>>>>>>>>>>>>>",e)

    return

def studentDetails():
    try:
        rollno = int(input("Roll No: "))
        query = "select * form students as S where S.roll_no = %d;" % (rollno)
        print(query)
        cur.execute(query)
        con.commit()

        print("Student Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch student details")
        print(">>>>>>>>>>>>>>",e)

    return

def equipDetails():
    try:
        sport = input("Enter Sport Name: ")
        query = "select * from equipment as E where E.sport_name = '%s';" % (sport)
        print(query)
        cur.execute(query)
        con.commit()

        print("Equipment Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch equipment details")
        print(">>>>>>>>>>>>>>",e) 

    return

def allEquip():
    try:
        query = "select * from equipment;"
        print(query)
        cur.execute(query)
        con.commit()

        print("Equipment Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch equipment details")
        print(">>>>>>>>>>>>>>",e) 

    return

def subDetails():
    try:
        sub = int(input("Course_id : "))
        query = "select * from subjects where course_id = %d;" % (sub)
        print(query)
        cur.execute(query)
        con.commit()

        print("Details fetched!")

    except Exception as e:
        con.rollback()
        print("Failed to fetch subject details")
        print(">>>>>>>>>>>>>>",e)  

    return

def newClub():
    try:
        row = {}
        print("Enter Club details: ")
        row["name"] = input("Name: ")
        row["no_of_members"] = int(input("No. of members: "))
        no_of_coords = int(input("No. of Coordinators (max 3): "))
        row["coord1"] = input("Coord 1 : ")
        if(no_of_coords > 1):
            row["coord2"] = input("Coord 2 : ")

        else:
            row["coord2"] = "NULL"

        if(no_of_coords > 2):
            row["coord3"] = input("Coord 3 : ")

        else:
            row["coord3"] = "NULL"

        query = " "
        print(query)
        cur.execute(query)
        con.commit()

        print("Added new club!")

    except Exception as e:
        con.rollback()
        print("Failed to add new club")
        print(">>>>>>>>>>>>>>",e)              

    return 

def recruitProf():
    try:
        row = {}
        print("Enter new proff's details: ")
        # name = (input("Name (Fname Minit Lname): ")).split(' ')
        name = (input("Name (Fname Minit Lname): "))
        # row["Fname"] = name[0]
        # row["Minit"] = name[1]
        # row["Lname"] = name[2]
        row["Prof_id"] = int(input("Prof_id: "))
        row["Sex"] = input("Sex(F/M): ")
        row["Salary"] = int(input("Salary: "))
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Dept"] = (input("Department: "))
        row["course_id"] = int(input("course_id: "))
        row["super_prof_id"] = int(input("super_prof_id: "))

        # derive age
        bdate = row["Bdate"]
        blist = bdate.split('-')
        dob = datetime.date(int(blist[0]),int(blist[1]),int(blist[2]))
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        query = " INSERT INTO professors values ('%d','%s','%c','%s,'%d','%d','%s','%s,'%d')" % (
            row["Prof_id"], name, row["Sex"], row["Dept"], row["Salary"], row["course_id"], row["Bdate"],age, row["super_prof_id"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Added Student to the Database!")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def admitAStudent():

    try:
        row = {}
        print("Enter new student's details: ")
        # name = (input("Name (Fname Minit Lname): ")).split(' ')
        name = (input("Name (Fname Minit Lname): "))
        # row["Fname"] = name[0]
        # row["Minit"] = name[1]
        # row["Lname"] = name[2]
        row["Roll_No"] = int(input("Roll No: "))
        # row["CGPA"] = input("CGPA: ")
        row["Sex"] = input("Sex(F/M): ")
        row["Batch"] = input("Batch: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Email"] = (input("Email: "))
        row["Dept"] = (input("Department: "))
        row["Hostel"] = input("Hostel: ")
        row["Password"] = (input("Password: "))

        # derive age
        bdate = row["Bdate"]
        blist = bdate.split('-')
        dob = datetime.date(int(blist[0]),int(blist[1]),int(blist[2]))
        today = datetime.date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        query = " INSERT INTO students values ('%d', NULL,'%c','%s',%d,'%s','%s','%s','%s','%s','%s')" % (
            row["Roll_No"], row["Sex"], row["Batch"], age, row["Dept"], row["Email"], row["Bdate"], name, row["Password"], row["Hostel"])

        # null is for cgpa

        print(query)
        cur.execute(query)
        con.commit()

        print("Added Student to the Database!")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if (ch == 1):
        admitAStudent()
    elif(ch == 2):
        recruitProf()
    # elif(ch == 3):
    #     option3()
    # elif(ch == 4):
    #     option4()
    else:
        print("Error: Invalid Option")


# Global
while (1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user=username,
                              password=password,
                              db='project_final',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if (con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
