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

# Load CSVs
df_e2e_s2a1 = pd.read_csv("s2a1E2E.csv")
df_e2e_s2a2 = pd.read_csv("s2a2E2E.csv")
df_jitter_s2a1 = pd.read_csv("s2a1Jitter.csv")
df_jitter_s2a2 = pd.read_csv("s2a2Jitter.csv")

# Parse vectors
e2e_time_s2a1 = df_e2e_s2a1["Time (s)"]
e2e_val_s2a1 = df_e2e_s2a1["Mean Bit Life Time Per Packet"]
e2e_time_s2a2 = df_e2e_s2a2["Time (s)"]
e2e_val_s2a2 = df_e2e_s2a2["Mean Bit Life Time Per Packet"]

jitter_time_s2a1 = df_jitter_s2a1["Time (s)"]
jitter_time_s2a2 = df_jitter_s2a2["Time (s)"]
jitter_val_s2a1 = df_jitter_s2a1["Jitter"]
jitter_val_s2a2 = df_jitter_s2a2["Jitter"]

# --- Combined Plot (Latency + Jitter with Boxplots) ---
fig, axs = plt.subplots(2, 2)

# Plot E2E Time Series
axs[0, 0].plot(e2e_time_s2a1, e2e_val_s2a1, label="S2A1", color='red')
axs[0, 0].plot(e2e_time_s2a2, e2e_val_s2a2, label="S2A2", color='blue')
axs[0, 0].set_xlabel("SimulationTime [s]")
axs[0, 0].set_xlim(0, 4)
axs[0, 0].set_ylabel("E2E Delay [s]")
axs[0, 0].axvline(x=2, label="Fault", color='black', linestyle='--')
axs[0, 0].axvline(x=3, label="Recover", color='green', linestyle='--')
axs[0, 0].legend()


# Plot E2E Box Plot
axs[0, 1].boxplot([e2e_val_s2a1, e2e_val_s2a2], tick_labels=["S2A1", "S2A2"], patch_artist=True,
                  boxprops=dict(facecolor='lightgreen'), medianprops=dict(color='black'), showfliers=False)
axs[0, 1].set_ylabel("E2E Delay [s]")

# Plot Jitter Box Plot
axs[1, 0].plot(jitter_time_s2a1, jitter_val_s2a1, color='brown', label="S2A1")
axs[1, 0].plot(jitter_time_s2a2, jitter_val_s2a2, color='green', label="S2A2")
axs[1, 0].axvline(x=2, label="Fault", color='black', linestyle='--')
axs[1, 0].axvline(x=3, label="Recover", color='green', linestyle='--')
axs[1, 0].set_xlabel("SimulationTime [s]")
axs[1, 0].set_ylabel("Jitter [s]")
axs[1, 0].set_xlim(0, 4)
axs[1, 0].legend()
# Plot Jitter Box Plot
axs[1, 1].boxplot([jitter_val_s2a1, jitter_val_s2a2], tick_labels=["S2A1", "S2A2"], patch_artist=True,
                  boxprops=dict(facecolor='lightyellow'), medianprops=dict(color='black'), showfliers=False)
axs[1, 1].set_ylabel("Jitter [s]")

plt.tight_layout()
plt.savefig("ieee_latency_jitter_2", dpi=300)
plt.close()