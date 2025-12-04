import mysql.connector
import sys
import parser

#Our functions
import table_functions as tf

# Connect to the database
database = mysql.connector.connect(
    host="localhost",
    user="test",
    password="password",
    database="cs122a"
)

cursor = database.cursor()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, x in enumerate(sys.argv):        # For debugging ###############################################################
            print(i, x)
        
        cmd = sys.argv[1]
        print(f"Command: {cmd}\n\n")
        match (cmd):
            case "import":                  # import [folderName:str]
                tf.import_data(sys.argv[2], cursor, database)
            case "insertAgentClient":       # insertAgentClient [uid:int]           [username:str] 
                                            #                   [email:str]         [card_number:int] 
                                            #                   [card_holder:str]   [expiration_date:date] 
                                            #                   [cvv:int]           [zip:int] 
                                            #                   [interests:str]
                pass
            case "addCustomizedModel":      # addCustomizedModel [mid:int] [bmid:int]
                pass
            case "deleteBaseModel":         # deleteBaseModel [bmid:int]
                pass
            case "listInternetService":     # listInternetService [bmid:int]
                pass
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