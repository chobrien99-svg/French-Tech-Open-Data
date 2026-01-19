#!/usr/bin/env python3
"""
Process and analyze i-Lab laureates dataset
"""

import csv
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

def load_csv_data(filepath):
    """Load CSV data and return as list of dictionaries"""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        # Try to detect delimiter
        sample = f.read(1024)
        f.seek(0)
        delimiter = ';' if sample.count(';') > sample.count(',') else ','

        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

def analyze_data(data):
    """Perform basic analysis on the dataset"""
    if not data:
        return {"error": "No data to analyze"}

    analysis = {
        "total_records": len(data),
        "fields": list(data[0].keys()) if data else [],
        "record_count": len(data)
    }

    # Analyze by year if year field exists
    year_fields = [f for f in analysis["fields"] if 'year' in f.lower() or 'annee' in f.lower() or 'date' in f.lower()]
    if year_fields:
        year_field = year_fields[0]
        years = [row.get(year_field, 'Unknown') for row in data]
        analysis["by_year"] = dict(Counter(years).most_common())

    # Analyze by region if region field exists
    region_fields = [f for f in analysis["fields"] if 'region' in f.lower() or 'territoire' in f.lower()]
    if region_fields:
        region_field = region_fields[0]
        regions = [row.get(region_field, 'Unknown') for row in data]
        analysis["by_region"] = dict(Counter(regions).most_common(20))

    # Analyze by category/domain if such field exists
    category_fields = [f for f in analysis["fields"] if any(term in f.lower() for term in ['categorie', 'category', 'domaine', 'domain', 'secteur'])]
    if category_fields:
        category_field = category_fields[0]
        categories = [row.get(category_field, 'Unknown') for row in data]
        analysis["by_category"] = dict(Counter(categories).most_common(20))

    return analysis

def save_analysis(analysis, output_file):
    """Save analysis results to a text file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("i-Lab Laureates Dataset Analysis\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Total Records: {analysis.get('total_records', 0)}\n\n")

        f.write("Fields in Dataset:\n")
        for field in analysis.get('fields', []):
            f.write(f"  - {field}\n")
        f.write("\n")

        if 'by_year' in analysis:
            f.write("Distribution by Year:\n")
            for year, count in sorted(analysis['by_year'].items()):
                f.write(f"  {year}: {count}\n")
            f.write("\n")

        if 'by_region' in analysis:
            f.write("Top Regions (Top 20):\n")
            for region, count in list(analysis['by_region'].items())[:20]:
                f.write(f"  {region}: {count}\n")
            f.write("\n")

        if 'by_category' in analysis:
            f.write("Top Categories/Domains (Top 20):\n")
            for category, count in list(analysis['by_category'].items())[:20]:
                f.write(f"  {category}: {count}\n")
            f.write("\n")

def main():
    """Main processing function"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data" / "ilab"

    # Look for CSV files
    csv_files = list(data_dir.glob("*.csv"))

    if not csv_files:
        print("❌ No CSV files found in data/ilab/")
        print("\nPlease download the i-Lab dataset and place it in data/ilab/")
        print("Download from: https://www.data.gouv.fr/datasets/laureats-i-lab-concours-national-daide-a-la-creation-dentreprises-de-technologies-innovantes-1")
        return

    input_file = csv_files[0]
    print(f"📊 Processing: {input_file.name}")

    # Load data
    print("Loading data...")
    data = load_csv_data(input_file)
    print(f"✓ Loaded {len(data)} records")

    # Analyze
    print("Analyzing data...")
    analysis = analyze_data(data)

    # Save processed data
    output_json = data_dir / "ilab_processed.json"
    print(f"Saving processed data to {output_json.name}...")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved {len(data)} records to JSON")

    # Save analysis
    output_analysis = data_dir / "ilab_analysis.txt"
    print(f"Saving analysis to {output_analysis.name}...")
    save_analysis(analysis, output_analysis)
    print(f"✓ Analysis saved")

    print("\n" + "=" * 80)
    print("Summary:")
    print(f"  Total records: {analysis.get('total_records', 0)}")
    print(f"  Fields: {len(analysis.get('fields', []))}")
    if 'by_year' in analysis:
        print(f"  Years covered: {len(analysis['by_year'])}")
    if 'by_region' in analysis:
        print(f"  Regions: {len(analysis['by_region'])}")
    print("=" * 80)

if __name__ == "__main__":
    main()
