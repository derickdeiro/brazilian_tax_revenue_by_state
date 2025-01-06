# Brazilian Tax Revenue by State

This project analyzes tax revenue data across different Brazilian states.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Installation](#installation)

## Overview

This project provides an in-depth analysis of tax revenue in Brazilian states. It includes data transformations to facilitate exploration and understanding of economic behaviors at the state level.

## Features

- Comprehensive data on state-level tax revenues in Brazil.
- Analysis of revenue trends over time.
- Python scripts for data processing and output validation.

## Data Sources

- Official Brazilian government tax revenue datasets.
- State-level economic indicators and related public data.

## Requirements

- [Docker](https://www.docker.com/) installed on your machine.
- Python 3.12 or higher (if running scripts locally).
- Required Python libraries listed in `requirements.txt`.

## Installation

### Using Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/derickdeiro/brazilian_tax_revenue_by_state.git
   cd brazilian_tax_revenue_by_state
   ```
2. Build the Docker image:
   ```bash
   docker build -t brazilian_tax_revenue .
   ```
3. Run the Docker container:
   ```bash
   docker run -d brazilian_tax_revenue
   ```

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/derickdeiro/brazilian_tax_revenue_by_state.git
   cd brazilian_tax_revenue_by_state
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git push origin feature-name
   ```
4. Open a pull request.
