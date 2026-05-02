import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("joint_states.csv", header=None)

time = df[0] + df[1]*1e-9
time = time - time.iloc[0]


link1_eff = df[43]
link2_eff = df[44]
link3_eff = df[45]
link4_eff = df[46]

arm_effort = (
    link1_eff +
    link2_eff+
    link3_eff +
    link4_eff
)


pinza1_eff = df[49]
pinza2_eff = df[50]

gripper_effort = (
    pinza1_eff +
    pinza2_eff
)

plt.figure(figsize=(10,5))

plt.plot(time, arm_effort, label="Brazo (torque total)")
plt.plot(time, gripper_effort, label="Gripper")

plt.xlabel("Tiempo (s)")
plt.ylabel("Torque (N·m)")
plt.title("Esfuerzo brazo vs gripper")
plt.grid(True)
plt.legend()

plt.show()