# Multi-Domain Data Analysis Portfolio – 5 Real Projects

**Author:** Madhurja Bhattacharjee  
**Internship:** Developers Arena  
**Project:** Multi-Domain Data Analysis Portfolio  
**Core Technologies:** Python, Pandas, NumPy, SciPy, Matplotlib, Seaborn, FPDF2, Pytest

---

## 🎯 Executive Summary

This portfolio presents five complete data analysis projects across different real-world domains:

1. **Supermarket Sales Analysis** – Retail & Commerce
2. **Student Performance Analysis** – Education
3. **Weather Data Analysis** – Meteorology & Environment
4. **COVID-19 Healthcare Trends** – Public Health
5. **Stock Market Risk & Return Analysis** – Finance

Each project demonstrates a complete analytical workflow covering data loading, data-quality validation, cleaning and transformation, exploratory analysis, statistical analysis, visualization, interpretation, and actionable recommendations.

The portfolio contains five Jupyter notebooks, five analytical PDF reports, 22 saved visualizations, reusable validation functions, an automated pytest test suite, and presentation deliverables.

---

## 📊 Projects Overview

| # | Project | Domain | Dataset Size | Key Focus |
|---|---|---|---:|---|
| 01 | Supermarket Sales Analysis | Retail | 2,000 × 14 | Sales trends, branches, customer behavior |
| 02 | Student Performance Analysis | Education | 500 × 10 | Academic performance and measured effort |
| 03 | Weather Data Analysis | Environment | 365 × 12 | Rainfall, temperature and seasonal patterns |
| 04 | COVID-19 Healthcare Trends | Public Health | 1,825 × 10 | Case activity, vaccination phases and regional patterns |
| 05 | Stock Market Risk & Return | Finance | 252 × 12 | Returns, volatility, drawdown and risk |

---

# 📂 Repository Structure

```text
Multi-Domain-Data-Analysis/
│
├── data/
│   └── raw/
│       ├── supermarket_sales.csv
│       ├── student_performance.csv
│       ├── weather_data.csv
│       ├── covid_healthcare_data.csv
│       └── stock_market_data.csv
│
├── notebooks/
│   ├── 01_supermarket_sales_analysis.ipynb
│   ├── 02_student_performance_analysis.ipynb
│   ├── 03_weather_data_analysis.ipynb
│   ├── 04_covid_healthcare_analysis.ipynb
│   └── 05_stock_market_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   └── data_validation.py
│
├── tests/
│   ├── __init__.py
│   ├── test_data_validation.py
│   ├── test_supermarket.py
│   ├── test_student.py
│   ├── test_weather.py
│   ├── test_covid.py
│   └── test_stock_market.py
│
├── visualizations/
│   └── 22 analytical PNG visualizations
│
├── reports/
│   ├── 01_supermarket_sales_report.pdf
│   ├── 02_student_performance_report.pdf
│   ├── 03_weather_analysis_report.pdf
│   ├── 04_covid_healthcare_report.pdf
│   └── 05_stock_market_report.pdf
│
├── presentation/
│   ├── multi_domain_data_analysis_portfolio.pptx
│   ├── multi_domain_data_analysis_portfolio.pdf
│   └── index.html
│
├── docs/
│   └── PORTFOLIO_PRESENTATION_GUIDE.md
│
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# 🛠️ Technologies Used

### Programming & Data Analysis
- Python
- Pandas
- NumPy
- SciPy

### Visualization
- Matplotlib
- Seaborn

### Reporting
- FPDF2
- Jupyter Notebook

### Testing
- Pytest

### Development
- VS Code
- Git
- GitHub

---

# ⚙️ Installation & Setup

## Prerequisites

- Python 3.13 or compatible Python 3.x version
- Git
- Jupyter Notebook or VS Code with the Jupyter extension

## Clone the Repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Multi-Domain-Data-Analysis
```

## Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Project Dependencies

```bash
pip install -r requirements.txt
```

## Jupyter Environment

If Jupyter is not already installed in your environment:

```bash
pip install jupyter ipykernel
```

Register the project kernel:

```bash
python -m ipykernel install --user --name multi-domain-analysis
```

When using VS Code, select the `multi-domain-analysis` kernel when running the notebooks.

---

# ▶️ How to Run the Projects

The portfolio is organized as five independent Jupyter Notebook analyses.

Open the `notebooks/` directory and run the projects individually:

```text
01_supermarket_sales_analysis.ipynb
02_student_performance_analysis.ipynb
03_weather_data_analysis.ipynb
04_covid_healthcare_analysis.ipynb
05_stock_market_analysis.ipynb
```

Each notebook follows a project-specific analytical workflow:

```text
Raw Dataset
    ↓
Data Loading
    ↓
Data Quality Checks
    ↓
Cleaning & Transformation
    ↓
Exploratory Data Analysis
    ↓
Statistical Analysis
    ↓
Visualization
    ↓
Insights & Recommendations
```

Generated charts are stored in:

```text
visualizations/
```

Analytical PDF reports are stored in:

