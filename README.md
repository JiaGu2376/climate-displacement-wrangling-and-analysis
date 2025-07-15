# Disaster Displacement & CO Emissions Analysis

Global climate risk is increasing, but its effects are not distributed equally. High-emission industrialised countries may not always face the most severe displacement impacts, while vulnerable regions often with lower emissions bear the consequences of natural hazards. This project seeks to quantify and visualise these dynamics to inform more equitable climate discussions. This project analyses the relationship between carbon monoxide (CO) emissions and disaster-induced internal displacement across countries, combining environmental and humanitarian datasets to explore patterns relevant to climate equity.

---

## Objective

To explore how national-level CO emissions relate to the frequency and severity of internal displacement caused by natural disasters. The aim is to identify trends, regional differences in hazard exposure, and disparities between emission responsibility and climate vulnerability.

---

## Data Sources

- **OECD** (Organisation for Economic Co-operation and Development) provides structured data on national air pollutant emissions (CSV format).
- **IDMC** (Internal Displacement Monitoring Centre) offers JSON-based event-level data on disaster-induced displacement, accessible via API upon request.

These datasets were merged at the country-year level after thorough cleaning and standardisation to enable robust comparative analysis.

> ⚠️ **Data Limitation:**  
> The OECD emissions dataset primarily covers OECD member countries. As a result, many developing countries are excluded in the emissions data. This limits the completeness of the global picture and means that findings related to climate disparity should be interpreted with this constraint in mind.

---

## Dataset Overview

| Column Name             | Description                                                |
|-------------------------|------------------------------------------------------------|
| `country_name`          | Name of the country                                         |
| `iso3`                  | 3-letter country code                                       |
| `year`                  | Year of observation                                         |
| `CO_emissions_tonnes`  | Carbon monoxide emissions in metric tonnes                 |
| `displacement`          | Number of people internally displaced due to disasters     |
| `hazard_type_name`      | Type of natural hazard (e.g., Storm, Flood, Wildfire)       |

Additional columns exist for pollutant data and disaster event details.

---

## Methodology

- Imported CSV (OECD) and JSON (IDMC) data
- Cleaned and standardised fields 
- Aggregated and merged datasets at the country-year level
- Identified top-emitting and most-affected countries
- Created comparative bar charts and heatmaps using Matplotlib and Seaborn
- Analyzed hazard-specific exposure and trends

---

## Key Analysis 

- Emissions vs Displacement: Imbalance between emitters and impact zones  
- Hazard Exposure: Regional variation in disaster types
- Trend Analysis: Emissions declining, displacement persisting in the US 

---

## Files in This Repository

| File Name | Description |
|-----------|-------------|
| [`Air Emissions and Disaster Displacement Project Report.pdf`](./Air%20Emissions%20and%20Disaster%20Displacement%20Project%20Report.pdf) | Summary report (PDF format) |
| [`Air_Emissions_and_Disaster_Displacement_Project.ipynb`](./Air_Emissions_and_Disaster_Displacement_Project.ipynb) | Full Jupyter Notebook with code and visualizations |
| [`merged_emissions_disasters.csv`](./merged_emissions_disasters.csv) | Cleaned, merged dataset (OECD + IDMC) |
| [`GIDDImport.json`](./GIDDImport.json) | Raw IDMC displacement dataset (JSON format) |
| [`OECD.ENV.EPI,DSD_AIR_EMISSIONS@DF_AIR_EMISSIONS,+all.csv`](./OECD.ENV.EPI,DSD_AIR_EMISSIONS@DF_AIR_EMISSIONS,+all.csv) | Raw OECD emissions dataset |


---

## Future Improvements
- Apply machine learning to forecast high-risk zones
- Include more pollutant types beyond CO for broader context
- Validate findings with external sources and case studies
