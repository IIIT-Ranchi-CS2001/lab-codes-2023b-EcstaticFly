import numpy as np
import matplotlib.pyplot as plt

data=np.array([
    [1500, 2000, 1800, 1200, 900],
    [1600, 2100, 1900, 1300, 950],
    [1700, 2200, 2000, 1400, 1000],
    [1650, 2150, 1950, 1350, 980],
    [1750, 2250, 2050, 1450, 1020],
    [1800, 2300, 2100, 1500, 1050], 
    [1900, 2400, 2200, 1600, 1100],
    
])

days=["Sunday","Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday"]
countries=["Country_A","Country_B","Country_C","Country_D","Country_E",]

# 1.a.
case_register_each_country=[sum(row[col] for row in data) for col in range(len(data[0]))]
print(case_register_each_country)

# 1.b
highest_case_country_value=max(case_register_each_country)
highest_case_country=np.argmax(case_register_each_country)
print(countries[highest_case_country])
# np.argmax

# 2.a.
case_register_each_day=[sum(row) for row in data]
print(case_register_each_day)

#2.b.
average_case_register_per_day_country=[num/7 for num in case_register_each_day]
# print(average_case_register_per_day_country)

max_case_day=np.argmax(case_register_each_day)
print(f"Day {max_case_day}")

# 3.a.
percentage_inc_dec_country=np.diff(case_register_each_country) / case_register_each_country[:-1] * 100
print(percentage_inc_dec_country)


#3.b. 
max_percent_inc=np.argmax(percentage_inc_dec_country)
print(f"Country_{max_percent_inc+1}")


# 4.a.
normalized_data = (case_register_each_country - np.min(case_register_each_country,  keepdims=True)) / (np.max(case_register_each_country, keepdims=True) - np.min(case_register_each_country, keepdims=True))

print("Normalized Data:\n", normalized_data)

# 4.b.
plt.bar(normalized_data,countries,width=0.3)
plt.show()


# 5.a.
plt.bar(countries,case_register_each_country)
plt.show()

# 5.b.
color = ['red' if i == highest_case_country_value else 'blue' for i in case_register_each_country]
plt.bar(countries,case_register_each_country,color=color)
plt.show()