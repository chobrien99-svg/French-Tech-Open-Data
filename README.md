# French Tech Open Data

This repository contains various French government open data projects, focusing on innovation, technology, and entrepreneurship in France.

## Projects

### 1. FranceTerme Official Terminology Database

**Status**: 🔄 Moved to dedicated repository

FranceTerme is the official French government database providing French equivalents for technical and scientific terms across various fields.

**New Location**: [franceterme-data](https://github.com/chobrien99-svg/franceterme-data)

**Dataset Contains**:
- 282 CSV export files with terminology data
- French terms with official definitions
- Foreign language equivalents (primarily English)
- Domain classifications (IT, engineering, medicine, etc.)
- Complete usage documentation

The dataset has been moved to its own repository for better organization and accessibility.

---

### 2. i-Lab Laureates Dataset

The i-Lab competition is France's national program supporting the creation of innovative technology companies, awarding funding to startups since 1999.

**Status**: ✅ Complete - Data imported and analyzed

**Location**: `data/ilab/`

**Key Findings**:
- 3,923 laureates over 27 years (1999-2025)
- 125 Grand Prix winners
- 25.5% concentrated in Île-de-France region
- Top sectors: IT Services (15.8%), Electronics (13.5%), Biotech (11.3%)
- Gender split: 88% Male, 12% Female

**Quick Start**:
```bash
# View comprehensive analysis
cat data/ilab/ilab_comprehensive_report.txt

# Re-run analysis
python3 scripts/analyze_ilab_detailed.py
```

See [data/ilab/README.md](data/ilab/README.md) for full documentation and insights.

## Repository Structure

```
French-Tech-Open-Data/
├── data/                    # Data files
│   └── ilab/               # i-Lab laureates dataset
│       └── README.md       # Dataset documentation
├── scripts/                 # Processing scripts
│   └── process_ilab.py     # i-Lab data processor
├── docs/                    # Documentation
└── README.md               # This file
```

## Data Sources

All datasets in this repository come from official French government open data portals:
- [data.gouv.fr](https://www.data.gouv.fr) - France's national open data portal
- [data.enseignementsup-recherche.gouv.fr](https://data.enseignementsup-recherche.gouv.fr) - Ministry of Higher Education and Research

## License

The datasets are published under **Licence Ouverte / Open Licence version 2.0**, which allows:
- Free reuse of information
- Commercial and non-commercial use
- Modification and redistribution
- Requirement: Attribution to the source

## Contributing

To add a new open data project:
1. Create a directory in `data/`
2. Add a README.md with dataset information
3. Create processing scripts in `scripts/`
4. Update this README

## About

This project aims to make French government open data more accessible and easier to analyze, particularly focusing on innovation, technology, and entrepreneurship ecosystems.
