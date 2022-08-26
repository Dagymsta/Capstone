import csv
import bcrypt



import sqlite3 
from datetime import datetime

connection = sqlite3.connect('comp_track.db')
cursor = connection.cursor()
salt=b'$2b$12$9jdfToNNzn4tTcQiF3TBQ.'
def user_view_competency_results(user_id):
    value= (user_id,)
    sql_inquiry= "SELECT Competencies.comp_name, Assessments.assessment_name, Results.comp_score, Results.date_taken FROM Assessments JOIN Competencies ON Assessments.comp_id=Competencies.comp_id JOIN Results ON Assessments.assessment_id=Results.assessment_id WHERE user_id = ?"
    rows= cursor.execute(sql_inquiry,value).fetchall()

    print(f'{"Competency":<15} {"Assessment":<30} {"Competency Score":<20} {"Date Taken"}')
    print(f'{"----------":<15} {"----------":<30} {"----------------":<20} {"----------"}')

    for row in rows:
        comp_name,assessment_name,comp_score,date_taken=row
        comp_name= comp_name if comp_name != None else ""
        assessment_name= assessment_name if assessment_name!= None else""
        comp_score= comp_score if comp_score != None else ""
        date_taken= date_taken if date_taken!= None else ""
        print(f'{comp_name:<15}|{assessment_name:<30}|{comp_score:<20}|{date_taken}')

