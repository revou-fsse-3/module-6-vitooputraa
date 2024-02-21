from os import path,getcwd

def getSqlPhat():
    basedir = path.join(getcwd(), "app", "assets")
    dbPhat='sqlite:///' + path.join(basedir, 'data.db')
    return dbPhat