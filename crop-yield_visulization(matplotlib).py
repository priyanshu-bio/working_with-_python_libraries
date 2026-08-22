import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("crop_yield_dataset.csv")

#  2x2 grids


fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "Agricultural Data Analysis & Climate Metrics",
    fontsize=16,
    fontweight="bold")

#  Bar Chart 
avg_yield_by_crop = (
    data.groupby("Crop_Type")["Crop_Yield"].mean().sort_values(ascending=False))

axes[0, 0].bar(
                avg_yield_by_crop.index,
                avg_yield_by_crop.values,
                color="skyblue",
                edgecolor="black")

axes[0, 0].set_title("Average Yield by Crop Type", fontweight="bold")
axes[0, 0].set_xlabel("Crop Type")
axes[0, 0].set_ylabel("Mean Yield (kg/ha)")
axes[0, 0].grid(axis="y", linestyle="--", alpha=0.7)



# Scatter Plot
scatter = axes[0, 1].scatter(
                            data["Temperature"],
                            data["Crop_Yield"],
                            c=data["Humidity"],
                            cmap="viridis",
                            alpha=0.7,
                            edgecolors="k",)

axes[0, 1].set_title("Temperature vs Crop Yield (Color = Humidity)", fontweight="bold")
axes[0, 1].set_xlabel("Temperature (°C)")
axes[0, 1].set_ylabel("Crop Yield (kg/ha)")
axes[0, 1].grid(True, linestyle="--", alpha=0.5)
cbar = fig.colorbar(scatter, ax=axes[0, 1])
cbar.set_label("Humidity (%)")





# Histogram
axes[1, 0].hist(
    data["Soil_pH"], bins=15, color="coral", edgecolor="black", alpha=0.8)
axes[1, 0].axvline(
                    data["Soil_pH"].mean(),
                    color="red",
                    linestyle="dashed",
                    linewidth=1.5,
                    label=f"Mean pH: {data['Soil_pH'].mean():.2f}")
                
axes[1, 0].set_title("Distribution of Soil pH", fontweight="bold")
axes[1, 0].set_xlabel("pH Level")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].legend()
axes[1, 0].grid(axis="y", linestyle="--", alpha=0.7)




#  Boxplot 
soil_types = data["Soil_Type"].unique()
yield_by_soil = [
    data[data["Soil_Type"] == soil]["Crop_Yield"] for soil in soil_types]

axes[1, 1].boxplot(yield_by_soil, tick_labels=soil_types, patch_artist=True)
axes[1, 1].set_title("Yield Spread across Soil Types", fontweight="bold")
axes[1, 1].set_xlabel("Soil Type")
axes[1, 1].set_ylabel("Crop Yield (kg/ha)")
axes[1, 1].grid(axis="y", linestyle="--", alpha=0.7)




plt.tight_layout()




plt.savefig("crop_yield_visualizations.png", dpi=300)
print("Visualizations saved successfully as 'crop_yield_visualizations.png'")


plt.show()
