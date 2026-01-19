# i-Lab Laureates Dataset

## About the Dataset

The i-Lab (Concours national d'aide à la création d'entreprises de technologies innovantes) is a national competition created by the French Ministry of Higher Education and Research to support the creation of innovative technology companies.

## Data Source

- **Primary Source**: [data.gouv.fr - i-Lab Laureates](https://www.data.gouv.fr/datasets/laureats-i-lab-concours-national-daide-a-la-creation-dentreprises-de-technologies-innovantes-1)
- **Alternative Source**: [data.enseignementsup-recherche.gouv.fr](https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-laureats-concours-national-i-lab/)
- **License**: Licence Ouverte / Open Licence version 2.0
- **Last Updated**: November 12, 2025
- **File Size**: ~3.8 MB (CSV format)
- **Total Downloads**: 792+ (as of January 2026)

## Dataset Description

This dataset contains information about the winners of the i-Lab competition across multiple years. The competition awards funding to innovative technology startups in France.

### Expected Fields

The dataset typically includes:
- Company/Project name
- Year of award
- Category/Domain
- Region
- Award amount
- Project description
- Contact information

## How to Download

1. Visit one of the source URLs above
2. Download the CSV file
3. Place it in this directory (`data/ilab/`)
4. Run the processing script: `python3 scripts/process_ilab.py`

## Files in this Directory

- `README.md` - This file
- `ilab_laureats.csv` - Raw data (to be downloaded)
- `ilab_processed.json` - Processed data (generated)
- `ilab_analysis.txt` - Analysis results (generated)
