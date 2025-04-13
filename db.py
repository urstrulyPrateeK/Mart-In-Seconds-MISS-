import pymysql as sqltr
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
import os

timestamp = str(time.time())


myconn = sqltr.connect(host='localhost',
                        user='root',
                        password='0000',
                        cursorclass=sqltr.cursors.DictCursor)
cursor = myconn.cursor()

def renewBase():
    try:
        cursor.execute('DROP DATABASE MISS;')
        myconn.commit()
    except:
        pass


def base():
    try:
        cursor.execute('CREATE DATABASE MISS;')
        myconn.commit()
        
        cursor.execute('USE MISS;')
        myconn.commit()

        cursor.execute('''CREATE TABLE PRICES
        (NAME VARCHAR(100),
        PRICE DECIMAL(10, 2));''')
        myconn.commit()

        cursor.execute('''INSERT INTO PRICES(NAME, PRICE) VALUES
        ("POTATO", 12.6),
        ("TOMATO", 60.4),
        ("LEMON", 30.7),
        ("LADY_FINGER", 20.8),
        ("BRINJAL", 25.2),
        ("SPINACH", 15.6),
        ("CAULIFLOWER", 45.4),
        ("CUCUMBER", 10.3),
        ("ONION", 30.2),
        ("RADDISH", 25.5);''')
        myconn.commit()

        cursor.execute('''INSERT INTO PRICES(NAME, PRICE) VALUES
        ("SHIRTS", 300.0),
        ("JEANS", 200.0),
        ("LEMON", 250.0),
        ("PANTS", 500.0),
        ("JACKETS", 700.0),
        ("SAREES", 600.0),
        ("SHORTS", 800.0),
        ("TROUSERS", 350.0),
        ("SWEATERS", 800.0),
        ("PYJAMAS", 250.0);''')
        myconn.commit()

        cursor.execute('''INSERT INTO PRICES(NAME, PRICE) VALUES
        ("TV", 300.0),
        ("MOBILE_PHONES", 200.0),
        ("WASHING_MACHINES", 250.0),
        ("MICROWAVE", 500.0),
        ("OVEN", 700.0),
        ("HEAD_PHONES", 600.0),
        ("EARPHONES", 800.0),
        ("REFRIGERATOR", 350.0),
        ("WATER_PURIFIERS", 800.0),
        ("HAND_MIXERS", 250.0);''')
        myconn.commit()

        cursor.execute('''CREATE TABLE VEGETABLES
        (NAME VARCHAR(100),
        MOBILE_NO VARCHAR(20),
        POTATO INT,
        TOMATO INT,
        LEMON INT,
        LADY_FINGER INT,
        BRINJAL INT,
        SPINACH INT,
        CAULIFLOWER INT,
        CUCUMBER INT,
        ONION INT,
        RADDISH INT,
        TOTAL DECIMAL(10, 2));''')
        myconn.commit()

        cursor.execute('''CREATE TABLE CLOTHING 
        (NAME VARCHAR(100),
        MOBILE_NO VARCHAR(20),
        SHIRTS INT,
        JEANS INT,
        PANTS INT,
        JACKETS INT,
        SAREES INT,
        SHORTS INT,
        SUITS INT,
        TROUSERS INT,
        SWEATERS INT,
        PYJAMAS INT,
        TOTAL DECIMAL(10, 2));''')                       
        myconn.commit()

        cursor.execute('''CREATE TABLE ELECTRONICS
        (NAME VARCHAR(100),
        MOBILE_NO VARCHAR(20),
        TV INT,
        MOBILE_PHONES INT,
        WASHING_MACHINES INT,
        MICROWAVE INT,
        OVEN INT,
        HEAD_PHONES INT,
        EARPHONES INT,
        REFRIGERATOR INT,
        WATER_PURIFIERS INT,
        HAND_MIXERS INT,
        TOTAL DECIMAL(10, 2));''')
        myconn.commit()

        cursor.execute('''CREATE TABLE LOGIN
        (USERNAME VARCHAR(100),
        PASSWORD VARCHAR(100));''')
        myconn.commit()

        cursor.execute('INSERT INTO LOGIN(USERNAME, PASSWORD) VALUES("{}", "{}");'.format('username', 'password'))
        myconn.commit()

    except Exception as e:
        print(e)


def login(username, password):
    cursor.execute('USE MISS;')
    myconn.commit()
    
    cursor.execute('SELECT * FROM LOGIN;')
    data = cursor.fetchmany()
    print(data)
    
    if [{'USERNAME': username, 'PASSWORD': password}] == data:
        return True

    return False


