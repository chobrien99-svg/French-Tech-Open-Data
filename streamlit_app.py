#!/usr/bin/env python3
"""
Interactive i-Lab Dashboard using Streamlit
Includes: Timeline, Maps, Filters, Domain Analysis, Gender Stats

Deploy to Streamlit Cloud:
1. Push to GitHub
2. Visit share.streamlit.io
3. Connect GitHub repo
4. Deploy!
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from pathlib import Path
from datetime import datetime

# Page config
st.set_page_config(
    page_title="i-Lab Laureates Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #0055A4 0%, #EF4135 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        color: #0055A4;
    }
    .metric-label {
        color: #666;
        font-size: 0.9em;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load CSV data - downloads from GitHub if not present"""
    import urllib.request

    # Define paths
    data_dir = Path(__file__).parent / "data" / "ilab"
    csv_path = data_dir / "ilab_laureats.csv"

    # Create directory if needed
    data_dir.mkdir(parents=True, exist_ok=True)

    # Download if file doesn't exist or is too small (corrupt/empty)
    min_file_size = 1000  # Expect at least 1KB for valid CSV
    needs_download = not csv_path.exists() or csv_path.stat().st_size < min_file_size

    if needs_download:
        url = 'https://raw.githubusercontent.com/chobrien99-svg/Laur-ats-I-LAB/main/fr-esr-laureats-concours-national-i-lab.csv'
        st.info(f"⬇️ Downloading data from GitHub (one-time, ~4MB)...")
        try:
            urllib.request.urlretrieve(url, csv_path)
            st.success(f"✅ Downloaded successfully!")
        except Exception as e:
            st.error(f"❌ Download failed: {e}")
            st.error(f"Please check: {url}")
            raise

    # Load the CSV
    try:
        # Try UTF-8 with BOM
        df = pd.read_csv(csv_path, delimiter=';', encoding='utf-8-sig')
    except Exception as e:
        try:
            # Fallback to regular UTF-8
            df = pd.read_csv(csv_path, delimiter=';', encoding='utf-8')
        except Exception as e2:
            st.error(f"Failed to parse CSV: {e2}")
            raise

    return df