```text
reports/
```

---

# 📈 Project 01 — Supermarket Sales Analysis

### Domain
Retail & Commerce

### Dataset
2,000 transactions across three branches.

### Analysis Focus

- Sales and revenue patterns
- Branch-level performance
- Product-line performance
- Customer behavior
- Payment methods
- Customer ratings
- Time-based purchasing patterns
- Basket and transaction characteristics

### Key Analysis

The project includes descriptive statistics, branch comparisons, product analysis, time-based analysis, customer-rating analysis, and financial data-quality validation.

A financial consistency check identified discrepancies between the supplied `Total` values and the calculated relationship:

```text
Unit Price × Quantity + Tax
```

The original source values were retained rather than artificially corrected, and the discrepancy is documented as a dataset limitation.

### Report

`reports/01_supermarket_sales_report.pdf`

### Notebook

`notebooks/01_supermarket_sales_analysis.ipynb`

---

# 🎓 Project 02 — Student Performance Analysis

### Domain
Education & Academia

### Dataset
500 academic records containing attendance, study hours, subject scores, grades, and related variables.

### Analysis Focus

- Overall academic performance
- Grade distribution
- Performance tiers
- Attendance
- Study hours
- Subject-level performance
- Correlation analysis
- Differences between performance groups

### Key Analysis

The analysis evaluates the relationship between measured effort variables and academic performance.

Observed correlations were weak:

- Attendance vs. grades: **r = 0.077**
- Study hours vs. grades: **r = 0.096**

The dataset therefore does not support strong conclusions about effort alone explaining performance differences.

The analysis does not directly measure factors such as teaching quality, socioeconomic conditions, learning environment, or other unobserved factors.

### Report

`reports/02_student_performance_report.pdf`

### Notebook

`notebooks/02_student_performance_analysis.ipynb`

---

# 🌦️ Project 03 — Weather Data Analysis

### Domain
Meteorology & Environment

### Dataset
365 daily meteorological observations from a single weather station.

### Analysis Focus

- Temperature trends
- Rainfall patterns
- Humidity
- Wind conditions
- Seasonal variation
- Monthly aggregation
- Rainfall concentration
- Weather-related planning considerations

### Key Analysis

The dataset records approximately **2,448 mm of annual rainfall**, with **64.7% concentrated within 77 days**.

The observed data shows a strong seasonal rainfall pattern consistent with a monsoon-like pattern.

However, the dataset covers only one year and one station, so it is not sufficient to establish a formal long-term climate classification.

### Report

`reports/03_weather_analysis_report.pdf`

### Notebook

`notebooks/03_weather_data_analysis.ipynb`

---

# 🏥 Project 04 — COVID-19 Healthcare Trends

### Domain
Public Health & Healthcare

### Dataset
1,825 daily observations across five regions.

### Analysis Focus

- Daily case activity
- Deaths and recoveries
- Active cases
- Vaccination phases
- Regional comparisons
- Monthly trends
- Correlation analysis
- Healthcare planning considerations

### Key Findings

The dataset contains:

- **391,062 total cases**
- **4,505 total deaths**
- **337,199 recoveries**
- **47.98% average vaccination level**
- **1.15% case fatality rate**
- **86.23% recovery rate**

The high-vaccination phase (60%+) recorded **56.7% lower observed daily cases** than the low-vaccination phase (0–30%).

This is an observed association within the dataset and should not be interpreted as proof of a causal vaccination effect.

Regional mortality differences are also examined, with further investigation recommended using demographic, healthcare-capacity, and other contextual variables.

### Report

`reports/04_covid_healthcare_report.pdf`

### Notebook

`notebooks/04_covid_healthcare_analysis.ipynb`

---

# 📈 Project 05 — Stock Market Risk & Return Analysis

### Domain
Finance & Quantitative Analysis

### Dataset
252 trading-day observations.

### Analysis Focus

- Price movement
- Daily returns
- Cumulative returns
- Monthly returns
- Quarterly returns
- Trading volume
- Volatility
- Maximum drawdown
- Sharpe ratio
- OHLC data validation

### Key Findings

- Period return: **+10.14%**
- Average daily return: **+0.057%**
- Median daily return: **+0.167%**
- Daily volatility: **1.944%**
- Annualized volatility: **30.87%**
- Maximum drawdown: **−26.85%**
- Sharpe ratio: **0.47** using a 0% risk-free rate
- Positive-return days: **130**
- Negative-return days: **121**

The dataset also contains **78 rows with OHLC inconsistencies**:

- 40 rows where `Open > High`
- 38 rows where `Open < Low`

The original values were preserved and documented rather than artificially corrected.

Daily Return and Cumulative Return calculations were independently validated against their expected formulas.

### Report

`reports/05_stock_market_report.pdf`

### Notebook

`notebooks/05_stock_market_analysis.ipynb`

---

# 🧪 Data Validation & Quality Assurance

Reusable validation functions are provided in:

```text
src/data_validation.py
```

The module currently provides checks for:

- Missing values
- Duplicate rows
- Dataset shape

