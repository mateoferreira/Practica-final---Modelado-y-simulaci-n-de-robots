import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("joint_states.csv", header=None)

# tiempo
time = df[0] + df[1]*1e-9
time = time - time.iloc[0]

# posiciones correctas
back_left = df[15]
back_right = df[16]
front_left = df[17]
front_right = df[18]
mid_left = df[23]
mid_right = df[24]

plt.figure(figsize=(10,5))

plt.plot(time, back_left, label="Back Left")
plt.plot(time, back_right, label="Back Right")
plt.plot(time, front_left, label="Front Left")
plt.plot(time, front_right, label="Front Right")
plt.plot(time, mid_left, label="Mid Left")
plt.plot(time, mid_right, label="Mid Right")

plt.xlabel("Tiempo (s)")
plt.ylabel("Posición angular (rad)")
plt.title("Posición ruedas vs tiempo")
plt.grid(True)
plt.legend()
plt.show()