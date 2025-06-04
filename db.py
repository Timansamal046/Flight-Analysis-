import mysql.connector

class mydb:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="timansamal@2003",
            database = "ts"
        )
        
        self.cursor = self.conn.cursor()
        
    def get_cities(self):
        
        self.cursor.execute("select distinct(source) from flights;")
        
        cities = []
        
        for i in self.cursor.fetchall():
            cities.append(i[0])
        
        return cities
    
    def get_destination(self):
        
        self.cursor.execute("select distinct(destination) from flights;")
        
        dst_cities = [] 
        
        for i in self.cursor.fetchall():
            dst_cities.append(i[0])
        
        return dst_cities
    
    def get_data(self , src , dst):
       query = """
        SELECT Airline, Source, Destination, Total_Stops, Price 
        FROM flights 
        WHERE Source = %s AND Destination = %s
    """
       self.cursor.execute(query, (src, dst))
       return self.cursor.fetchall()
   
    def airline_flights(self ):
        self.cursor.execute("SELECT Airline , count(*) as x  FROM flights group by Airline order by x")
        data = self.cursor.fetchall()
        
        airline_name = [i[0] for i in data] 
        flight_count = [i[1] for i in data]
        
        return airline_name , flight_count
    
    def busy_airports(self):
        self.cursor.execute("select source ,  count(*) as q from (select source from flights union all select destination from flights) as t group by source order by q desc")
        
        data = self.cursor.fetchall()
        
        airport = []
        ct = []
        
        for i in data:
            airport.append(i[0])
            ct.append(i[1])
            
        return airport , ct
    
    def monthly_flight(self):
        self.cursor.execute("SELECT DATE_FORMAT(Date_of_Journey, '%Y-%m') as month, COUNT(*) as flight_count FROM flights GROUP BY month ORDER BY month;")
        
        data = self.cursor.fetchall()
        
        month = []
        count = []
        
        for i in data:
            month.append(i[0])
            count.append(i[1])     
            
        return month , count
        
    def airline_avg_price(self):
        
        self.cursor.execute("SELECT Airline, AVG(Price) AS avg_price FROM flights GROUP BY Airline;")
        
        data = self.cursor.fetchall()
        
        airline = [i[0] for i in data] 
        price  = [i[1] for i in data]   
        return airline , price
    
    
    def flight_avg_duration(self):
        
        self.cursor.execute("select Airline , ROUND(AVG(Duration), 2)  as avg_duration from flights group by Airline order by avg_duration desc ")
    
        data = self.cursor.fetchall()
        
        airline = [i[0] for i in data]
        
        duration = [i[1] for i in data]

        return airline , duration    
    
    def top_routes(self):
        
        self.cursor.execute("select Source, Destination, count(*) from flights group by Source, Destination order by count(*) desc limit 10")    
        
        data = self.cursor.fetchall()
        
        return [(i[0], i[1], i[2]) for i in data]
    
    def get_airlines(self):
        self.cursor.execute("select distinct airline from flights")
        result = self.cursor.fetchall()
        return [i[0] for i in result]
    
    
    def get_airline_stats(self, airline):
      self.cursor.execute("""
        SELECT 
            COUNT(*) AS total_flights,
            ROUND(AVG(price), 2) AS avg_price,
            ROUND(AVG(duration), 2) AS avg_duration
        FROM flights
        WHERE airline = %s
    """, (airline,))
      row = self.cursor.fetchone()
      return {
        "Total Flights": row[0],
        "Average Price": row[1],
        "Average Duration": row[2]
    } if row else {"Total Flights": 0, "Average Price": 0, "Average Duration": 0}
    
        
a = mydb()
a.get_cities()
