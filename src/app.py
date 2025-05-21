import streamlit as st
import pandas as pd
import warnings
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt
import plotly.express as px
from utils.gsheets import connect_to_gsheet
import calendar
import numpy as np
import plotly.express as px
import folium
from streamlit_folium import folium_static
from PIL import Image
import requests
from io import BytesIO
import gspread
from google.oauth2 import service_account
from datetime import datetime
import altair as alt
import matplotlib.pyplot as plt

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
        "Home", "GHATZ Area Map", "Dam Instrumentation", "GHATZ Facilities", 
        "GHATZ Building Structures", "GHATZ Air Valves", "GHATZ Center Pivot", 
        "Machineries and Others", "GHATZ Standpipe", "GHATZ Vibrating Wire",
        "GHATZ Seepage", "GHATZ Weather", "GHATZ Security", "GHATZ Water Level", 
        "GHATZ Staff Composition"
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

elif option == "GHATZ Area Map":
    st.title("🌍 GHATZ Area Maps - still on Production")
    st.markdown("Interactive maps of the GHATZ area with multiple viewing options")
    
    # Warning about large files
    st.warning("""
    ⚠️ These are high-resolution maps - for best performance on slower devices, 
    use the low-resolution preview or download images to view locally.
    """)
    
    # Define your image paths (adjust these to your actual image paths)
    image_paths = {
        "GHATZ Regional Topography Map": "map1.jpg",
        "Landuse/Landcover Map": "map2.jpg",
        "Vegetation Pattern Map": "map3.jpg"
    }
    
    # Predefined annotations for each map (customize these as needed)
    annotations = {
        "GHATZ Regional Topography Map": [
            dict(x=150, y=200, text="Main Dam", showarrow=True, arrowhead=2, ax=0, ay=-40),
            dict(x=300, y=150, text="Reservoir", showarrow=True, arrowhead=2, ax=0, ay=-30)
        ],
        "Landuse/Landcover Map": [
            dict(x=200, y=250, text="Irrigation Areas", showarrow=True, arrowhead=2, ax=20, ay=-30),
            dict(x=350, y=100, text="Dam Area", showarrow=True, arrowhead=2, ax=-30, ay=20)
        ],
        "Vegetation Pattern Map": [
            dict(x=100, y=300, text="Most Vegetate Zone", showarrow=True, arrowhead=2, ax=0, ay=-40),
            dict(x=400, y=200, text="low Vegetated Zone", showarrow=True, arrowhead=2, ax=-30, ay=30)
        ]
    }
    
    # View mode selector
    view_mode = st.selectbox(
        "Select View Mode",
        ["Interactive (Full Features)", "Static Image (Faster)", "Low-Resolution Preview"],
        index=0
    )
    
    # Create tabs for each map
    tabs = st.tabs(list(image_paths.keys()))
    
    for tab, (caption, img_path) in zip(tabs, image_paths.items()):
        with tab:
            st.subheader(caption)
            
            try:
                with st.spinner(f"Loading {caption}..."):
                    img = Image.open(img_path)
                    
                    if view_mode == "Low-Resolution Preview":
                        # Create thumbnail for preview
                        preview_img = img.copy()
                        preview_img.thumbnail((800, 800))
                        st.image(preview_img, use_column_width=True, caption=f"Preview: {caption}")
                        
                    elif view_mode == "Static Image":
                        st.image(img, use_column_width=True, caption=caption)
                        
                    else:  # Interactive mode
                        fig = px.imshow(img)
                        fig.update_layout(
                            title=caption,
                            coloraxis_showscale=False,
                            annotations=annotations.get(caption, [])
                        )
                        st.plotly_chart(fig, use_column_width=True)
                    
                    # Download section
                    st.markdown("---")
                    col1, col2 = st.columns(2)
                    with col1:
                        with open(img_path, "rb") as file:
                            st.download_button(
                                label="📥 Download Full Resolution",
                                data=file,
                                file_name=f"GHATZ_{caption.replace(' ', '_')}_FULL.jpg",
                                mime="image/jpeg"
                            )
                    with col2:
                        if view_mode == "Low-Resolution Preview":
                            buf = BytesIO()
                            preview_img.save(buf, format="JPEG")
                            st.download_button(
                                label="📥 Download Preview Version",
                                data=buf.getvalue(),
                                file_name=f"GHATZ_{caption.replace(' ', '_')}_PREVIEW.jpg",
                                mime="image/jpeg"
                            )
            
            except FileNotFoundError:
                st.error(f"Image file not found: {img_path}")
            except Exception as e:
                st.error(f"Error loading image: {str(e)}")
    
    # Map legend/instructions
    st.markdown("""
    ### Map Interaction Guide
    - **Zoom**: Scroll or pinch (on touch devices)
    - **Pan**: Click and drag
    - **Reset View**: Double click
    - **Annotations**: Hover over marked points for details
    """)
