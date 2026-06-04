from django.shortcuts import render
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from django.utils.timezone import now
from expenses.models import Expense
from django.contrib import messages
import matplotlib.pyplot as plt
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')
def forecast(request):
    expenses = Expense.objects.filter(owner=request.user).order_by('-date')[:30]

    if len(expenses) < 10:
        messages.error(request, "Not enough expenses to make a forecast. Please add more expenses.")
        return render(request, 'expense_forecast/index.html')

    # Build DataFrame
    data = pd.DataFrame({
        'Date': [e.date for e in expenses],
        'Expenses': [e.amount for e in expenses],
        'Category': [e.category for e in expenses]
    })
    data.set_index('Date', inplace=True)

    # Fill missing categories so groupby never fails
    data['Category'] = data['Category'].fillna('Uncategorized')

    # Forecasting
    model = ARIMA(data['Expenses'], order=(5, 1, 0))
    model_fit = model.fit()
    steps = 30
    next_day = now().date() + pd.DateOffset(days=1)
    idx = pd.date_range(start=next_day, periods=steps, freq='D')
    forecast = model_fit.forecast(steps=steps)

    # Prepare data for template
    forecast_df = pd.DataFrame({'Date': idx, 'Forecasted_Expenses': forecast})
    forecast_list = forecast_df.reset_index().to_dict(orient='records')
    total = np.sum(forecast)

    # **Here’s the new, safe grouping:**
    category_forecasts = data.groupby('Category')['Expenses'].sum().to_dict()

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Expenses'], label='Previous')
    plt.plot(idx, forecast, label='Forecast', color='red')
    plt.xlabel('Date'); plt.ylabel('Expenses')
    plt.title('30-Day Expense Forecast'); plt.legend()
    plot_file = 'static/img/forecast_plot.png'
    plt.savefig(plot_file); plt.close()

    context = {
        'forecast_data': forecast_list,
        'total_forecasted_expenses': total,
        'category_forecasts': category_forecasts,
        'plot_file': plot_file,
    }
    return render(request, 'expense_forecast/index.html', context)
