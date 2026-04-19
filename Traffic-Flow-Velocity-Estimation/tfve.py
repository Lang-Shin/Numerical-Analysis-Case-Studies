import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def velo_estimate(df, time):
    """
        Gets the growth rate for the year 2021-2023

                            x(t+1) - x(t-1)
        FORMULA : v(t) = ---------------------
                                   2
    """

    x1 = df.loc[df['time(s)'] == time+1, 'position(m)'].iloc[0]
    x2 = df.loc[df['time(s)'] == time-1, 'position(m)'].iloc[0]

    v = (x1 - x2) / 2

    return v


def acceleration(v_prev, v_next):
    """
        Gets the acceleration insight for time 2 & 3

                            v(t+h) - x(t-h)
        FORMULA : a(t) = ---------------------
                                  2h
    """
    h = 1

    return (
        (v_next - v_prev) / (2*h)
    )




def total_change(df): 

    return (
        np.trapz( df['position(m)'], df['time(s)'])
    )


df = pd.read_csv("Traffic-Flow-Velocity-Estimation/data.csv")

velo_esti1 = velo_estimate(df, 1)
velo_esti2 = velo_estimate(df, 2)
velo_esti3 = velo_estimate(df, 3)
velo_esti4 = velo_estimate(df, 4)

acce1 = acceleration(velo_esti1, velo_esti3)
acce2 = acceleration(velo_esti2, velo_esti4)

print("\n\nVelocity Estimation : ")
print("Velocity 1 : ", velo_esti1)
print("Velocity 2 : ", velo_esti2)
print("Velocity 3 : ", velo_esti3)
print("Velocity 4 : ", velo_esti4)
print("\n\nTotal Change : ", total_change(df))
print("\n\nAcceleration Insight : ")
print("Acceleration Insight 1 : ", acce1)
print("Acceleration Insight 2 : ", acce2)


# VISUALIZATION
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
axes[0].plot(df['time(s)'], df['position(m)'], marker='o', color="#2C7B0A")
axes[0].set_xticks(df['time(s)'])
axes[0].grid(True, alpha=0.6, linestyle='-', animated=True)
axes[0].set_title("Position vs Time", fontweight="bold")
axes[0].set_xlabel("Time(s)", fontweight="bold")
axes[0].set_ylabel("Position(m)", fontweight="bold")

times = np.arange(1, 5)
velos = np.array([velo_esti1, velo_esti2, velo_esti3, velo_esti4])
axes[1].plot(times, velos, marker='o', color="#2C7B0A")
axes[1].set_xticks(times)
axes[1].grid(True, alpha=0.6, linestyle='-')
axes[1].set_title("Velocity vs Time", fontweight="bold")
axes[1].set_xlabel("Time", fontweight="bold")
axes[1].set_ylabel("Velocity", fontweight="bold")

plt.tight_layout()
plt.show()