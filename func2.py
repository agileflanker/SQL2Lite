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
