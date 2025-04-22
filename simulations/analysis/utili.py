import pandas as pd
import matplotlib.pyplot as plt
import re
import matplotlib as mpl

# --- IEEE-Compliant Style ---
mpl.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 10,
    'axes.titlesize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'lines.linewidth': 1.0,
    'figure.figsize': (7, 5),
    'savefig.dpi': 300,
})


# Helper to extract and trim vectime/vecvalue pairs
def extract_time_value_trimmed(df, module_name):
    row = df[df["module"] == module_name].iloc[0]
    t = list(map(float, re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", row["vectime"])))
    v = list(map(float, re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", row["vecvalue"])))
    return t, v


# Load data
s1a1 = pd.read_csv("s1a1utiliz.csv")
s1a2 = pd.read_csv("s1a2utiliz.csv")

# Common modules for comparison
modules = [
    "IN2C.SwitchA_1.eth[0].phyLayer.transmitter",
    "IN2C.SwitchA_1.eth[1].phyLayer.transmitter",
    "IN2C.centralSwitch_1.eth[3].phyLayer.transmitter"
]
names = [
    "SwitchA_1 -> centralSwitch_1",
    "SwitchA_1 -> SwitchB_1",
    "centralSwitch_1 -> SwitchB_1"
]
# Set up subplot figure
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 10), sharex=True)

for idx, module in enumerate(modules):
    t1, v1 = extract_time_value_trimmed(s1a1, module)
    t2, v2 = extract_time_value_trimmed(s1a2, module)

    ax = axes[idx]
    ax.plot(t1, v1, label="S1A1", color='red')
    ax.plot(t2, v2, label="S1A2", color='blue')
    ax.set_title(f"{names[idx]}")
    ax.set_ylabel("Utilization (%)")
    ax.grid(True)
    if idx == 2:
        ax.set_xlabel("SimulationTime [s]")
    ax.legend()

plt.tight_layout()
plt.savefig("ieee_util", dpi=300)
plt.close()
