import numpy as np
transactions =np.array([
[1200,1500,1600,1800,2000,2200],
[1000,1100,1200,1300,1400,1500],
[2000,2100,2200,2300,2400,2500],
[1700,1600,1500,1400,1300,1200]
])
print("Transaction volumes:\n",transactions)
totals_per_branch=transactions.sum(axis=1)
print("Total per branch:",totals_per_branch)
highest_branch=np.argmax(totals_per_branch)
+1
print("Branch with higher transactions:Branch",highest_branch)
avg_monthly= transactions.mean()
print("Average monthly volume:",avg_monthly)
reshaped= transactions.reshaped(3,8)
print("Reshaped 3*8 array:\n",reshaped)