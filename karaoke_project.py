# Projeto Musica pro karaoke
import sqlite3 as db
from datetime import datetime, timedelta
import time
import os

class mexe_banco (): 
    def __init__(self):
        try:
            self.conn = db.connect('musicas.db')
            self.cur = self.conn.cursor()
            print('Conexão bem sucedida')
           # self.cur.execute('CREATE TABLE IFNOT EXISTS tocatta ')
            
        except Exception as e:
            print("Erro na conexão", e)
    
    def fetchall(self):
        return self.cur.fetchall()

    def query(self, sql, params=None):
        self.cur.execute(sql, params or ())
        return self.fetchall()
    
    def execute(self, sql, params=None):
        self.cur.execute(sql, params or ())

    def reset(self):
        self.cur.execute('UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME="tocatta"')
        self.cur.execute('DELETE FROM tocatta ')
        self.conn.commit()
        return print(' reset do id concluido')
    
    def adicionar_valor(self,comanda, id, time):
        
        self.cur.execute('INSERT INTO tocatta (comanda, hora, id_cliente) VALUES (?, ?, ?)', (comanda,  time, id))
        self.conn.commit()

    def calcula_tempo (self,tt):
        agora = datetime.now()
        data_hora_formatada = datetime(tt)
        diferenca = agora - data_hora_formatada
        return diferenca.total_seconds() / 60
    
    def ve_por_hora(self):
        tabs = (self.query(f'''SELECT * FROM tocatta ORDER BY hora DESC LIMIT 20'''))
        for row in tabs:
                u = row[0]
                d = row[1]
                t = row[2]
                q = row[3]
                print ('|',u, ' |  ' ,d,'   | ',t,' |   ',q,' ')
        
         
    def procura(self,com):
        apps = (self.query(f"""
                    SELECT comanda, id_cliente, hora FROM tocatta WHERE comanda = '{com}' ORDER BY hora DESC 
                  ;"""))
        if apps:
            print (' Resultado da procura pela comanda: ',com)
            print('\n')
            x = 1
            for row in apps:
                    #um = row[0]
                    dos = row[1]
                    tre = row[2]  
                    if x == 1:
                        print('Cantor/Mesa  --> ',dos)
                        print('Hora da ultima cantada  --> ',tre)
                        x =x + 1
                    else: x= x+1
            print ('\n', (x-1),' -> Quantidade que a comanda ', com, ' cantou')
        else: print('A comanda ', com , ' não foi encontrado')
    def menu ():
        print('------------------------------')
        print('1- Inserir musica')
        print('2- Procurar por comanda')
        print('3- Mostrar Lista ')
        print('0- Sair')
        print('------------------------------\n')
        z =input('Sua escolha: ')
        return z



class tudo (mexe_banco): 
    def __init__(self):
        mexe_banco.__init__(self)
        i = True
        while i == True:
            x = mexe_banco.menu()
            if (x == '1'):
                com = input('\n Numero da comanda: ')
                nome = input(' Id dos cantores: ')
                xx = input(' Inserir hora manual s/n? ')
                if xx =='s' or xx =='1' or xx=='S':
                    tim = input(' Hora desejada:  ')
                else: 
                    tim = datetime.now().strftime('%H:%M')
                mexe_banco.adicionar_valor(self,com, nome, tim)
            elif(x == '0'): i = False
            elif(x =='2'): 
                cc = input('Qual comanda deseja procurar? ')
                mexe_banco.procura(self,cc)
            elif (x=='reset'):
                mexe_banco.reset(self)
            elif (x=='clear'):
                os.system('cls')
            else: 
                print('| ID | Comanda |  Hora   |  Identificador ')
                mexe_banco.ve_por_hora(self)


if __name__ == "__main__":
    
    banco = tudo()