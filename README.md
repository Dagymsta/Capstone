Comp Track:
Employer Competency Tracking Application

Log in with email and password. Developer has created admin profile for Managers. All user profiles must change passwords after login.
There are 2 different menus. One is an admin menu for managers another is for users. 

Original Admin ID: Email=someone@devpipeline.com
                    Password=Manager
Manager/Admin Menu:
	1. View/Edit Users
	2. View/Edit Reports
	3. View/Edit Learning
	4. Export/Import
	5. Logout

1. View/Edit Users:
    -This has 7 operations
    1.View All Users
    2.Search User
    3.Edit User
    4.Add User
    5.Activate/Deactivate User
    6.Return to Main Menu
    *View All Users - Allows admin to View all Users/Employees information registered in Comp Track app, Admin or User.
        ~User information provided
            -User ID
            -First Name
            -Last Name
            -Phone Number
            -Email
            -Password
            -Date Created
            -Hire Date
            -Active/Inactive
            -Manager status
        ~Password is not available to see in database. Manager must reset password if User forgets password.
        ~Manager status will be established at initial set up and cannot be changed. If User becomes Manager admin must set up a new manager profile.	
    *Search User
        ~Allows admin to search user by first and last name and see user information.
        ~If first and last name not entered correctly. The application will not provide any data
    *Edit User
        ~Allows Manager to Edit information of user, change password of user and activate and deactivate user.
    *Add User
        ~Allows manager to add any type of user, and their personal information. 
        ~Manager will set password and then user can use password and change to their own password after initial log in.
    *Activate/Deactivate User
        ~Allows admin to Activate and Deactivate a user.
        ~When a user is deactivated they cannot will not be able to access their profile.
        ~This can be used for both users and managers.
        ~Admin can reactivate user after deactivation.
        ~All information will be available after reactivation.
    *Return to Main Menu
        ~Takes user back to Main Menu of program

2. View/Edit Reports
    -Has 5 operators
    1.View Reports
    2.Add Score
    3.Change score
    4.Delete Score
    5.Return to Main Menu
    *View Reports
        ~Allows Manager to view results of all assessments taken for their corresponding competency for all users.
        ~Also allows to search for individual results and provides a search tool.
        ~If User has not taken assessment there will be no assessment result to display.
    *Add Score
        ~Allows Manager to add a result of an assessment finished by user.
    *Change Score
        ~Allows Manager to change a result of an assessment
    *Delete Score
        ~Allows Manager to delete a result of an assessment. 
        ~Once this information is deleted there is no bringing it back.
    *Return to Main Menu
        ~Returns user to Main Menu

3. View/Edit Learning
    -Has 7 operations
    1.View Competencies
    2.View Assessments
    3.Add Competency
    4.Add Assessment
    5.Edit Competency
    6.Edit Assessment
    7.Return to Main Menu
    *View Competencies
        ~Allows Manager to View all competencies created
    *View Assessments
        ~Allows Manager to view all assessments created
    *Add Competency
        ~Allows Manager to Add a competency
    *Add Assessment
        ~Allows Manager to Add an assessment and assign that assessment to a competency
        ~It is best to create the competency first before creating a corresponding assessment.
        ~If assessment is added before creating competency, manager can assign assessment in edit assessment operation. 
    *Edit Competency
        ~Allows manager to edit the name of a competency
        ~Also allows another avenue to create a new competency.
    *Edit Assessment
        ~Allows manager to edit name of assessment
        ~Allows manager to add assessment to Competency
        ~Allows manager to add a result of an assessment
        ~Allows manager to change a result of an assessment
        ~Allows manager to Delete Assessment Result
    *Return to Main Menu
        ~Returns Manager to Main Menu

4. Export/Import
    -Has 4 Operations
    1.Export User Information
    2.Export Results
    3.Import Results
    4.Return to Main Menu
    *Export User Information
        ~Allows Manager to export user information to a csv file to be printed
    *Export Results
        ~Allows Manager to export assessment results
        ~Report will contain Result ID, User ID, Assessment ID, Competency Score, Date Taken and Admin ID
    *Import Results
        ~Allows Manager to import results to data base from a pre-written CSV file.
        ~Information must contain user_id, assessment_id, score and date taken.
    *Return to Main Menu
        ~Takes Manager back to Main Menu

5. Logout
        ~Logs manager out of application

User Menu
	1. Edit User Information
	2. View Reports
	3. Export Files
	4. Logout

1. Edit User Information
        ~Allows User to edit their own personal information 
        ~Allows User to change their password
    *Return to Main Menu
        ~Allows User to Return to Main Menu

2. View Reports
        ~Allows User to View all of their assessment/competency results
    *Press 1 to return to main menu
        ~Returns user to main menu

3. Export Files 
        ~Allows users to Export assessment results
    *Do you want to Export your results?
        ~Confirms with user that they want to export their results with Yes or No prompt
4. Logout
        ~Logs user out of application

