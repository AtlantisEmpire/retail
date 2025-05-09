import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("retail_store_inventory.csv")
print(df.head())

# Calculate the Forecast Error
df["Forecast Error"] = df["Demand Forecast"] -df ["Units Sold"]
print(df[["Demand Forecast", "Units Sold", "Forecast Error"]].head())

# Analyze Forecast Error by Weather
error_by_weather = df.groupby("Weather Condition")["Forecast Error"].mean()
print(error_by_weather)

# Overstock Loss
# Start by setting all losses to 0
df["Overstock Loss"] = 0.0
df.loc[df["Units Ordered"] > df["Units Sold"], "Overstock Loss"] = (df["Units Ordered"] - df["Units Sold"]) * df["Price"]
# Understock Loss
df["Understock Loss"] = 0.0 # Start by setting all losses to 0
df.loc[df["Units Sold"] > df["Demand Forecast"], "Understock Loss"] = (df["Units Sold"] - df["Demand Forecast"]) * df["Price"]

#Total Loss
df["Total Loss"] = df["Overstock Loss"] + df["Understock Loss"]


# Filter out non-discounted rows
discount_df = df[df["Discount"] > 0]

# Define bins that match your values
discount_df["Discount Range"] = pd.cut(discount_df["Discount"],
                                       bins=[0, 5, 10, 15, 20],
                                       labels=["1-5%", "6-10%", "11-15%", "16-20%"])

# Group by discount range
discount_impact = discount_df.groupby("Discount Range", observed=True)[["Forecast Error", "Total Loss"]].mean().round(2)

# Plotting
plt.figure(figsize=(8, 5))
sns.barplot(data=discount_df, x="Discount Range", y="Total Loss", estimator="mean", errorbar=None, color="orange")

# Set labels and title
plt.title("Average Total Loss by Discount Range")
plt.xlabel("Discount Range")
plt.ylabel("Total Loss")

# Show the plot
plt.tight_layout()
plt.show()


#Calculate and Visualize Total Loss by Category
# Group by category and sum the total loss (assuming 'Overstock Loss' and 'Understock Loss' columns exist)
df['Total Loss'] = df['Overstock Loss'] + df['Understock Loss']  # Ensure you have this column

# Group by Category and calculate average total loss per category
category_loss = df.groupby("Category")["Total Loss"].sum().round(2).reset_index()

# Sort by Total Loss for better visualization
category_loss = category_loss.sort_values("Total Loss", ascending=False)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=category_loss, x="Category", y="Total Loss", palette="viridis")
plt.title("Total Loss by Product Category")
plt.ylabel("Total Loss")
plt.xlabel("Category")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



#Calculate and Visualize Total Loss by Region
# Group by Region and calculate total loss
region_loss = df.groupby("Region")["Total Loss"].sum().round(2).reset_index()

# Sort by Total Loss
region_loss = region_loss.sort_values("Total Loss", ascending=False)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=region_loss, x="Region", y="Total Loss", palette="coolwarm")
plt.title("Total Loss by Region")
plt.ylabel("Total Loss")
plt.xlabel("Region")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



 #Calculate and Visualize Total Loss by Weather Condition
# Group by Weather Condition and calculate total loss
weather_loss = df.groupby("Weather Condition")["Total Loss"].sum().round(2).reset_index()

# Sort by Total Loss
weather_loss = weather_loss.sort_values("Total Loss", ascending=False)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=weather_loss, x="Weather Condition", y="Total Loss", palette="Blues")
plt.title("Total Loss by Weather Condition")
plt.ylabel("Total Loss")
plt.xlabel("Weather Condition")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Group by Promotion status (0 = no promotion, 1 = promotion) and calculate total loss
promo_loss = df.groupby("Holiday/Promotion")["Total Loss"].sum().round(2).reset_index()

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=promo_loss, x="Holiday/Promotion", y="Total Loss", palette="YlGnBu")
plt.title("Total Loss by Promotion Status")
plt.ylabel("Total Loss")
plt.xlabel("Promotion Status (0 = No, 1 = Yes)")
plt.tight_layout()
plt.show()
