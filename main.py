#  INF601 - Advanced Programming in Python
#  Fernando Duffoo
#  Mini Project 2

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data into a Pandas DataFrame
drugs = pd.read_csv("drug-overdose-death-rates new.csv", parse_dates=True)

# Set 'Year' column as the index
drugs['Year'] = pd.to_datetime(drugs['Year'])
drugs.set_index('Year', inplace=True)

# Check the data types and date range
print(drugs.index)
print(drugs.index.min(), drugs.index.max())
# Check the structure of your DataFrame
print(drugs.head())

# Create 'charts' folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Plotting the overall drug overdose death rates as a bar chart
plt.figure(figsize=(12, 6))
for column in drugs.columns:
    plt.bar(drugs.index, drugs[column], label=column, alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Overall Drug Overdose Death Rates in the US')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to separate the two graphs
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the overall plot as a PNG file inside the 'charts' folder
plt.savefig('charts/overall_drug_overdose_death_rates.png')

# Show the overall plot
plt.show()

#--------------------------------------------------------------------------------------------------------------

# Plotting deaths from cocaine overdose only as a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(drugs.index, drugs['Cocaine overdose death rates (CDC WONDER)'], label='Cocaine', s=50, alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Cocaine Overdose Death Rates in the US')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to mark the separation
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the cocaine plot as a PNG file inside the 'charts' folder
plt.savefig('charts/cocaine_overdose_death_rates.png')

# Show the cocaine plot
plt.show()

#--------------------------------------------------------------------------------------------------------------

# Plotting deaths from opioid overdose only as a box plot
plt.figure(figsize=(12, 6))
plt.boxplot(drugs['Any opioid death rates (CDC WONDER)'])

# Adding labels and legend
plt.xlabel('Opioid Overdose Death Rates')
plt.title('Opioid Overdose Death Rates in the US')

# Save the opioid plot as a PNG file inside the 'charts' folder
plt.savefig('charts/opioid_overdose_death_rates.png')

# Show the opioid plot
plt.show()

#--------------------------------------------------------------------------------------------------------------

# Plotting deaths from heroin overdose only as a line plot
plt.figure(figsize=(12, 6))
plt.plot(drugs.index, drugs['Heroin overdose death rates (CDC WONDER)'], label='Heroin', linestyle='-', marker='o', markersize=5, alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Heroin Overdose Death Rates in the US')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to mark the separation
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the heroin plot as a PNG file inside the 'charts' folder
plt.savefig('charts/heroin_overdose_death_rates.png')

# Show the heroin plot
plt.show()

#--------------------------------------------------------------------------------------------------------------

# Plotting deaths from synthetic drug overdoses as a step plot
plt.figure(figsize=(12, 6))
plt.step(drugs.index, drugs['Synthetic opioids death rates (CDC WONDER)'], label='Synthetic', where='post', linestyle='-', marker='o', markersize=5, alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Synthetic Drug Overdose Death Rates in the US')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to mark the separation
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the synthetic plot as a PNG file inside the 'charts' folder
plt.savefig('charts/synthetic_overdose_death_rates.png')

# Show the synthetic plot
plt.show()

#--------------------------------------------------------------------------------------------------------------

# Plotting deaths from prescription drug overdoses as a filled area plot
plt.figure(figsize=(12, 6))
plt.fill_between(drugs.index, 0, drugs['Prescription Opioids death rates (US CDC WONDER)'], label='Prescription', alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Prescription Drug Overdose Death Rates in the US')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to mark the separation
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the prescription plot as a PNG file inside the 'charts' folder
plt.savefig('charts/prescription_overdose_death_rates.png')

# Show the prescription plot
plt.show()