#!/usr/bin/env python3
"""
Analyze French Open Data datasets for relevance to The French Tech Journal audience.
Target audience: entrepreneurs, startups, digital transformation leaders,
corporate leaders, investors, VCs, and policy makers.
"""

import csv
import glob
import json
from collections import defaultdict
from typing import Dict, List, Set

# Keywords indicating relevance to tech/business/startup audience
RELEVANCE_KEYWORDS = {
    # Business & Entrepreneurship
    'entreprise', 'entreprises', 'startup', 'start-up', 'pme', 'tpe', 'business',
    'entrepreneuriat', 'entrepreneur', 'commerce', 'commercial',

    # Innovation & Tech
    'innovation', 'innovant', 'technologie', 'tech', 'digital', 'numerique',
    'numérique', 'transformation', 'r&d', 'recherche', 'développement',
    'ia', 'intelligence-artificielle', 'data', 'données', 'cybersecurite',
    'cybersécurité', 'blockchain', 'cloud', 'saas',

    # Finance & Investment
    'investissement', 'financement', 'capital', 'venture', 'levee-de-fonds',
    'levée', 'subvention', 'aide', 'credit', 'crédit', 'financier',
    'economie', 'économie', 'economique', 'économique', 'bourse',

    # Employment & Talent
    'emploi', 'travail', 'salaire', 'competence', 'compétence', 'formation',
    'qualification', 'recrutement', 'cadre', 'cadres', 'rh',

    # Industry sectors
    'industrie', 'industriel', 'production', 'manufacture', 'usine',
    'energie', 'énergie', 'cleantech', 'greentech', 'biotech', 'fintech',
    'healthtech', 'edtech', 'agritech', 'proptech',

    # Infrastructure
    'infrastructure', 'reseau', 'réseau', 'telecommunication',
    'télécommunication', 'internet', 'broadband', 'fibre', 'haut-debit',
    'connectivite', 'connectivité',

    # Policy & Regulation
    'reglementation', 'réglementation', 'politique', 'loi', 'legislation',
    'législation', 'norme', 'standard', 'directive', 'reforme', 'réforme',

    # Corporate & Markets
    'societe', 'société', 'marche', 'marché', 'secteur', 'activite', 'activité',
    'commerce', 'export', 'import', 'international', 'competitivite',
    'compétitivité', 'productivite', 'productivité',

    # IP & Patents
    'brevet', 'propriete-intellectuelle', 'propriété', 'marque', 'copyright',

    # Statistics & Indicators
    'statistique', 'indicateur', 'performance', 'croissance', 'chiffre-affaires',
    'ca', 'resultat', 'résultat', 'benefice', 'bénéfice',

    # Specific databases
    'sirene', 'siret', 'siren', 'rcs', 'registre', 'repertoire', 'répertoire',
    'bodacc', 'inpi',

    # Geo-economic
    'zone-franche', 'zone-economique', 'économique', 'cluster', 'pole', 'pôle',
    'technopole', 'incubateur', 'accelerateur', 'accélérateur', 'pepiniere',
    'pépinière', 'fab-lab', 'coworking',
}

def normalize_text(text: str) -> str:
    """Normalize text for keyword matching."""
    if not text:
        return ""
    return text.lower().strip()

def calculate_relevance_score(row: Dict[str, str]) -> tuple[int, Set[str]]:
    """
    Calculate relevance score based on keywords in title, description, and tags.
    Returns (score, matching_keywords)
    """
    score = 0
    matching_keywords = set()

    # Fields to check
    title = normalize_text(row.get('title', ''))
    description = normalize_text(row.get('description', ''))
    tags = normalize_text(row.get('tags', ''))
    org = normalize_text(row.get('organization', ''))

    # Combine all text
    all_text = f"{title} {description} {tags} {org}"

    # Check each keyword
    for keyword in RELEVANCE_KEYWORDS:
        if keyword in all_text:
            # Weight by field
            if keyword in title:
                score += 10
                matching_keywords.add(keyword)
            if keyword in tags:
                score += 5
                matching_keywords.add(keyword)
            if keyword in description:
                score += 3
                matching_keywords.add(keyword)

    return score, matching_keywords

