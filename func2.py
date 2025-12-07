# Problem 6
def countCustomizedModel(bmids: list[int], cursor):
    # Create placeholders of proper length for WHERE condition
    placeholders = ', '.join(['%s'] * len(bmids))

    sql = f"""
    SELECT B.bmid, B.description, COUNT(C.mid) as customizedModelCount
    FROM BaseModel B
    LEFT JOIN CustomizedModel C ON B.bmid = C.bmid
    WHERE B.bmid IN ({placeholders})
    GROUP BY B.bmid
    ORDER BY B.bmid ASC;
    """

    cursor.execute(sql, bmids)
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]},{row[1]},{row[2]}")

# Problem 7
def topNDurationConfig(uid: int, N: int, cursor):
    sql = """
    SELECT C.client_uid, C.cid, C.labels, C.content, MAX(MC.duration) as max_duration
    FROM Configuration C 
    JOIN ModelConfigurations MC ON MC.cid = C.cid
    WHERE C.client_uid = %s
    GROUP BY C.cid
    ORDER BY max_duration DESC
    LIMIT %s;
    """

    cursor.execute(sql, (uid, N))
    results = cursor.fetchall()

    for row in results:
        print(f"{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}")