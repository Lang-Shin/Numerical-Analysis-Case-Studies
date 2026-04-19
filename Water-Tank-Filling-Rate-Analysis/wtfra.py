import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Water-Tank-Filling-Rate-Analysis/data.csv")

def flow_rate(df, time):
    """
        Gets the flow rate 
    """

    y1 = df.loc[df['time'] == time+2, 'volume'].iloc[0]
    y2 = df.loc[df['time'] == time-2, 'volume'].iloc[0]

    p = (y1 - y2) / 4

    return p

def total_volume(df):
    """Get the total volume accumulated"""

    return (
        np.trapz(df['volume'], df['time'])
    )


frate2 = flow_rate(df, 2)
frate4 = flow_rate(df, 4)
frate6 = flow_rate(df, 6)
frate8 = flow_rate(df, 8)

volume_accumulated = total_volume(df)

print(f"total acccumulated volume: {volume_accumulated}")

print("\n\n", "Flow Rate")
print("Flow Rate of 2 : ", frate2)
print("Flow Rate of 4 : ",frate4)
print("Flow Rate of 6 : ",frate6)
print("Flow Rate of 8 : ",frate8)

# VISUALIZATION
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
axes[0].plot(df['time'], df['volume'], marker='o', color="#2C7B0A")
axes[0].set_xticks(df['time'])
axes[0].grid(True, alpha=0.6, linestyle='-', animated=True)
axes[0].set_title("Volume vs Time", fontweight="bold")
axes[0].set_xlabel("Time", fontweight="bold")
axes[0].set_ylabel("Volume", fontweight="bold")

times = np.array([2, 4, 6, 8])
frates = np.array([frate2, frate4, frate6, frate8])
axes[1].plot(times, frates, marker='o', color="#2C7B0A")
axes[1].set_xticks(times)
axes[1].grid(True, alpha=0.6, linestyle='-')
axes[1].set_title("Flow Rate vs Time", fontweight="bold")
axes[1].set_xlabel("Time", fontweight="bold")
axes[1].set_ylabel("Flow Rate", fontweight="bold")

plt.tight_layout()
plt.show()
