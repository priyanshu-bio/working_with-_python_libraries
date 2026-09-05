import numpy as np
import pandas as pd

data = pd.read_csv("crop_yield_dataset.csv")

cropp = input("enter the crop name:- ").capitalize()
data_sorted = data.sort_values(by="Crop_Yield", ascending=False)

try:
    
    result = data_sorted[data_sorted["Crop_Type"] == cropp].reset_index(drop=True)

        
    if not result.empty:
        
        yields = result["Crop_Yield"].to_numpy()

        
   

        mean_yield = np.mean(yields)
        max_yield = np.max(yields)
        min_yield = np.min(yields)
        mean_temperature = np.mean(result["Temperature"].to_numpy())


     
        result["Performance"] = np.where(result["Crop_Yield"] >= mean_yield, "High", "Low")


        # A. sdfghjkl;iuytrsasdcvbn

        high_perf = result[result["Performance"] == "High"]


        total_npk = (high_perf["N"].to_numpy() + high_perf["P"].to_numpy() + high_perf["K"].to_numpy())
        avg_temp = np.mean(high_perf["Temperature"].to_numpy())
        avg_humidity = np.mean(high_perf["Humidity"].to_numpy())
        avg_npk = np.mean(total_npk)
       
       
       
        conditions = [
            result["Soil_pH"] < 6.0,
            (result["Soil_pH"] >= 6.0) & (result["Soil_pH"] <= 7.5),
            result["Soil_pH"] > 7.5,]

        
        choices = ["Acidic", "Optimal", "Alkaline"]
        result["pH_Status"] = np.select(conditions, choices, default="Unknown")

        
        print(f"\n------------- DATASET FOR {cropp.upper()} -------------")
        print(result.to_string(index=False))

        print(f"\n----------------****************** NUMPY ANALYTICS SUMMARY ******************----------------")
        print(f"Max Yield:     {max_yield:.2f}")
        print(f"Average Yield: {mean_yield:.2f}")
        print(f"Min Yield:     {min_yield:.2f}")
        print(f"Average Temperature: {mean_temperature:.2f} °C")


        # B hkdkefeih
       
        print(f"\n-------------****************** HIGH PERFORMANCE METRICS FOR {cropp.upper()} ******************-------------")
        print(f"Average Temperature : {avg_temp:.2f} °C")
        print(f"Average Humidity    : {avg_humidity:.2f} %")
        print(f"Average Total NPK   : {avg_npk:.2f} kg/ha")

        # C weffekmgmekgoer

        

     
        summary_data = {
            "Crop_Type": [cropp],
            "Max_Yield": [round(max_yield, 2)],
            "Average_Yield": [round(mean_yield, 2)],
            "Min_Yield": [round(min_yield, 2)],
            "High_Perf_Avg_Temp_C": [round(avg_temp, 2)],
            "High_Perf_Avg_Humidity_Pct": [round(avg_humidity, 2)],
            "High_Perf_Avg_NPK_kg_ha": [round(avg_npk, 2)],}

 
        summary_df = pd.DataFrame(summary_data)


        output_filename = f"{cropp.lower()}_summary_analytics.csv"
        summary_df.to_csv(output_filename, index=False)

        print(f"\nAnalytics summary saved to '{output_filename}' successfully!")


    else:
        print(f"{cropp} not found")

except Exception as e:
    print(f"Error: {e}")
