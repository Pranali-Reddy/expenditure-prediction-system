# Expenditure Prediction System

## Overview
The **Expenditure Prediction System** is a data-driven personal finance application built with Django. It focuses on helping users manage their daily finances by providing automated categorization and predictive insights into future spending patterns using Machine Learning.

## Core Capabilities
- **Predictive Analytics**: Utilizes historical data to forecast upcoming expenses, helping users plan their budgets more effectively.
- **Automated Categorization**: Employs a Random Forest Classifier to automatically assign categories to expenses based on their descriptions.
- **Financial Tracking**: Unified management of both income and expenses with detailed history and search capabilities.
- **Goal Management**: Allows users to set specific savings goals, track their progress, and receive automated progress updates.
- **Visual Reporting**: Generates summaries and charts to provide a clear picture of financial health.

## Technical Stack
- **Backend**: Django (Python)
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **NLP**: NLTK (Natural Language Toolkit)
- **Frontend**: Bootstrap, Chart.js
- **Database**: SQLite (default for development)

## Setup and Installation

1. **Clone the Project**:
   ```bash
   git clone https://github.com/Pranali-Reddy/expenditure-prediction-system.git
   ```

2. **Environment Configuration**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Dependency Management**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize System**:
   ```bash
   python manage.py migrate
   ```

5. **Start Application**:
   ```bash
   python manage.py runserver
   ```

## Development and Contributions
This system was developed as a specialized tool for expenditure forecasting. It is designed to be extensible, allowing for the addition of more complex prediction models and financial instruments in the future.
