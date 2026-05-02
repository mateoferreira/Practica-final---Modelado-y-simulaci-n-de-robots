import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./imu.csv", header=None)

time = df[0] + df[1]*1e-9
time = time - time.iloc[0]

ax_imu = df[28]
ay_imu = df[29]
az_imu = df[30]

fig, ax = plt.subplots(figsize=(10,5), layout='constrained')

ax.plot(time, ax_imu, label='Aceleración X', color='red')
ax.plot(time, ay_imu, label='Aceleración Y', color='blue')
ax.plot(time, az_imu, label='Aceleración Z', color='green')

ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Aceleración (m/s²)")
plt.title("Aceleración IMU vs tiempo")


plt.legend()
plt.grid(True)
plt.show()