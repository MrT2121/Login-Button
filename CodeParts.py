#LOGS USER IN
def handlePushButton():
    global userID_logged # store userid of logged in globally
    #mitigate sql error
    try:
        sqlselect = "select * from UserTable where Username = '"  + textbox.value + "'" 
    except sqlite3.Error as er:
        print('sql error you are not allowed to login')
        quit()
    
   
    print(sqlselect)
    print(textbox.value)
    rows = query_database(database_file, sqlselect)
    print(rows)
    print(len(rows))
   # 
    print('hello')
    #check user has been found
    if len(rows) > 0:
        #check password seperatly and not in the select statment to mitigate sql injection
        #
        if passbox.value == rows[0][2]:
            info("Logged On Succesfully", "User Found")
            userID_logged = rows[0][0]
            HandleDashboard()
        else:
            info("Not Ok", "Password Incorrect")
    else:
        info("Not Ok", "User Not Found")
