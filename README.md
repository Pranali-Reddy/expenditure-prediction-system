# SmartSpend AI - Intelligent Expense Management

## Overview
SmartSpend AI is a modern personal finance management application built with Django. It empowers users to take control of their financial health through intelligent expense logging, automated categorization using Machine Learning, and predictive analytics for future spending patterns.

## Key Features
- **AI-Powered Categorization**: Uses advanced Natural Language Processing to automatically categorize your expenses based on descriptions.
- **Financial Forecasting**: Predicts future expenses based on historical spending trends to help with proactive budgeting.
- **Comprehensive Tracking**: Log income, expenses, and savings goals in one unified dashboard.
- **Visual Analytics**: Interactive charts and summaries for better financial insights.
- **Secure Authentication**: Robust user management and data privacy.

## Getting Started

1. **Clone the Project**:
   ```bash
   git clone https://github.com/Pranali-Reddy/expenditure-prediction-system.git
   ```

2. **Environment Setup**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Initialization**:
   ```bash
   python manage.py migrate
   ```

5. **Run the App**:
   ```bash
   python manage.py runserver
   ```

Access your smart financial assistant at `http://localhost:8000`.