elif option == "GHATZ Facilities":
    # Default camp coordinates
    CAMP_COORDINATES = {
        "Gurara Camp": {"lat": 9.65, "lon": 7.72},
        "Jere Camp": {"lat": 9.54, "lon": 7.50}
    }

    # Load data from Google Sheets
    @st.cache_data(ttl=3600)
    def load_data():
        try:
            sheet = client.open("GHATZ_Data").worksheet("buildings_items")
            data = sheet.get_all_records()
            df = pd.DataFrame(data)

            # Clean and convert data
            numeric_cols = ['quantity']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            # Standardize condition status
            df['condition_status'] = df['condition_status'].str.strip().str.title()

            # Add default coordinates based on camp
            df['latitude'] = df['Camp'].map(
                lambda x: CAMP_COORDINATES.get(x, {}).get('lat'))
            df['longitude'] = df['Camp'].map(
                lambda x: CAMP_COORDINATES.get(x, {}).get('lon'))

            return df

        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            return pd.DataFrame()

    # Load the data
    df = load_data()

    # Title and description
    st.title("🏗️ GHATZ Building Facilities Analysis")
    st.markdown("""
        Comprehensive analysis of facility conditions across GHATZ camps with geospatial visualization.
        """)

    # Sidebar filters
    with st.sidebar:
        st.header("🔍 Filters")

        selected_camp = st.multiselect(
            "Select Camp(s)",
            options=sorted(df['Camp'].unique()),
            default=sorted(df['Camp'].unique())
        )

        selected_facility = st.selectbox(
            "Select Facility Type",
            ['All'] + sorted(df['building_details'].unique().tolist())
        )

        selected_condition = st.multiselect(
            "Select Condition(s)",
            options=sorted(df['condition_status'].unique().tolist()),
            default=sorted(df['condition_status'].unique().tolist())
        )

        building_type = st.multiselect(
            "Select Building Type(s)",
            options=sorted(df['buildingType'].unique().tolist()),
            default=sorted(df['buildingType'].unique().tolist())
        )

    # Apply filters
    filtered_df = df.copy()
    if selected_camp:
        filtered_df = filtered_df[filtered_df['Camp'].isin(selected_camp)]
    if selected_facility != 'All':
        filtered_df = filtered_df[filtered_df['building_details']
                                  == selected_facility]
    if selected_condition:
        filtered_df = filtered_df[filtered_df['condition_status'].isin(
            selected_condition)]
    if building_type:
        filtered_df = filtered_df[filtered_df['buildingType'].isin(
            building_type)]

    # Main content
    st.write(f"📊 Displaying {len(filtered_df)} of {len(df)} records")

    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Facilities", len(filtered_df))
    col2.metric("Camps Represented", filtered_df['Camp'].nunique())
    col3.metric("Facility Types", filtered_df['building_details'].nunique())
    col4.metric("Total Quantity", int(filtered_df['quantity'].sum()))

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "🏢 By Facility", "🏛️ By Building", "🗺️ Geospatial", "📝 Details"
    ])

    with tab1:
        st.header("Overall Condition Analysis")

        # Condition distribution
        fig = px.pie(
            filtered_df.groupby(
                'condition_status').size().reset_index(name='count'),
            names='condition_status',
            values='count',
            hole=0.3,
            title='Facility Condition Distribution',
            color='condition_status',
            color_discrete_map={
                'Critical': 'red',
                'Poor': 'orange',
                'Fair': 'yellow',
                'Good': 'lightgreen',
                'Excellent': 'darkgreen'
            }
        )
        st.plotly_chart(fig, use_container_width=True)

        # Condition by camp
        st.subheader("Condition by Camp")
        camp_data = filtered_df.groupby(
            ['Camp', 'condition_status']).size().unstack().fillna(0)
        st.bar_chart(camp_data)

    with tab2:
        st.header("Facility Type Analysis")

        # Facility condition breakdown
        fig = px.bar(
            filtered_df.groupby(
                ['building_details', 'condition_status']).size().reset_index(name='count'),
            x='building_details',
            y='count',
            color='condition_status',
            title='Condition by Facility Type',
            labels={'building_details': 'Facility Type',
                    'count': 'Number of Items'}
        )
        st.plotly_chart(fig, use_container_width=True)

        # Quantity by facility
        st.subheader("Total Quantity by Facility")
        quantity_data = filtered_df.groupby('building_details')[
            'quantity'].sum().sort_values(ascending=False)
        st.bar_chart(quantity_data)

    with tab3:
        st.header("Building Type Analysis")

        # Building type condition
        fig = px.sunburst(
            filtered_df,
            path=['buildingType', 'condition_status'],
            values='quantity',
            title='Condition Distribution by Building Type'
        )
        st.plotly_chart(fig, use_container_width=True)

        # Problem facilities by building type
        st.subheader("Critical/Poor Facilities by Building Type")
        critical_df = filtered_df[filtered_df['condition_status'].isin(
            ['Critical', 'Poor'])]
        if not critical_df.empty:
            fig = px.treemap(
                critical_df,
                path=['buildingType', 'building_details'],
                values='quantity',
                color='condition_status',
                color_discrete_map={'Critical': 'red', 'Poor': 'orange'}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No Critical/Poor facilities for current filters")

    with tab4:
        st.header("Geospatial View")

        if not filtered_df.empty:
            # Create base map centered between the two camps
            avg_lat = sum(
                coord['lat'] for coord in CAMP_COORDINATES.values()) / len(CAMP_COORDINATES)
            avg_lon = sum(
                coord['lon'] for coord in CAMP_COORDINATES.values()) / len(CAMP_COORDINATES)
            m = folium.Map(location=[avg_lat, avg_lon], zoom_start=9)

            # Add camp location markers
            for camp_name, coords in CAMP_COORDINATES.items():
                if camp_name in selected_camp or not selected_camp:
                    # Get camp-specific data
                    camp_data = filtered_df[filtered_df['Camp'] == camp_name]
                    condition_summary = camp_data['condition_status'].value_counts(
                    ).to_dict()

                    # Create popup content
                    popup_content = f"""
                        <h4>{camp_name}</h4>
                        <b>Total Facilities:</b> {len(camp_data)}<br>
                        <b>Critical:</b> {condition_summary.get('Critical', 0)}<br>
                        <b>Poor:</b> {condition_summary.get('Poor', 0)}<br>
                        <b>Fair:</b> {condition_summary.get('Fair', 0)}<br>
                        <b>Good:</b> {condition_summary.get('Good', 0)}<br>
                        <b>Excellent:</b> {condition_summary.get('Excellent', 0)}
                        """

                    folium.Marker(
                        [coords['lat'], coords['lon']],
                        popup=folium.Popup(popup_content, max_width=300),
                        tooltip=f"Click for {camp_name} details",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(m)

            # Add facility condition circles around each camp
            for camp_name, coords in CAMP_COORDINATES.items():
                if camp_name in selected_camp or not selected_camp:
                    camp_data = filtered_df[filtered_df['Camp'] == camp_name]

                    # Add circle for each condition status
                    condition_colors = {
                        'Critical': 'red',
                        'Poor': 'orange',
                        'Fair': 'yellow',
                        'Good': 'lightgreen',
                        'Excellent': 'darkgreen'
                    }

                    for condition, color in condition_colors.items():
                        condition_count = len(
                            camp_data[camp_data['condition_status'] == condition])
                        if condition_count > 0:
                            radius = condition_count * 100  # Adjust multiplier as needed
                            folium.Circle(
                                location=[coords['lat'], coords['lon']],
                                radius=radius,
                                color=color,
                                fill=True,
                                fill_color=color,
                                fill_opacity=0.4,
                                popup=f"{condition}: {condition_count} facilities"
                            ).add_to(m)

            # Display the map
            folium_static(m, width=1200, height=600)

            # Add summary statistics
            st.subheader("Geospatial Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Facilities by Camp**")
                camp_counts = filtered_df['Camp'].value_counts()
                st.bar_chart(camp_counts)

            with col2:
                st.markdown("**Condition Distribution**")
                condition_dist = filtered_df['condition_status'].value_counts()
                st.bar_chart(condition_dist)
        else:
            st.warning("No data available for the selected filters")

    with tab5:
        st.header("Detailed Facility View")

        # Search functionality
        search_query = st.text_input("🔍 Search facility comments")
        if search_query:
            detailed_df = filtered_df[
                filtered_df['item_comment'].str.contains(
                    search_query, case=False, na=False)
            ]
        else:
            detailed_df = filtered_df

        # Show data table
        st.dataframe(
            detailed_df[[
                'building_details', 'quantity', 'condition_status',
                'item_comment', 'Camp', 'buildingType'
            ]].sort_values(['condition_status', 'quantity'], ascending=[True, False]),
            column_config={
                "building_details": "Facility",
                "quantity": "Qty",
                "condition_status": "Condition",
                "item_comment": "Comments",
                "Camp": "Camp",
                "buildingType": "Building Type"
            },
            use_container_width=True,
            height=600,
            hide_index=True
        )

    # Download button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data",
        data=csv,
        file_name='ghatz_facilities.csv',
        mime='text/csv'
    )

    # Footer
    st.markdown("---")
    st.caption("GHATZ Facilities Analysis Dashboard - Last updated: 2023")

    # Add conditional formatting explanation
    with st.expander("ℹ️ Condition Status Definitions"):
        st.markdown("""
            - **Critical**: Immediate replacement needed
            - **Poor**: Significant repairs required
            - **Fair**: Functional but needs attention
            - **Good**: Fully functional, minor wear
            - **Excellent**: Like-new condition
            """)
elif option == "GHATZ Building Structures":
    @st.cache_data(ttl=3600)
    def load_building_data():
        try:
            sheet = client.open("GHATZ_Data").worksheet("buildings_")
            data = sheet.get_all_records()
            df = pd.DataFrame(data)

            # Convert and clean data
            df['date'] = pd.to_datetime(
                df['date'], dayfirst=True, errors='coerce')

            # Handle numeric columns
            numeric_cols = ['latitude', 'longitude', 'altitude']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')

            return df

        except Exception as e:
            st.error(f"Error loading data: {str(e)}")
            return pd.DataFrame()

    # Display image with error handling
    def display_image_from_url(url):
        try:
            if pd.notna(url):
                response = requests.get(url, timeout=10)  # Added timeout
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                st.image(img, caption='Building Image', use_column_width=True)
        except Exception as e:
            st.warning(f"Couldn't load image: {str(e)}")
    # Main app function
    def main():
        st.title("🏗️ GHATZ Camp Building Structures Analysis")
        st.markdown(
            "### Comprehensive analysis of building infrastructure across GHATZ camps")

        # Load data
        df = load_building_data()

        if df.empty:
            st.warning("No data loaded. Please check your connection.")
            return

        # Data preparation
        df['year_month'] = df['date'].dt.to_period('M').astype(str)
        df['condition_category'] = df['generalcomments'].str.extract(
            r'(Severe|Moderate|Slight|Good|Extreme)')[0]

        # Sidebar filters
        with st.sidebar:
            st.header("🔍 Filters")
            selected_camp = st.selectbox(
                "Select Camp",
                ['All'] + sorted(df['location'].unique()),
                index=0
            )

            selected_condition = st.selectbox(
                "Select Condition",
                ['All'] + sorted(df['generalcomments'].dropna().unique()),
                index=0
            )

            selected_type = st.multiselect(
                "Select Building Type(s)",
                options=sorted(df['typeBuilding'].dropna().unique()),
                default=[]
            )

            date_range = st.date_input(
                "Date Range",
                value=[df['date'].min(), df['date'].max()],
                min_value=df['date'].min(),
                max_value=df['date'].max()
            )

        # Apply filters
        filtered_df = df.copy()
        if selected_camp != 'All':
            filtered_df = filtered_df[filtered_df['location'] == selected_camp]
        if selected_condition != 'All':
            filtered_df = filtered_df[filtered_df['generalcomments']
                                      == selected_condition]
        if selected_type:
            filtered_df = filtered_df[filtered_df['typeBuilding'].isin(
                selected_type)]
        if len(date_range) == 2:
            filtered_df = filtered_df[
                (filtered_df['date'].dt.date >= date_range[0]) &
                (filtered_df['date'].dt.date <= date_range[1])
            ]

        # Main content
        st.write(f"📊 Displaying {len(filtered_df)} of {len(df)} records")

        # Tabs layout
        tab1, tab2, tab3, tab4 = st.tabs([
            "📈 Overview Dashboard",
            "🗺️ Geospatial View",
            "🏢 Building Details",
            "🖼️ Image Gallery"
        ])

        with tab1:
            st.header("Overview Dashboard")

            # Metrics row
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Buildings", len(filtered_df))
            col2.metric("Camps Represented", filtered_df['location'].nunique())
            col3.metric("Building Types",
                        filtered_df['typeBuilding'].nunique())
            col4.metric("Date Range",
                        f"{filtered_df['date'].min().strftime('%Y-%m-%d')} to {filtered_df['date'].max().strftime('%Y-%m-%d')}")

            # Condition distribution - FIXED VERSION
            st.subheader("Condition Distribution")
            condition_counts = filtered_df['condition_category'].value_counts(
            ).reset_index()
            condition_counts.columns = [
                'condition', 'count']  # Proper column naming

            fig = px.pie(
                condition_counts,
                names='condition',
                values='count',
                hole=0.3,
                title='Building Condition Distribution'
            )
            st.plotly_chart(fig, use_container_width=True)

            # Time series analysis
            st.subheader("Assessments Over Time")
            time_series = filtered_df.groupby(
                ['year_month', 'condition_category']).size().unstack().fillna(0)
            st.area_chart(time_series)
        with tab2:
            st.header("Geospatial View")

            if not filtered_df[['latitude', 'longitude']].dropna().empty:
                # Create map
                map_center = [
                    filtered_df['latitude'].mean(),
                    filtered_df['longitude'].mean()
                ]
                m = folium.Map(location=map_center, zoom_start=10)

                # Add markers
                for _, row in filtered_df.dropna(subset=['latitude', 'longitude']).iterrows():
                    popup_content = f"""
                    <b>Name:</b> {row['name_Building']}<br>
                    <b>Type:</b> {row['typeBuilding']}<br>
                    <b>Condition:</b> {row['generalcomments']}<br>
                    <b>Last Assessed:</b> {row['date'].strftime('%Y-%m-%d')}
                    """
                    if pd.notna(row['image_url']):
                        popup_content += f"<br><a href='{row['image_url']}' target='_blank'>View Image</a>"

                    # Color coding by condition
                    color_map = {
                        'Extreme': 'black',
                        'Severe': 'red',
                        'Moderate': 'orange',
                        'Slight': 'beige',
                        'Good': 'green'
                    }
                    color = color_map.get(row['condition_category'], 'gray')

                    folium.Marker(
                        [row['latitude'], row['longitude']],
                        popup=folium.Popup(popup_content, max_width=300),
                        tooltip=row['name_Building'],
                        icon=folium.Icon(
                            color=color, icon='building', prefix='fa')
                    ).add_to(m)

                folium_static(m, width=1200, height=600)
            else:
                st.warning(
                    "No geospatial data available for the selected filters")

            with tab3:
                st.header("Building Details")

                # Search functionality
                search_query = st.text_input("🔍 Search buildings by name")
                if search_query:
                    display_df = filtered_df[
                        filtered_df['name_Building'].str.contains(
                            search_query, case=False, na=False)
                    ]
                else:
                    display_df = filtered_df.copy()

                # Display the dataframe without image_url (we'll handle images separately)
                st.dataframe(
                    display_df[[
                        'name_Building', 'typeBuilding', 'location',
                        'generalcomments', 'final_comment', 'date',
                        'latitude', 'longitude'
                    ]].sort_values('date', ascending=False),
                    use_container_width=True,
                    height=400
                )

                # Image viewer section
                st.subheader("Image Viewer")

                if not display_df.empty:
                    # Create session state to track current image index if it doesn't exist
                    if 'current_img_idx' not in st.session_state:
                        st.session_state.current_img_idx = 0

                    # Get all rows with valid image URLs
                    image_rows = display_df[pd.notna(
                        display_df['image_url'])].reset_index(drop=True)

                    if len(image_rows) > 0:
                        col1, col2, col3 = st.columns([1, 2, 1])

                        with col1:
                            if st.button("⏮️ Previous") and st.session_state.current_img_idx > 0:
                                st.session_state.current_img_idx -= 1

                        with col3:
                            if st.button("⏭️ Next") and st.session_state.current_img_idx < len(image_rows) - 1:
                                st.session_state.current_img_idx += 1

                        with col2:
                            current_row = image_rows.iloc[st.session_state.current_img_idx]
                            st.markdown(f"**{current_row['name_Building']}**")
                            st.caption(
                                f"Image {st.session_state.current_img_idx + 1} of {len(image_rows)}")

                            try:
                                response = requests.get(
                                    current_row['image_url'], timeout=10)
                                img = Image.open(BytesIO(response.content))
                                st.image(img, use_column_width=True)

                                # Display image URL as clickable link
                                st.markdown(
                                    f"[📎 Open Image URL]({current_row['image_url']})", unsafe_allow_html=True)
                            except Exception as e:
                                st.warning(f"Couldn't load image: {str(e)}")

                        # Display current building info
                        with st.expander("📝 Building Details"):
                            st.write(
                                f"**Name:** {current_row['name_Building']}")
                            st.write(
                                f"**Type:** {current_row['typeBuilding']}")
                            st.write(
                                f"**Location:** {current_row['location']}")
                            st.write(
                                f"**Condition:** {current_row['generalcomments']}")
                            st.write(
                                f"**Date:** {current_row['date'].strftime('%Y-%m-%d')}")
                            st.write(
                                f"**Coordinates:** {current_row['latitude']}, {current_row['longitude']}")
                            st.write(
                                f"**Comments:** {current_row['final_comment']}")
                    else:
                        st.warning("No images available for these buildings")
                else:
                    st.warning("No buildings match your search criteria")
            with tab4:
                st.header("Image Gallery")

                buildings_with_images = filtered_df[pd.notna(
                    filtered_df['image_url'])]

                if not buildings_with_images.empty:
                    cols = st.columns(3)
                    successful_loads = 0

                    for idx, row in buildings_with_images.iterrows():
                        with cols[idx % 3]:
                            try:
                                # Create expander for each building
                                with st.expander(f"{row['name_Building']} ({row['condition_category']})"):
                                    # Try to display image
                                    display_image_from_url(row['image_url'])

                                    # Show building info
                                    st.caption(f"""
                                    **Location:** {row['location']}  
                                    **Type:** {row['typeBuilding']}  
                                    **Condition:** {row['generalcomments']}  
                                    **Date:** {row['date'].strftime('%Y-%m-%d')}
                                    """)

                                    successful_loads += 1
                            except Exception as e:
                                st.warning(
                                    f"Couldn't display {row['name_Building']}: {str(e)}")

                    if successful_loads == 0:
                        st.warning(
                            "No images could be loaded from the available URLs")
                else:
                    st.warning("No images available for the selected filters")
    if __name__ == "__main__":
        main()
elif option == "GHATZ Air Valves":
    def air_valve_analysis():
        @st.cache_data(ttl=3600)
        def load_airvalve_data():
            try:
                # Load data from Google Sheets (replace with your actual sheet name)
                sheet = client.open("GHATZ_Data").worksheet("airvalves")
                data = sheet.get_all_records()
                df = pd.DataFrame(data)

                # Convert and clean data
                df['_submission_time'] = pd.to_datetime(
                    df['_submission_time'], errors='coerce')

                # Handle numeric columns
                numeric_cols = ['latitude', 'longitude', 'altitude']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')

                return df

            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
                return pd.DataFrame()

        # Display image with error handling
        def display_image_from_url(url):
            try:
                if pd.notna(url):
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption='Air Valve Image',
                             use_column_width=True)
            except Exception as e:
                st.warning(f"Couldn't load image: {str(e)}")

        # Main app function
        def main():
            st.title("🛢️ GHATZ Camp Air Valve Analysis")
            st.markdown(
                "### Comprehensive analysis of air valve infrastructure across GHATZ camps")

            # Load data
            df = load_airvalve_data()

            if df.empty:
                st.warning("No data loaded. Please check your connection.")
                return

            # Data preparation
            df['year_month'] = df['_submission_time'].dt.to_period(
                'M').astype(str)

            # Sidebar filters
            with st.sidebar:
                st.header("🔍 Filters")
                selected_camp = st.selectbox(
                    "Select Camp",
                    ['All'] + sorted(df['location'].unique()),
                    index=0
                )

                selected_condition = st.selectbox(
                    "Select Condition",
                    ['All'] +
                    sorted(df['condition_category'].dropna().unique()),
                    index=0
                )

                selected_access = st.selectbox(
                    "Select Accessibility",
                    ['All'] +
                    sorted(df['accessibility_state'].dropna().unique()),
                    index=0
                )

                date_range = st.date_input(
                    "Date Range",
                    value=[df['_submission_time'].min(
                    ), df['_submission_time'].max()],
                    min_value=df['_submission_time'].min(),
                    max_value=df['_submission_time'].max()
                )

            # Apply filters
            filtered_df = df.copy()
            if selected_camp != 'All':
                filtered_df = filtered_df[filtered_df['location']
                                          == selected_camp]
            if selected_condition != 'All':
                filtered_df = filtered_df[filtered_df['condition_category']
                                          == selected_condition]
            if selected_access != 'All':
                filtered_df = filtered_df[filtered_df['accessibility_state']
                                          == selected_access]
            if len(date_range) == 2:
                filtered_df = filtered_df[
                    (filtered_df['_submission_time'].dt.date >= date_range[0]) &
                    (filtered_df['_submission_time'].dt.date <= date_range[1])
                ]

            # Main content
            st.write(f"📊 Displaying {len(filtered_df)} of {len(df)} records")

            # Tabs layout
            tab1, tab2, tab3, tab4 = st.tabs([
                "📈 Overview Dashboard",
                "🗺️ Geospatial View",
                "🛢️ Valve Details",
                "🖼️ Image Gallery"
            ])

            with tab1:
                st.header("Overview Dashboard")

                # Metrics row
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Valves", len(filtered_df))
                col2.metric("Camps Represented",
                            filtered_df['location'].nunique())
                col3.metric("Valves Needing Repair",
                            len(filtered_df[filtered_df['condition_category'].isin(['Severe Damage', 'Slight Damage'])]))
                col4.metric("Date Range",
                            f"{filtered_df['_submission_time'].min().strftime('%Y-%m-%d')} to {filtered_df['_submission_time'].max().strftime('%Y-%m-%d')}")

                # Condition distribution
                st.subheader("Condition Distribution")
                condition_counts = filtered_df['condition_category'].value_counts(
                ).reset_index()
                condition_counts.columns = ['condition', 'count']

                fig = px.pie(
                    condition_counts,
                    names='condition',
                    values='count',
                    hole=0.3,
                    title='Air Valve Condition Distribution'
                )
                st.plotly_chart(fig, use_container_width=True)

                # Accessibility distribution
                st.subheader("Accessibility Status")
                access_counts = filtered_df['accessibility_state'].value_counts(
                ).reset_index()
                access_counts.columns = ['accessibility', 'count']

                fig = px.bar(
                    access_counts,
                    x='accessibility',
                    y='count',
                    title='Air Valve Accessibility Status'
                )
                st.plotly_chart(fig, use_container_width=True)

                # Time series analysis
                st.subheader("Assessments Over Time")
                time_series = filtered_df.groupby(
                    ['year_month', 'condition_category']).size().unstack().fillna(0)
                st.area_chart(time_series)

            with tab2:
                st.header("Geospatial View")

                if not filtered_df[['latitude', 'longitude']].dropna().empty:
                    # Create map
                    map_center = [
                        filtered_df['latitude'].mean(),
                        filtered_df['longitude'].mean()
                    ]
                    m = folium.Map(location=map_center, zoom_start=12)

                    # Add markers
                    for _, row in filtered_df.dropna(subset=['latitude', 'longitude']).iterrows():
                        popup_content = f"""
                        <b>Location:</b> {row['location']}<br>
                        <b>Valve ID:</b> {row['airvalves_facilities/airvalves_number']}<br>
                        <b>Condition:</b> {row['condition_category']}<br>
                        <b>Accessibility:</b> {row['accessibility_state']}<br>
                        <b>Last Assessed:</b> {row['_submission_time'].strftime('%Y-%m-%d')}
                        """
                        if pd.notna(row['image_url']):
                            popup_content += f"<br><a href='{row['image_url']}' target='_blank'>View Image</a>"

                        # Color coding by condition
                        color_map = {
                            'Severe Damage': 'red',
                            'Slight Damage': 'orange',
                            'Good Condition': 'green'
                        }
                        color = color_map.get(
                            row['condition_category'], 'gray')

                        folium.Marker(
                            [row['latitude'], row['longitude']],
                            popup=folium.Popup(popup_content, max_width=300),
                            tooltip=f"Valve {row['airvalves_facilities/airvalves_number']}",
                            icon=folium.Icon(
                                color=color, icon='tint', prefix='fa')
                        ).add_to(m)

                    folium_static(m, width=1200, height=600)
                else:
                    st.warning(
                        "No geospatial data available for the selected filters")

            with tab3:
                st.header("Valve Details")

                # Search functionality
                search_query = st.text_input("🔍 Search valves by ID")
                if search_query:
                    display_df = filtered_df[
                        filtered_df['airvalves_facilities/airvalves_number'].astype(
                            str).str.contains(search_query, case=False, na=False)
                    ]
                else:
                    display_df = filtered_df.copy()

                # Display the dataframe without image_url (we'll handle images separately)
                st.dataframe(
                    display_df[[
                        'airvalves_facilities/airvalves_number', 'location', 'condition_category',
                        'accessibility_state', 'generalcomments', '_submission_time',
                        'latitude', 'longitude'
                    ]].sort_values('_submission_time', ascending=False),
                    use_container_width=True,
                    height=400
                )

                # Image viewer section
                st.subheader("Image Viewer")

                if not display_df.empty:
                    # Create session state to track current image index if it doesn't exist
                    if 'current_img_idx' not in st.session_state:
                        st.session_state.current_img_idx = 0

                    # Get all rows with valid image URLs
                    image_rows = display_df[pd.notna(
                        display_df['image_url'])].reset_index(drop=True)

                    if len(image_rows) > 0:
                        col1, col2, col3 = st.columns([1, 2, 1])

                        with col1:
                            if st.button("⏮️ Previous") and st.session_state.current_img_idx > 0:
                                st.session_state.current_img_idx -= 1

                        with col3:
                            if st.button("⏭️ Next") and st.session_state.current_img_idx < len(image_rows) - 1:
                                st.session_state.current_img_idx += 1

                        with col2:
                            current_row = image_rows.iloc[st.session_state.current_img_idx]
                            st.markdown(
                                f"**Valve {current_row['airvalves_facilities/airvalves_number']}**")
                            st.caption(
                                f"Image {st.session_state.current_img_idx + 1} of {len(image_rows)}")

                            try:
                                display_image_from_url(
                                    current_row['image_url'])

                                # Display image URL as clickable link
                                st.markdown(
                                    f"[📎 Open Image URL]({current_row['image_url']})", unsafe_allow_html=True)
                            except Exception as e:
                                st.warning(f"Couldn't load image: {str(e)}")

                        # Display current valve info
                        with st.expander("📝 Valve Details"):
                            st.write(
                                f"**Valve ID:** {current_row['airvalves_facilities/airvalves_number']}")
                            st.write(
                                f"**Location:** {current_row['location']}")
                            st.write(
                                f"**Condition:** {current_row['condition_category']}")
                            st.write(
                                f"**Accessibility:** {current_row['accessibility_state']}")
                            st.write(
                                f"**Date:** {current_row['_submission_time'].strftime('%Y-%m-%d')}")
                            st.write(
                                f"**Coordinates:** {current_row['latitude']}, {current_row['longitude']}")
                            st.write(
                                f"**Comments:** {current_row['generalcomments']}")
                    else:
                        st.warning("No images available for these valves")
                else:
                    st.warning("No valves match your search criteria")

            with tab4:
                st.header("Image Gallery")

                valves_with_images = filtered_df[pd.notna(
                    filtered_df['image_url'])]

                if not valves_with_images.empty:
                    cols = st.columns(3)
                    successful_loads = 0

                    for idx, row in valves_with_images.iterrows():
                        with cols[idx % 3]:
                            try:
                                # Create expander for each valve
                                with st.expander(f"Valve {row['airvalves_facilities/airvalves_number']} ({row['condition_category']})"):
                                    # Try to display image
                                    display_image_from_url(row['image_url'])

                                    # Show valve info
                                    st.caption(f"""
                                    **Location:** {row['location']}  
                                    **Condition:** {row['condition_category']}  
                                    **Accessibility:** {row['accessibility_state']}  
                                    **Date:** {row['_submission_time'].strftime('%Y-%m-%d')}
                                    """)

                                    successful_loads += 1
                            except Exception as e:
                                st.warning(
                                    f"Couldn't display Valve {row['airvalves_facilities/airvalves_number']}: {str(e)}")

                    if successful_loads == 0:
                        st.warning(
                            "No images could be loaded from the available URLs")
                else:
                    st.warning("No images available for the selected filters")

        if __name__ == "__main__":
            main()

    # Call the function to run the app
    air_valve_analysis()
