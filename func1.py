

#Problem 2
def insertAgentClient(args, cursor, database):
    #print(f'Args after splicing: {args}\n\n')
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
