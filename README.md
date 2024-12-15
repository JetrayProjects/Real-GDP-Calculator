# Real GDP Calculator and Visualizer

This script calculates and visualizes the Real GDP of a country over the years based on the GDP deflator and nominal GDP values.

## Features

- Reads and processes GDP Deflator and Nominal GDP data from CSV files.
- Filters and cleans data to ensure consistency between datasets.
- Allows user selection of a country for Real GDP calculation.
- Calculates Real GDP for the years 2010-2020 (or other specified years).
- Generates a bar chart comparing Real GDP and Nominal GDP values.

## Prerequisites

- Python 3.x
- Required libraries:
  - pandas
  - matplotlib

Install the required libraries using:
```bash
pip install pandas matplotlib
```

## Input Files

1. **GDP_deflator.csv**:
   - Contains GDP deflator values by country and year.
   - Expected columns: `Country Name`, `Country Code`, `2010`, `2011`, ..., `2020`.

2. **NominalGDP.csv**:
   - Contains nominal GDP values by country and year.
   - Expected columns: `Country Name`, `Country Code`, `2010`, `2011`, ..., `2020`.

## How to Use

1. Place the `GDP_deflator.csv` and `NominalGDP.csv` files in the same directory as the script.

2. Run the script:
   ```bash
   python script.py
   ```

3. Follow the prompts to select a country for Real GDP calculation.

4. View the calculated Real GDP and Nominal GDP values in the console and a bar chart.

## Code Highlights

### Data Cleaning and Filtering
- Rows with missing values (`NaN`) are removed.
- Indexes are reset to ensure alignment between datasets.

### User Interaction
- The user selects a country by index from a displayed list of country names.

### Calculation of Real GDP
- Formula used:
  ```
  Real GDP = (Nominal GDP / GDP Deflator) * 100
  ```

### Visualization
- A bar plot is generated to compare Real GDP and Nominal GDP values over the years.

## Example Output

### Console Output:
```
Enter the index(number) of the country's Real GDP you would like to calculate: 42
You have selected 42 Country Name: Example Country
Your real GDP values are:
2010    12345.67
2011    13000.00
...

Real GDP and Nominal GDP values together are:
   Real GDP values  Nominal GDP values
2010         12345              14000
2011         13000              15000
...
```

### Bar Chart:
- A bar chart comparing Real GDP and Nominal GDP values from 2010 to 2020.

## Notes

- Ensure the input CSV files match the expected format and column names.
- You can modify the years by adjusting the `usecols` parameter in the `pd.read_csv()` calls.

## License

This project is licensed under the MIT License. Feel free to use and modify the script for educational or personal projects.
