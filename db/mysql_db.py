# pokemon-app/db/mysql_db.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE"),
        port=int(os.getenv("MYSQL_PORT", 3306))
    )

def insert_pokemon(pokemon: dict):
    conn = get_conn()
    cursor = conn.cursor()
    # Insert or update (ignores duplicate id)
    cursor.execute("""
        INSERT INTO pokemon (id, name, height, weight, type1, type2)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE name=name
    """, (
        pokemon["id"],
        pokemon["name"],
        pokemon.get("height"),
        pokemon.get("weight"),
        pokemon.get("types", ["", ""])[0],
        pokemon.get("types", ["", ""])[1] if len(pokemon.get("types", [])) > 1 else None
    ))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"{pokemon['name']} added to MySQL.")

def search_by_name(name: str):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE name=%s", (name,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def search_by_id(pid: int):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pokemon WHERE id=%s", (pid,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
