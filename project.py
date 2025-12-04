import mysql.connector
import sys

#Our functions
import parser
import func1 as f1

def convert_null_to_none(args):
    for i in range(len(args)):
        if args[i] == "NULL":
            args[i] = None
    return args

# Connect to the database
database = mysql.connector.connect(
    host="localhost",
    user="test",
    password="password",
    database="cs122a"
)

cursor = database.cursor()

if __name__ == "__main__":
    sys.argv = convert_null_to_none(sys.argv) #This is so 'NULL' will not be inputted, but instead None
    if len(sys.argv) > 1:
        for i, x in enumerate(sys.argv):        # For debugging ###############################################################
            print(i, x)
        
        cmd = sys.argv[1]
        print(f"Command: {cmd}\n\n")
        match (cmd):
            case "import":                  # import [folderName:str]
                parser.import_data(sys.argv[2], cursor, database)
            case "insertAgentClient":       # insertAgentClient [uid:int]           [username:str] 
                f1.insertAgentClient(sys.argv[2:], cursor, database)                            #                   [email:str]         [card_number:int] 
                                            #                   [card_holder:str]   [expiration_date:date] 
                                            #                   [cvv:int]           [zip:int] 
                                            #                   [interests:str]
                pass
            case "addCustomizedModel":      # addCustomizedModel [mid:int] [bmid:int]
                f1.addCustomizedModel(sys.argv[2:], cursor, database)
            case "deleteBaseModel":         # deleteBaseModel [bmid:int]
                f1.deleteBaseModel(sys.argv[2], cursor, database)
            case "listInternetService":     # listInternetService [bmid:int]
                f1.listInternetService(sys.argv[2], cursor)
            case "countCustomizedModel":    # countCustomizedModel [bmid:int]
                pass
            case "topNDurationConfig":      # topNDurationConfig [uid:int] [N:int]
                pass
            case "listBaseModelKeyWord":    # listBaseModelKeyWord [keyword:str]
                pass
            case _:
                print(f"Invalid command: {cmd}")
        

    else:
        print("No arguments found.")


cursor.close()
database.close()