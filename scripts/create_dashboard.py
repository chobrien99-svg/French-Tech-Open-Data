#!/usr/bin/env python3
"""
Interactive i-Lab Data Dashboard using Plotly Dash
Creates a web-based visualization of i-Lab laureates data
"""

import json
import pandas as pd
from pathlib import Path
from collections import Counter
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_data():
    """Load the i-Lab analysis data"""
    base_dir = Path(__file__).parent.parent
    analysis_file = base_dir / "data" / "ilab" / "ilab_analysis_detailed.json"

    with open(analysis_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_year_trend_chart(analysis):
    """Create year-over-year trend chart"""
    if 'by_year' not in analysis:
        return None

    years = sorted(analysis['by_year'].items(), key=lambda x: x[0])
    years_list = [int(y[0]) for y in years if y[0].isdigit()]
    counts = [y[1] for y in years if y[0].isdigit()]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years_list,
        y=counts,
        mode='lines+markers',
        name='Laureates',
        line=dict(color='#0055A4', width=3),
        marker=dict(size=8)
    ))

    fig.update_layout(
        title='i-Lab Laureates Over Time (1999-2025)',
        xaxis_title='Year',
        yaxis_title='Number of Laureates',
        hovermode='x unified',
        template='plotly_white',
        height=400
    )

    return fig

def create_regional_map(analysis):
    """Create regional distribution chart"""
    if 'by_region' not in analysis:
        return None

    regions = list(analysis['by_region'].items())[:15]
    region_names = [r[0] for r in regions]
    counts = [r[1] for r in regions]

    fig = go.Figure(go.Bar(
        y=region_names[::-1],  # Reverse for better display
        x=counts[::-1],
        orientation='h',
        marker=dict(
            color=counts[::-1],
            colorscale='Blues',
            showscale=True
        )
    ))

    fig.update_layout(
        title='Top 15 Regions by Number of Laureates',
        xaxis_title='Number of Laureates',
        yaxis_title='Region',
        height=500,
        template='plotly_white'
    )

    return fig

def create_domain_sunburst(analysis):
    """Create technology domain sunburst chart"""
    if 'by_domain' not in analysis:
        return None

    domains = list(analysis['by_domain'].items())[:15]

    labels = ['All Domains'] + [d[0] for d in domains]
    parents = [''] + ['All Domains'] * len(domains)
    values = [sum(d[1] for d in domains)] + [d[1] for d in domains]

    fig = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues="total",
        marker=dict(colorscale='RdBu')
    ))

    fig.update_layout(
        title='Technology Domains Distribution',
        height=600,
        template='plotly_white'
    )

    return fig

def create_gender_distribution(analysis):
    """Create gender distribution pie chart"""
    if 'gender_distribution' not in analysis:
        return None

    labels = list(analysis['gender_distribution'].keys())
    values = list(analysis['gender_distribution'].values())

    fig = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker=dict(colors=['#0055A4', '#EF4135'])
    ))

    fig.update_layout(
        title='Gender Distribution of Laureates',
        height=400,
        template='plotly_white'
    )

    return fig

def create_heatmap_region_year(analysis):
    """Create heatmap of regions over time"""
    if 'region_year_detail' not in analysis:
        return None

    # Get top 10 regions
    top_regions = sorted(
        analysis['by_region'].items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    region_names = [r[0] for r in top_regions]

    # Get all years
    all_years = set()
    for region_data in analysis['region_year_detail'].values():
        all_years.update(region_data.keys())
    years = sorted([y for y in all_years if y.isdigit()], key=int)

    # Build matrix
    matrix = []
    for region in region_names:
        row = []
        region_data = analysis['region_year_detail'].get(region, {})
        for year in years:
            row.append(region_data.get(year, 0))
        matrix.append(row)

    fig = go.Figure(go.Heatmap(
        z=matrix,
        x=years,
        y=region_names,
        colorscale='Blues',
        hovertemplate='Year: %{x}<br>Region: %{y}<br>Laureates: %{z}<extra></extra>'
    ))

    fig.update_layout(
        title='Regional Activity Heatmap Over Time',
        xaxis_title='Year',
        yaxis_title='Region',
        height=500,
        template='plotly_white'
    )

    return fig

def create_static_html_dashboard():
    """Create a static HTML dashboard with all visualizations"""
    print("Loading data...")
    analysis = load_data()

    print("Creating visualizations...")

    # Create all charts
    year_trend = create_year_trend_chart(analysis)
    regional_map = create_regional_map(analysis)
    domain_chart = create_domain_sunburst(analysis)
    gender_chart = create_gender_distribution(analysis)
    heatmap = create_heatmap_region_year(analysis)

    # Create HTML
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>i-Lab Laureates Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .header {
            background: linear-gradient(135deg, #0055A4 0%, #EF4135 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 2.5em;
        }
        .header p {
            margin: 5px 0;
            font-size: 1.1em;
            opacity: 0.95;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .stat-box {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            text-align: center;
        }
        .stat-value {
            font-size: 2.5em;
            font-weight: bold;
            color: #0055A4;
            margin: 10px 0;
        }
        .stat-label {
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .chart-container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .chart-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        footer {
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 i-Lab Laureates Dashboard</h1>
        <p>Concours national d'aide à la création d'entreprises de technologies innovantes</p>
        <p>Analysis of 3,923 laureates from 1999-2025</p>
    </div>

    <div class="stats">
        <div class="stat-box">
            <div class="stat-label">Total Laureates</div>
            <div class="stat-value">3,923</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Years</div>
            <div class="stat-value">27</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Grand Prix</div>
            <div class="stat-value">125</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Regions</div>
            <div class="stat-value">15+</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Repeat Laureates</div>
            <div class="stat-value">871</div>
        </div>
    </div>

    <div class="chart-container">
        <div id="yearTrend"></div>
    </div>

    <div class="chart-grid">
        <div class="chart-container">
            <div id="genderChart"></div>
        </div>
        <div class="chart-container">
            <div id="regionalMap"></div>
        </div>
    </div>

    <div class="chart-container">
        <div id="heatmap"></div>
    </div>

    <div class="chart-container">
        <div id="domainChart"></div>
    </div>

    <footer>
        <p>Data source: data.gouv.fr | Licence Ouverte 2.0</p>
        <p>Dashboard generated: """ + pd.Timestamp.now().strftime('%Y-%m-%d %H:%M') + """</p>
    </footer>

    <script>
"""

    # Add Plotly charts
    if year_trend:
        html_content += f"    Plotly.newPlot('yearTrend', {year_trend.to_json()});\n"
    if gender_chart:
        html_content += f"    Plotly.newPlot('genderChart', {gender_chart.to_json()});\n"
    if regional_map:
        html_content += f"    Plotly.newPlot('regionalMap', {regional_map.to_json()});\n"
    if heatmap:
        html_content += f"    Plotly.newPlot('heatmap', {heatmap.to_json()});\n"
    if domain_chart:
        html_content += f"    Plotly.newPlot('domainChart', {domain_chart.to_json()});\n"

    html_content += """
    </script>
</body>
</html>
"""

    # Save HTML
    output_file = Path(__file__).parent.parent / "data" / "ilab" / "ilab_dashboard.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Dashboard created: {output_file}")
    print(f"\nOpen in browser: file://{output_file.absolute()}")

    return output_file

if __name__ == "__main__":
    create_static_html_dashboard()
