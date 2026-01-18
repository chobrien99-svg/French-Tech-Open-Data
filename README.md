# French Tech Open Data Analysis

Analysis of 282 CSV files containing 122,738+ datasets from the French government's Open Data portal (data.gouv.fr), specifically curated for **The French Tech Journal** newsletter audience.

## 📊 Analysis Overview

This repository contains:
- **282 CSV files** with complete French Open Data catalog exports
- **Comprehensive analysis** identifying 112,495+ relevant datasets (91.7% relevance rate)
- **Curated recommendations** for newsletter content targeting entrepreneurs, startups, VCs, and tech leaders

## 🎯 Target Audience

The French Tech Journal readers:
- Entrepreneurs & Startup Founders
- Digital Transformation Leaders
- Corporate Leaders & Executives
- Investors & Venture Capitalists
- Policy Makers
- Innovation Professionals

## 📁 Key Files

### Analysis Results
- **`FRENCH_TECH_JOURNAL_RECOMMENDATIONS.md`** - Main recommendations document with top 50 datasets and content ideas
- **`analysis_results.json`** - Detailed analysis data (top 100 datasets with metadata)
- **`relevant_datasets_summary.csv`** - Spreadsheet-friendly export of relevant datasets
- **`analyze_datasets.py`** - Python analysis script (reproducible analysis)

### Source Data
- **`export-dataset-20260116-055249-*.csv`** - 282 CSV files from data.gouv.fr (214MB total)

## 🚀 Top Dataset Categories

1. **Innovation & Startups** - I-LAB competitions, PEPITE programs, innovation contests
2. **Business Intelligence** - SIRENE registry, company statistics, economic indicators
3. **Digital Infrastructure** - Fiber optic deployment, telecom markets, connectivity
4. **R&D & Patents** - Research funding, patent data, tech transfer
5. **Employment & Talent** - Tech jobs, recruitment trends, salary data
6. **Funding & Investment** - Startup grants, VC activity, regional programs

## 📈 Highlights

### Top 5 Most Relevant Datasets

1. **Telecommunications Market Analysis (2000-2025)** - 25-year technology evolution (207 pts)
2. **I-LAB Innovation Competition Winners** - France's premier tech startup awards (195 pts)
3. **PEPITE Student Entrepreneurship Award Winners** - Young founder pipeline (175 pts)
4. **Innov'up Leader PIA** - Île-de-France innovation program (163 pts)
5. **SIRENE Business Registry** - Complete French company database (144 pts)

## 🔧 How to Use This Analysis

### For Newsletter Content
1. Review `FRENCH_TECH_JOURNAL_RECOMMENDATIONS.md` for editorial ideas
2. Access datasets via provided URLs
3. Use thematic groupings for content planning
4. Leverage recurring data for regular columns

### For Data Analysis
1. Run `python3 analyze_datasets.py` to regenerate analysis
2. Import `relevant_datasets_summary.csv` into Excel/Sheets
3. Query `analysis_results.json` for programmatic access
4. Extend the Python script for custom analyses

### For Research
1. Explore source CSV files in repository
2. Filter by keywords, organizations, or categories
3. Track temporal coverage for time-series analysis
4. Cross-reference multiple datasets for deep insights

## 📊 Statistics

- **Total Datasets Analyzed:** 122,738
- **Relevant Datasets Found:** 112,495 (91.7%)
- **High Relevance (50+ points):** Significant number
- **Source Files:** 282 CSV files
- **Total Data Size:** 214+ MB
- **Analysis Date:** January 16-18, 2026

## 🛠️ Technical Details

### Analysis Methodology
- **Keyword matching** against 100+ tech/business/innovation terms
- **Weighted scoring:** Title (10pts), Tags (5pts), Description (3pts)
- **Multi-dimensional relevance:** Business, tech, innovation, funding, employment, infrastructure

### Requirements
```bash
python3
# Standard library only - no external dependencies
```

### Run Analysis
```bash
python3 analyze_datasets.py
```

Output files:
- `analysis_results.json`
- `relevant_datasets_summary.csv`
- Console output with top datasets

## 🌐 Data Sources

**Primary Portal:** [data.gouv.fr](https://www.data.gouv.fr)
**License:** Licence Ouverte / Open Licence 2.0 (most datasets)
**Export Date:** January 16, 2026

### Key Data Publishers
- Ministère de l'Enseignement supérieur, de la Recherche et de l'Espace
- Institut national de la statistique et des études économiques (Insee)
- Regional authorities (Île-de-France, Occitanie, Pays de la Loire, etc.)
- ANCT (Agence nationale de la cohésion des territoires)
- APEC (Association Pour l'Emploi des Cadres)

## 💡 Content Opportunities

### Feature Stories
- "The I-LAB Effect: 25 Years of French Tech Innovation"
- "France's Fiber Revolution: Infrastructure Data Reveals Digital Divide"
- "Student Startups to Scale-ups: The PEPITE Pipeline"
- "Where France Innovates: R&D Spending by Region"

### Recurring Columns
- **Startup Tracker** - Monthly innovation program updates
- **Funding Pulse** - Investment activity indicators
- **Tech Jobs Index** - Employment trends
- **Innovation Scoreboard** - R&D and patent activity

### Data Series
- **Sector Spotlights** - Industry-specific deep dives
- **Regional Innovation Stories** - Geographic focus
- **From Lab to Market** - Tech transfer successes
- **Policy Impact Reports** - Government program effectiveness

## 📞 Contact & Contributions

For questions about this analysis or to suggest improvements:
- Open an issue in this repository
- Review the methodology in `analyze_datasets.py`
- Consult `FRENCH_TECH_JOURNAL_RECOMMENDATIONS.md` for detailed insights

## 📜 License

This analysis is provided as-is for editorial and research purposes.
Source datasets retain their original licenses (primarily Licence Ouverte 2.0).

---

**Generated:** January 18, 2026
**Repository:** French-Tech-Open-Data
**Purpose:** Editorial research for The French Tech Journal
