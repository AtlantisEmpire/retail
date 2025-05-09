# Retail Store Loss Channel Analysis

## Description

This project investigates the various factors contributing to financial losses within a retail store by analyzing inventory, sales, and forecasting data. The analysis aims to identify key drivers of loss related to promotions, discount strategies, geographical regions, product categories, and weather conditions. The insights gained from this analysis can be used to inform strategies for loss mitigation and improve overall profitability.

## Data Source

The dataset used for this analysis was obtained from Kaggle.

## Tools Used

* Python: 
      Pandas,
      Matplotlib,
      Seaborn
  
## Methodology

The analysis involved the following steps:

1.  **Data Loading and Initial Exploration:** The retail store inventory dataset was loaded into a Pandas DataFrame. Initial exploration involved examining the structure of the data, data types, and identifying relevant columns for the analysis.

2.  **Loss Calculation:**
    * **Overstock Loss:** Calculated as the cost of unsold units when the number of units ordered exceeded the units sold: $\text{Overstock Loss} = (\text{Units Ordered} - \text{Units Sold}) \times \text{Price}$, where $\text{Units Ordered} > \text{Units Sold}$.
    * **Understock Loss:** Calculated as the potential revenue lost due to unmet demand when the number of units sold exceeded the demand forecast: $\text{Understock Loss} = (\text{Units Sold} - \text{Demand Forecast}) \times \text{Price}$, where $\text{Units Sold} > \text{Demand Forecast}$.
    * **Total Loss:** The sum of Overstock Loss and Understock Loss: $\text{Total Loss} = \text{Overstock Loss} + \text{Understock Loss}$.

3.  **Analysis of Promotion Impact:** The dataset was grouped by the 'Holiday/Promotion' status (0 for no promotion, 1 for promotion) to compare the average 'Forecast Error' (absolute difference between 'Units Sold' and 'Demand Forecast') and the average 'Total Loss' during promotional and non-promotional periods.

4.  **Analysis of Discount Range Impact:** Rows with discounts greater than 0 were filtered, and a new categorical variable 'Discount Range' was created to group discounts into 1-5%, 6-10%, 11-15%, and 16-20% ranges. The average 'Total Loss' for each discount range was then calculated and visualized.

5.  **Analysis of Loss by Region, Product Category, and Weather Condition:** The 'Total Loss' was aggregated by 'Region', 'Category', and 'Weather Condition' to identify which regions, product categories, and weather conditions were associated with the highest total losses. The results were visualized using bar plots to facilitate comparison.

## Results

The key findings from the analysis are:

* **Promotion Impact on Forecast Error & Total Loss:**
    * There was no significant difference in average forecast error between periods with and without promotions.
    * The average total loss was slightly higher during promotional periods compared to non-promotional periods.

* **Discount Range Impact on Total Loss:**
    * The average total loss showed minimal variation across the different discount ranges (1-5%, 6-10%, 11-15%, 16-20%), with losses remaining relatively high across all ranges.

* **Loss by Region:**
    * The **East region** experienced the highest total financial loss.

* **Loss by Product Category:**
    * The **Electronics** and **Furniture** categories contributed the most to the total financial loss.

* **Loss by Weather Condition:**
    * **Snowy** weather conditions were associated with the highest total financial loss, followed by **Rainy** and then **Cloudy** conditions.

## Recommendations

Based on the analysis, the following recommendations are suggested:

1.  **Improve Demand Forecasting:** Given that promotions do not improve forecast accuracy and can lead to higher losses, there is a need to refine the demand forecasting models. Incorporating factors such as promotional activities, seasonality, weather conditions, and regional trends more effectively could lead to better predictions.

2.  **Re-evaluate Promotion Strategy:** The slight increase in total loss during promotions suggests that the current promotional strategies might not be optimally balanced against potential losses from overstocking or understocking. A review of promotion planning, including the depth of discounts and inventory management during these periods, is recommended.

3.  **Optimize Discount Strategy:** The consistent high losses across all discount ranges indicate that the current discount strategy is not effectively driving loss reduction. Experimenting with different discount levels, targeting specific products or regions, or implementing dynamic pricing strategies could be beneficial.

4.  **Investigate High-Loss Areas:** Further investigation is needed to understand the specific factors contributing to higher losses in the East region and within the Electronics and Furniture categories. This could involve analyzing sales patterns, inventory management practices, and regional demand variations.

5.  **Consider Weather Impact on Inventory and Sales:** The correlation between weather conditions and losses, particularly the high losses during snowy weather, suggests that weather patterns should be considered in inventory planning and potentially in localized promotional activities.

This analysis provides a foundational understanding of the loss channels within the retail store. Further in-depth analysis and potentially the incorporation of other relevant data could provide even more granular and actionable insights.
