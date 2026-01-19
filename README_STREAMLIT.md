# 🚀 i-Lab Interactive Dashboard

## Test Locally (Before Deploying)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

Opens automatically at: http://localhost:8501

## Features

### Interactive Filters
- **Year Range Slider**: Select any period from 1999-2025
- **Region Multi-Select**: Focus on specific regions
- **Domain Multi-Select**: Filter by technology sector
- **Gender Filter**: Analyze by gender distribution

### Visualizations
- 📈 **Year-over-Year Trend**: Line chart with hover details
- 🗺️ **Geographic Map**: Interactive map using GeoJSON data
- 📊 **Regional Distribution**: Top 15 regions bar chart
- ⚡ **Technology Domains**: Pie chart of top sectors
- 👥 **Gender Breakdown**: Percentage splits
- 🔥 **Regional Heatmap**: Region × Year activity matrix

### Data Export
- Download filtered data as CSV
- View first 100 rows in expandable table

## Deploy to Streamlit Cloud

See [DEPLOYMENT.md](DEPLOYMENT.md) for full instructions.

**Quick steps**:
1. Push to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy this repo
5. Share your URL!

## File Requirements

Make sure these files are in your repo:
- ✅ `streamlit_app.py` (main app)
- ✅ `requirements.txt` (dependencies)
- ✅ `data/ilab/ilab_laureats.csv` (data)
- ✅ `data/ilab/ilab_laureats.geojson` (map data)

## Deployment URL

Once deployed, your app will be at:
```
https://[username]-french-tech-open-data-[id].streamlit.app
```

Share this URL with anyone - no login required for viewers!

## Troubleshooting

### "ModuleNotFoundError"
→ Make sure `requirements.txt` includes all dependencies

### "FileNotFoundError"
→ Make sure CSV and GeoJSON files are committed to GitHub

### "App won't load"
→ Check Streamlit Cloud logs for error messages

### Map not showing
→ Requires GeoJSON file in `data/ilab/` directory

## Customization

Want to add more features? Edit `streamlit_app.py`:

```python
# Add new filters
new_filter = st.sidebar.multiselect("New Filter", options=[...])

# Add new charts
fig = px.bar(data, x='col1', y='col2')
st.plotly_chart(fig)

# Add new sections
st.subheader("New Section")
st.write("Content here")
```

## Support

- Streamlit docs: https://docs.streamlit.io
- Plotly docs: https://plotly.com/python/
- Community: https://discuss.streamlit.io
