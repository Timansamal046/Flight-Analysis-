import streamlit as st
from db import mydb
import plotly.graph_objects as go 
import plotly.express as px 
import pandas as pd 
#python -m streamlit run app.py 
st.sidebar.title("Flights Analysis")

choice = st.sidebar.selectbox("Menu" , ["Select one" , "Check Flights", "Flight Analysis"])

db = mydb()

if choice == "Check Flights":
    st.title("Check Flights")
    
    col1 , col2 = st.columns(2)
    
    with col1:
        
        source = st.selectbox("Source City" , db.get_cities())
        
    with col2:
        
        destination = st.selectbox("Destination City" , db.get_destination())
        
    if st.button("Search"):
        
        all_flights = db.get_data(source,destination)
        st.dataframe(all_flights)
        
elif choice == "Flight Analysis":
    st.title("📊 Flight Analysis Dashboard")
    st.markdown("Explore trends, prices, durations, and routes across different airlines and airports.")

    # Tabs for cleaner navigation
    tab1, tab2, tab3, tab4 = st.tabs([
        "🛫 Overview",
        "📈 Monthly Trends",
        "✈️ Flight Durations",
        "📍 Routes & Airlines"
    ])
    
    with tab1:
        
        
        air_name , flt_cnt = db.airline_flights()
            
        df = pd.DataFrame({
            'Airline': air_name,
            'Flights': flt_cnt
            })

        # Create pie chart
        fig = px.pie(df, names='Airline', values='Flights', title='Flight Distribution by Airline')
            
        st.header("Airlines Count")
        # Show it in Streamlit
        st.plotly_chart(fig)
            
        st.divider()
        
        airport  , ct = db.busy_airports()
            
        df = pd.DataFrame({
            'Airport': airport,
            'Count': ct
            })
            
        fig1 = px.bar(df, x='Airport', y='Count', color='Airport', title='Busy Airports')
            
        st.header("Busiest Airport")
            
        st.plotly_chart(fig1)
        
        st.divider()
        
        airlines, avg_prices = db.airline_avg_price()
        
        df_price = pd.DataFrame({'Airline': airlines, 'Avg Price': avg_prices})
       
        st.subheader("Average Ticket Price per Airline")
        
        fig2 = px.bar(df_price, x='Airline', y='Avg Price', color='Airline', title='Avg Prices')
        
        st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
    
        month , count = db.monthly_flight()
        
        df = pd.DataFrame({
        'Month': month,
        'Count': count
        }) 
        
        fig2  = px.line(df, x='Month', y='Count', markers=True, title='Monthly Flight Trend')
        
        st.header("Monthly Flight Trend")
        
        st.plotly_chart(fig2)  
        
        
    with tab3:
        
        airlines, durations = db.flight_avg_duration()
        
        if airlines:
            
            df_dur = pd.DataFrame({'Airline': airlines, 'Avg Duration (mins)': durations})
            
            st.subheader("Flight Duration per Airline")
            
            fig3 = px.bar(df_dur, x='Airline', y='Avg Duration (mins)', color='Airline', title='Avg Duration')
            
            st.plotly_chart(fig3, use_container_width=True)  
            
     
    with tab4:
        
        routes = db.top_routes() 
        
        if routes:
           
            df_routes = pd.DataFrame(routes, columns=["Source", "Destination", "Count"])
           
            st.subheader("Top Flight Routes")
           
            fig5 = px.bar(df_routes, x='Count', y='Source', color='Destination',
                          orientation='h', title='Frequent Routes')
            st.plotly_chart(fig5, use_container_width=True)

        st.divider()
       
        airline_list = db.get_airlines()
       
        selected_airline = st.selectbox("Select Airline to View Stats", airline_list)

        if selected_airline:
       
            stats = db.get_airline_stats(selected_airline)
           
            st.markdown(f"""
            ### ✈️ {selected_airline} Overview
            - **Total Flights**: `{stats['Total Flights']}`
            - **Average Price**: `₹{stats['Average Price']}`
            - **Average Duration**: `{stats['Average Duration']} mins`
            """)
            
else:
    if choice == "Select one":
        
        st.title("🛬 Welcome to Flight Explorer Dashboard")
        
        st.markdown("""
        ### 👋 Hello!
        Welcome to your **interactive flight insights dashboard**.
        
        Here’s what you can do:
        
        - 🔍 **Check Flights** between cities.
        - 📊 **Analyze Flights** by routes, airlines, and prices.
        
        Use the sidebar to get started 🚀
        """)
        
        # st.image("https://cdn.pixabay.com/photo/2017/01/06/19/15/airplane-1959532_960_720.jpg", 
        #         caption="Explore the skies!", use_column_width=True)

        st.info("Select an option from the sidebar to continue.")