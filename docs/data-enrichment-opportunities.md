# Data Enrichment Opportunities for i-Lab Laureates

This document outlines how to enrich the i-Lab laureates dataset with additional data sources to track funding, exits, company performance, and research activity.

## Available Data Sources

### 1. **scanR** - French Research & Innovation Database
**URL**: https://scanr.enseignementsup-recherche.gouv.fr/

**What it offers**:
- 30,000+ public/private research structures
- 800,000+ researchers
- 115,000+ funding sources
- 4 million+ scientific publications
- **Open API** with free access
- Already linked in i-Lab dataset (field: "Lien vers scanR")

**Match strategy**:
- Direct: Many i-Lab records already have scanR links
- SIREN/SIRET matching
- Company name matching

**Enrichment value**:
- Research publications by company
- Researcher profiles
- Additional funding sources
- Patent information
- Academic partnerships

**API Documentation**: https://scanr.enseignementsup-recherche.gouv.fr/api/

---

### 2. **API Sirene** - French Company Registry (INSEE)
**URL**: https://www.data.gouv.fr/dataservices/api-sirene-open-data

**What it offers**:
- 23 million legal units
- 28 million establishments
- Complete company history since 1973
- Legal status, address, activity codes
- Creation/closure dates
- **Free open data API**

**Match strategy**:
- 636 i-Lab laureates have SIRET numbers (direct match)
- 3,923 i-Lab laureates have company names (fuzzy match)

**Enrichment value**:
- Company survival rate (still active vs closed)
- Legal form changes (incorporation, transformations)
- Employee count ranges
- Activity sector (NAF codes)
- Geographic moves/expansions

**API Query Example**:
```bash
curl "https://api.insee.fr/entreprises/sirene/V3/siret/40303041900015"
```

---

### 3. **French Tech Next40/120** - Top French Startups
**URL**: https://www.datablist.com/learn/datasets/dataset-frenchtech-120-csv

**What it offers**:
- CSV list of France's top 120 fastest-growing startups
- Updated regularly
- Recognized by French government

**Match strategy**:
- Company name matching
- SIREN/SIRET if available

**Enrichment value**:
- Success indicator (made it to Next40/120)
- Approximate valuation tier
- Growth trajectory

---

### 4. **Bpifrance Funding Data**
**Status**: Not yet available as open data API

**Potential value**:
- Follow-on funding after i-Lab
- Loan amounts
- Investment types
- Bpifrance accounts for 58% of French startup investments

**Alternative**: May need manual scraping or partnership request

---

### 5. **Infogreffe** - Commercial Court Registry
**URL**: https://www.infogreffe.fr/

**What it offers**:
- Financial statements (comptes annuels)
- Legal documents
- Beneficial owners
- Litigation history

**Match strategy**:
- SIREN/SIRET matching (636 direct matches)

**Enrichment value**:
- Revenue/profit data
- Balance sheets
- Employee counts (exact)
- Capital raises (via legal filings)
- M&A activity
- Bankruptcy/liquidation status

**Note**: Partial open data, some information requires payment

---

### 6. **data.gouv.fr** - Additional Government Datasets

Potential datasets to cross-reference:
- **JEI (Jeune Entreprise Innovante)** status companies
- **CIR (Crédit Impôt Recherche)** tax credit recipients
- **ANR (Agence Nationale de la Recherche)** funding recipients
- **Regional innovation funding** programs
- **European grants** (Horizon 2020, etc.)

---

### 7. **Crunchbase / Dealroom** (Commercial)
**Not open data**, but comprehensive:
- Venture capital funding rounds
- Acquisition events
- IPOs
- Investor information
- Valuation data

**Cost**: Requires subscription ($29-$99+/month)

---

## Recommended Enrichment Strategy

### Phase 1: Free/Open Data Sources (Immediate)
1. **scanR API** - Already linked for many companies
   - Pull publication counts
   - Extract patent information
   - Identify research partnerships

2. **API Sirene** - Match via SIRET
   - Validate company survival status
   - Get accurate employee counts
   - Track company transformations

3. **French Tech Next40/120 CSV** - Simple merge
   - Flag i-Lab alumni who reached top tier

### Phase 2: Semi-Public Data (Medium effort)
4. **Infogreffe** - SIRET-based extraction
   - Extract financial data for 636 companies with SIRET
   - Calculate revenue growth rates
   - Identify exits/acquisitions

5. **data.gouv.fr datasets** - Additional cross-matching
   - JEI status correlation
   - Other grant programs

### Phase 3: Commercial Data (If budget available)
6. **Crunchbase/Dealroom** - Professional-grade data
   - VC funding amounts
   - Exit valuations
   - Investment rounds

---

## Implementation Scripts

### Script 1: scanR Enrichment
```python
# Match i-Lab companies to scanR data
# Pull publication counts, patents, funding
```

### Script 2: Sirene API Validation
```python
# Check company status (active/closed)
# Extract employee counts, sector codes
# Calculate survival rates by cohort
```

### Script 3: Financial Performance
```python
# Extract Infogreffe data for companies with SIRET
# Calculate revenue growth
# Identify unicorns/exits
```

---

## Key Metrics to Calculate

Once enriched, we can answer:

### Success Metrics
1. **Survival Rate**: % still active after 5/10/15 years
2. **Growth Rate**: Revenue CAGR for survivors
3. **Exit Rate**: % acquired or IPO'd
4. **Unicorn Rate**: % reaching €1B+ valuation
5. **Follow-on Funding**: % securing VC after i-Lab

### Impact Metrics
6. **Publication Impact**: Research output correlation
7. **Patent Activity**: IP generation rates
8. **Job Creation**: Employment growth
9. **Geographic Retention**: % staying in original region
10. **Sector Success**: Which tech domains perform best

### Comparative Metrics
11. **i-Lab ROI**: Public investment vs. economic output
12. **Grand Prix Effect**: Do winners outperform?
13. **Regional Variations**: Success by region
14. **Gender Gap Impact**: Male vs. female founder outcomes

---

## Data Quality Considerations

### Matching Challenges
- **Name variations**: Legal name vs. trading name
- **SIRET changes**: Companies may change registration
- **Mergers**: Tracking acquired companies
- **Pivots**: Companies changing business model

### Solutions
- Fuzzy matching algorithms (fuzzywuzzy, RapidFuzz)
- Manual validation for high-value matches
- Historical SIRET tracking via Sirene API
- scanR links as ground truth

---

## Legal/Ethical Considerations

All recommended sources are:
- ✅ Public open data (except commercial options)
- ✅ Compliant with GDPR (company data, not personal)
- ✅ Licensed for reuse (Licence Ouverte 2.0)
- ✅ Attribution required (source citations)

---

## Next Steps

1. **Immediate**: Build scanR API integration (many companies already linked)
2. **Week 1**: Implement Sirene API validation script
3. **Week 2**: Download French Tech Next40/120 and merge
4. **Month 1**: Extract Infogreffe data for SIRET-matched companies
5. **Month 2**: Calculate success metrics and create enriched dashboard

---

## Expected Outcomes

**Enriched dataset will enable**:
- Success story identification (for French Tech promotion)
- Policy impact analysis (ROI of i-Lab program)
- Sector-specific insights (which domains need support)
- Regional equity assessment (is funding distributed fairly)
- Gender gap quantification (hard evidence for policy)
- Best practices identification (what makes winners succeed)

This enriched analysis could be extremely valuable for:
- Ministry of Higher Education & Research
- Bpifrance investment decisions
- Regional innovation agencies
- Startup accelerators
- Academic researchers studying innovation policy
