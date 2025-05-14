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
    st.header("🌧️ GHATZ Rainfall Analysis - Right and Left Bank")
    st.markdown("""
    <div style="background-color:#f0f8ff; padding:15px; border-radius:10px; margin-bottom:20px">
    Comprehensive rainfall monitoring with comparative analysis between banks
    </div>
    """, unsafe_allow_html=True)

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

        # Create time-based features
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["month_name"] = df["date"].dt.month_name()
        df["day_of_year"] = df["date"].dt.dayofyear
        df["week"] = df["date"].dt.isocalendar().week
        
        return df

    try:
        df = load_rainfall_data()

        # Sidebar filters
        st.sidebar.header("🔍 Filter Options")
        
        # Date range filter
        min_date = df["date"].min().date()
        max_date = df["date"].max().date()
        date_range = st.sidebar.date_input(
            "Select Date Range",
            value=[min_date, max_date],
            min_value=min_date,
            max_value=max_date
        )
        
        # Year filter
        available_years = sorted(df["year"].unique())
        selected_years = st.sidebar.multiselect(
            "Select Years",
            options=available_years,
            default=available_years
        )
        
        # Bank selection
        banks = st.sidebar.multiselect(
            "Select Banks to Compare",
            options=["rightbank", "leftbank"],
            default=["rightbank", "leftbank"]
        )

        # Apply filters
        filtered_df = df[
            (df["date"].dt.date >= date_range[0]) &
            (df["date"].dt.date <= date_range[1]) &
            (df["year"].isin(selected_years))
        ].copy()

        if filtered_df.empty:
            st.warning("No data available for selected filters")
            st.stop()

        # Main dashboard
        st.subheader("📊 Rainfall Overview")
        cols = st.columns(3)
        cols[0].metric("Date Range", f"{date_range[0]} to {date_range[1]}")
        cols[1].metric("Days Recorded", len(filtered_df))
        cols[2].metric("Years Included", len(selected_years))
        
        st.divider()

        # Visualization tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ["📅 Daily View", "📆 Monthly Analysis", "📈 Annual Trends", "📋 Raw Data"])

        with tab1:
            st.subheader("Daily Rainfall Comparison")
            fig = px.line(
                filtered_df,
                x="date",
                y=banks,
                title="Daily Rainfall (mm)",
                labels={"value": "Rainfall (mm)", "variable": "Bank"},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("Rainfall Distribution")
            col1, col2 = st.columns(2)
            with col1:
                fig = px.histogram(
                    filtered_df,
                    x="rightbank",
                    nbins=30,
                    title="Right Bank Distribution",
                    labels={"rightbank": "Rainfall (mm)"}
                )
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                fig = px.histogram(
                    filtered_df,
                    x="leftbank",
                    nbins=30,
                    title="Left Bank Distribution",
                    labels={"leftbank": "Rainfall (mm)"}
                )
                st.plotly_chart(fig, use_container_width=True)

        with tab2:
            # Monthly aggregation
            monthly = filtered_df.groupby(["year", "month", "month_name"])[banks].sum().reset_index()
            monthly["month_year"] = monthly["month_name"] + " " + monthly["year"].astype(str)
            
            st.subheader("Monthly Rainfall Totals")
            fig = px.bar(
                monthly,
                x="month_year",
                y=banks,
                barmode="group",
                title="Monthly Rainfall Comparison (mm)",
                labels={"value": "Rainfall (mm)", "variable": "Bank"},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Monthly Averages")
            monthly_avg = filtered_df.groupby("month_name")[banks].mean().reset_index()
            fig = px.line_polar(
                monthly_avg,
                r="rightbank",
                theta="month_name",
                line_close=True,
                title="Seasonal Pattern - Right Bank",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            # Annual analysis
            annual = filtered_df.groupby("year")[banks].sum().reset_index()
            
            st.subheader("Annual Rainfall Totals")
            fig = px.bar(
                annual,
                x="year",
                y=banks,
                barmode="group",
                title="Annual Rainfall Comparison (mm)",
                labels={"value": "Rainfall (mm)", "variable": "Bank"},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Cumulative Rainfall")
            cumulative = filtered_df.sort_values("date").groupby("year")[banks].cumsum()
            cumulative["date"] = filtered_df["date"]
            fig = px.line(
                cumulative,
                x="date",
                y=banks,
                title="Cumulative Rainfall by Year (mm)",
                labels={"value": "Cumulative Rainfall (mm)", "variable": "Bank"},
                height=500
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab4:
            st.subheader("Rainfall Records")
            st.dataframe(
                filtered_df.sort_values("date", ascending=False),
                column_config={
                    "date": st.column_config.DatetimeColumn(format="YYYY-MM-DD"),
                    "rightbank": st.column_config.NumberColumn(label="Right Bank (mm)", format="%.1f"),
                    "leftbank": st.column_config.NumberColumn(label="Left Bank (mm)", format="%.1f")
                },
                hide_index=True,
                use_container_width=True,
                height=600
            )

        # Additional metrics
        st.sidebar.divider()
        st.sidebar.subheader("Key Metrics")
        for bank in banks:
            st.sidebar.metric(
                f"{bank.title()} - Max Daily",
                f"{filtered_df[bank].max():.1f} mm"
            )
            st.sidebar.metric(
                f"{bank.title()} - Total",
                f"{filtered_df[bank].sum():.1f} mm"
            )

        # Data export
        st.sidebar.download_button(
            label="📥 Export Data",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name=f"rainfall_data_{date_range[0]}_{date_range[1]}.csv",
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"Error loading rainfall data: {str(e)}")
elif option == "GHATZ Security":
    st.header("🚨 GHATZ Security Incident Dashboard")
    st.markdown("""
    <div style="background-color:#fff8f8; padding:15px; border-radius:10px; margin-bottom:20px">
    Comprehensive security monitoring and threat analysis for Gurara Dam and surrounding areas
    </div>
    """, unsafe_allow_html=True)

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

        # Clean and standardize text data
        text_cols = ['Category', 'Sub-Category', 'Details', 'Location']
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip().str.title()

        return df

    try:
        security_data = load_security_data()

        # Sidebar filters
        st.sidebar.header("🔍 Filter Options")

        # Category filter with safe defaults
        categories = security_data['Category'].dropna().unique().tolist()
        default_categories = [cat for cat in ["Incident Summary", "Incident Breakdown", "Notable Incidents"] if cat in categories]

        selected_categories = st.sidebar.multiselect(
            "Select Categories",
            options=categories,
            default=default_categories
        )

        show_impact = st.sidebar.checkbox("Show Impact Analysis", True)
        show_recommendations = st.sidebar.checkbox("Show Recommendations", True)

        # Filter data
        filtered_data = security_data[security_data['Category'].isin(selected_categories)].copy()

        st.subheader("📊 Security Metrics Overview")

        def calculate_metric(df, category, sub_category):
            try:
                subset = df[(df['Category'] == category) & (df['Sub-Category'] == sub_category)]
                return subset['Numeric_Value'].iloc[0] if not subset.empty else 0
            except:
                return 0

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_incidents = calculate_metric(filtered_data, "Incident Summary", "Total Incidents")
            st.metric("Total Incidents", total_incidents)

        with col2:
            fatalities = calculate_metric(filtered_data, "Incident Summary", "Fatalities")
            st.metric("Fatalities", fatalities)

        with col3:
            abductions = calculate_metric(filtered_data, "Incident Summary", "Abductions")
            st.metric("Abductions", abductions)

        with col4:
            fatality_rate = (fatalities / total_incidents * 100) if total_incidents > 0 else 0
            st.metric("Fatality Rate", f"{fatality_rate:.1f}%")

        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs(["Incident Analysis", "Location Intelligence", "Impact Assessment", "Recommendations"])

        with tab1:
            incident_types = filtered_data[filtered_data['Category'] == "Incident Breakdown"]
            if not incident_types.empty:
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Incident Composition")
                    viz_df = incident_types[['Sub-Category', 'Numeric_Value']].rename(
                        columns={'Sub-Category': 'Incident Type', 'Numeric_Value': 'Count'}
                    )
                    fig = px.pie(viz_df, names='Incident Type', values='Count', hole=0.3)
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    st.subheader("Incident Severity")
                    severity_df = viz_df.copy()
                    severity_df['Percentage'] = (severity_df['Count'] / severity_df['Count'].sum()) * 100
                    fig = px.bar(severity_df, x='Incident Type', y='Percentage', color='Count', text='Percentage')
                    fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
                    st.plotly_chart(fig, use_container_width=True)

                st.subheader("Incident Details")
                st.dataframe(
                    incident_types[['Sub-Category', 'Details', 'Numeric_Value']].sort_values('Numeric_Value', ascending=False),
                    column_config={"Numeric_Value": st.column_config.NumberColumn("Count")},
                    hide_index=True,
                    use_container_width=True
                )

        with tab2:
            if 'Location' in filtered_data.columns:
                loc_data = filtered_data[(filtered_data['Location'].notna()) & (filtered_data['Location'] != '-')]
                if not loc_data.empty:
                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Incident Hotspots")
                        loc_counts = loc_data['Location'].value_counts().reset_index()
                        fig = px.bar(loc_counts.head(10), x='Location', y='count', color='count', labels={'count': 'Incidents'})
                        st.plotly_chart(fig, use_container_width=True)

                    with col2:
                        st.subheader("Location Risk Map")
                        st.info("Map visualization would appear here with geographic data")

                    st.subheader("Location Details")
                    location_details = loc_data.groupby('Location').agg({
                        'Numeric_Value': 'sum',
                        'Sub-Category': lambda x: ', '.join(set(x))
                    }).reset_index()
                    st.dataframe(
                        location_details.sort_values('Numeric_Value', ascending=False),
                        column_config={
                            "Numeric_Value": st.column_config.NumberColumn("Total Incidents"),
                            "Sub-Category": st.column_config.TextColumn("Incident Types")
                        },
                        hide_index=True,
                        use_container_width=True
                    )

        with tab3:
            if show_impact:
                impact_data = security_data[security_data['Category'] == "Impact"]
                if not impact_data.empty:
                    st.subheader("Operational Impact Analysis")
                    for _, row in impact_data.iterrows():
                        with st.expander(f"🔹 {row['Sub-Category']}"):
                            st.markdown(f"**Details:** {row['Details']}")

                measures_data = security_data[security_data['Category'] == "Security Measures"]
                if not measures_data.empty:
                    st.subheader("Security Measures Timeline")
                    measures_df = measures_data[['Sub-Category', 'Details']]
                    st.dataframe(
                        measures_df,
                        column_config={"Sub-Category": "Measure", "Details": "Description"},
                        hide_index=True,
                        use_container_width=True
                    )

        with tab4:
            if show_recommendations:
                recommendations = security_data[security_data['Category'] == "Recommendations"]
                if not recommendations.empty:
                    st.subheader("Security Recommendations")
                    cols = st.columns(2)
                    for idx, (_, row) in enumerate(recommendations.iterrows()):
                        with cols[idx % 2]:
                            with st.container(border=True):
                                st.markdown(f"#### {row['Sub-Category']}")
                                st.markdown(row['Details'])
                                st.progress(min((idx + 1) * 20, 100), text=f"Priority {idx + 1}")

        st.sidebar.download_button(
            label="📅 Export Analysis",
            data=filtered_data.to_csv(index=False).encode('utf-8'),
            file_name="ghatz_security_analysis.csv",
            mime='text/csv',
            help="Export filtered data with all analysis"
        )

    except Exception as e:
        st.error(f"⚠️ Error processing data: {str(e)}")
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