def analyze_datasets():
    """Main analysis function."""
    csv_files = sorted(glob.glob('/home/user/French-Tech-Open-Data/*.csv'))

    print(f"Found {len(csv_files)} CSV files to analyze\n")

    all_datasets = []
    relevant_datasets = []

    # Read all datasets
    for csv_file in csv_files:
        try:
            with open(csv_file, 'r', encoding='utf-8') as f:
                # Use semicolon delimiter based on the file structure
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    # Clean quotes from all fields
                    cleaned_row = {k: v.strip('"') if v else '' for k, v in row.items()}
                    all_datasets.append(cleaned_row)
        except Exception as e:
            print(f"Error reading {csv_file}: {e}")

    print(f"Total datasets loaded: {len(all_datasets)}\n")

    # Analyze relevance
    for dataset in all_datasets:
        score, keywords = calculate_relevance_score(dataset)

        if score > 0:  # Any relevance
            dataset['relevance_score'] = score
            dataset['matching_keywords'] = list(keywords)
            relevant_datasets.append(dataset)

    # Sort by relevance score
    relevant_datasets.sort(key=lambda x: x['relevance_score'], reverse=True)

    print(f"Relevant datasets found: {len(relevant_datasets)}\n")
    print("="*100)

    # Group by category
    categories = defaultdict(list)

    for dataset in relevant_datasets[:200]:  # Top 200 most relevant
        primary_keywords = dataset['matching_keywords'][:3] if dataset['matching_keywords'] else ['other']
        category = primary_keywords[0]
        categories[category].append(dataset)

    # Print top datasets by score
    print("\n" + "="*100)
    print("TOP 50 MOST RELEVANT DATASETS")
    print("="*100 + "\n")

    for i, dataset in enumerate(relevant_datasets[:50], 1):
        print(f"{i}. [{dataset['relevance_score']} points] {dataset['title']}")
        print(f"   Organization: {dataset['organization']}")
        print(f"   URL: {dataset['url']}")
        print(f"   Keywords: {', '.join(dataset['matching_keywords'][:10])}")
        if dataset.get('description_short'):
            desc = dataset['description_short'][:200]
            print(f"   Description: {desc}...")
        print()

    # Category summary
    print("\n" + "="*100)
    print("DATASETS BY PRIMARY CATEGORY")
    print("="*100 + "\n")

    for category, datasets in sorted(categories.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n{category.upper()} ({len(datasets)} datasets):")
        for dataset in datasets[:5]:  # Top 5 per category
            print(f"  - {dataset['title']} (score: {dataset['relevance_score']})")

    # Save detailed results
    with open('/home/user/French-Tech-Open-Data/analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump({
            'total_datasets': len(all_datasets),
            'relevant_datasets_count': len(relevant_datasets),
            'top_100_datasets': relevant_datasets[:100]
        }, f, ensure_ascii=False, indent=2)

    print(f"\n\nDetailed results saved to: analysis_results.json")

    # Export CSV summary
    with open('/home/user/French-Tech-Open-Data/relevant_datasets_summary.csv', 'w',
              encoding='utf-8', newline='') as f:
        if relevant_datasets:
            fieldnames = ['relevance_score', 'title', 'organization', 'url',
                         'tags', 'matching_keywords']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for dataset in relevant_datasets[:100]:
                writer.writerow({
                    'relevance_score': dataset['relevance_score'],
                    'title': dataset['title'],
                    'organization': dataset['organization'],
                    'url': dataset['url'],
                    'tags': dataset.get('tags', ''),
                    'matching_keywords': ', '.join(dataset['matching_keywords'])
                })

    print(f"CSV summary saved to: relevant_datasets_summary.csv")

    # Print statistics
    print("\n" + "="*100)
    print("STATISTICS")
    print("="*100)
    print(f"Total datasets analyzed: {len(all_datasets)}")
    print(f"Datasets with relevance: {len(relevant_datasets)}")
    print(f"Relevance rate: {len(relevant_datasets)/len(all_datasets)*100:.1f}%")

    # Score distribution
    high_relevance = len([d for d in relevant_datasets if d['relevance_score'] >= 50])
    medium_relevance = len([d for d in relevant_datasets if 20 <= d['relevance_score'] < 50])
    low_relevance = len([d for d in relevant_datasets if d['relevance_score'] < 20])

    print(f"\nRelevance distribution:")
    print(f"  High relevance (50+ points): {high_relevance}")
    print(f"  Medium relevance (20-49 points): {medium_relevance}")
    print(f"  Low relevance (1-19 points): {low_relevance}")

if __name__ == '__main__':
    analyze_datasets()