def user_update(user_id):
    while True:
        print("\n***Update User Information***")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. email")
        print("5. Password")
        print("6. Quit\n")
        prompt= input("Enter number affiliated with data needing updated or enter Q for quit if you are done updating information: ")
        if prompt == "1":
            prompt_2=input("Enter new first name: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET first_name= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged First Name")
        elif prompt== "2":
            prompt_2=input("Enter new last name: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET last_name= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged Last Name")
        elif prompt == "3":
            prompt_2=input("Enter new phone number: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET phone= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged phone number")
        elif prompt == "4":
            prompt_2=input("Enter new email: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET email= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged email")
        elif prompt == "5":
            recieve=input("Enter new password: ")
            password = bcrypt.hashpw(recieve.encode("utf-8"),salt)
            values= (password,user_id)
            sql_update=(f'UPDATE Users SET password= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged password")
        elif prompt=="6":
            break
        else:
            print("Not a Valid Entry")

def export_user_data(user_id):
    value=(user_id,)
    sql_inquiry="SELECT * from Results WHERE user_id=? "
    row=cursor.execute(sql_inquiry,value).fetchall()
    with open("results_database.csv","w") as outfile:
        wrt=csv.writer(outfile)
        header=["result_id","user_id","assessment_id","comp_score","date_taken","admin_id"]
        wrt.writerow(header)
        wrt.writerows(row)

def manager_view_all():
    rows= cursor.execute("SELECT user_id, first_name,last_name,phone,email,date_created,hire_date FROM Users WHERE active=1").fetchall()
  
    print(f'{"User_ID":<12} {"First Name":<12} {"Last Name":<12} {"Phone":<20} {"Email":<30}{"Date Created":<30} {"Hire Date"}')
    print(f'{"-------":<12} {"----------":<12} {"---------":<12} {"-----":<20} {"-----":<30}{"------------":<30} {"---------"}')

    for row in rows:
        user_id,first_name,last_name,phone,email,date_created,hire_date=row
        user_id=user_id if user_id != None else""
        first_name= first_name if first_name != None else ""
        last_name= last_name if last_name != None else""
        phone= phone if phone!= None else""
        email= email if email!= None else ""
        date_created= date_created if date_created!= None else""
        hire_date= hire_date if hire_date!= None else""
       
        
        print(f'{user_id:<12}|{first_name:<12}|{last_name:<12}|{phone:<20}|{email:<30}|{date_created:<30}|{hire_date}')

def manager_search_users():
        first_name=input("Enter First Name: ")
        name_1=f'%{first_name}%'
        last_name=input("Enter Last Name: ")
        name_2=f'%{last_name}%'
        rows = cursor.execute("SELECT user_id,first_name,last_name,phone,email,date_created,hire_date FROM Users WHERE first_name LIKE ? AND last_name LIKE ?",(name_1,name_2)).fetchall()
        
        print(f'{"User_ID":<12} {"First Name":<12} {"Last Name":<12} {"Phone":<20} {"Email":<30} {"Date Created":<30}{"Hire Date"}')
        print(f'{"-------":<12} {"----------":<12} {"---------":<12} {"-----":<20} {"-----":<30} {"------------":<30}{"---------"}')
        for row in rows:
            user_id,first_name,last_name,phone,email,date_created,hire_date=row
            user_id=user_id if user_id!=None else""
            first_name=first_name if first_name != None else ""
            last_name=last_name if last_name != None else""
            phone= phone if phone!= None else ""
            email=email if email!= None else""
            date_created=date_created if date_created!= None else""
            hire_date=hire_date if hire_date!= None else""
            print(f'{user_id:<12}|{first_name:<12}|{last_name:<12}|{phone:<20}|{email:<30}|{date_created:<30}{hire_date}')

def view_report():
    while True:
        print("***Reports***")
        print("1. View All")
        print("2. View Individual")
        print("3. Quit")
        prompt=input("\nEnter number of desired action: ")
        if prompt== "1":
            rows = cursor.execute("SELECT Results.user_id, Users.first_name, Users.last_name, Competencies.comp_name, Results.comp_score FROM Results JOIN Users ON Results.user_id=Users.user_id JOIN Assessments ON Assessments.assessment_id= Results.assessment_id JOIN Competencies ON Competencies.comp_id=Assessments.comp_id ORDER BY last_name DESC").fetchall()
        
            print(f'{"User_ID":<9}{"First Name":<20}{"Last Name":<25}{"Competency":<30}{"Comp_Score"}')
            print(f'{"-------":<9}{"----------":<20}{"---------":<25}{"----------":<30}{"----------"}')
            for row in rows:
                user_id,first_name,last_name,comp_name,comp_score=row
                user_id=user_id if user_id!=None else""
                first_name=first_name if first_name != None else ""
                last_name=last_name if last_name != None else""
                comp_name=comp_name if comp_name != None else""
                comp_score= comp_score if comp_score!= None else""
                print(f'{user_id:<9}|{first_name:<19}|{last_name:<23}|{comp_name:<30}|{comp_score}')
        elif prompt=="2":
            entry=input("Enter First name of User: ")
            first_name=f'%{entry}%'
            entry_2=input("Enter Last name of User: ")
            last_name=f'%{entry_2}%'
            rows = cursor.execute("SELECT Results.user_id, Users.first_name, Users.last_name, Competencies.comp_name, Results.comp_score FROM Results JOIN Users ON Results.user_id=Users.user_id JOIN Assessments ON Assessments.assessment_id= Results.assessment_id JOIN Competencies ON Competencies.comp_id=Assessments.comp_id Where first_name LIKE ? AND last_name LIKE?",(first_name,last_name)).fetchall()
        
            print(f'{"User_ID":<9}{"First Name":<20}{"Last Name":<25}{"Competency":<30}{"Comp_Score"}')
            print(f'{"-------":<9}{"----------":<20}{"---------":<25}{"----------":<30}{"----------"}')
            for row in rows:
                user_id,first_name,last_name,comp_name,comp_score=row
                user_id=user_id if user_id!=None else""
                first_name=first_name if first_name != None else ""
                last_name=last_name if last_name != None else""
                comp_name=comp_name if comp_name!= None else""
                comp_score= comp_score if comp_score!= None else""
                print(f'{user_id:<9}|{first_name:<19}|{last_name:<23}|{comp_name:<30}|{comp_score}')
        elif prompt=="3":
            break
        else:
            print("Please Enter Valid Input")

def view_user_id():
    rows= cursor.execute("SELECT first_name, last_name, user_id ,active FROM Users").fetchall()
    
    print(f'{"First Name":<12}{"Last Name":<13}{"User_ID":<13}{"Active?"}')
    print(f'{"----------":<12}{"---------":<13}{"-------":<13}{"-------"}')
    for row in rows:
        first_name,last_name,user_id,active=row
        first_name=first_name if first_name != None else""
        last_name=last_name if last_name!= None else""
        user_id=user_id if user_id != None else""
        active=active if active!=None else""
    
        print(f'{first_name:<12}|{last_name:<12}|{user_id:<12}|{active}')
   
def view_assesments():
    view_user_id()
    prompt=input("\nEnter user_id of user: ")
    value=(prompt,)
    sql_query="SELECT Results.user_id,Results.assessment_id,Assessments.assessment_name,Assessments.date_created FROM Results JOIN Assessments ON Results.assessment_id=Assessments.assessment_id WHERE user_id=?"
    rows= cursor.execute(sql_query,value).fetchall()
  
    print(f'{"User_ID":<14} {"Assessment ID":<18} {"Assessment Name":<25} {"Date Created"}')
    print(f'{"-------":<14} {"-------------":<18} {"---------------":<25} {"------------"}')

    for row in rows:
        user_id,assessment_id,assessment_name,date_created=row
        user_id= user_id if user_id!= None else ""
        assessment_id=assessment_id if assessment_id != None else""
        assessment_name= assessment_name if assessment_name!= None else ""
        date_created=date_created if date_created!= None else""
        
        print(f'{user_id:<14}|{assessment_id:<18}|{assessment_name:<25}|{date_created}')

def add_user():
    first_name = input('Enter first name: ')
    last_name = input('Enter last_name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')
    recieve=input("Enter password: ")
    password = bcrypt.hashpw(recieve.encode("utf-8"),salt)
    date_created= datetime.now()
    hire_date= input('Enter date of hire in mm/dd/yyyy format: ')
    manager=""
    while True:   
        if manager!="0" and manager!="1":
            manager=input("Manager?\n1 for yes\n0 for no ")
        else:
            break

    insert_sql = "INSERT INTO Users(first_name,last_name,phone,email,password,date_created,hire_date,manager) VALUES(?,?,?,?,?,?,?,?)"
    values = (first_name,last_name,phone,email,password,date_created,hire_date,manager)
    cursor.execute(insert_sql,values)
    connection.commit()
    return print("User record added")

def add_competency():
    comp_name=input("Enter enter name of Competency: ")
    date_created= datetime.now()
    values=(comp_name,date_created)
    insert_sql= "INSERT INTO Competencies(comp_name,date_created) VALUES(?,?)"
    cursor.execute(insert_sql,values)
    connection.commit()
    return print("New competency created")

def view_manager_id():
    rows= cursor.execute("SELECT first_name, last_name, user_id FROM Users WHERE manager=1").fetchall()
    
    print(f'{"First Name":<13}{"Last Name":<13}{"User_ID"}')
    print(f'{"----------":<13}{"---------":<13}{"-------"}')
    for row in rows:
        first_name,last_name,user_id=row
        first_name=first_name if first_name != None else""
        last_name=last_name if last_name!= None else""
        user_id=user_id if user_id != None else""
    
        print(f'|{first_name:<12}|{last_name:<12}|{user_id}')

def view_assessment_id():
    rows= cursor.execute("SELECT assessment_name,date_created,assessment_id FROM assessments").fetchall()
    
    print(f'{"Assessment Name":<30}{"Date Created":<30}{"Assessment ID"}')
    print(f'{"---------------":<30}{"------------":<30}{"-------------"}')
    for row in rows:
        assessment_name,date_created,assessment_id=row
        assessment_name=assessment_name if assessment_name != None else""
        date_created=date_created if date_created!= None else""
        assessment_id=assessment_id if assessment_id != None else""
    
        print(f'|{assessment_name:<30}|{date_created:<29}|{assessment_id}')

def view_comp_id():
    rows= cursor.execute("SELECT comp_name,date_created,comp_id FROM Competencies").fetchall()
    
    print(f'{"Comp Name":<20}{"Date Created":<30}{"Comp_ID"}')
    print(f'{"---------":<20}{"------------":<30}{"-------"}')
    for row in rows:
        comp_name,date_created,comp_id=row
        comp_name=comp_name if comp_name != None else""
        date_created=date_created if date_created!= None else""
        comp_id=comp_id if comp_id!= None else""
    
        print(f'{comp_name:<20}|{date_created:<28}|{comp_id}')

def add_new_assessment():
    name=input("Enter assessment name: ")
    date_created=datetime.now()
    view_comp_id()
    comp_id=input("\nEnter ID of affiliated competency: ")
    values=(name,comp_id,date_created)
    insert_sql= "INSERT INTO Assessments(assessment_name,comp_id,date_created) VALUES(?,?,?)"
    cursor.execute(insert_sql,values)
    connection.commit()
    return print("\nAssessment Created")

def add_result():
    view_user_id()  
    user_id = input("\nEnter ID of User: ")
    view_assessment_id()
    assessment_id=input("\nEnter ID of Assessment to be reported: ")
    view_manager_id()
    admin_id=input("\nEnter ID of Manager Administering Test: ")
    date_taken=datetime.now()
    print ("\n0:No competency- Needs Training and Direction\n1:Basic Competency- Needs Ongoing Support\n2:Intermediate Competency- Needs Occasional Support\n3:Advanced Competency- Completes Task Independently\n4:Expert Competency- Can Effectively pass on this knowledge and can initiate optimizations")
    score= input("\nEnter Score of Assessment 1-4: ")
    while True:
        if score in ["0","1","2","3","4"]:
            sql_update=(f'INSERT INTO Results (user_id,assessment_id,comp_score,date_taken,admin_id) VALUES (?,?,?,?,?)')
            update_values=(user_id,assessment_id,score,date_taken,admin_id)
            cursor.execute(sql_update,update_values)
            connection.commit()
            return print("\nResult has been recorded")
        else:
            print("\nIt appears there was an error, please make sure tthat you entered a valid score for the assessment\n")

def change_score():
    view_user_id()  
    user_id = input("\nEnter ID of User: ")
    view_assessment_id()
    assessment_id=input("\nEnter ID of Assessment to be edited: ")
    while True:
        print("\n0:No competency- Needs Training and Direction\n1:Basic Competency- Needs Ongoing Support\n2:Intermediate Competency- Needs Occasional Support\n3:Advanced Competency- Completes Task Independently\n4:Expert Competency- Can Effectively pass on this knowledge and can initiate optimizations\n")
        score=input("Enter new score: ")
        if score in ["0","1","2","3","4"]:
            sql_update=(f'UPDATE Results SET comp_score=? WHERE user_id=? AND assessment_id=?')
            values=(score,user_id,assessment_id)
            cursor.execute(sql_update,values)
            connection.commit()
            return print("Score has been changed")
        else:
            print("\nPlease enter a valid score number\n")

def delete_assessment_result():
    view_user_id()  
    user_id = input("\nEnter ID of User: ")
    view_assessment_id()
    assessment_id=input("\nEnter ID of Assessment to be edited: ")
    sql_delete="DELETE FROM Results Where user_id=? AND assessment_id=?"
    values=(user_id,assessment_id)
    cursor.execute(sql_delete,values)
    connection.commit()
    return print("Assessment Result Deleted")

def manager_edit_user_info():
    view_user_id()
    user_id=input("\nEnter ID of User to edit information: ")
    while True:
        print("***Update User Information***")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. email")
        print("5. Password")
        print("6. Quit")
        prompt= input("Enter number affiliated with data needing updated or enter Q for quit if you are done updating information: ")
        if prompt == "1":
            prompt_2=input("Enter new first name: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET first_name= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged first name\n")
        elif prompt== "2":
            prompt_2=input("Enter new last name: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET last_name= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged last name\n")
        elif prompt == "3":
            prompt_2=input("Enter new phone number: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET phone= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged Phone Number\n")
        elif prompt == "4":
            prompt_2=input("Enter new email: ")
            values= (prompt_2,user_id)
            sql_update=(f'UPDATE Users SET email= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged email\n")
        elif prompt == "5":
            recieve=input("Enter password: ")
            password = bcrypt.hashpw(recieve.encode("utf-8"),salt)
            values= (password,user_id)
            sql_update=(f'UPDATE Users SET password= ? WHERE user_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nChanged password\n")
        elif prompt=="6":
            break
        else:
            print("Not a Valid Entry") 

def edit_competencies():
    while True:
        print("***Competencies editor***")
        print("1.Edit name of competency")
        print("2.Create Competency")
        print("3.Quit")
        prompt=input("\nEnter affiliated number to desired action listed: ")
        if prompt=="1":
            view_comp_id()
            comp_id= input("\nEnter ID of Competency: ")
            comp_name=input("\nEnter new name of Competency: ")
            values= (comp_name,comp_id)
            sql_update=(f'UPDATE Competencies SET comp_name= ? WHERE comp_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nCompetency Name Changed\n")
        elif prompt=="2":
            add_competency()
        elif prompt=="3":
            break
        else:
            print("\nNot a Valid Entry\n") 
    
def edit_assessments():         
    while True:
        print("***Assessments editor***")
        print("1.Edit name of Assessment")
        print("2.Add Assessment to Competency")
        print("3.Enter Result of Assessment")
        print("4.Change score for assessment")
        print("5.Delete an Assessment Result")
        print("6.Quit")
        prompt=input("\nEnter affiliated number to desired action listed: ")
        if prompt=="1":
            view_assessment_id()
            assess_id= input("\nEnter ID of assessment: ")
            assess_name=input("\nEnter new name of assessment: ")
            values= (assess_name,assess_id)
            sql_update=(f'UPDATE assessments SET assessment_name= ? WHERE assessment_id=?')
            cursor.execute(sql_update,values)
            connection.commit()
            print("\nAssessment Name Changed\n")
        elif prompt=="2":
            add_new_assessment()
        elif prompt=="3":
            add_result()
        elif prompt== "4":
            change_score()
        elif prompt=="5":
            delete_assessment_result()
        elif prompt=="6":
            break
        else:
            print("Not a Valid Entry") 

def export_users_to_csv():
    row=cursor.execute("Select * from Users").fetchall()
    with open("users_database.csv","w") as outfile:
        wrt=csv.writer(outfile)
        header=["user_id","first_name","last_name","phone","email","password","date","hire_date","active","manager"]
        wrt.writerow(header)
        wrt.writerows(row)

def export_results_to_csv():
    row=cursor.execute("Select * from Results").fetchall()
    with open("results_database.csv","w") as outfile:
        wrt=csv.writer(outfile)
        header=["result_id","user_id","assessment_id","comp_score","date_taken","admin_id"]
        wrt.writerow(header)
        wrt.writerows(row)

def import_csv_to_database():
    with open("assessment.csv","r") as infile:
        
        values=infile.readlines()[1::]
        for value in values:
            value=value.strip().split(",")
            sql_import="INSERT INTO Results(user_id,assessment_id,comp_score,date_taken) VALUES(?,?,?,?)"
            print(value)
            cursor.execute(sql_import,value)
        connection.commit()

def activate_deactivate():
    while True:
        prompt_2=input("(A)ctivate\n(D)eactivate\n(Q)uit\n").lower()
        if prompt_2=="a":
            view_user_id()
            id =input(f'Enter ID # of user to activate: ')
            sql_update=(f'UPDATE Users SET active=1 WHERE user_id=?')
            update_values=(id,)
            cursor.execute(sql_update,update_values)
            connection.commit()
            sql_update
            return print(f'User #{id} has been activated')
        elif prompt_2=="d":
            view_user_id()
            id=input(f'Enter ID of User to deactivate: ')
            while True:
                confirm=input(f'Are you sure you want to deactivate User#{id}?\n(Y) for yes\n(N) for no\n').lower()
                if confirm=='y':
                        sql_update=(f'UPDATE Users SET active=0 WHERE user_id=?')
                        update_values=(id,)
                        cursor.execute(sql_update,update_values)
                        connection.commit()
                        return print(f'User#{id} has been deactivated')
                elif confirm=='n':
                    break
        elif prompt_2=="q":
            break
        else:
            print("invalid character")

def manager_menu():
    prompt=""
    while True:
        print("\n***Admin Menu***")
        print("1. View/Edit Users")
        print("2. View/Edit Reports")
        print("3. View/Edit Learning")
        print("4. Export/Import")
        print("5. Logout\n")
        prompt=input("Enter Number of desired action: ")
        if prompt=="1":
            while True:
                print("\n***View/Edit Users***")
                print("1. View All Users")
                print("2. Search User")
                print("3. Edit User")
                print("4. Add User")
                print("5. Activate/Deactivate User")
                print("6. Return to Main Menu")
                prompt2=input("\nEnter Number of desired action: ")
                if prompt2=="1":
                    manager_view_all()
                elif prompt2=="2":
                    manager_search_users()
                elif prompt2=="3":
                    manager_edit_user_info()
                elif prompt2=="4":
                    add_user()
                elif prompt2=="5":
                    activate_deactivate()
                elif prompt2== "6":
                    break
                else:
                    print("Please enter valid input")
        elif prompt=="2":
            while True:
                print("\n***View/Edit Reports***")
                print("1. View Reports")
                print("2. Add Score")
                print("3. Change Score")
                print("4. Delete Score")
                print("5. Return to Main Menu\n")
                prompt2=input("\nEnter Number of desired action: ")
                if prompt2=="1":
                    view_report()
                elif prompt2=="2":
                    add_result()
                elif prompt2=="3":
                    change_score()
                elif prompt2=="4":
                    delete_assessment_result()
                elif prompt2=="5":
                    break
                else:
                    print("Please enter a valid input")
        elif prompt=="3":
            while True:
                print("\n***View/Edit Learning***")
                print("1. View Competencies")
                print("2. View Assessments")
                print("3. Add Competency")
                print("4. Add Assessment")
                print("5. Edit Competency")
                print("6. Edit Assessment")
                print("7. Return to Main Menu\n")
                prompt2=input("\nEnter Number of desired action: ")
                if prompt2=="1":
                    view_comp_id()
                elif prompt2=="2":
                    view_assesments()
                elif prompt2=="3":
                    add_competency()
                elif prompt2=="4":
                    add_new_assessment()
                elif prompt2=="5":
                    edit_competencies()
                elif prompt2=="6":
                    edit_assessments()
                elif prompt2=="7":
                    break
                else:
                    print("Please enter a valid input")
        elif prompt=="4":
            while True:
                print("\n***Export/Import***")
                print("1. Export User Information")
                print("2. Export Results")
                print("3. Import Results")
                print("4. Return to Main Menu\n")
                prompt2=input("\nEnter Number of desired action: ")
                if prompt2=="1":
                    export_users_to_csv()
                elif prompt2=="2":
                    export_results_to_csv()
                elif prompt2=="3":
                    import_csv_to_database()
                elif prompt2=="4":
                    break
                else:
                    print("Please enter a valid input")
        elif prompt=="5":
            print("\nLogged out")
            break
        else:
            print("Please enter valid input")

def user_menu(user_id):
    while True:
        print("\n***User Menu***")
        print("1. Edit User Information")
        print("2. View Reports")
        print("3. Export Files")
        print("4. Logout\n")
        prompt=input("Enter Number of desired action: ")
        if prompt=="1":
            while True:
                print("\n***View Edit User info***")
                print("1. Edit Information")
                print("2. Return to Main Menu")
                prompt2= input("Enter Number of desired action: ")
                if prompt2== "1":
                    user_update(user_id)
                elif prompt2== "2":
                    break
                else: 
                    print("Please Enter valid input")
        elif prompt=="2":
            while True:
                print("\n***View Reports***\n")
                user_view_competency_results(user_id)
                prompt_2=input("\nPress 1 to return to main menu: ")
                if prompt_2== "1":
                    break
                else:
                    print("Press 1 to return to Main Menu")
        elif prompt== "3":
            while True:
                print("\n***Export***")
                print("Do you want to Export your results?")
                print("(Y)es")
                print("(N)o")
                print("(Q)uit")
                prompt2= input().lower()
                if prompt2== "y":
                    export_user_data(user_id)
                elif prompt2=="n":
                    break
                elif prompt2== "q":
                    break
                else:
                    print("Please enter valid input")
        elif prompt=="4":
            print("Good Bye")
            break
        else:
            print("Please enter valid input")
    
def login():
    email=input("Enter User email: ")
    elist=[]
    sql_find_email=("SELECT email FROM Users WHERE active=1")
    rows= cursor.execute(sql_find_email,).fetchall()
    for row in rows:
        elist.append(row[0])
    while True:
        if email in elist:
            password=input("Enter password: ")
            values=(email,)
            sql_find_email=("SELECT password FROM Users WHERE email=?")
            row= cursor.execute(sql_find_email,values).fetchone()
            recieve=bcrypt.hashpw(password.encode("utf-8"),salt)
            if recieve == row[0] :
                sql_find_email=("SELECT manager FROM Users WHERE email=?")
                row= cursor.execute(sql_find_email,values).fetchone() 
                manager=row[0]
                if manager== 1:
                    manager_menu() 
                    break
                elif manager== 0:
                    value=(email,)
                    sql_find_user_id=("SELECT user_id FROM Users WHERE email=?")
                    row= cursor.execute(sql_find_user_id,value).fetchone()
                    user_id=row[0]
                    user_menu(user_id)
                    break
                else:
                    print("It appears there is a technical issue. Please contact you IT cordinator")
            else:
                print("Invalid Password Try again")
        else:
            print("\ntry again\n")
            
login()
    