@st.cache_data
def load_geojson():
    """Load GeoJSON data - downloads from GitHub if not present"""
    import urllib.request

    # Define paths
    data_dir = Path(__file__).parent / "data" / "ilab"
    geojson_path = data_dir / "ilab_laureats.geojson"

    # Create directory if needed
    data_dir.mkdir(parents=True, exist_ok=True)

    # Download if file doesn't exist or is too small (corrupt/empty)
    min_file_size = 1000  # Expect at least 1KB for valid GeoJSON
    needs_download = not geojson_path.exists() or geojson_path.stat().st_size < min_file_size

    if needs_download:
        url = 'https://raw.githubusercontent.com/chobrien99-svg/Laur-ats-I-LAB/main/fr-esr-laureats-concours-national-i-lab.geojson'
        st.info(f"⬇️ Downloading map data from GitHub (one-time, ~6MB)...")
        try:
            urllib.request.urlretrieve(url, geojson_path)
            st.success(f"✅ Map data downloaded successfully!")
        except Exception as e:
            st.error(f"❌ Download failed: {e}")
            st.error(f"Please check: {url}")
            raise

    # Load the GeoJSON
    try:
        with open(geojson_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Failed to parse GeoJSON: {e}")
        raise

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 i-Lab Laureates Dashboard</h1>
        <p>Concours national d'aide à la création d'entreprises de technologies innovantes</p>
        <p>Interactive analysis of 3,923 laureates from 1999-2025</p>
    </div>
    """, unsafe_allow_html=True)

    # Load data
    with st.spinner("Loading data..."):
        df = load_data()

    # Data cleaning
    year_col = 'Année de concours'
    region_col = 'Région'
    domain_col = 'Domaine technologique'
    gender_col = 'Genre'
    type_col = 'Type de candidature'

    # Sidebar filters
    st.sidebar.header("🔍 Filters")

    # Year range
    years = sorted([int(y) for y in df[year_col].unique() if pd.notna(y) and str(y).isdigit()])
    year_range = st.sidebar.slider(
        "Year Range",
        min_value=min(years),
        max_value=max(years),
        value=(min(years), max(years))
    )

    # Region filter
    regions = sorted([r for r in df[region_col].unique() if pd.notna(r)])
    selected_regions = st.sidebar.multiselect(
        "Regions",
        options=regions,
        default=[]
    )

    # Domain filter
    domains = sorted([d for d in df[domain_col].unique() if pd.notna(d)])
    selected_domains = st.sidebar.multiselect(
        "Technology Domains",
        options=domains,
        default=[]
    )

    # Gender filter
    genders = [g for g in df[gender_col].unique() if pd.notna(g)]
    selected_genders = st.sidebar.multiselect(
        "Gender",
        options=genders,
        default=genders
    )

    # Apply filters
    filtered_df = df.copy()
    filtered_df = filtered_df[
        (filtered_df[year_col].astype(str).str.isdigit()) &
        (filtered_df[year_col].astype(int) >= year_range[0]) &
        (filtered_df[year_col].astype(int) <= year_range[1])
    ]

    if selected_regions:
        filtered_df = filtered_df[filtered_df[region_col].isin(selected_regions)]

    if selected_domains:
        filtered_df = filtered_df[filtered_df[domain_col].isin(selected_domains)]

    if selected_genders:
        filtered_df = filtered_df[filtered_df[gender_col].isin(selected_genders)]

    # Metrics row
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Laureates", f"{len(filtered_df):,}")

    with col2:
        years_span = year_range[1] - year_range[0] + 1
        st.metric("Years", years_span)

    with col3:
        regions_count = filtered_df[region_col].nunique()
        st.metric("Regions", regions_count)

    with col4:
        domains_count = filtered_df[domain_col].nunique()
        st.metric("Domains", domains_count)

    with col5:
        avg_per_year = len(filtered_df) / years_span if years_span > 0 else 0
        st.metric("Avg/Year", f"{avg_per_year:.0f}")

    st.divider()

    # Year trend chart
    st.subheader("📈 Laureates Over Time")

    year_counts = filtered_df.groupby(year_col).size().reset_index(name='count')
    year_counts[year_col] = year_counts[year_col].astype(int)
    year_counts = year_counts.sort_values(year_col)

    fig_year = px.line(
        year_counts,
        x=year_col,
        y='count',
        markers=True,
        title='Number of Laureates per Year',
        labels={year_col: 'Year', 'count': 'Number of Laureates'}
    )
    fig_year.update_traces(line_color='#0055A4', line_width=3, marker_size=8)
    fig_year.update_layout(hovermode='x unified', height=400)

    st.plotly_chart(fig_year, use_container_width=True)

    # Two columns for charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🗺️ Regional Distribution")

        region_counts = filtered_df[region_col].value_counts().head(15)

        fig_region = px.bar(
            x=region_counts.values[::-1],
            y=region_counts.index[::-1],
            orientation='h',
            title='Top 15 Regions',
            labels={'x': 'Number of Laureates', 'y': 'Region'}
        )
        fig_region.update_traces(marker_color='#0055A4')
        fig_region.update_layout(height=500)

        st.plotly_chart(fig_region, use_container_width=True)

    with col2:
        st.subheader("⚡ Technology Domains")

        domain_counts = filtered_df[domain_col].value_counts().head(10)

        fig_domain = px.pie(
            values=domain_counts.values,
            names=domain_counts.index,
            title='Top 10 Technology Domains',
            hole=0.4
        )
        fig_domain.update_layout(height=500)

        st.plotly_chart(fig_domain, use_container_width=True)

    st.divider()

    # Gender and Type analysis
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👥 Gender Distribution")

        gender_counts = filtered_df[gender_col].value_counts()

        fig_gender = go.Figure(data=[go.Pie(
            labels=gender_counts.index,
            values=gender_counts.values,
            hole=0.4,
            marker=dict(colors=['#0055A4', '#EF4135'])
        )])
        fig_gender.update_layout(height=400)

        st.plotly_chart(fig_gender, use_container_width=True)

        # Calculate percentages
        total = gender_counts.sum()
        for gender, count in gender_counts.items():
            pct = (count / total * 100) if total > 0 else 0
            st.metric(f"{gender}", f"{count:,}", f"{pct:.1f}%")

    with col2:
        st.subheader("📋 Candidature Type")

        type_counts = filtered_df[type_col].value_counts()

        fig_type = go.Figure(data=[go.Pie(
            labels=type_counts.index,
            values=type_counts.values,
            hole=0.4,
            marker=dict(colors=['#0055A4', '#EF4135', '#FFD700'])
        )])
        fig_type.update_layout(height=400)

        st.plotly_chart(fig_type, use_container_width=True)

        # Calculate percentages
        total = type_counts.sum()
        for ctype, count in type_counts.items():
            pct = (count / total * 100) if total > 0 else 0
            st.metric(f"{ctype}", f"{count:,}", f"{pct:.1f}%")

    st.divider()

    # Heatmap: Region x Year
    st.subheader("🔥 Regional Activity Heatmap")

    # Get top 10 regions
    top_regions = filtered_df[region_col].value_counts().head(10).index

    # Create pivot table
    heatmap_data = filtered_df[filtered_df[region_col].isin(top_regions)]
    pivot = heatmap_data.groupby([region_col, year_col]).size().reset_index(name='count')
    pivot_table = pivot.pivot(index=region_col, columns=year_col, values='count').fillna(0)

    fig_heatmap = px.imshow(
        pivot_table,
        labels=dict(x="Year", y="Region", color="Laureates"),
        x=pivot_table.columns,
        y=pivot_table.index,
        color_continuous_scale='Blues',
        aspect='auto'
    )
    fig_heatmap.update_layout(height=500)

    st.plotly_chart(fig_heatmap, use_container_width=True)

    st.divider()

    # Map visualization
    st.subheader("🌍 Geographic Distribution")

    st.info("💡 Tip: The GeoJSON data contains precise coordinates for each laureate. This map shows the distribution across France.")

    # Try to create a simple map
    try:
        geojson_data = load_geojson()

        # Extract coordinates
        map_data = []
        for feature in geojson_data.get('features', []):
            props = feature.get('properties', {})
            coords = feature.get('geometry', {}).get('coordinates', [])

            if coords and len(coords) == 2:
                map_data.append({
                    'lon': coords[0],
                    'lat': coords[1],
                    'region': props.get('Région', 'Unknown'),
                    'year': props.get('Année de concours', 'Unknown'),
                    'project': props.get('Projet', 'Unknown')
                })

        map_df = pd.DataFrame(map_data)

        # Filter map data based on current filters
        if not map_df.empty:
            if selected_regions:
                map_df = map_df[map_df['region'].isin(selected_regions)]

            fig_map = px.scatter_mapbox(
                map_df,
                lat='lat',
                lon='lon',
                hover_name='project',
                hover_data={'region': True, 'year': True, 'lat': False, 'lon': False},
                color='region',
                zoom=5,
                height=600,
                title=f'Geographic Distribution of {len(map_df):,} Laureates'
            )

            fig_map.update_layout(
                mapbox_style="open-street-map",
                margin={"r":0,"t":40,"l":0,"b":0}
            )

            st.plotly_chart(fig_map, use_container_width=True)
        else:
            st.warning("No geographic data available for the selected filters.")

    except Exception as e:
        st.error(f"Error loading map: {e}")
        st.info("Map visualization requires the GeoJSON file to be present.")

    st.divider()

    # Data explorer
    with st.expander("📊 View Filtered Data"):
        st.dataframe(
            filtered_df[[
                'Nom du lauréat',
                year_col,
                region_col,
                domain_col,
                gender_col,
                'Projet'
            ]].head(100),
            use_container_width=True
        )

        st.download_button(
            label="Download Filtered Data (CSV)",
            data=filtered_df.to_csv(index=False).encode('utf-8'),
            file_name=f'ilab_filtered_{datetime.now().strftime("%Y%m%d")}.csv',
            mime='text/csv'
        )

    # Footer
    st.divider()
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p><strong>Data Source:</strong> data.gouv.fr | <strong>License:</strong> Licence Ouverte 2.0</p>
        <p>Dashboard created with Streamlit • Last updated: {}</p>
    </div>
    """.format(datetime.now().strftime('%Y-%m-%d')), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
