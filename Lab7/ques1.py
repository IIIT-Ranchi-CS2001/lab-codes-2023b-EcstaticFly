

import matplotlib.pyplot as plt
import numpy as np


mp_seats = [163, 66, 0, 1]  
raj_seats = [115, 69, 2, 13]  
parties = ['BJP', 'INC', 'BSP', 'Others']
mp_percentages = [seat / sum(mp_seats) * 100 for seat in mp_seats]
raj_percentage=[seat / sum(raj_seats) * 100 for seat in raj_seats]

explode_mp=[0.1 if num==max(mp_seats) else 0 for num in mp_seats]
explode_raj=[0.1 if num==max(raj_seats) else 0 for num in raj_seats]

# mp_labels = [f"{party} ({seats}, {seats / np.sum(mp_seats) * 100:.1f}%)" for party, seats in zip(parties, mp_seats)]
# raj_labels = [f"{party} ({seats}, {seats / np.sum(raj_seats) * 100:.1f}%)" for party, seats in zip(parties, raj_seats)]


fig,axs=plt.subplots(1,2)

axs[0].pie(mp_seats,labels=parties, autopct='%1.1f%%',explode=explode_mp)
axs[0].legend(parties, loc='best')
axs[0].set_title("Madhya Pradesh Assembly Election 2023")
axs[0].text(1.1, 1, f"Highest: BJP ({mp_percentages[0]:.1f}%)", horizontalalignment='center', verticalalignment='center')

axs[1].pie(raj_seats,labels=parties, autopct='%1.1f%%', explode=explode_raj)
axs[1].legend(parties, loc='best')
axs[1].set_title("Rajasthan Assembly Election 2023")
axs[1].text(1.1, 1, f"Highest: BJP ({raj_percentage[0]:.1f}%)", horizontalalignment='center', verticalalignment='center')



# plt.show()


fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(parties, mp_seats, label="Madhya Pradesh", alpha=0.7)
ax.bar(parties, raj_seats, label="Rajasthan", alpha=0.7)
ax.set_xlabel("Parties")
ax.set_ylabel("Seats Won")
ax.set_title("Seats Won by Parties in Madhya Pradesh and Rajasthan Assembly Elections 2023")
ax.legend()
plt.tight_layout()
plt.show()