# Contributing

Thank you for your interest in contributing to the Multi-Domain Data Analysis Portfolio.

This repository is primarily an internship portfolio demonstrating data cleaning, statistical analysis, visualization, validation, and business insight generation across five domains. Suggestions, improvements, and educational contributions are welcome.

## How to Contribute

Fork the repository.

Create a feature branch:

git checkout -b feature/your-change

Make your changes while keeping the existing project structure intact.

If you modify analysis logic, update the relevant notebook and documentation.

Run the test suite:

pytest

Verify that the notebooks and generated artifacts remain consistent with the documented results.

Commit your changes with a clear message.

Open a pull request describing what was changed and why.

## Guidelines

Preserve the original source data unless a documented transformation is part of the analysis.

Do not introduce unsupported statistical or causal claims.

Document important data-quality limitations and analytical assumptions.

Keep visualizations clearly labelled with appropriate units and titles.

Add or update tests when reusable validation logic is changed.

Do not commit API keys, passwords, credentials, or other secrets.

Avoid committing generated caches such as __pycache__ or .pytest_cache.

## Reporting Issues

For bugs, incorrect calculations, documentation problems, or reproducibility issues, please open an issue with:

A clear description of the problem

Steps to reproduce it

The affected project/notebook

Relevant error messages or screenshots, if applicable

## Pull Requests

Pull requests should include a concise description of the changes and should pass the available automated tests before submission.

For substantial analytical changes, please explain how the change affects the reported results or conclusions.