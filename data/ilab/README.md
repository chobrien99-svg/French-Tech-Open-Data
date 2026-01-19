# i-Lab Laureates Dataset

## About the Dataset

The i-Lab (Concours national d'aide à la création d'entreprises de technologies innovantes) is a national competition created by the French Ministry of Higher Education and Research to support the creation of innovative technology companies.

## Data Source

- **Primary Source**: [data.gouv.fr - i-Lab Laureates](https://www.data.gouv.fr/datasets/laureats-i-lab-concours-national-daide-a-la-creation-dentreprises-de-technologies-innovantes-1)
- **Alternative Source**: [data.enseignementsup-recherche.gouv.fr](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-laureats-concours-national-i-lab/)
- **GitHub Mirror**: [chobrien99-svg/Laur-ats-I-LAB](https://github.com/chobrien99-svg/Laur-ats-I-LAB)
- **License**: Licence Ouverte / Open Licence version 2.0
- **Last Updated**: November 12, 2025
- **File Size**: 4.0 MB (CSV), 28 MB (DBF uncompressed)

## Key Statistics

- **Total Records**: 3,923 laureates
- **Time Period**: 1999 - 2025 (27 years)
- **Grand Prix Winners**: 125
- **Repeat Laureates**: 871
- **Gender Split**: 88% Male, 12% Female

### Top Regions
1. Île-de-France (25.5%)
2. Auvergne-Rhône-Alpes (14.8%)
3. Occitanie (11.8%)

### Top Technology Domains
1. IT Services (15.8%)
2. Electronics, Signal & Telecommunications (13.5%)
3. Biotechnology and Pharmacy (11.3%)

## Dataset Fields

The dataset includes 28 fields:
- Personal info: Name, Gender, Email
- Competition: Year, Candidature Type, Jury Level
- Project: Domain, Summary, Grand Prix status
- Company: SIRET/SIREN, Name, Website
- Location: Region
- Research: Linked research units and structures

## Files in this Directory

- `README.md` - This file
- `ilab_laureats.csv` - Raw CSV data (4.0 MB)
- `ilab_laureats.json` - Raw JSON data (6.9 MB)
- `ilab_laureats.geojson` - Geographic data (6.0 MB)
- `ilab_laureats.dbf.zip` - Compressed database file (1.1 MB)
- `fr-esr-laureats-concours-national-i-lab.dbf` - Uncompressed DBF (27 MB)
- `ilab_processed.json` - Processed data
- `ilab_analysis.txt` - Basic analysis
- `ilab_analysis_detailed.json` - Detailed analysis (JSON)
- `ilab_comprehensive_report.txt` - Comprehensive report

## How to Use

### Quick Analysis
```bash
# Run comprehensive analysis
python3 scripts/analyze_ilab_detailed.py

# View the report
cat data/ilab/ilab_comprehensive_report.txt
```

### Data Processing
```bash
# Basic processing
python3 scripts/process_ilab.py
```

## Insights

The i-Lab competition has supported nearly 4,000 innovative technology startups over 27 years. The data shows:
- Strong concentration in Île-de-France region (Paris area)
- Dominance of IT/software and biotech sectors
- Significant gender disparity in entrepreneurship
- Recent years show decline in award numbers (from ~200/year to ~70/year)
