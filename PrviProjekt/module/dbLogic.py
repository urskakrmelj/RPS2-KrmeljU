from module import dbConfig

def getAll(param = ""):
    
    try:
        mydb = dbConfi.dbConnect()
        cursor = mydb.cursor()
        
        cursor.close()
        mydb.close()
        return True
        
    except:
        return False
        
    finally:
        pass