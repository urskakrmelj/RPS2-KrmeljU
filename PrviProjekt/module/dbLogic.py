from module import dbConfig
from module.objects import DnevnikObj

def getAll(param = ""):
    sql = """
        SELECT d.ID, d.DatumCas, d.Visina, d.Teza, d.Itm FROM dnevnik d;
      """
    
    try:
        mydb = dbConfi.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(spl)
        result = cursor.fetchall()
        rtn = []
        for r in result:
            obj = DnevnikObj(r[0],r[1],r[2],r[3],r[4])
            rtn.append(obj)
        return rtn
    except:
        return []
    finally:
        cursor.close()
        mydb.close()
        
        pass
        
def insertData(Visina, teza, itm):
    
    sql = """
    INSERT INTO dnevnik (datumcas, visina, teza, itm)
    VALUES (NOW(), {}, {}, {});
    """ .format(visina, teza, itm)
    
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sqkl)
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        mydb.rollback()
        return vrniID
    finally:
        cursor.close()
        mydb.close()