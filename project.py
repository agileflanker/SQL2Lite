import mysql.connector
import sys
import parser

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, x in enumerate(sys.argv):        # For debugging ###############################################################
            print(i, x)
        
        cmd = sys.argv[1]
        match (cmd):
            case "import":                  # import [folderName:str]
                pass
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
