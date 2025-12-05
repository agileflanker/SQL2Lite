
            
#Problem 2
def insertAgentClient(args, cursor, database):
    #parse args
    uid = int(args[0])
    username = args[1]
    email = args[2]
    card_number = int(args[3])
    card_holder = args[4]
    expiration_date = args[5] #YYYY-MM-DD
    cvv = int(args[6])
    zip = int(args[7])
    interests = args[8]

    #check for uid in User
    cursor.execute(f"SELECT uid FROM User WHERE uid = {uid};")
    result = cursor.fetchone()
    if result is None:
        print("Fail")
        return
    
    #check if uid in AgentClient
    cursor.execute(f"SELECT uid FROM AgentClient WHERE uid = {uid};")
    result = cursor.fetchone()
    if result is not None:
        print("Fail")
        return
    
    sql = """
    INSERT INTO AgentClient (uid, interests, cardholder, expire, cardno, cvv, zip)
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(sql, (uid, interests, card_holder, expiration_date, card_number, cvv, zip))
    database.commit()
    print("Success")


#problem 3
def addCustomizedModel(args, cursor, database):
    #parse args
    mid = int(args[0]) #FIXME May need to flip
    bmid = int(args[1])

    #check if bmid in BaseModel
    cursor.execute(f"SELECT bmid FROM BaseModel WHERE bmid = {bmid};")
    result = cursor.fetchone()
    if result is None:
        print("Fail")
        return
    
    #check if mid in CustomizedModel
    cursor.execute(f"SELECT mid FROM CustomizedModel WHERE mid = {mid};")
    result = cursor.fetchone()
    if result is not None:
        print("Fail")
        return
    
    sql = """
    INSERT INTO CustomizedModel (bmid, mid)
    VALUES (%s, %s);
    """
    
    cursor.execute(sql, (bmid, mid))
    database.commit()
    print("Success")

#problem 4
def deleteBaseModel(arg, cursor, database):
    bmid = int(arg)

    #check if bmid in BaseModel
    cursor.execute(f"SELECT bmid FROM BaseModel WHERE bmid = {bmid};")
    result = cursor.fetchone()
    if result is None:
        print("Fail") #FIXME May change based on if fail is if no bmid exists
        return
    
    sql = f"DELETE FROM BaseModel WHERE bmid = %s;"
    cursor.execute(sql, (bmid,))
    database.commit()
    print("Success")

#problem 5
def listInternetService(arg, cursor):
    bmid = int(arg)

    sql = """
    SELECT DISTINCT sid, endpoints, provider
    FROM InternetService
    WHERE sid IN (
        SELECT sid
        FROM ModelServices
        WHERE bmid = %s
    ) 
    ORDER BY provider ASC;
    """ #FIXME might be looking for LLM and DataStorage as well?

    cursor.execute(sql, (bmid,))
    results = cursor.fetchall()

    if len(results) == 0:
        print("Fail") #FIXME might want different input
        return
    
    for row in results:
        print(f'{row[0]},{row[1]},{row[2]}')