def getPrice(name):
    cursor.execute('USE MISS;')
    myconn.commit()
    
    cursor.execute(f'SELECT * FROM PRICES WHERE UPPER(NAME) = "{name.upper()}";')
    data = cursor.fetchall()
    print(data, name)

    if not data:
        print(f"No price found for {name}")
        return 0  # or raise an error
    
    return data[0]['PRICE']


# def addVegetables(name, mobile,Potato,Tomato,Lemon,Lady_Finger,Brinjal,Spinach,Cauliflower,Cucumber,Onion,Radish, total):

#     cursor.execute('USE MISS;')
#     myconn.commit()

#     Potato = ','.join(map(str, Potato))
#     Tomato = ','.join(map(str, Tomato))
#     Lemon = ','.join(map(str, Lemon))
#     Lady_Finger = ','.join(map(str, Lady_Finger))
#     Brinjal = ','.join(map(str, Brinjal))
#     Spinach = ','.join(map(str, Spinach))
#     Cauliflower = ','.join(map(str, Cauliflower))
#     Cucumber = ','.join(map(str, Cucumber))
#     Onion = ','.join(map(str, Onion))
#     Radish = ','.join(map(str, Radish))


#     total = str(total)

#     print(f'''INSERT INTO VEGETABLES(NAME,MOBILE_NO,POTATO ,TOMATO ,LEMON ,LADY_FINGER ,BRINJAL ,SPINACH ,CAULIFLOWER ,CUCUMBER ,ONION ,RADDISH ,
#         TOTAL)  VALUES("{name}", "{mobile}", {Potato}, {Tomato}, {Lemon}, {Lady_Finger}, {Brinjal}, {Spinach}, {Cauliflower}, {Cucumber}, {Onion},{Radish}, {total} );''')

#     cursor.execute(f'''INSERT INTO VEGETABLES(NAME,MOBILE_NO,POTATO ,TOMATO ,LEMON ,LADY_FINGER ,BRINJAL ,SPINACH ,CAULIFLOWER ,CUCUMBER ,ONION ,RADDISH ,
#         TOTAL)  VALUES("{name}", "{mobile}", {Potato}, {Tomato}, {Lemon}, {Lady_Finger}, {Brinjal}, {Spinach}, {Cauliflower}, {Cucumber}, {Onion},{Radish}, {total} );''')
#     myconn.commit()


def addVegetables(name, mobile, q, d, total):
    cursor.execute('USE MISS;')
    myconn.commit()

    print(f'''INSERT INTO VEGETABLES(NAME,MOBILE_NO,{d},TOTAL) VALUES
    ("{name}", "{mobile}", {q}, {total});''')

    cursor.execute(f'''INSERT INTO VEGETABLES(NAME,MOBILE_NO,{d},TOTAL) VALUES
    ("{name}", "{mobile}", {q}, {total});''')
    myconn.commit()


def getVegetables():
    cursor.execute('USE MISS;')
    myconn.commit()
    
    cursor.execute('SELECT * FROM VEGETABLES;')
    data = []
    for row in cursor:
        print(row)
        x = []
        for r in row:
            if row[r] is None:
                x.append('')
            else:
                x.append(row[r])
        data.append(x)

    print(data)

    return data



def addClothing(name, mobile, q, d, total):
    cursor.execute('USE MISS;')
    myconn.commit()

    print(f'''INSERT INTO CLOTHING(NAME, MOBILE_NO, {d}, TOTAL) VALUES ("{name}", "{mobile}", {q}, {total});''')

    cursor.execute(f'''INSERT INTO CLOTHING(NAME, MOBILE_NO, {d}, TOTAL) VALUES ("{name}", "{mobile}", {q}, {total});''')
    myconn.commit()

def getClothing():
    cursor.execute('USE MISS')
    myconn.commit()
    
    cursor.execute('SELECT * FROM CLOTHING;')
    data = []
    for row in cursor:
        print(row)
        x = []
        for r in row:
            if row[r] is None:
                x.append('')
            else:
                x.append(row[r])
        data.append(x)

    print(data)

    return data

def addElectronics(name, mobile, q, d, total):
    cursor.execute('USE MISS;')
    myconn.commit()

    print(f'''INSERT INTO ELECTRONICS(NAME, MOBILE_NO, {d}, TOTAL) VALUES ("{name}", "{mobile}", {q}, {total});''')

    cursor.execute(f'''INSERT INTO ELECTRONICS(NAME, MOBILE_NO, {d}, TOTAL) VALUES ("{name}", "{mobile}", {q}, {total});''')
    myconn.commit()

def getElectronics():
    cursor.execute('USE MISS')
    myconn.commit()
    
    cursor.execute('SELECT * FROM ELECTRONICS;')
    data = []
    for row in cursor:
        print(row)
        x = []
        for r in row:
            if row[r] is None:
                x.append('')
            else:
                x.append(row[r])
        data.append(x)

    print(data)

    return data

