import mysql.connector

connection = mysql.connector.connect(
    user = "hoang",
    port=3306,
    password = "hoangvu",
    host = "localhost",
    database = "hoang",
    collation = "utf8mb4_general_ci",
    charset = "utf8mb4",
    autocommit = True
)
#1
import sqlite3


def fetch_airport_details(icao_code):

    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()
    query = '''
    SELECT name, municipality FROM airport WHERE ident = ?
    '''

    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    conn.close()
    if result:
        airport_name, town = result
        print(f"Airport Name: {airport_name}")
        print(f"Location (Town): {town}")
    else:
        print(f"No airport found with ICAO code: {icao_code}")


def main():
    icao_code = input("Enter the ICAO code of the airport: ").upper().strip()

    fetch_airport_details(icao_code)


if __name__ == "__main__":
    main()
#2
import sqlite3

def fetch_airports_by_country(area_code):

    conn = sqlite3.connect('airports.db')
    cursor = conn.cursor()


    query = '''
    SELECT type, COUNT(*) as airport_count 
    FROM airport 
    WHERE iso_country = ? 
    GROUP BY type 
    ORDER BY type
    '''

    cursor.execute(query, (area_code,))
    results = cursor.fetchall()
    conn.close()

    if results:
        print(f"Airports in country with area code {area_code}:")
        for row in results:
            airport_type, count = row
            print(f"{airport_type}: {count} airport(s)")
    else:
        print(f"No airports found for country code: {area_code}")

def main():
    area_code = input("Enter the area code (e.g., FI for Finland): ").upper().strip()

    fetch_airports_by_country(area_code)

if __name__ == "__main__":
    main()
