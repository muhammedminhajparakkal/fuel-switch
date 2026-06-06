import streamlit as st
import duckdb
import plotly.express as px
import pandas as pd


st.set_page_config(
    page_title="The Fuel Switch - India EV Transition", 
    layout="wide",
)

# Custom Title Styling
st.title('The Fuel Switch: India Automobile Market Transition')
st.markdown("---")
st.caption("Data: [Indian Car Sell Dataset](https://www.kaggle.com/datasets/milapgohil/car-dataset) by Milap Gohil · Kaggle | License: Apache 2.0")
st.markdown("---")


DB_PATH = "data/warehouse.duckdb"



# Cached Data Ingestion Function for Speed
@st.cache_data
def load_data(query):
    conn = duckdb.connect(DB_PATH)
    df = conn.execute(query).df()
    conn.close()
    return df

# tabs

tab1, tab2, tab3 = st.tabs([
    "📊 Fuel Mix Trends", 
    "🗺️ State EV Penetration", 
    "🏎️ Maker EV Share"
])

# TAB 1 — FUEL MIX TRENDS
#----------------------------------------------------------------------------
with tab1:
    st.header("Grand Fuel Transition & YoY Growth")
    st.markdown("Analyze vehicle fuel type distribution and annual growth rates.")

    fuel_query = "SELECT * FROM mart_fuel_transition ORDER BY year DESC, fuel_type"
    df_fuel = load_data(fuel_query)


    col_filter1, _ = st.columns([3, 7])
    with col_filter1:
        # Get unique years sorted chronologically for the dropdown
        unique_years = sorted(df_fuel["year"].unique(), reverse=True)
        selected_year = st.selectbox("📅 Select Registration Year:", unique_years, key="tab1_year")

    # Filter the Pandas DataFrame based on user selection
    df_filtered = df_fuel[df_fuel["year"] == selected_year]

    # --- VISUALIZATION 1
    
    st.subheader(f"📊 Market Share Distribution in {selected_year}")
    
    fig_share = px.bar(
        df_filtered,
        x="fuel_type",
        y="fuel_share_percentage",
        text=df_filtered["fuel_share_percentage"].apply(lambda n: f"{n:.2f}%"),
        labels={"fuel_type": "Fuel Type", "fuel_share_percentage": "Market Share (%)"},
        color="fuel_type",
        color_discrete_map={
            "PETROL": "#EF553B",
            "DIESEL": "#636EFA",
            "EV": "#00CC96",
            "HYBRID": "#AB63FA",
            "CNG": "#FFA15A"
        }
    )
    fig_share.update_layout(showlegend=False, yaxis_range=[0, 100])
    st.plotly_chart(fig_share, use_container_width=True)

    # --- VISUALIZATION 2: Dynamic KPI Cards for YoY Growth 
    st.subheader(f"📈 Year-over-Year Growth Rates ({selected_year})")
    st.markdown("How registrations changed compared to the previous year:")
    
    # Create layout columns  for each fuel type present
    kpi_cols = st.columns(len(df_filtered))
    
    for col, (_, row) in zip(kpi_cols, df_filtered.iterrows()):
        fuel = row["fuel_type"]
        reg_count = int(row["registrations"])
        yoy_growth = row["yoy_growth_percentage"]
        
        # Format the growth text nicely
        if yoy_growth is None or pd.isna(yoy_growth):
            delta_val = "No baseline data"
        else:
            delta_val = f"{yoy_growth:+.2f}% YoY"
            
        with col:
            st.metric(
                label=f"{fuel} Volume",
                value=f"{reg_count:,}",
                delta=delta_val,
                delta_color="normal" if fuel in ["EV", "HYBRID", "CNG"] else "inverse" 
                )

