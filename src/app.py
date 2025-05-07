import streamlit as st
import pandas as pd
import warnings
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
from utils.gsheets import connect_to_gsheet

# Initialize connection with error handling
try:
    client = connect_to_gsheet()
    if client is None:
        st.error(
            "❌ Failed to connect to Google Sheets. Please check your credentials.")
        st.stop()
except Exception as e:
    st.error(f"❌ Critical initialization error: {str(e)}")
    st.stop()

warnings.filterwarnings('ignore')
# ========================================
# APP CONFIGURATION
# ========================================
st.set_page_config(
    page_title="GHATZ Data Visualization",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.markdown(
    '<style>div.block-container{padding-top:1rem; padding-bottom:0.0rem;}</style>', unsafe_allow_html=True)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    .css-18e3th9 {
        padding-top: 0rem;
        padding-bottom: 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    .css-1d391kg {
        padding-top: 3.5rem;
        padding-right: 1rem;
        padding-bottom: 3.5rem;
        padding-left: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# CUSTOM HEADER
# ========================================
st.markdown(f"""
<div style="background-color:#c7c4c1;padding:10px;border-radius:10px;margin:-25px -25px 20px -25px">
    <table style="width:100%;border-collapse:collapse">
        <tr>
            <td style="width:60%;text-align:center;">
                <h2 style="color:green;margin:0;">🔍📊 GHATZ DATA PLATFORM</h1>
                <p style="color:white;margin:0;">Advanced Analytics and Visualization Dashboard</p>
            </td>
            <td style="width:20%;text-align:right;color:white;">
                {datetime.now().strftime('%d %b %Y')}
            </td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

# ========================================
# SIDEBAR NAVIGATION
# ========================================
st.sidebar.header("Navigation")
option = st.sidebar.selectbox(
    "Choose a visualization:",
    [
        "Home", "Data Overview", "Dam Instrumentation", "GHATZ Building Infrastructure",
        "GHATZ Weather", "GHATZ Security", "GHATZ Water Level", "GHATZ Staff Composition"
    ]
)

# Footer
current_year = datetime.now().year
st.sidebar.markdown(
    f'<div class="sidebar-footer">Developed by <b>Gridhall Limited</b> © {current_year}</div>',
    unsafe_allow_html=True
)

# ========================================
# PAGE CONTENT
# ========================================
if option == "Home":
    st.markdown("""
        Welcome to the **GHATZ (Gurara Hydro, Agriculture, and Tourism Zone)** Data Analysis and Visualization Platform.

        ### 🔍 What You Can Do Here:
        - **Explore Instrumentation Records** for monitoring dam safety and performance.
        - **View Building Infrastructure Data** to assess development and facilities.
        - **Analyze Weather Trends** that impact agriculture and hydropower.
        - **Monitor Security Reports** across the GHATZ zone.
        - **Track Water Levels** in the Gurara reservoir with time-based analysis.
        - **Understand Staff Composition** to evaluate workforce distribution.

        ### 📊 Why Use This Platform?
        - Intuitive interface with **interactive filters**
        - Dynamic **visualizations and metrics**
        - Useful for **policy planning, engineering analysis,** and **development tracking**
        """)

elif option == "Data Overview":
    st.write("Here we can display an overview of your data.")

elif option == "GHATZ Building Infrastructure":
    st.write("Here we can view GHATZ Building Infrastructure Records/History")

elif option == "Dam Instrumentation":
    st.header("Relief Well Monitoring and Analysis")
    st.divider()

    @st.cache_data(ttl=3600)
    def load_relief_well_data():
        sheet = client.open("GHATZ_Data").worksheet("ReliefWells")
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        # Convert date column
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        df = df[df['Date'].notna()]

        # Convert numeric columns
        numeric_cols = ['Depth', 'Elevation']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col].astype(
                str).str.replace(',', ''), errors='coerce')
            df = df[df[col].notna()]

        # Calculate changes
        df['Depth Change'] = df.groupby('RW_ID')['Depth'].diff()
        df['Elevation Change'] = df.groupby('RW_ID')['Elevation'].diff()

        return df

    try:
        df = load_relief_well_data()

        # Sidebar filters
        st.sidebar.subheader("Relief Well Filters")
        well_ids = df['RW_ID'].unique()
        selected_well = st.sidebar.selectbox("Select Relief Well", well_ids)

        # Date range filter
        min_date = df['Date'].min().date()
        max_date = df['Date'].max().date()
        date_range = st.sidebar.date_input(
            "Date Range",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date
        )

        # Filter data
        filtered_df = df[
            (df['RW_ID'] == selected_well) &
            (df['Date'].dt.date >= date_range[0]) &
            (df['Date'].dt.date <= date_range[1])
        ].copy()

        # Main dashboard
        st.subheader(f"Analysis for Relief Well {selected_well}")

        # Key metrics
        col1, col2, col3 = st.columns(3)
        col1.metric("First Measurement",
                    filtered_df['Date'].min().strftime('%Y-%m-%d'))
        col2.metric("Last Measurement",
                    filtered_df['Date'].max().strftime('%Y-%m-%d'))
        col3.metric("Valid Measurements", len(filtered_df))

        st.divider()

        # Visualization tabs
        tab1, tab2, tab3 = st.tabs(
            ["Time Series", "Depth Analysis", "Data Table"])

        with tab1:
            st.subheader("Time Series Analysis")
            fig = px.line(
                filtered_df,
                x='Date',
                y=['Depth', 'Elevation'],
                title=f'Measurements Over Time - {selected_well}',
                labels={'value': 'Measurement (m)', 'variable': 'Parameter'},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Depth Change (m)")
                st.line_chart(filtered_df.set_index('Date')['Depth Change'])
            with col2:
                st.subheader("Elevation Change (m)")
                st.line_chart(filtered_df.set_index(
                    'Date')['Elevation Change'])

        with tab2:
            st.subheader("Depth Analysis")
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(filtered_df['Depth'], bins=15,
                    edgecolor='black', color='teal')
            ax.set_xlabel('Depth (m)')
            ax.set_ylabel('Frequency')
            st.pyplot(fig)

            st.subheader("Depth Over Time")
            chart = alt.Chart(filtered_df).mark_circle(size=60).encode(
                x='Date',
                y='Depth',
                tooltip=['Date', 'Depth', 'Elevation']
            ).interactive()
            st.altair_chart(chart, use_container_width=True)

        with tab3:
            st.subheader("Measurement Data")
            st.dataframe(
                filtered_df.sort_values('Date', ascending=False)[
                    ['Date', 'RW_ID', 'Depth', 'Elevation',
                        'Depth Change', 'Elevation Change']
                ],
                column_config={
                    "Date": st.column_config.DatetimeColumn(format="YYYY-MM-DD"),
                    "Depth": st.column_config.NumberColumn(format="%.2f m"),
                    "Elevation": st.column_config.NumberColumn(format="%.2f m")
                },
                hide_index=True,
                use_container_width=True
            )

        # Data export
        st.sidebar.download_button(
            label="📥 Download Data",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name=f"relief_well_{selected_well}.csv",
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif option == "GHATZ Weather":
    st.header("GHATZ Rainfall Analysis - Right and Left Bank")
    st.divider()

    @st.cache_data(ttl=3600)
    def load_rainfall_data():
        sheet = client.open("GHATZ_Data").worksheet("Rainfall")
        records = sheet.get_all_records()
        df = pd.DataFrame(records)

        # Clean and preprocess
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={"righbank": "rightbank"}, inplace=True)

        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df = df.dropna(subset=["date"])
        df = df.sort_values("date")

        # Convert rainfall values to numeric
        df["rightbank"] = pd.to_numeric(df["rightbank"], errors="coerce")
        df["leftbank"] = pd.to_numeric(df["leftbank"], errors="coerce")

        return df

    try:
        df = load_rainfall_data()

        # Show data preview
        st.subheader("Rainfall Data")
        st.dataframe(df, use_container_width=True)

        # Line chart
        st.subheader("Daily Rainfall (mm) - Line Chart")
        st.line_chart(df.set_index("date")[
                      ["rightbank", "leftbank"]], use_container_width=True)

        # Monthly Aggregation
        df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
        monthly = df.groupby("month")[
            ["rightbank", "leftbank"]].sum().reset_index()

        st.subheader("Monthly Total Rainfall (mm) - Bar Chart")
        st.bar_chart(monthly.set_index("month"), use_container_width=True)

        # Summary Statistics
        st.subheader("Summary Statistics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Right Bank - Total", f"{df['rightbank'].sum():.2f} mm")
            st.metric("Right Bank - Max", f"{df['rightbank'].max():.2f} mm")
            st.metric("Right Bank - Mean", f"{df['rightbank'].mean():.2f} mm")
        with col2:
            st.metric("Left Bank - Total", f"{df['leftbank'].sum():.2f} mm")
            st.metric("Left Bank - Max", f"{df['leftbank'].max():.2f} mm")
            st.metric("Left Bank - Mean", f"{df['leftbank'].mean():.2f} mm")

    except Exception as e:
        st.error(f"Error loading rainfall data: {str(e)}")

elif option == "GHATZ Security":
    st.header("GHATZ Security Incident Dashboard")
    st.divider()

    @st.cache_data(ttl=3600)
    def load_security_data():
        sheet = client.open("GHATZ_Data").worksheet("Security")
        records = sheet.get_all_records()
        df = pd.DataFrame(records)

        # Convert Value column to numeric
        df['Numeric_Value'] = (
            df['Value']
            .astype(str)
            .str.extract('(\d+)', expand=False)
            .astype(float)
            .fillna(0)
        )

        # Convert dates
        df['Date'] = pd.to_datetime(
            df['Date'], errors='coerce', format='mixed')

        return df

    try:
        security_data = load_security_data()

        # Key metrics
        st.subheader("Key Security Metrics")
        col1, col2, col3 = st.columns(3)

        def get_metric(category, sub_category):
            try:
                value = security_data[
                    (security_data['Category'] == category) &
                    (security_data['Sub-Category'] == sub_category)
                ]['Numeric_Value'].iloc[0]
                return int(value)
            except (IndexError, KeyError):
                return 0

        with col1:
            st.metric("Total Incidents", get_metric(
                "INCIDENT SUMMARY", "Total Incidents"))
        with col2:
            st.metric("Fatalities", get_metric(
                "INCIDENT SUMMARY", "Fatalities"))
        with col3:
            st.metric("Abductions", get_metric(
                "INCIDENT SUMMARY", "Abductions"))

        st.divider()

        # Incident Analysis
        tab1, tab2, tab3 = st.tabs(["Incident Types", "Timeline", "Locations"])

        with tab1:
            incident_types = security_data[
                security_data['Category'] == "INCIDENT BREAKDOWN"
            ]

            if not incident_types.empty:
                st.subheader("Incident Type Distribution")
                viz_df = incident_types[['Sub-Category', 'Numeric_Value']].rename(
                    columns={'Sub-Category': 'Incident Type',
                             'Numeric_Value': 'Count'}
                )

                fig = px.pie(viz_df, names='Incident Type',
                             values='Count', title='Incident Composition')
                st.plotly_chart(fig, use_container_width=True)
                st.bar_chart(viz_df.set_index('Incident Type'))

        with tab2:
            notable = security_data[
                (security_data['Category'] == "NOTABLE INCIDENTS") &
                (security_data['Date'].notna())
            ]

            if not notable.empty:
                st.subheader("Incident Timeline")
                notable['Month'] = notable['Date'].dt.to_period(
                    'M').astype(str)
                monthly_counts = notable.groupby('Month').size()
                st.line_chart(monthly_counts)

        with tab3:
            if 'Location' in security_data.columns:
                st.subheader("Incidents by Location")
                loc_counts = security_data[security_data['Location'].notna(
                )]['Location'].value_counts()
                if not loc_counts.empty:
                    st.bar_chart(loc_counts)

        # Data export
        st.sidebar.download_button(
            label="📥 Download Security Data",
            data=security_data.to_csv(index=False).encode('utf-8'),
            file_name="GHATZ_security_export.csv",
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif option == "GHATZ Water Level":
    st.header("Gurara Reservoir Water Level - Yearly and Monthly Analysis")
    st.divider()

    @st.cache_data(ttl=3600)
    def load_water_level_data():
        sheet = client.open("GHATZ_Data").worksheet("guraradamwaterlevel")
        records = sheet.get_all_records()
        df = pd.DataFrame(records)

        # Parse dates and remove invalid ones
        df["date"] = pd.to_datetime(df["date"], errors='coerce')
        df = df.dropna(subset=["date"])

        # Convert reservoir_level to numeric
        df["reservoir_level"] = pd.to_numeric(
            df["reservoir_level"], errors='coerce')
        df = df.dropna(subset=["reservoir_level"])

        return df

    try:
        df = load_water_level_data()

        # Date range selection
        startDate = df["date"].min()
        endDate = min(df["date"].max(), pd.to_datetime("2025-12-31"))

        col1, col2 = st.columns((2))
        with col1:
            date1 = pd.to_datetime(st.date_input(
                "Start Date", startDate, min_value=startDate, max_value=endDate))
        with col2:
            date2 = pd.to_datetime(st.date_input(
                "End Date", endDate, min_value=startDate, max_value=endDate))

        # Filter based on selected range
        df_filtered = df[(df["date"] >= date1) & (df["date"] <= date2)].copy()

        if df_filtered.empty:
            st.warning("No data available for the selected date range")
            st.stop()

        # Yearly Analysis
        df_filtered["year"] = df_filtered["date"].dt.year
        yearly_avg = df_filtered.groupby(
            "year")["reservoir_level"].mean().reset_index()
        yearly_avg = yearly_avg[yearly_avg["year"] <= 2025]

        st.subheader("Average Reservoir Water Level per Year")

        if not yearly_avg.empty:
            yearly_chart = alt.Chart(yearly_avg).mark_line(point=True).encode(
                x=alt.X("year:O", title="Year"),
                y=alt.Y("reservoir_level:Q", title="Avg Reservoir Level",
                        scale=alt.Scale(domain=[600, 630])),
                tooltip=["year", alt.Tooltip(
                    "reservoir_level:Q", title="Level", format=".2f")]
            ).properties(
                width="container",
                height=400,
                title="Average Reservoir Water Level per Year (600–630m Range)"
            )
            st.altair_chart(yearly_chart, use_container_width=True)

        # Monthly Analysis
        st.subheader("Average Reservoir Water Level per Month")
        df_filtered["month"] = df_filtered["date"].dt.strftime("%B")
        df_filtered["month_num"] = df_filtered["date"].dt.month

        monthly_avg = df_filtered.groupby(["month", "month_num"])[
            "reservoir_level"].mean().reset_index()
        monthly_avg = monthly_avg.sort_values("month_num")

        if not monthly_avg.empty:
            monthly_chart = alt.Chart(monthly_avg).mark_bar().encode(
                x=alt.X("month:N", sort=list(
                    monthly_avg["month"]), title="Month"),
                y=alt.Y("reservoir_level:Q", title="Avg Reservoir Level",
                        scale=alt.Scale(domain=[600, 630])),
                tooltip=["month", alt.Tooltip(
                    "reservoir_level:Q", title="Level", format=".2f")]
            ).properties(
                width="container",
                height=400,
                title="Average Reservoir Water Level per Month (600–630m Range)"
            )
            st.altair_chart(monthly_chart, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif option == "GHATZ Staff Composition":
    st.header("Staff Composition Overview")
    st.divider()

    @st.cache_data(ttl=3600)
    def load_staff_data():
        sheet = client.open("GHATZ_Data").worksheet("Staffcomposition")
        records = sheet.get_all_records()
        df = pd.DataFrame(records)

        # Clean column names
        df.columns = df.columns.str.strip().str.lower()
        df.rename(columns={"names": "name", "position": "position",
                  "location": "location"}, inplace=True)

        return df

    try:
        df = load_staff_data()

        # Staff count by location
        st.subheader("📍 Staff Distribution by Location")
        location_count = df["location"].value_counts(
        ).sort_values(ascending=True)
        st.bar_chart(location_count)

        # Top 10 job titles
        st.subheader("🧑‍🔧 Most Common Job Titles")
        top_positions = df["position"].value_counts().head(10)

        st.dataframe(top_positions.reset_index().rename(
            columns={"index": "Position", "position": "Count"}))

        fig, ax = plt.subplots()
        top_positions.plot(kind="barh", ax=ax, color="teal")
        ax.set_xlabel("Count")
        ax.set_title("Top 10 Job Titles")
        st.pyplot(fig)

        # Summary Metrics
        st.subheader("📊 Summary Metrics")
        total_staff = len(df)
        unique_locations = df["location"].nunique()
        unique_roles = df["position"].nunique()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Staff", total_staff)
        col2.metric("Locations", unique_locations)
        col3.metric("Unique Roles", unique_roles)

        # Filter by Location
        st.subheader("🔍 Explore by Location")
        selected_location = st.selectbox(
            "Select a Location", sorted(df["location"].unique()))
        filtered_df = df[df["location"] == selected_location]

        st.dataframe(filtered_df.reset_index(drop=True))

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
