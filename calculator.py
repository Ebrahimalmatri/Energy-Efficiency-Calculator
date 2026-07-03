def calculate_dewa_bill(kwh):
    cost = 0
    
    if kwh <= 2000:
        cost = kwh * 0.230
    elif kwh <= 4000:
        cost = (2000 * 0.230) + ((kwh - 2000) * 0.280)
    elif kwh <= 6000:
        cost = (2000 * 0.230) + (2000 * 0.280) + ((kwh - 4000) * 0.320)
    else:
        cost = (2000 * 0.230) + (2000 * 0.280) + (2000 * 0.320) + ((kwh - 6000) * 0.380)
        
    fuel_surcharge = kwh * 0.060
    total_before_vat = cost + fuel_surcharge
    vat = total_before_vat * 0.05
    final_bill = total_before_vat + vat
    
    return final_bill, cost, fuel_surcharge, vat

print("--- DEWA Electricity Bill Calculator ---")
try:
    consumption = float(input("Enter monthly consumption in kWh: "))
    
    final_total, base_cost, fuel, vat_amount = calculate_dewa_bill(consumption)
    
    print("\n--- Bill Details ---")
    print(f"Base Consumption Cost: {base_cost:.2f} AED")
    print(f"Fuel Surcharge:        {fuel:.2f} AED")
    print(f"VAT (5%):              {vat_amount:.2f} AED")
    print("-" * 30)
    print(f"Total Final Bill:      {final_total:.2f} AED")
    
except ValueError:
    print("Invalid input. Please enter numeric values only.")
