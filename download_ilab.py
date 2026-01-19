#!/usr/bin/env python3
"""
Script to download i-Lab laureates dataset from French government open data portal
"""

import requests
import time

def download_ilab_data():
    """Download i-Lab dataset from data.enseignementsup-recherche.gouv.fr"""

    # Try different URL formats for the i-Lab dataset
    urls = [
        "https://data.enseignementsup-recherche.gouv.fr/api/explore/v2.1/catalog/datasets/fr-esr-laureats-concours-national-i-lab/exports/csv",
        "https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-laureats-concours-national-i-lab/download/?format=csv",
        "https://data.enseignementsup-recherche.gouv.fr/api/records/1.0/download?dataset=fr-esr-laureats-concours-national-i-lab&format=csv",
    ]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/csv,application/csv,*/*',
        'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
        'Referer': 'https://data.enseignementsup-recherche.gouv.fr/'
    }

    for i, url in enumerate(urls, 1):
        print(f"Attempt {i}/{len(urls)}: Trying {url}")
        try:
            response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)

            if response.status_code == 200:
                # Check if we got CSV data
                content_type = response.headers.get('Content-Type', '')
                if 'csv' in content_type.lower() or len(response.content) > 1000:
                    output_file = 'ilab_laureats.csv'
                    with open(output_file, 'wb') as f:
                        f.write(response.content)
                    print(f"✓ Successfully downloaded data to {output_file}")
                    print(f"  File size: {len(response.content)} bytes")
                    return True
                else:
                    print(f"  Response doesn't appear to be CSV data")
            else:
                print(f"  HTTP {response.status_code}: {response.reason}")

        except requests.exceptions.RequestException as e:
            print(f"  Error: {e}")

        if i < len(urls):
            time.sleep(2)

    print("\n✗ All download attempts failed")
    print("\nAlternative: Please manually download the file from:")
    print("https://www.data.gouv.fr/datasets/laureats-i-lab-concours-national-daide-a-la-creation-dentreprises-de-technologies-innovantes-1")
    print("or")
    print("https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-laureats-concours-national-i-lab/")
    return False

if __name__ == "__main__":
    download_ilab_data()
