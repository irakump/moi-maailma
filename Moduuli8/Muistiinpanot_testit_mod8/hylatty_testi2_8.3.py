#testi 8.3

from geopy import distance
"""
wellington = (-41.32, 174.81)
salamanca = (40.96, -5.50)
print(distance.distance(wellington, salamanca).km)
#19959.6792674
"""
######

import mysql.connector


connection = mysql.connector.connect(
             host='127.0.0.1',
             port= 3306,
             database='flight_game',
             user='ira',
             password='lunni',
             autocommit=True
             )

def find_coordinates1(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{input1}';"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    place1 = (result[0][0], result[0][1])
    print(place1)
    return place1

def find_coordinates2(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{input2}';"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    place2 = (result[0][0], result[0][1])
    print(place2)
    return place2


input1 = "EFHK"
input2 = "EFIV"

# ????????
print(find_coordinates1(input1)) #tässä on monikko, pitää saada arvot erikseen!?
tuple1 = find_coordinates1(input1)
latitude1 = float(tuple1[0])
longitude1 = float(tuple1[1])
lasku1 = (latitude1, longitude1)
print(lasku1)

print(find_coordinates2(input2))

#print(input1)
#print(distance.distance(input1, input2))
