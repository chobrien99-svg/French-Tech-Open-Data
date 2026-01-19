#!/usr/bin/env python3
"""
Detailed analysis of i-Lab laureates dataset
Provides comprehensive statistics and insights
"""

import csv
import json
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

def load_csv_data(filepath):
    """Load CSV data with proper delimiter detection"""
    data = []
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        sample = f.read(2048)
        f.seek(0)
        delimiter = ';' if sample.count(';') > sample.count(',') else ','

        reader = csv.DictReader(f, delimiter=delimiter)
        for row in reader:
            # Clean empty rows
            if any(row.values()):
                data.append(row)
    return data

def analyze_comprehensive(data):
    """Perform comprehensive analysis"""

    analysis = {
        "metadata": {
            "total_records": len(data),
            "analysis_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "fields": list(data[0].keys()) if data else []
        }
    }

    # Gender distribution
    gender_field = 'Genre'
    if gender_field in data[0]:
        genders = [row.get(gender_field, 'Non spécifié') for row in data]
        analysis['gender_distribution'] = dict(Counter(genders))

    # Year distribution
    year_field = 'Année de concours'
    if year_field in data[0]:
        years = [row.get(year_field, 'Unknown') for row in data if row.get(year_field)]
        year_counts = Counter(years)
        analysis['by_year'] = dict(sorted(year_counts.items()))

        # Calculate trends
        if len(year_counts) > 1:
            years_list = sorted([int(y) for y in year_counts.keys() if y.isdigit()])
            if years_list:
                analysis['year_range'] = {
                    'first': years_list[0],
                    'last': years_list[-1],
                    'span': years_list[-1] - years_list[0] + 1
                }

    # Region distribution
    region_field = 'Région'
    if region_field in data[0]:
        regions = [row.get(region_field, 'Non spécifié') for row in data if row.get(region_field)]
        analysis['by_region'] = dict(Counter(regions).most_common())

    # Technology domain
    domain_field = 'Domaine technologique'
    if domain_field in data[0]:
        domains = [row.get(domain_field, 'Non spécifié') for row in data if row.get(domain_field)]
        analysis['by_domain'] = dict(Counter(domains).most_common(25))

    # Candidature type
    type_field = 'Type de candidature'
    if type_field in data[0]:
        types = [row.get(type_field, 'Non spécifié') for row in data if row.get(type_field)]
        analysis['by_candidature_type'] = dict(Counter(types))

    # Grand Prix winners
    prix_field = 'Grand-Prix'
    if prix_field in data[0]:
        prix_count = sum(1 for row in data if row.get(prix_field))
        analysis['grand_prix_winners'] = prix_count

    # Jury level
    jury_field = 'Jury'
    if jury_field in data[0]:
        juries = [row.get(jury_field, 'Non spécifié') for row in data if row.get(jury_field)]
        analysis['by_jury'] = dict(Counter(juries))

    # Companies with SIRET/SIREN
    siret_count = sum(1 for row in data if row.get('N° SIRET'))
    siren_count = sum(1 for row in data if row.get('N° SIREN'))
    analysis['company_info'] = {
        'with_siret': siret_count,
        'with_siren': siren_count
    }

    # Previous winners (repeat laureates)
    prev_field = 'Déjà lauréat en'
    repeat_winners = sum(1 for row in data if row.get(prev_field))
    analysis['repeat_laureates'] = repeat_winners

    # Region + Year cross-analysis
    if year_field in data[0] and region_field in data[0]:
        region_year = defaultdict(lambda: defaultdict(int))
        for row in data:
            year = row.get(year_field)
            region = row.get(region_field)
            if year and region:
                region_year[region][year] += 1
        analysis['region_year_detail'] = {
            region: dict(years) for region, years in region_year.items()
        }

    return analysis

