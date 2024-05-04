import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

# Read .csv file and include columns only from 2010~2022
# You can change the number of years based on what you prefer
df = pd.read_csv("GDP_deflator.csv", header=0,
                 usecols=["Country Name", "Country Code", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                          "2017", "2018", "2019", "2020"])
df2 = pd.read_csv("NominalGDP.csv", header=2,
                  usecols=["Country Name", "Country Code", "2010", "2011", "2012", "2013", "2014", "2015", "2016",
                           "2017", "2018", "2019", "2020"])

# Remove rows with NaN values
df = df.dropna()
df2 = df2.dropna()

# Rearrange the indexes
df = df.reset_index(drop=True)
df2 = df2.reset_index(drop=True)

# Make sure the number of countries and the countries for both the dataframes is same
# Clean the data of df2 to match the data available in df
for i, c in df2["Country Code"].items():
    drop = False
    for i1, c1 in df["Country Code"].items():
        if c == c1:
            break
        elif i1 == (len(df) - 1):
            drop = True
    if drop:
        df2.drop(index=i, inplace=True)

df2 = df2.reset_index(drop=True)

# Accept user input for country of which Real GDP is to be calculated
def select_country(ser):
    # Print the Country Name and index
    print(ser)
    # Accept index of the selected country
    country_code = input("Enter the index(number) of the country's Real GDP you would like to calculate: ")
    # Print the index and country selected by user
    print("You have selected " + country_code + " Country Name: " + df.at[int(country_code), 'Country Name'])
    # Return the index
    return country_code


# Find the index in df2 that corresponds to the country in df
def find_index_for_nominalGDP(ccode):
    for i, c in df2["Country Code"].items():
        if c == df.at[int(ccode), 'Country Code']:
            return i

ser = df["Country Name"]
# Pass the series with country names to select_country function
ccode = select_country(ser)

# Store the index of ccode in a variable
index_in_NGDP = find_index_for_nominalGDP(ccode)

country_name = df2.at[int(index_in_NGDP), 'Country Name']

# Create 2 series
# GDP Deflator value series
de = df.loc[int(ccode)]

# Nominal GDP value series
nom = df2.loc[index_in_NGDP]

# Create a copy of the series
de_copy = de.copy()
nom_copy = nom.copy()

# Drop labels 'Country Name' and 'Country Code'
de_copy.drop(labels=['Country Name', 'Country Code'], inplace=True)
nom_copy.drop(labels=['Country Name', 'Country Code'], inplace=True)

# Loop to calculate Real GDP and store all the values in a list
# real_GDP: a list to store the values calculated
real_GDP = []
for i, c in de_copy.items():
    calculate = (nom_copy.loc[i] / de_copy.loc[i]) * 100
    real_GDP.append(calculate)

# Create a copy of the index values
index_for_real = de_copy.index

# Convert the list real_GDP into a series realGDP with the years [2010...2020] as index
realGDP = pd.Series(data=real_GDP, index=index_for_real)

# Print the series
print("Your real GDP values are: \n")
print(realGDP)

# Combine the values in a dataframe
combined = pd.DataFrame({
    'Real GDP values': realGDP,
    'Nominal GDP values': nom_copy
})

# Print the combines values
print("Real GDP and Nominal GDP values together are: \n")
print(combined)

# Now we want to graph both the real GDP value and Nominal GDP value of the country_name selected
# Bar plot
combined.plot.bar()
plt.xlabel('Years')
plt.ylabel('Values($)')
plt.title(country_name)

plt.show()
