# Portfolio Presentation Guide

## Overview
This document provides a complete guide to the 12-slide presentation for the Developers Arena internship project:
**“Multi-Domain Data Analysis Portfolio – 5 Real Projects”** by **Madhurja Bhattacharjee**.

---

## Deliverables & Usage

### 1. PowerPoint Deck (`presentation/multi_domain_data_analysis_portfolio.pptx`)
- **Format:** Microsoft PowerPoint (.pptx), 16:9 Widescreen (13.333" × 7.5").
- **Theme:** Clean modern data-analytics palette (Deep Navy `#0F172A`, Slate `#334155`, Brand Teal `#0D9488`, Blue `#0284C7`, Off-white `#F8FAFC`).
- **Visuals:** Embedded high-resolution PNG charts from `visualizations/`.
- **Audience:** Executive presentation, hiring reviews, technical portfolio evaluation.

### 2. Interactive HTML Deck (`presentation/index.html`)
- **Format:** Standalone HTML/CSS/JS file.
- **Controls:** Arrow keys (Left/Right), Space, PageUp/PageDown, Home/End.
- **Features:** Control bar, slide counter, full-screen toggle, and print-to-PDF stylesheet (`Ctrl+P`).
- **Access:** Double-click `presentation/index.html` to open directly in any web browser.

### 3. Landscape PDF Deck (`presentation/multi_domain_data_analysis_portfolio.pdf`)
- **Format:** Landscape A4 PDF (297mm × 210mm) generated with FPDF2.
- **Features:** Standalone, self-contained document ready for sharing or printing.

---

## 12-Slide Outline & Key Verified Data Points

| Slide | Topic | Primary Metrics & Focus | Embedded Visuals |
| :---: | :--- | :--- | :--- |
| **01** | Title | Portfolio Title, Author: Madhurja Bhattacharjee, Developers Arena | Custom Domain Cards |
| **02** | Methodology | 7-stage pipeline (Ingestion to Decisions), Python stack, statistical tools | Workflow Banner |
| **03** | Project 01: Supermarket | ₹519k rev, ₹259.64 avg basket, afternoon peak (42.2%), financial check limit | `02_branch_performance`, `01_time_period_distribution` |
| **04** | Project 02: Student Performance | 74.38 avg score, weak r=0.077/0.096 correlations, avoiding innate ability | `07_grade_distribution`, `09_subject_performance_heatmap` |
| **05** | Project 03: Weather Analysis | 2,448 mm rain, 65% monsoon concentration in 77 days, single-station limit | `11_temperature_trend`, `12_monthly_rainfall` |
| **06** | Project 04: COVID Trends | 391k cases, 56.7% drop in high-vax phase, Central 42.1% excess mortality, correlation vs causation | `15_covid_cases_by_region`, `16_vaccination_vs_cases` |
| **07** | Project 05: Stock Market | +10.14% return, 30.87% vol, -26.85% drawdown, Sharpe 0.47 (Rf=0%), 78 OHLC limits | `19_stock_price_trend`, `21_cumulative_returns` |
| **08** | Cross-Domain Synthesis | Comparative matrix across 5 domains, common analytical rigor | Cross-Domain Matrix |
| **09** | Quality & Testing | `src/data_validation.py`, dimensions, null/duplicate checks, **18 pytest tests passed** | Test Success Banner |
| **10** | Business Recommendations | Testable operational actions & target KPIs across all 5 projects | Action & KPI Cards |
| **11** | Technical Architecture | Python, Pandas, NumPy, SciPy, Matplotlib, Seaborn, FPDF2, Pytest, repo tree | Full Repository Tree |
| **12** | Conclusion | 6 core data capabilities, motto: *“Turning Data into Decisions”* | Competency Grid |