elif option == "GHATZ Center Pivot":

    def center_pivot_analysis():
        @st.cache_data(ttl=3600)
        def load_pivot_data():
            try:
                # Load data from Google Sheets
                sheet = client.open("GHATZ_Data").worksheet("centerPivot")
                data = sheet.get_all_records()
                df = pd.DataFrame(data)

                # Clean and standardize condition categories
                df['pivot_Condition'] = df['pivot_Condition'].str.strip().str.title()

                # Convert numeric columns
                numeric_cols = ['latitude', 'longitude', 'altitude']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')

                return df

            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
                return pd.DataFrame()

        def display_image_from_url(url):
            try:
                if pd.notna(url):
                    response = requests.get(url, timeout=5)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption='Center Pivot Image',
                             use_column_width=True)
            except Exception as e:
                st.warning(f"Couldn't load image: {str(e)}")

        def main():
            st.title("🌾 GHATZ Center Pivot Irrigation Analysis")
            st.markdown(
                "### Comprehensive analysis of center pivot irrigation systems across GHATZ camps")

            # Load data
            df = load_pivot_data()

            if df.empty:
                st.warning("No data loaded. Please check your connection.")
                return

            # Sidebar filters
            with st.sidebar:
                st.header("🔍 Filters")

                # Location filter
                selected_location = st.selectbox(
                    "Select Camp Location",
                    ['All'] + sorted(df['location'].unique()),
                    index=0
                )

                # Condition filter
                condition_options = [
                    'All'] + sorted(df['pivot_Condition'].dropna().unique())
                selected_condition = st.selectbox(
                    "Select Pivot Condition",
                    condition_options,
                    index=0
                )

                # Ownership filter
                ownership_options = [
                    'All'] + sorted(df['pivot_ownership'].dropna().unique())
                selected_ownership = st.multiselect(
                    "Select Ownership(s)",
                    options=ownership_options[1:],  # Skip 'All'
                    default=[]
                )

                # Functionality filter
                functionality_options = [
                    'All', 'Functioning', 'Not Functioning']
                selected_functionality = st.selectbox(
                    "Select Functionality Status",
                    functionality_options,
                    index=0
                )

            # Apply filters
            filtered_df = df.copy()
            if selected_location != 'All':
                filtered_df = filtered_df[filtered_df['location']
                                          == selected_location]
            if selected_condition != 'All':
                filtered_df = filtered_df[filtered_df['pivot_Condition']
                                          == selected_condition]
            if selected_ownership:
                filtered_df = filtered_df[filtered_df['pivot_ownership'].isin(
                    selected_ownership)]
            if selected_functionality != 'All':
                if selected_functionality == 'Functioning':
                    filtered_df = filtered_df[filtered_df['generalcomments'].str.contains(
                        'Functioning', case=False, na=False)]
                else:
                    filtered_df = filtered_df[filtered_df['generalcomments'].str.contains(
                        'Not Functioning', case=False, na=False)]

            # Main content
            st.write(f"📊 Displaying {len(filtered_df)} of {len(df)} records")

            # Tabs layout
            tab1, tab2, tab3, tab4 = st.tabs([
                "📈 Overview Dashboard",
                "🗺️ Geospatial View",
                "🌾 Pivot Details",
                "🖼️ Image Gallery"
            ])

