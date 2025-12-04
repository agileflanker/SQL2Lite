import os
import csv

tables = ["User", 
          "AgentCreator",
          "AgentClient",
          "BaseModel",
          "CustomizedModel",
          "Configuration",
          "InternetService",
          "LLMService",
          "DataStorage",
          "ModelServices",
          "ModelConfigurations"
    ]

#helper function to delete all tables
def delete_tables(cursor, database):
    #cannot drop user when it is referenced by other tables
    #drop in reverse order to avoid this
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    for table in reversed(tables): 
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    database.commit()

#create all the tables with the HW2 solutions
def create_tables(cursor, database):
    #create User
    cursor.execute("""CREATE TABLE User (
    uid INT,
    email TEXT NOT NULL,
    username TEXT NOT NULL,
    PRIMARY KEY (uid)
    );
    """)
    
    cursor.execute("""CREATE TABLE AgentCreator (
    uid INT,
    bio TEXT,
    payout TEXT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""CREATE TABLE AgentClient (
    uid INT,
    interests TEXT NOT NULL,
    cardholder TEXT NOT NULL,
    expire DATE NOT NULL,
    cardno INT NOT NULL,
    cvv INT NOT NULL,
    zip INT NOT NULL,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""CREATE TABLE BaseModel (
    bmid INT,
    creator_uid INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (bmid),
    FOREIGN KEY (creator_uid) REFERENCES AgentCreator(uid) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""CREATE TABLE CustomizedModel (
    bmid INT,
    mid INT NOT NULL,
    PRIMARY KEY (bmid, mid),
    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE
    );
    """)
    
    cursor.execute("""CREATE TABLE Configuration (
    cid INT,
    client_uid INT NOT NULL,
    content TEXT NOT NULL,
    labels TEXT NOT NULL,
    PRIMARY KEY (cid),
    FOREIGN KEY (client_uid) REFERENCES AgentClient(uid) ON DELETE CASCADE
    );
    """)

    cursor.execute("""CREATE TABLE InternetService (
    sid INT,
    provider TEXT NOT NULL,
    endpoints TEXT NOT NULL,
    PRIMARY KEY (sid)
    );
    """)

    cursor.execute("""CREATE TABLE LLMService (
    sid INT,
    domain TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """)

    cursor.execute("""CREATE TABLE DataStorage (
    sid INT,
    type TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """)

    cursor.execute("""CREATE TABLE ModelServices (
    bmid INT NOT NULL,
    sid INT NOT NULL,
    version INT NOT NULL,
    PRIMARY KEY (bmid, sid),
    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE,
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
    );
    """)

    cursor.execute("""CREATE TABLE ModelConfigurations (
    bmid INT NOT NULL,
    mid INT NOT NULL,
    cid INT NOT NULL,
    duration INT NOT NULL,
    PRIMARY KEY (bmid, mid, cid),
    FOREIGN KEY (bmid, mid) REFERENCES CustomizedModel(bmid, mid) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES Configuration(cid) ON DELETE CASCADE
    );
    """)

    database.commit()


#import function
def import_data(folder, cursor, database):
    delete_tables(cursor, database)
    create_tables(cursor, database)

    for table in tables:
        path = os.path.join(folder, f'{table}.csv')
        with open(path, mode='r', newline='') as f: #open the file
            reader = csv.reader(f) #read the csv file
            next(reader) #skip first row of column titles
            for row in reader:
                #print(row)
                placeholders = ','.join(['%s'] * len(row)) 
                sql = f"INSERT INTO {table} VALUES ({placeholders})"
                cursor.execute(sql, row)
    database.commit()
