#  INF601 - Advanced Programming in Python
#  Fernando Duffoo
#  Mini Project 2

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data into a Pandas DataFrame
drugs = pd.read_csv("drug-overdose-death-rates new.csv", parse_dates=['Year'])

# Set 'Year' column as the index
drugs.set_index('Year', inplace=True)

# Check the data types and date range
print(drugs.index)
print(drugs.index.min(), drugs.index.max())
# Check the structure of your DataFrame
print(drugs.head())

# Create 'charts' folder if it doesn't exist
os.makedirs('charts', exist_ok=True)

# Exclude rows
entities_and_codes_to_exclude = [('Entity1', 'Code1'), ('Entity2', 'Code2')]

# Filtering
filtered_drugs = drugs[~drugs['Entity'].isin([e[0] for e in entities_and_codes_to_exclude]) &
                       ~drugs['Code'].isin([e[1] for e in entities_and_codes_to_exclude])]

# Exclude 'Entity' and 'Code' columns from the DataFrame
filtered_drugs = filtered_drugs.drop(['Entity', 'Code'], axis=1)

# Plotting the overall drug overdose death rates on the y-axis
plt.figure(figsize=(12, 6))
for column in filtered_drugs.columns:
    plt.plot(filtered_drugs.index, filtered_drugs[column], label=column, marker='o', linestyle='-', alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates (log scale)')
plt.title('Overall Drug Overdose Death Rates in the US (1999-2020)')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Add a horizontal line to separate the two graphs
plt.axvline(x=filtered_drugs.index[-1], color='red', linestyle='--', label='Separation Line')

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
plt.title('Cocaine Overdose Death Rates in the US (1999-2020)')
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

# Plotting deaths from opioid overdose only as a bar chart with annotations
plt.figure(figsize=(12, 6))
bars = plt.bar(drugs.index, drugs['Any opioid death rates (CDC WONDER)'], label='Opioid', alpha=0.7)

# Adding labels and legend
plt.xlabel('Date')
plt.ylabel('Death Rates')
plt.title('Opioid Overdose Death Rates in the US (1999-2020)')
plt.legend()

# Adding annotations to display the exact values on the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

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
plt.title('Heroin Overdose Death Rates in the US (1999-2020)')
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
plt.title('Synthetic Drug Overdose Death Rates in the US (1999-2020)')
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
plt.title('Prescription Drug Overdose Death Rates in the US (1999-2020)')
plt.legend()

# Formatting date on x-axis
plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))

# Add a horizontal line to mark the separation
plt.axvline(x=drugs.index[-1], color='red', linestyle='--', label='Separation Line')

# Save the prescription plot as a PNG file inside the 'charts' folder
plt.savefig('charts/prescription_overdose_death_rates.png')

# Show the prescription plot
plt.show()