import sqlite3



def conectar():
    conn = sqlite3.connect(r'C:/Users/douglas.favaro/PycharmProjects/ProcessMapping_v1/process_mapping.db')
    conn.execute("""CREATE TABLE IF NOT EXISTS processos(
        cordenada_X TEXT ,
        coordenada_Y TEXT,
        hora TEXT NOT NULL,
        aplicacao TEXT NOT NULL,
        tecla TEXT);""")
    return conn

def desconectar(conn):
    conn.close()

def insertMouse(conn,x,y,agora,app,key):
    conn = conectar()
    cursor = conn.cursor()
    #query = f"INSERT INTO processos(cordenada_X, coordenada_Y,aplicacao) VALUES({x},{y},{str(app)})"
    cursor.execute("INSERT INTO processos(cordenada_X, coordenada_Y,hora,aplicacao, tecla) VALUES(?,?,?,?,?)",(x,y,agora,str(app),str(key)))
    conn.commit()

    if cursor.rowcount ==1:
        print("Insert realizado com sucesso.")


def insertKeyboard(conn,app,agora, key):
    conn = conectar()
    cursor = conn.cursor()
    #query = f"INSERT INTO processos(aplicacao, tecla ) VALUES({str(app)}, {key})"
    #query = "INSERT INTO processos(aplicacao,hora, tecla ) VALUES(?,?,?)"
    data_tuple = (app, key)
    cursor.execute("INSERT INTO processos(aplicacao,hora, tecla ) VALUES(?,?,?)", (str(app),agora,str(key)))
    conn.commit()

    if cursor.rowcount ==1:
        print("Insert realizado com sucesso.")

def select(conn):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("Select * from processos")
    processos = cursor.fetchall()

    if len(processos)>0:
        for item in processos:
            print(f'X:{item[0]}')
            print(f'Y:{item[1]}')
            print(f'HORA:{item[2]}')
            print(f'APLICACAO:{item[3]}')
            print(f'TECLA:{item[4]}')

    else:
        print("Sem processos mapeados")
        desconectar(conn)
def update():
    pass

