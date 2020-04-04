import pandas as pd

# adoptions by month/year
monthly_adoption_data = pd.read_csv('data/monthly_adoption.csv')
monthly_adoption_data = monthly_adoption_data[monthly_adoption_data['Outcome'] == 'Adoption']
monthly_adoption_data = monthly_adoption_data[monthly_adoption_data['Date'] != '2018-04']
by_date = monthly_adoption_data.groupby('Date')['Outcome'].count()
x_monthly_adoption = by_date.index
y_monthly_adoption = by_date.values

# intakes by month/year
monthly_intake_data = pd.read_csv('data/monthly_intake.csv')
intake_by_date = monthly_intake_data.groupby('Date')['Intake'].count()
x_monthly_intake = intake_by_date.index
y_monthly_intake = intake_by_date.values
