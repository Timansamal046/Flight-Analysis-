# ✈️ Flight Analysis Dashboard

An interactive web-based dashboard built with **Streamlit** for analyzing flight data. The dashboard provides insightful visualizations about flight trends, prices, durations, airlines, and routes using a MySQL backend.

---

## 📌 Key Features

🔍 **Check Flights**  
- Search flights between selected source and destination cities.

📊 **Flight Analysis Tabs**  
- **Airlines Overview**: Distribution of flights by airline.  
- **Monthly Trends**: Number of flights per month.  
- **Flight Durations**: Average duration per airline.  
- **Routes & Airlines**: Top 10 routes, and airline-level stats.

---

## 🧰 Tech Stack

| Tool          | Description                       |
|---------------|-----------------------------------|
| Streamlit     | Web framework for interactive apps|
| MySQL         | Relational database for flight data|
| Pandas        | Data manipulation and analysis    |
| Plotly        | Advanced interactive visualizations|
| Python        | Main programming language         |

---

## 🗃️ Database Schema

**Table: `flights`**

| Column           | Type     | Description                         |
|------------------|----------|-------------------------------------|
| Airline          | VARCHAR  | Name of the airline                 |
| Source           | VARCHAR  | Source city                         |
| Destination      | VARCHAR  | Destination city                    |
| Total_Stops      | VARCHAR  | Number of stops in the journey      |
| Price            | INT      | Ticket price in INR                 |
| Date_of_Journey  | DATE     | Date of the flight                  |
| Duration         | FLOAT    | Duration in minutes                 |

---


