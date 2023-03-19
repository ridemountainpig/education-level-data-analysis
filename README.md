# Education Level Data Analysis

This repository contains code and data for an analysis of the relationship between education levels, unemployment rates, and credit card spending in Taiwan's six major cities: Taipei, New Taipei, Taoyuan, Taichung, Tainan, and Kaohsiung.

The data used in this analysis was obtained from [Taiwan Government Open Data Platform](https://data.gov.tw), and was processed using the Python libraries Pandas and Matplotlib. Specifically, the [main.ipynb](https://github.com/ridemountainpig/education-level-data-analysis/blob/main/main.ipynb) Jupyter Notebook file contains the code used to clean and analyze the data, and the data folder contains the raw and processed data files.

# Data Description
The dataset used in this analysis includes the following variables:

- city: The name of the city.
- education_level: The education level of the population, categorized as "College and above", "High school", or "Junior high school and below".
- unemployment_rate: The unemployment rate in the city, categorized as "College and above", "High school", or "Junior high school and below".
- credit_card_spending: The average monthly credit card spending per each education level in the city.

The dataset covers the period from 2015 to 2019.

# Analysis Results

<div align="center">
  <img src="https://github.com/ridemountainpig/education-level-data-analysis/blob/main/images/creditAmountSenior.png"/>
</div>
<div align="center">
    <b>High school education level credit card consumption</b>
</div>

<div align="center">
  <img src="https://github.com/ridemountainpig/education-level-data-analysis/blob/main/images/creditAmountUniversity.png"/>
</div>
<div align="center">
    <b>College education level or above credit card consumption</b>
</div>

<div align="center">
  <img src="https://github.com/ridemountainpig/education-level-data-analysis/blob/main/images/umploymentRateSenior.png"/>
</div>
<div align="center">
    <b>High School Education unemployment Rate</b>
</div>

<div align="center">
  <img src="https://github.com/ridemountainpig/education-level-data-analysis/blob/main/images/umploymentRateUniversity.png"/>
</div>
<div align="center">
    <b>College education or above unemployment Rate</b>
</div>

1. Education Level and Unemployment Rate Relationship

    Based on the data, there appears to be a slight negative relationship between education level and unemployment rate in the six major cities in Taiwan. In general, cities with higher percentages of individuals with college degrees or above tend to have lower unemployment rates, while cities with higher percentages of individuals with only high school or vocational school degrees tend to have higher unemployment rates.

2. Education Level and Credit Card Spending Relationship

    There also appears to be a positive relationship between education level and credit card spending in the six major cities. Cities with higher percentages of individuals with college degrees or above tend to have higher credit card transaction amounts, while cities with higher percentages of individuals with only high school or vocational school degrees tend to have lower credit card transaction amounts.

3. Regional Differences in Education Level and Unemployment Rate/Credit Card Spending

    There are also notable regional differences in the relationship between education level and unemployment rate/credit card spending. For example, in Taipei City, there is a strong negative relationship between education level and unemployment rate, but a weaker positive relationship between education level and credit card spending. In contrast, in Kaohsiung City, there is a weaker negative relationship between education level and unemployment rate, but a stronger positive relationship between education level and credit card spending. These regional differences could be attributed to various factors, such as differences in economic development, industries, and demographic characteristics.

    Overall, this dataset provides interesting insights into the relationship between education level, unemployment rate, and credit card spending in different regions of Taiwan.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ridemountainpig/education-level-data-analysis/blob/main/LICENSE) file for details.