def updateVegetables(name, inp, val):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute('DESCRIBE VEGETABLES;')

    for i, row in enumerate(cursor):
        print(row)
        if i == int(inp[3:]) - 1:
            column = row['Field']
            break
            
    cursor.execute(f'SELECT * FROM VEGETABLES WHERE NAME = "{name}";')

    data = []
    for row in cursor:
        data.append(row)

    cursor.execute(f'SELECT * FROM PRICES WHERE NAME = "{column}";')

    prices = []
    for row in cursor:
        prices.append(row)

    print(prices)
    total = float(data[0]['TOTAL'])
    total += float(val) * float(prices[0]['PRICE'])
    
    c = list(data[0].keys())[int(inp[3:]) - 1]
    if data[0][c] is not None:
        total -= float(data[0][c]) * float(prices[0]['PRICE'])

    cursor.execute(f'UPDATE VEGETABLES SET {column} = {val}, TOTAL = {total} WHERE NAME = "{name}";')
    myconn.commit()
    

def updateClothing(name, inp, val):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute('DESCRIBE CLOTHING;')

    for i, row in enumerate(cursor):
        if i == int(inp[3:]) - 1:
            column = row['Field']
            break
            
    cursor.execute(f'SELECT * FROM CLOTHING WHERE NAME = "{name}";')

    data = []
    for row in cursor:
        data.append(row)

    cursor.execute(f'SELECT * FROM PRICES WHERE NAME = "{column}";')

    prices = []
    for row in cursor:
        prices.append(row)

    print(prices)
    total = float(data[0]['TOTAL'])
    total += float(val) * float(prices[0]['PRICE'])
    
    c = list(data[0].keys())[int(inp[3:]) - 1]
    if data[0][c] is not None:
        total -= float(data[0][c]) * float(prices[0]['PRICE'])

    cursor.execute(f'UPDATE CLOTHING SET {column} = {val}, TOTAL = {total} WHERE NAME = "{name}";')
    myconn.commit()

def updateElectronics(name, inp, val):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute('DESCRIBE ELECTRONICS;')

    for i, row in enumerate(cursor):
        if i == int(inp[3:]) - 1:
            column = row['Field']
            break
            
    cursor.execute(f'SELECT * FROM ELECTRONICS WHERE NAME = "{name}";')

    data = []
    for row in cursor:
        data.append(row)

    cursor.execute(f'SELECT * FROM PRICES WHERE NAME = "{column}";')

    prices = []
    for row in cursor:
        prices.append(row)

    total = float(data[0]['TOTAL'])
    total += float(val) * float(prices[0]['PRICE'])
    
    c = list(data[0].keys())[int(inp[3:]) - 1]
    if data[0][c] is not None:
        total -= float(data[0][c]) * float(prices[0]['PRICE'])

    cursor.execute(f'UPDATE ELECTRONICS SET {column} = {val}, TOTAL = {total} WHERE NAME = "{name}";')
    myconn.commit()

def deleteVegetables(name):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute(f'DELETE FROM VEGETABLES WHERE NAME = "{name}";')
    myconn.commit()

def deleteClothing(name):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute(f'DELETE FROM CLOTHING WHERE NAME = "{name}";')
    myconn.commit()

def deleteElectronics(name):
    cursor.execute('USE MISS;')
    myconn.commit()

    cursor.execute(f'DELETE FROM ELECTRONICS WHERE NAME = "{name}";')
    myconn.commit()

filename = f'piechart_{timestamp}.png'

def pieChart():
    cursor.execute('USE MISS;')
    myconn.commit()

    plt.clf()

    cursor.execute("SELECT SUM(TOTAL) FROM VEGETABLES")
    for c in cursor:
        vTotal = float(c['SUM(TOTAL)'] if c['SUM(TOTAL)'] is not None else 0)

    cursor.execute("SELECT SUM(TOTAL) FROM CLOTHING")
    for c in cursor:
        cTotal = float(c['SUM(TOTAL)'] if c['SUM(TOTAL)'] is not None else 0)

    cursor.execute("SELECT SUM(TOTAL) FROM ELECTRONICS")
    for c in cursor:
        eTotal = float(c['SUM(TOTAL)'] if c['SUM(TOTAL)'] is not None else 0)

    labels = ['Vegetable Store', 'Clothing Store', 'Electronics Store']
    sizes=[vTotal, cTotal, eTotal]
    colors=['yellowgreen', 'lightskyblue', 'gold']
    plt.pie(sizes, labels=labels, colors=colors, startangle=90, autopct='%.1f%%')

    if os.path.exists('piechart.png'):
        os.remove('piechart.png') 

    filename = 'piechart.png'
    plt.savefig(f'static/images/{filename}')
    
    return filename  # Return the filename