# Replace the functionality by ownership section in tab1 with this:

            with tab1:
                st.header("Overview Dashboard")

                # Metrics row
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Pivots", len(filtered_df))
                functioning_count = len(filtered_df[filtered_df['generalcomments'].str.contains(
                    'Functioning', case=False, na=False)])
                col2.metric("Functioning Pivots", functioning_count)
                col3.metric("Ownership Types",
                            filtered_df['pivot_ownership'].nunique())

                # Condition distribution
                st.subheader("Condition Distribution")
                if not filtered_df.empty:
                    condition_counts = filtered_df['pivot_Condition'].value_counts(
                    ).reset_index()
                    condition_counts.columns = ['Condition', 'Count']

                    fig = px.pie(
                        condition_counts,
                        names='Condition',
                        values='Count',
                        hole=0.3,
                        title='Center Pivot Condition Distribution'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No data available for condition distribution")

                # Ownership distribution
                st.subheader("Ownership Distribution")
                if not filtered_df.empty:
                    ownership_counts = filtered_df['pivot_ownership'].value_counts(
                    ).reset_index()
                    ownership_counts.columns = ['Ownership', 'Count']

                    fig = px.bar(
                        ownership_counts,
                        x='Ownership',
                        y='Count',
                        title='Center Pivot Ownership Distribution'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No data available for ownership distribution")

                # Functionality by ownership
                st.subheader("Functionality by Ownership")
                if not filtered_df.empty:
                    try:
                        # Create a cross-tabulation of ownership vs functionality
                        func_by_owner = pd.crosstab(
                            filtered_df['pivot_ownership'],
                            filtered_df['generalcomments'].str.contains(
                                'Functioning'),
                            rownames=['Ownership'],
                            colnames=['Functioning']
                        )

                        # Only try to rename columns if we have both statuses
                        if len(func_by_owner.columns) == 2:
                            func_by_owner.columns = [
                                'Not Functioning', 'Functioning']
                        elif len(func_by_owner.columns) == 1:
                            # Handle case where we only have one status
                            if func_by_owner.columns[0]:
                                func_by_owner.columns = ['Functioning']
                            else:
                                func_by_owner.columns = ['Not Functioning']

                        st.bar_chart(func_by_owner)
                    except Exception as e:
                        st.warning(
                            f"Could not display functionality by ownership: {str(e)}")
                else:
                    st.warning("No data available for functionality analysis")
            with tab2:
                st.header("Geospatial View")

                if not filtered_df[['latitude', 'longitude']].dropna().empty:
                    # Create map
                    map_center = [
                        filtered_df['latitude'].mean(),
                        filtered_df['longitude'].mean()
                    ]
                    m = folium.Map(location=map_center, zoom_start=12)

                    # Color mapping for conditions
                    color_map = {
                        'Critical': 'red',
                        'Good': 'orange',
                        'Excellent': 'green'
                    }

                    # Add markers
                    for _, row in filtered_df.dropna(subset=['latitude', 'longitude']).iterrows():
                        # Determine marker color
                        condition = row['pivot_Condition']
                        color = color_map.get(condition, 'gray')

                        # Create popup content
                        popup_content = f"""
                        <b>Pivot ID:</b> {row['pivot_number']}<br>
                        <b>Location:</b> {row['location']}<br>
                        <b>Ownership:</b> {row['pivot_ownership']}<br>
                        <b>Condition:</b> {condition}<br>
                        <b>Status:</b> {row['generalcomments']}
                        """
                        if pd.notna(row['image_url']):
                            popup_content += f"<br><a href='{row['image_url']}' target='_blank'>View Image</a>"

                        folium.Marker(
                            [row['latitude'], row['longitude']],
                            popup=folium.Popup(popup_content, max_width=300),
                            tooltip=f"Pivot {row['pivot_number']}",
                            icon=folium.Icon(
                                color=color, icon='tint', prefix='fa')
                        ).add_to(m)

                    folium_static(m, width=1200, height=600)
                else:
                    st.warning(
                        "No geospatial data available for the selected filters")

            with tab3:
                st.header("Pivot Details")

                # Search functionality
                search_query = st.text_input(
                    "🔍 Search pivots by ID or ownership")
                if search_query:
                    display_df = filtered_df[
                        filtered_df['pivot_number'].astype(str).str.contains(search_query, case=False, na=False) |
                        filtered_df['pivot_ownership'].astype(str).str.contains(
                            search_query, case=False, na=False)
                    ]
                else:
                    display_df = filtered_df.copy()

                # Display the dataframe
                st.dataframe(
                    display_df[[
                        'pivot_number', 'location', 'pivot_ownership',
                        'pivot_Condition', 'generalcomments', 'latitude', 'longitude'
                    ]].sort_values('pivot_number'),
                    use_container_width=True,
                    height=400
                )

                # Image viewer section
                st.subheader("Image Viewer")

                if not display_df.empty:
                    # Create session state to track current image index
                    if 'current_img_idx' not in st.session_state:
                        st.session_state.current_img_idx = 0

                    # Get all rows with valid image URLs
                    image_rows = display_df[pd.notna(
                        display_df['image_url'])].reset_index(drop=True)

                    if len(image_rows) > 0:
                        col1, col2, col3 = st.columns([1, 2, 1])

                        with col1:
                            if st.button("⏮️ Previous") and st.session_state.current_img_idx > 0:
                                st.session_state.current_img_idx -= 1

                        with col3:
                            if st.button("⏭️ Next") and st.session_state.current_img_idx < len(image_rows) - 1:
                                st.session_state.current_img_idx += 1

                        with col2:
                            current_row = image_rows.iloc[st.session_state.current_img_idx]
                            st.markdown(
                                f"**Pivot {current_row['pivot_number']}**")
                            st.caption(
                                f"Image {st.session_state.current_img_idx + 1} of {len(image_rows)}")

                            try:
                                display_image_from_url(
                                    current_row['image_url'])
                                st.markdown(
                                    f"[📎 Open Image URL]({current_row['image_url']})", unsafe_allow_html=True)
                            except Exception as e:
                                st.warning(f"Couldn't load image: {str(e)}")

                        # Display current pivot info
                        with st.expander("📝 Pivot Details"):
                            st.write(
                                f"**Pivot ID:** {current_row['pivot_number']}")
                            st.write(
                                f"**Location:** {current_row['location']}")
                            st.write(
                                f"**Ownership:** {current_row['pivot_ownership']}")
                            st.write(
                                f"**Condition:** {current_row['pivot_Condition']}")
                            st.write(
                                f"**Status:** {current_row['generalcomments']}")
                            st.write(
                                f"**Coordinates:** {current_row['latitude']}, {current_row['longitude']}")
                    else:
                        st.warning("No images available for these pivots")
                else:
                    st.warning("No pivots match your search criteria")

            with tab4:
                st.header("Image Gallery")

                pivots_with_images = filtered_df[pd.notna(
                    filtered_df['image_url'])]

                if not pivots_with_images.empty:
                    cols = st.columns(3)
                    successful_loads = 0

                    for idx, row in pivots_with_images.iterrows():
                        with cols[idx % 3]:
                            try:
                                # Create expander for each pivot
                                with st.expander(f"Pivot {row['pivot_number']} ({row['pivot_Condition']})"):
                                    # Try to display image
                                    display_image_from_url(row['image_url'])

                                    # Show pivot info
                                    st.caption(f"""
                                    **Location:** {row['location']}  
                                    **Ownership:** {row['pivot_ownership']}  
                                    **Status:** {row['generalcomments']}
                                    """)

                                    successful_loads += 1
                            except Exception as e:
                                st.warning(
                                    f"Couldn't display Pivot {row['pivot_number']}: {str(e)}")

                    if successful_loads == 0:
                        st.warning(
                            "No images could be loaded from the available URLs")
                else:
                    st.warning("No images available for the selected filters")

        if __name__ == "__main__":
            main()

    # Call the function to run the app
    center_pivot_analysis()
elif option == "Machineries and Others":
    def machinery_analysis():
        @st.cache_data(ttl=3600)
        def load_machinery_data():
            try:
                # Load data from Google Sheets
                sheet = client.open("GHATZ_Data").worksheet("machineries")
                data = sheet.get_all_records()
                df = pd.DataFrame(data)

                # Clean and standardize condition categories
                df['generalcomments'] = df['generalcomments'].str.strip()
                df['accessibility_state'] = df['accessibility_state'].str.strip()

                # Convert numeric columns
                numeric_cols = ['latitude', 'longitude', 'altitude']
                for col in numeric_cols:
                    if col in df.columns:
                        df[col] = pd.to_numeric(df[col], errors='coerce')

                return df

            except Exception as e:
                st.error(f"Error loading data: {str(e)}")
                return pd.DataFrame()

        def display_image_from_url(url):
            try:
                if pd.notna(url):
                    response = requests.get(url, timeout=10)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    st.image(img, caption='Machinery Image',
                             use_column_width=True)
            except Exception as e:
                st.warning(f"Couldn't load image: {str(e)}")

        def determine_functionality(comment):
            if pd.isna(comment):
                return "Unknown"
            comment = str(comment).lower()
            if "functioning" in comment:
                return "Functioning"
            elif "not functioning" in comment:
                return "Not Functioning"
            elif "functional" in comment:
                return "Functioning"
            elif "not functional" in comment:
                return "Not Functioning"
            else:
                return "Unknown"

        def main():
            st.title("🏭 GHATZ Machinery Equipment Analysis")
            st.markdown(
                "### Comprehensive analysis of machinery and equipment across GHATZ camps")

            # Load data
            df = load_machinery_data()

            if df.empty:
                st.warning("No data loaded. Please check your connection.")
                return

            # Add functionality column
            df['functionality'] = df['generalcomments'].apply(
                determine_functionality)

            # Sidebar filters
            with st.sidebar:
                st.header("🔍 Filters")

                # Location filter
                selected_location = st.selectbox(
                    "Select Camp Location",
                    ['All'] + sorted(df['location'].unique()),
                    index=0
                )

                # Equipment type filter
                equipment_types = [
                    'All'] + sorted(df['type_equip_machine'].dropna().unique())
                selected_equipment = st.selectbox(
                    "Select Equipment Type",
                    equipment_types,
                    index=0
                )

                # Condition filter
                condition_options = [
                    'All'] + sorted(df['generalcomments'].dropna().unique())
                selected_condition = st.selectbox(
                    "Select Condition",
                    condition_options,
                    index=0
                )

                # Functionality filter
                functionality_options = ['All'] + \
                    sorted(df['functionality'].unique())
                selected_functionality = st.selectbox(
                    "Select Functionality Status",
                    functionality_options,
                    index=0
                )

                # Accessibility filter
                accessibility_options = ['All'] + \
                    sorted(df['accessibility_state'].unique())
                selected_accessibility = st.selectbox(
                    "Select Accessibility",
                    accessibility_options,
                    index=0
                )

            # Apply filters
            filtered_df = df.copy()
            if selected_location != 'All':
                filtered_df = filtered_df[filtered_df['location']
                                          == selected_location]
            if selected_equipment != 'All':
                filtered_df = filtered_df[filtered_df['type_equip_machine']
                                          == selected_equipment]
            if selected_condition != 'All':
                filtered_df = filtered_df[filtered_df['generalcomments']
                                          == selected_condition]
            if selected_functionality != 'All':
                filtered_df = filtered_df[filtered_df['functionality']
                                          == selected_functionality]
            if selected_accessibility != 'All':
                filtered_df = filtered_df[filtered_df['accessibility_state']
                                          == selected_accessibility]

            # Main content
            st.write(f"📊 Displaying {len(filtered_df)} of {len(df)} records")

            # Tabs layout
            tab1, tab2, tab3, tab4 = st.tabs([
                "📈 Overview Dashboard",
                "🗺️ Geospatial View",
                "🛠️ Equipment Details",
                "🖼️ Image Gallery"
            ])

            with tab1:
                st.header("Overview Dashboard")

                # Metrics row
                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Equipment", len(filtered_df))
                functioning_count = len(
                    filtered_df[filtered_df['functionality'] == "Functioning"])
                col2.metric("Functioning Equipment", functioning_count)
                col3.metric("Equipment Types",
                            filtered_df['type_equip_machine'].nunique())
                col4.metric("Camps Represented",
                            filtered_df['location'].nunique())

                # Equipment type distribution
                st.subheader("Equipment Type Distribution")
                if not filtered_df.empty:
                    type_counts = filtered_df['type_equip_machine'].value_counts(
                    ).reset_index()
                    type_counts.columns = ['Equipment Type', 'Count']

                    fig = px.bar(
                        type_counts,
                        x='Equipment Type',
                        y='Count',
                        title='Equipment Type Distribution'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning(
                        "No data available for equipment type distribution")

                # Functionality distribution
                st.subheader("Functionality Status")
                if not filtered_df.empty:
                    func_counts = filtered_df['functionality'].value_counts(
                    ).reset_index()
                    func_counts.columns = ['Status', 'Count']

                    fig = px.pie(
                        func_counts,
                        names='Status',
                        values='Count',
                        hole=0.3,
                        title='Equipment Functionality Status'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning(
                        "No data available for functionality distribution")

                # Accessibility distribution
                st.subheader("Accessibility Status")
                if not filtered_df.empty:
                    access_counts = filtered_df['accessibility_state'].value_counts(
                    ).reset_index()
                    access_counts.columns = ['Accessibility', 'Count']

                    fig = px.bar(
                        access_counts,
                        x='Accessibility',
                        y='Count',
                        title='Equipment Accessibility Status'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning(
                        "No data available for accessibility distribution")

            with tab2:
                st.header("Geospatial View")

                if not filtered_df[['latitude', 'longitude']].dropna().empty:
                    # Create map
                    map_center = [
                        filtered_df['latitude'].mean(),
                        filtered_df['longitude'].mean()
                    ]
                    m = folium.Map(location=map_center, zoom_start=12)

                    # Color mapping for functionality
                    color_map = {
                        'Functioning': 'green',
                        'Not Functioning': 'red',
                        'Unknown': 'gray'
                    }

                    # Add markers
                    for _, row in filtered_df.dropna(subset=['latitude', 'longitude']).iterrows():
                        # Determine marker color
                        functionality = row['functionality']
                        color = color_map.get(functionality, 'blue')

                        # Create popup content
                        popup_content = f"""
                        <b>Type:</b> {row['type_equip_machine']}<br>
                        <b>Location:</b> {row['location']}<br>
                        <b>Condition:</b> {row['generalcomments']}<br>
                        <b>Functionality:</b> {functionality}<br>
                        <b>Accessibility:</b> {row['accessibility_state']}
                        """
                        if pd.notna(row['image_url']):
                            popup_content += f"<br><a href='{row['image_url']}' target='_blank'>View Image</a>"

                        folium.Marker(
                            [row['latitude'], row['longitude']],
                            popup=folium.Popup(popup_content, max_width=300),
                            tooltip=row['type_equip_machine'],
                            icon=folium.Icon(
                                color=color, icon='gear', prefix='fa')
                        ).add_to(m)

                    folium_static(m, width=1200, height=600)
                else:
                    st.warning(
                        "No geospatial data available for the selected filters")

            with tab3:
                st.header("Equipment Details")

                # Search functionality
                search_query = st.text_input(
                    "🔍 Search equipment by type or description")
                if search_query:
                    display_df = filtered_df[
                        filtered_df['type_equip_machine'].str.contains(search_query, case=False, na=False) |
                        filtered_df['model_description'].str.contains(
                            search_query, case=False, na=False)
                    ]
                else:
                    display_df = filtered_df.copy()

                # Display the dataframe
                st.dataframe(
                    display_df[[
                        'type_equip_machine', 'model_description', 'location',
                        'generalcomments', 'functionality', 'accessibility_state',
                        'latitude', 'longitude'
                    ]].sort_values('type_equip_machine'),
                    use_container_width=True,
                    height=400
                )

                # Image viewer section
                st.subheader("Image Viewer")

                if not display_df.empty:
                    # Create session state to track current image index
                    if 'current_img_idx' not in st.session_state:
                        st.session_state.current_img_idx = 0

                    # Get all rows with valid image URLs
                    image_rows = display_df[pd.notna(
                        display_df['image_url'])].reset_index(drop=True)

                    if len(image_rows) > 0:
                        col1, col2, col3 = st.columns([1, 2, 1])

                        with col1:
                            if st.button("⏮️ Previous") and st.session_state.current_img_idx > 0:
                                st.session_state.current_img_idx -= 1

                        with col3:
                            if st.button("⏭️ Next") and st.session_state.current_img_idx < len(image_rows) - 1:
                                st.session_state.current_img_idx += 1

                        with col2:
                            current_row = image_rows.iloc[st.session_state.current_img_idx]
                            st.markdown(
                                f"**{current_row['type_equip_machine']}**")
                            st.caption(
                                f"Image {st.session_state.current_img_idx + 1} of {len(image_rows)}")

                            try:
                                display_image_from_url(
                                    current_row['image_url'])
                                st.markdown(
                                    f"[📎 Open Image URL]({current_row['image_url']})", unsafe_allow_html=True)
                            except Exception as e:
                                st.warning(f"Couldn't load image: {str(e)}")

                        # Display current equipment info
                        with st.expander("📝 Equipment Details"):
                            st.write(
                                f"**Type:** {current_row['type_equip_machine']}")
                            st.write(
                                f"**Model/Description:** {current_row['model_description']}")
                            st.write(
                                f"**Location:** {current_row['location']}")
                            st.write(
                                f"**Condition:** {current_row['generalcomments']}")
                            st.write(
                                f"**Functionality:** {current_row['functionality']}")
                            st.write(
                                f"**Accessibility:** {current_row['accessibility_state']}")
                            st.write(
                                f"**Coordinates:** {current_row['latitude']}, {current_row['longitude']}")
                    else:
                        st.warning(
                            "No images available for these equipment items")
                else:
                    st.warning("No equipment matches your search criteria")

            with tab4:
                st.header("Image Gallery")

                equipment_with_images = filtered_df[pd.notna(
                    filtered_df['image_url'])]

                if not equipment_with_images.empty:
                    cols = st.columns(3)
                    successful_loads = 0

                    for idx, row in equipment_with_images.iterrows():
                        with cols[idx % 3]:
                            try:
                                # Create expander for each equipment
                                with st.expander(f"{row['type_equip_machine']} ({row['functionality']})"):
                                    # Try to display image
                                    display_image_from_url(row['image_url'])

                                    # Show equipment info
                                    st.caption(f"""
                                    **Location:** {row['location']}  
                                    **Condition:** {row['generalcomments']}  
                                    **Accessibility:** {row['accessibility_state']}
                                    """)

                                    successful_loads += 1
                            except Exception as e:
                                st.warning(
                                    f"Couldn't display {row['type_equip_machine']}: {str(e)}")

                    if successful_loads == 0:
                        st.warning(
                            "No images could be loaded from the available URLs")
                else:
                    st.warning("No images available for the selected filters")

        if __name__ == "__main__":
            main()

    # Call the function to run the app
    machinery_analysis()
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
        df['Date of Installation'] = pd.to_datetime(
            df['Date of Installation'], dayfirst=True, errors='coerce')

        numeric_cols = ['Depth', 'Elevation', 'x', 'y', 'GROUND LEVEL', 'FOUNDATION LEVEL',
                        'TOP OF PVC LEVEL', 'TOTAL DEPTH ( m )', 'HEIGHT OF PVC ABOVE G.L', 'NTPL']

        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col].astype(
                str).str.replace(',', ''), errors='coerce')

        # Calculate metrics
        df['Days Since Installation'] = (
            df['Date'] - df['Date of Installation']).dt.days
        df['Depth Change'] = df.groupby('RW_ID')['Depth'].diff()
        df['Elevation Change'] = df.groupby('RW_ID')['Elevation'].diff()
        df['Cumulative Depth Change'] = df.groupby(
            'RW_ID')['Depth Change'].cumsum()

        return df.dropna(subset=['Date'])

    try:
        df = load_relief_well_data()

        # Sidebar filters - expanded
        st.sidebar.header("🔍 Filter Options")
        well_ids = df['RW_ID'].unique()
        selected_wells = st.sidebar.multiselect(
            "Select Relief Well(s)", well_ids, default=well_ids[0])

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
        cols[2].metric("Avg Depth Change",
                       f"{filtered_df['Depth Change'].mean():.2f} m")
        cols[3].metric("Max Elevation",
                       f"{filtered_df['Elevation'].max():.2f} m")

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
            st.dataframe(change_rates.style.format(
                "{:.4f}"), use_container_width=True)

            # New: Correlation matrix
            st.subheader("Parameter Correlations")
            numeric_df = filtered_df.select_dtypes(
                include=['float64', 'int64'])
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
                filtered_df.sort_values(
                    ['RW_ID', 'Date'], ascending=[True, False]),
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
            monthly = filtered_df.groupby(["year", "month", "month_name"])[
                banks].sum().reset_index()
            monthly["month_year"] = monthly["month_name"] + \
                " " + monthly["year"].astype(str)

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
            monthly_avg = filtered_df.groupby(
                "month_name")[banks].mean().reset_index()
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
            cumulative = filtered_df.sort_values(
                "date").groupby("year")[banks].cumsum()
            cumulative["date"] = filtered_df["date"]
            fig = px.line(
                cumulative,
                x="date",
                y=banks,
                title="Cumulative Rainfall by Year (mm)",
                labels={
                    "value": "Cumulative Rainfall (mm)", "variable": "Bank"},
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
        default_categories = [cat for cat in [
            "Incident Summary", "Incident Breakdown", "Notable Incidents"] if cat in categories]

        selected_categories = st.sidebar.multiselect(
            "Select Categories",
            options=categories,
            default=default_categories
        )

        show_impact = st.sidebar.checkbox("Show Impact Analysis", True)
        show_recommendations = st.sidebar.checkbox(
            "Show Recommendations", True)

        # Filter data
        filtered_data = security_data[security_data['Category'].isin(
            selected_categories)].copy()

        st.subheader("📊 Security Metrics Overview")

        def calculate_metric(df, category, sub_category):
            try:
                subset = df[(df['Category'] == category) & (
                    df['Sub-Category'] == sub_category)]
                return subset['Numeric_Value'].iloc[0] if not subset.empty else 0
            except:
                return 0

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            total_incidents = calculate_metric(
                filtered_data, "Incident Summary", "Total Incidents")
            st.metric("Total Incidents", total_incidents)

        with col2:
            fatalities = calculate_metric(
                filtered_data, "Incident Summary", "Fatalities")
            st.metric("Fatalities", fatalities)

        with col3:
            abductions = calculate_metric(
                filtered_data, "Incident Summary", "Abductions")
            st.metric("Abductions", abductions)

        with col4:
            fatality_rate = (fatalities / total_incidents *
                             100) if total_incidents > 0 else 0
            st.metric("Fatality Rate", f"{fatality_rate:.1f}%")

        st.divider()

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Incident Analysis", "Location Intelligence", "Impact Assessment", "Recommendations"])

        with tab1:
            incident_types = filtered_data[filtered_data['Category']
                                           == "Incident Breakdown"]
            if not incident_types.empty:
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Incident Composition")
                    viz_df = incident_types[['Sub-Category', 'Numeric_Value']].rename(
                        columns={'Sub-Category': 'Incident Type',
                                 'Numeric_Value': 'Count'}
                    )
                    fig = px.pie(viz_df, names='Incident Type',
                                 values='Count', hole=0.3)
                    st.plotly_chart(fig, use_container_width=True)

                with col2:
                    st.subheader("Incident Severity")
                    severity_df = viz_df.copy()
                    severity_df['Percentage'] = (
                        severity_df['Count'] / severity_df['Count'].sum()) * 100
                    fig = px.bar(severity_df, x='Incident Type',
                                 y='Percentage', color='Count', text='Percentage')
                    fig.update_traces(
                        texttemplate='%{text:.1f}%', textposition='outside')
                    st.plotly_chart(fig, use_container_width=True)

                st.subheader("Incident Details")
                st.dataframe(
                    incident_types[['Sub-Category', 'Details', 'Numeric_Value']
                                   ].sort_values('Numeric_Value', ascending=False),
                    column_config={
                        "Numeric_Value": st.column_config.NumberColumn("Count")},
                    hide_index=True,
                    use_container_width=True
                )

        with tab2:
            if 'Location' in filtered_data.columns:
                loc_data = filtered_data[(filtered_data['Location'].notna()) & (
                    filtered_data['Location'] != '-')]
                if not loc_data.empty:
                    col1, col2 = st.columns(2)

                    with col1:
                        st.subheader("Incident Hotspots")
                        loc_counts = loc_data['Location'].value_counts(
                        ).reset_index()
                        fig = px.bar(loc_counts.head(
                            10), x='Location', y='count', color='count', labels={'count': 'Incidents'})
                        st.plotly_chart(fig, use_container_width=True)

                    with col2:
                        st.subheader("Location Risk Map")
                        st.info(
                            "Map visualization would appear here with geographic data")

                    st.subheader("Location Details")
                    location_details = loc_data.groupby('Location').agg({
                        'Numeric_Value': 'sum',
                        'Sub-Category': lambda x: ', '.join(set(x))
                    }).reset_index()
                    st.dataframe(
                        location_details.sort_values(
                            'Numeric_Value', ascending=False),
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

                measures_data = security_data[security_data['Category']
                                              == "Security Measures"]
                if not measures_data.empty:
                    st.subheader("Security Measures Timeline")
                    measures_df = measures_data[['Sub-Category', 'Details']]
                    st.dataframe(
                        measures_df,
                        column_config={"Sub-Category": "Measure",
                                       "Details": "Description"},
                        hide_index=True,
                        use_container_width=True
                    )

        with tab4:
            if show_recommendations:
                recommendations = security_data[security_data['Category']
                                                == "Recommendations"]
                if not recommendations.empty:
                    st.subheader("Security Recommendations")
                    cols = st.columns(2)
                    for idx, (_, row) in enumerate(recommendations.iterrows()):
                        with cols[idx % 2]:
                            with st.container(border=True):
                                st.markdown(f"#### {row['Sub-Category']}")
                                st.markdown(row['Details'])
                                st.progress(min((idx + 1) * 20, 100),
                                            text=f"Priority {idx + 1}")

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
    st.header("🌊 Gurara Reservoir Water Level Analysis")
    st.markdown("""
    <div style="background-color:#e6f3ff; padding:15px; border-radius:10px; margin-bottom:20px">
    Comprehensive monitoring and analysis of reservoir water levels with historical trends and anomaly detection
    </div>
    """, unsafe_allow_html=True)

    @st.cache_data(ttl=3600)
    def load_water_level_data():
        sheet = client.open("GHATZ_Data").worksheet("guraradamwaterlevel")
        records = sheet.get_all_records()
        df = pd.DataFrame(records)

        # Robust date parsing with dayfirst=True for DD/MM/YYYY format
        df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors='coerce')
        df = df.dropna(subset=["date"])

        # Convert and clean water level data
        df["reservoir_level"] = pd.to_numeric(
            df["reservoir_level"], errors='coerce')
        df = df.dropna(subset=["reservoir_level"])

        # Extract temporal features
        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month
        df["month_name"] = df["date"].dt.month_name()
        df["day_of_year"] = df["date"].dt.dayofyear
        df["quarter"] = df["date"].dt.quarter

        return df.sort_values("date")

    try:
        df = load_water_level_data()

        # Calculate overall stats for reference
        min_level, max_level = df["reservoir_level"].min(
        ), df["reservoir_level"].max()
        avg_level = df["reservoir_level"].mean()

        # Sidebar controls
        st.sidebar.header("🔧 Analysis Controls")
        analysis_years = st.sidebar.multiselect(
            "Select Years",
            options=sorted(df["year"].unique()),
            default=sorted(df["year"].unique())
        )

        show_anomalies = st.sidebar.checkbox("Show Anomaly Detection", True)
        show_histogram = st.sidebar.checkbox(
            "Show Distribution Analysis", True)

        # Filter data based on selected years
        df_filtered = df[df["year"].isin(
            analysis_years)] if analysis_years else df

        if df_filtered.empty:
            st.warning("No data available for the selected filters")
            st.stop()

        # Key metrics
        st.subheader("📊 Water Level Metrics")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Current Level",
                      f"{df_filtered['reservoir_level'].iloc[-1]:.2f} m",
                      help="Most recent measurement")
        with col2:
            st.metric("Historical Avg",
                      f"{avg_level:.2f} m",
                      delta=f"{(df_filtered['reservoir_level'].iloc[-1] - avg_level):.2f} m")
        with col3:
            st.metric("Minimum Recorded",
                      f"{min_level:.2f} m")
        with col4:
            st.metric("Maximum Recorded",
                      f"{max_level:.2f} m")

        st.divider()

        # Main analysis tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ["📈 Temporal Trends", "🌦 Seasonal Patterns", "📉 Anomaly Detection", "📋 Raw Data"])

        with tab1:
            st.subheader("Water Level Timeline")

            # Interactive time series plot
            line_chart = alt.Chart(df_filtered).mark_line(
                point=True,
                interpolate='monotone'
            ).encode(
                x=alt.X('date:T', title='Date'),
                y=alt.Y('reservoir_level:Q',
                        title='Water Level (m)',
                        scale=alt.Scale(domain=[min_level-1, max_level+1])),
                tooltip=[
                    alt.Tooltip('date:T', title='Date', format='%d %b %Y'),
                    alt.Tooltip('reservoir_level:Q',
                                title='Level', format='.2f')
                ]
            ).properties(
                width='container',
                height=500
            )
            st.altair_chart(line_chart, use_container_width=True)

            # Rolling average analysis
            st.subheader("30-Day Rolling Average")
            rolling_df = df_filtered.set_index(
                'date')['reservoir_level'].rolling(30).mean().reset_index()
            rolling_chart = alt.Chart(rolling_df.dropna()).mark_area(
                line={'color': 'darkblue'},
                color=alt.Gradient(
                    gradient='linear',
                    stops=[alt.GradientStop(color='white', offset=0),
                           alt.GradientStop(color='lightblue', offset=1)],
                    x1=1, x2=1, y1=1, y2=0
                )
            ).encode(
                x='date:T',
                y='reservoir_level:Q'
            )
            st.altair_chart(rolling_chart, use_container_width=True)

        with tab2:
            st.subheader("Seasonal Patterns")

            # Monthly analysis
            monthly_avg = df_filtered.groupby(['month', 'month_name'])[
                'reservoir_level'].mean().reset_index()
            monthly_avg = monthly_avg.sort_values('month')

            monthly_chart = alt.Chart(monthly_avg).mark_bar().encode(
                x=alt.X('month_name:N', sort=list(
                    calendar.month_name[1:]), title="Month"),
                y=alt.Y('reservoir_level:Q', title='Average Level (m)'),
                color=alt.Color('reservoir_level:Q',
                                scale=alt.Scale(scheme='blues')),
                tooltip=['month_name', alt.Tooltip(
                    'reservoir_level:Q', format='.2f')]
            ).properties(
                width='container',
                height=400
            )

            st.altair_chart(monthly_chart, use_container_width=True)

            # Heatmap by year-month
            st.subheader("Year-Month Heatmap")
            heatmap_data = df_filtered.groupby(['year', 'month_name'])[
                'reservoir_level'].mean().unstack()
            fig = px.imshow(
                heatmap_data,
                labels=dict(x="Month", y="Year", color="Water Level"),
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig, use_container_width=True)

        with tab3:
            if show_anomalies:
                st.subheader("Anomaly Detection")

                # Calculate z-scores for anomaly detection
                df_filtered['z_score'] = (
                    df_filtered['reservoir_level'] - df_filtered['reservoir_level'].mean()) / df_filtered['reservoir_level'].std()
                anomalies = df_filtered[abs(df_filtered['z_score']) > 2.5]

                if not anomalies.empty:
                    # Anomaly timeline
                    base = alt.Chart(df_filtered).mark_line(color='lightblue').encode(
                        x='date:T',
                        y='reservoir_level:Q'
                    )

                    points = alt.Chart(anomalies).mark_point(
                        color='red',
                        size=100
                    ).encode(
                        x='date:T',
                        y='reservoir_level:Q',
                        tooltip=[
                            alt.Tooltip('date:T', format='%d %b %Y'),
                            alt.Tooltip('reservoir_level:Q', format='.2f')
                        ]
                    )

                    st.altair_chart(base + points, use_container_width=True)

                    # Anomaly details table
                    st.subheader("Anomaly Details")
                    st.dataframe(
                        anomalies.sort_values('z_score', ascending=False)[
                            ['date', 'reservoir_level', 'z_score']],
                        column_config={
                            "date": st.column_config.DatetimeColumn(format="DD/MM/YYYY"),
                            "reservoir_level": st.column_config.NumberColumn(format="%.2f m"),
                            "z_score": st.column_config.NumberColumn(
                                "Deviation Score",
                                help="Standard deviations from mean")
                        },
                        hide_index=True
                    )
                else:
                    st.info(
                        "No significant anomalies detected in selected data range")

        with tab4:
            st.subheader("Raw Measurement Data")
            st.dataframe(
                df_filtered.sort_values('date', ascending=False),
                column_config={
                    "date": st.column_config.DatetimeColumn(format="DD/MM/YYYY"),
                    "reservoir_level": st.column_config.NumberColumn(format="%.2f m")
                },
                hide_index=True,
                use_container_width=True
            )

        # Data export
        st.sidebar.download_button(
            label="📥 Export Water Level Data",
            data=df_filtered.to_csv(index=False).encode('utf-8'),
            file_name=f"gurara_reservoir_levels_{min(analysis_years)}_{max(analysis_years)}.csv",
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"⚠️ Error processing water level data: {str(e)}")
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
elif option == "GHATZ Standpipe": 
    st.write("Stand Pipe Analysis")
elif option == "GHATZ Vibrating Wire":
    st.write("Vibrating Wire Analysis")      
elif option == "GHATZ Seepage":
    st.write("Gurara Seepage Analysis")      

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