Project-specific notebooks additionally perform analytical validation relevant to each dataset.

Examples include:

- Financial consistency checks
- Date and time validation
- Return formula validation
- Cumulative-return validation
- OHLC consistency checks
- Statistical consistency checks

Source-data anomalies are documented rather than silently modified when correction cannot be justified from the supplied data.

---

# ✅ Automated Testing

The repository includes an automated pytest test suite.

Run:

```bash
pytest
```

The current test suite contains **18 tests** covering:

- Dataset shapes
- Missing-value checks
- Duplicate-record checks
- Reusable validation functions
- Stock-market handling of expected first-row return values

Expected result:

```text
18 passed
```

The tests complement, rather than replace, the deeper analytical validation performed inside the notebooks.

---

# 📊 Visualizations

The portfolio contains **22 saved analytical visualizations** generated using Matplotlib and Seaborn.

The visualizations include multiple analytical formats such as:

- Bar charts
- Line charts
- Histograms
- Box plots
- Heatmaps
- Scatter/relationship plots
- Pie charts
- Area charts
- Return and trend visualizations

All saved visualizations are available in:

```text
visualizations/
```

---

# 📄 Analytical Reports

Each project includes a professional PDF report containing an executive summary, analytical findings, visual interpretation, recommendations, and relevant limitations.

Available reports:

```text
reports/
├── 01_supermarket_sales_report.pdf
├── 02_student_performance_report.pdf
├── 03_weather_analysis_report.pdf
├── 04_covid_healthcare_report.pdf
└── 05_stock_market_report.pdf
```

---

# 🎤 Presentation

The portfolio presentation is available in three formats:

### PowerPoint

```text
presentation/multi_domain_data_analysis_portfolio.pptx
```

### PDF

```text
presentation/multi_domain_data_analysis_portfolio.pdf
```

### Interactive HTML

```text
presentation/index.html
```

The presentation summarizes the portfolio methodology, project findings, data-quality considerations, testing approach, and practical applications.

---

# ⚖️ Data Quality Limitations & Scientific Cautions

The portfolio emphasizes transparent interpretation of analytical results.

### Supermarket Sales

The supplied `Total` field contains substantial discrepancies when compared with `Unit Price × Quantity + Tax`. The original values were retained and the issue is documented as a source-data limitation.

### Student Performance

Observed correlations between attendance, study hours, and performance are weak. The dataset does not contain enough variables to explain all observed differences in academic performance.

### Weather

The dataset contains one year of observations from a single station. It can demonstrate observed seasonal patterns but cannot establish a formal long-term climate classification.

### COVID-19

Differences between vaccination phases and regions represent observed associations in the supplied dataset. They do not establish causal relationships.

### Stock Market

The supplied dataset contains 78 OHLC inconsistencies. Original values were preserved, and the inconsistencies are documented in the analysis and report.

---

# 🔬 Analytical Methodology

Across the five projects, the portfolio applies a combination of:

- Data loading with Pandas
- Data cleaning and transformation
- Missing-value analysis
- Duplicate detection
- Descriptive statistics
- Mean and median analysis
- Correlation analysis
- Trend analysis
- Time-based aggregation
- Performance segmentation
- Return calculations
- Volatility analysis
- Drawdown analysis
- Data-quality validation
- Visualization
- Business interpretation
- Recommendation generation

The methodology is adapted to the characteristics of each domain rather than applying an identical analytical template to every dataset.

---

# 💼 Skills Demonstrated

This portfolio demonstrates practical experience in:

- Python data analysis
- Pandas
- NumPy
- Statistical analysis
- Exploratory Data Analysis (EDA)
- Data cleaning
- Data validation
- Data visualization
- Time-series analysis
- Correlation analysis
- Financial analytics
- Healthcare data analysis
- Environmental data analysis
- Educational analytics
- Retail analytics
- Automated testing with Pytest
- Technical documentation
- Analytical reporting
- Git and GitHub

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before submitting changes.

For significant analytical changes, please explain how the modification affects the analysis, results, or conclusions.

Before submitting a pull request, run:

```bash
pytest
```

---

# 📋 Changelog

Project changes and releases are documented in:

[`CHANGELOG.md`](CHANGELOG.md)

---

# 📜 License

This project is licensed under the **MIT License**.

See [`LICENSE`](LICENSE) for the complete license text.

> **Note:** The project license applies to the project's original code and documentation. It does not necessarily grant rights to third-party datasets or other externally sourced materials.

---

# 👩‍💻 Author

**Madhurja Bhattacharjee**

B.Sc. Cyber Security  
Institute of Advance Education and Research (IAER)  
MAKAUT

---

# 📌 Internship

Developed as part of the **Developers Arena Internship** project requirements.

---

# 🚀 Conclusion

> **Turning Data into Decisions**

This portfolio demonstrates an end-to-end approach to multi-domain data analysis—from data-quality validation and statistical exploration to visualization, reporting, testing, and evidence-based recommendations.

The project prioritizes reproducibility, transparent interpretation, and responsible handling of data limitations.
