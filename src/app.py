import streamlit as st
import pandas as pd
import warnings
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
from utils.gsheets import connect_to_gsheet


current_year = datetime.now().year

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
    '<style>div.block-container{padding-top:1rem; padding-bottom:3rem;}</style>', unsafe_allow_html=True)
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
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
st.sidebar.header("Select Data")
option = st.sidebar.selectbox(
    "Choose Data to visualization:",
    [
        "Home", "Data Overview", "Dam Instrumentation", "GHATZ Building Infrastructure",
        "GHATZ Weather", "GHATZ Security", "GHATZ Water Level", "GHATZ Staff Composition"
    ]
)

# Footer

# ========================================
# PAGE CONTENT
# ========================================
if option == "Home":
    st.title("🌍 Welcome to GHATZ Analytics Platform")
    st.markdown("""
    **Your central hub for Gurara Hydro, Agriculture, and Tourism Zone data intelligence**  
    *Monitoring • Analysis • Decision Support*
    """)

    # Add a relevant banner image with corrected parameter
    st.image("https://example.com/ghatz-banner.jpg",
             use_container_width=True)  # Updated parameter

    with st.container():
        st.markdown("""
        ### 🔍 Core Capabilities
        <div style="padding:15px; background-color:#f8f9fa; border-radius:10px; margin:10px 0">
        <div style="column-count:2; column-gap:20px;">
        <div style="break-inside:avoid;">
        <h4>🏗️ Infrastructure Monitoring</h4>
        • Real-time <strong>dam instrumentation</strong> analysis<br>
        • <strong>Building infrastructure</strong> development tracking<br>
        • <strong>Water level</strong> historical trends
        </div>
        <div style="break-inside:avoid;">
        <h4>🌦️ Environmental Insights</h4>
        • Agricultural <strong>weather impact</strong> analysis<br>
        • Zone-wide <strong>security monitoring</strong><br>
        • Workforce <strong>staff composition</strong> analytics
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    ### 📊 Value Proposition
    <div style="background-color:#e8f4fc; padding:20px; border-radius:10px; margin:15px 0">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
    <div style="background:white; padding:15px; border-radius:8px;">
    <h4>📋 Interactive Dashboards</h4>
    <span style="font-size:14px">Dynamic filters and parameter controls</span>
    </div>
    <div style="background:white; padding:15px; border-radius:8px;">
    <h4>📈 Advanced Visualizations</h4>
    <span style="font-size:14px">Time-series charts and geospatial views</span>
    </div>
    <div style="background:white; padding:15px; border-radius:8px;">
    <h4>⚙️ Engineering Tools</h4>
    <span style="font-size:14px">Technical analysis for infrastructure</span>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🚀 Quick Start Guide", expanded=False):
        st.markdown("""
        1. **Select a module** from the sidebar  
        2. **Adjust filters** for your analysis period  
        3. **Hover/click** visualizations for details  
        4. **Export** any view using the download buttons  
        """)
        st.button("📚 View Tutorial", key="tutorial_btn")

    # Feature highlights with updated icons
    st.markdown("""
    ### ✨ Key Features
    <div style="font-size:14px">
    ▸ Policy-ready reports generation<br>
    ▸ Mobile-responsive design<br>
    ▸ Automated data refreshes<br>
    ▸ Multi-user collaboration
    </div>
    """, unsafe_allow_html=True)

elif option == "Data Overview":
    st.write("Here we can display an overview of your data.")

elif option == "GHATZ Building Infrastructure":
    st.write("Here we can view GHATZ Building Infrastructure Records/History")

elif option == "Dam Instrumentation":
    st.header("🌊 Relief Well Monitoring and Analysis")
    st.markdown("""
    <div style="background-color:#f0f8ff; padding:15px; border-radius:10px; margin-bottom:20px">
    Comprehensive monitoring of relief well performance including depth, elevation, and spatial analysis
    </div>
    """, unsafe_allow_html=True)

    @st.cache_data(ttl=3600)
    def load_relief_well_data():
        sheet = client.open("GHATZ_Data").worksheet("ReliefWells")
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        # Convert and clean data
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
        df['Date of Installation'] = pd.to_datetime(df['Date of Installation'], dayfirst=True, errors='coerce')
        
        numeric_cols = ['Depth', 'Elevation', 'x', 'y', 'GROUND LEVEL', 'FOUNDATION LEVEL', 
                       'TOP OF PVC LEVEL', 'TOTAL DEPTH ( m )', 'HEIGHT OF PVC ABOVE G.L', 'NTPL']
        
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')
        
        # Calculate metrics
        df['Days Since Installation'] = (df['Date'] - df['Date of Installation']).dt.days
        df['Depth Change'] = df.groupby('RW_ID')['Depth'].diff()
        df['Elevation Change'] = df.groupby('RW_ID')['Elevation'].diff()
        df['Cumulative Depth Change'] = df.groupby('RW_ID')['Depth Change'].cumsum()
        
        return df.dropna(subset=['Date'])

    try:
        df = load_relief_well_data()

        # Sidebar filters - expanded
        st.sidebar.header("🔍 Filter Options")
        well_ids = df['RW_ID'].unique()
        selected_wells = st.sidebar.multiselect("Select Relief Well(s)", well_ids, default=well_ids[0])
        
        date_range = st.sidebar.date_input(
            "Date Range",
            value=[df['Date'].min().date(), df['Date'].max().date()],
            min_value=df['Date'].min().date(),
            max_value=df['Date'].max().date()
        )
        
        # Main dashboard
        filtered_df = df[
            (df['RW_ID'].isin(selected_wells)) &
            (df['Date'].dt.date >= date_range[0]) &
            (df['Date'].dt.date <= date_range[1])
        ].copy()
        
        if filtered_df.empty:
            st.warning("No data available for selected filters")
            st.stop()

        # Summary metrics
        st.subheader("📊 Performance Summary")
        cols = st.columns(4)
        cols[0].metric("Selected Wells", len(selected_wells))
        cols[1].metric("Date Range", f"{date_range[0]} to {date_range[1]}")
        cols[2].metric("Avg Depth Change", f"{filtered_df['Depth Change'].mean():.2f} m")
        cols[3].metric("Max Elevation", f"{filtered_df['Elevation'].max():.2f} m")
        
        st.divider()

        # Enhanced visualization tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ["📈 Time Trends", "📉 Depth Analysis", "📊 Statistical Summary", "📋 Raw Data"])

        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Depth Over Time")
                fig = px.line(
                    filtered_df,
                    x='Date',
                    y='Depth',
                    color='RW_ID',
                    title='Depth Measurements',
                    labels={'Depth': 'Depth (m)'},
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
            with col2:
                st.subheader("Elevation Trends")
                fig = px.area(
                    filtered_df,
                    x='Date',
                    y='Elevation',
                    color='RW_ID',
                    title='Elevation Changes',
                    labels={'Elevation': 'Elevation (m)'},
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Cumulative Changes")
            fig = px.line(
                filtered_df,
                x='Date',
                y='Cumulative Depth Change',
                color='RW_ID',
                title='Total Depth Change Since First Measurement',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

            # New: Scatter plot of Depth vs Elevation
            st.subheader("Depth vs Elevation Relationship")
            fig = px.scatter(
                filtered_df,
                x='Depth',
                y='Elevation',
                color='RW_ID',
                # trendline="lowess",
                hover_data=['Date'],
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader("Depth Distribution Analysis")
            col1, col2 = st.columns(2)
            with col1:
                fig = px.histogram(
                    filtered_df,
                    x='Depth',
                    nbins=20,
                    color='RW_ID',
                    title='Depth Measurement Distribution',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
            with col2:
                fig = px.box(
                    filtered_df,
                    y='Depth',
                    x='RW_ID',
                    color='RW_ID',
                    title='Depth Variation by Well',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            # New: Violin plot showing distribution
            st.subheader("Depth Distribution Density")
            fig = px.violin(
                filtered_df,
                y='Depth',
                x='RW_ID',
                color='RW_ID',
                box=True,
                points="all",
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            st.subheader("Statistical Summary")
            st.dataframe(
                filtered_df.groupby('RW_ID').agg({
                    'Depth': ['mean', 'std', 'min', 'max', 'count'],
                    'Elevation': ['mean', 'std', 'min', 'max'],
                    'Days Since Installation': ['max']
                }).style.format("{:.2f}"),
                use_container_width=True
            )
            
            st.subheader("Change Rate Analysis")
            change_rates = filtered_df.groupby('RW_ID').apply(
                lambda x: pd.Series({
                    'Depth Change Rate (m/day)': x['Depth Change'].mean() / ((x['Date'].max() - x['Date'].min()).days + 1),
                    'Elevation Change Rate (m/day)': x['Elevation Change'].mean() / ((x['Date'].max() - x['Date'].min()).days + 1),
                    'Measurement Frequency (days)': ((x['Date'].max() - x['Date'].min()).days + 1) / len(x)
                })
            )
            st.dataframe(change_rates.style.format("{:.4f}"), use_container_width=True)

            # New: Correlation matrix
            st.subheader("Parameter Correlations")
            numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
            corr_matrix = numeric_df.corr()
            fig = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                color_continuous_scale='RdBu',
                range_color=[-1, 1],
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab4:
            st.subheader("Measurement Records")
            st.dataframe(
                filtered_df.sort_values(['RW_ID', 'Date'], ascending=[True, False]),
                column_config={
                    "Date": st.column_config.DatetimeColumn(format="YYYY-MM-DD"),
                    "Date of Installation": st.column_config.DatetimeColumn(format="YYYY-MM-DD"),
                    "Depth": st.column_config.NumberColumn(format="%.2f m"),
                    "Elevation": st.column_config.NumberColumn(format="%.2f m"),
                    "GROUND LEVEL": st.column_config.NumberColumn(format="%.2f m")
                },
                hide_index=True,
                use_container_width=True,
                height=600
            )

        # Enhanced data export
        st.sidebar.divider()
        st.sidebar.download_button(
            label="📥 Export Current View",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name=f"relief_wells_{date_range[0]}_{date_range[1]}.csv",
            mime='text/csv',
            help="Download filtered data as CSV"
        )

    except Exception as e:
        st.error(f"❌ Data loading error: {str(e)}")
        st.error("Please check your data connection and filters")
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

# Add the sticky footer
st.markdown(

    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        border-top: 1px solid #e1e4e8;
    }
    </style>
    <div class="footer">
        Developed by <b>Gridhall Limited</b> © 2025 | All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