def generate_report(analysis, output_file):
    """Generate a comprehensive text report"""

    with open(output_file, 'w', encoding='utf-8') as f:
        # Header
        f.write("=" * 100 + "\n")
        f.write("I-LAB LAUREATES - COMPREHENSIVE ANALYSIS REPORT\n")
        f.write("Concours national d'aide à la création d'entreprises de technologies innovantes\n")
        f.write("=" * 100 + "\n\n")

        f.write(f"Generated: {analysis['metadata']['analysis_date']}\n")
        f.write(f"Total Records: {analysis['metadata']['total_records']:,}\n\n")

        # Executive Summary
        f.write("EXECUTIVE SUMMARY\n")
        f.write("-" * 100 + "\n")
        if 'year_range' in analysis:
            yr = analysis['year_range']
            f.write(f"Competition Period: {yr['first']} - {yr['last']} ({yr['span']} years)\n")
        f.write(f"Grand Prix Winners: {analysis.get('grand_prix_winners', 0)}\n")
        f.write(f"Repeat Laureates: {analysis.get('repeat_laureates', 0)}\n")
        f.write(f"Companies with SIRET: {analysis['company_info']['with_siret']}\n\n")

        # Gender Distribution
        if 'gender_distribution' in analysis:
            f.write("\nGENDER DISTRIBUTION\n")
            f.write("-" * 100 + "\n")
            total = sum(analysis['gender_distribution'].values())
            for gender, count in sorted(analysis['gender_distribution'].items(), key=lambda x: x[1], reverse=True):
                pct = (count / total * 100) if total > 0 else 0
                f.write(f"{gender:20s}: {count:5,} ({pct:5.1f}%)\n")

        # Year Distribution
        if 'by_year' in analysis:
            f.write("\n\nYEAR DISTRIBUTION\n")
            f.write("-" * 100 + "\n")
            for year, count in sorted(analysis['by_year'].items()):
                f.write(f"{year}: {'█' * (count // 10)} {count}\n")

        # Region Distribution
        if 'by_region' in analysis:
            f.write("\n\nREGIONAL DISTRIBUTION (Top 15)\n")
            f.write("-" * 100 + "\n")
            total = sum(analysis['by_region'].values())
            for i, (region, count) in enumerate(list(analysis['by_region'].items())[:15], 1):
                pct = (count / total * 100) if total > 0 else 0
                f.write(f"{i:2d}. {region:35s}: {count:5,} ({pct:5.1f}%)\n")

        # Technology Domains
        if 'by_domain' in analysis:
            f.write("\n\nTECHNOLOGY DOMAINS (Top 20)\n")
            f.write("-" * 100 + "\n")
            total = sum(analysis['by_domain'].values())
            for i, (domain, count) in enumerate(list(analysis['by_domain'].items())[:20], 1):
                pct = (count / total * 100) if total > 0 else 0
                f.write(f"{i:2d}. {domain:60s}: {count:5,} ({pct:5.1f}%)\n")

        # Candidature Type
        if 'by_candidature_type' in analysis:
            f.write("\n\nCANDIDATURE TYPE\n")
            f.write("-" * 100 + "\n")
            total = sum(analysis['by_candidature_type'].values())
            for ctype, count in sorted(analysis['by_candidature_type'].items(), key=lambda x: x[1], reverse=True):
                pct = (count / total * 100) if total > 0 else 0
                f.write(f"{ctype:30s}: {count:5,} ({pct:5.1f}%)\n")

        # Jury Level
        if 'by_jury' in analysis:
            f.write("\n\nJURY LEVEL\n")
            f.write("-" * 100 + "\n")
            total = sum(analysis['by_jury'].values())
            for jury, count in sorted(analysis['by_jury'].items(), key=lambda x: x[1], reverse=True):
                pct = (count / total * 100) if total > 0 else 0
                f.write(f"{jury:20s}: {count:5,} ({pct:5.1f}%)\n")

        # Top performing regions by recent years
        if 'region_year_detail' in analysis:
            f.write("\n\nTOP 5 REGIONS - RECENT ACTIVITY (Last 5 Years)\n")
            f.write("-" * 100 + "\n")

            # Get recent years
            all_years = set()
            for region_data in analysis['region_year_detail'].values():
                all_years.update(region_data.keys())
            recent_years = sorted([y for y in all_years if y.isdigit()], key=int, reverse=True)[:5]

            # Calculate totals for recent years
            region_recent = {}
            for region, years in analysis['region_year_detail'].items():
                total = sum(years.get(year, 0) for year in recent_years)
                if total > 0:
                    region_recent[region] = total

            for i, (region, count) in enumerate(sorted(region_recent.items(), key=lambda x: x[1], reverse=True)[:5], 1):
                f.write(f"{i}. {region}: {count} laureates\n")

        f.write("\n" + "=" * 100 + "\n")
        f.write("END OF REPORT\n")
        f.write("=" * 100 + "\n")

def main():
    """Main execution"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data" / "ilab"

    csv_file = data_dir / "ilab_laureats.csv"

    if not csv_file.exists():
        print(f"❌ File not found: {csv_file}")
        return

    print(f"📊 Analyzing: {csv_file.name}")

    # Load data
    print("Loading data...")
    data = load_csv_data(csv_file)
    print(f"✓ Loaded {len(data):,} records")

    # Analyze
    print("Performing comprehensive analysis...")
    analysis = analyze_comprehensive(data)

    # Save detailed JSON
    output_json = data_dir / "ilab_analysis_detailed.json"
    print(f"Saving detailed analysis to {output_json.name}...")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)

    # Generate report
    output_report = data_dir / "ilab_comprehensive_report.txt"
    print(f"Generating comprehensive report...")
    generate_report(analysis, output_report)

    print(f"\n✅ Analysis complete!")
    print(f"   - Detailed JSON: {output_json.name}")
    print(f"   - Report: {output_report.name}")

if __name__ == "__main__":
    main()
