# French Tech Open Data

This repository contains various French government open data projects, focusing on innovation, technology, and entrepreneurship in France.

## Projects

### 1. i-Lab Laureates Dataset

The i-Lab competition is a national program supporting the creation of innovative technology companies in France.

**Status**: Structure ready, awaiting data download

**Location**: `data/ilab/`

**Quick Start**:
```bash
# 1. Download the dataset from:
# https://www.data.gouv.fr/datasets/laureats-i-lab-concours-national-daide-a-la-creation-dentreprises-de-technologies-innovantes-1

# 2. Place the CSV file in data/ilab/

# 3. Process the data:
python3 scripts/process_ilab.py
```

See [data/ilab/README.md](data/ilab/README.md) for more details.

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
