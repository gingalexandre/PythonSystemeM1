#! /usr/bin/python3
# -*- coding: utf8 -*-

__author__ = 'Mathieu Mourot, Alexandre GINGEMBRE, Arthur MOUREY et Baptiste ROUX'

import sqlite3
#connection = sqlite3.connect("BDD_tweets.db")
conn = None
try :
    # Cas où on initialise la base
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        age INTERGER
    )
    """)
    conn.commit()
except sqlite3.OperationalError:
    # Cas où la base existe déjà
    cursor.execute("""SELECT id, name, age FROM users""")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} \t {2}'.format(row[0], row[1], row[2]))
    users = []
    users.append(("olivier", 30))
    users.append(("jean-louis", 90))
    cursor.executemany("""
    INSERT INTO users(name, age) VALUES(?, ?)""", users)
    cursor.execute("""SELECT id, name, age FROM users""")
    rows = cursor.fetchall()
    for row in rows:
        print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
except Exception as e:
    print("Erreur")
    conn.rollback()
    # raise e
finally:
    conn.commit() #Sauvegarde des données dans la base
    conn.close()
