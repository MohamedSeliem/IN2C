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


def parse_vector_string(series):
    return list(map(float, re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", series.iloc[0])))


# Load CSVs
df_e2e_s1a1 = pd.read_csv("s1a1E2E.csv")
df_e2e_s1a2 = pd.read_csv("s1a2E2E.csv")
df_jitter_s1a1 = pd.read_csv("s1a1Jit.csv")
df_jitter_s1a2 = pd.read_csv("s1a2Jit.csv")

# Parse vectors
e2e_time_s1a1 = parse_vector_string(df_e2e_s1a1["vectime"])
e2e_val_s1a1 = parse_vector_string(df_e2e_s1a1["vecvalue"])
e2e_time_s1a2 = parse_vector_string(df_e2e_s1a2["vectime"])
e2e_val_s1a2 = parse_vector_string(df_e2e_s1a2["vecvalue"])

jitter_time_s1a1 = parse_vector_string(df_jitter_s1a1["vectime"])
jitter_time_s1a2 = parse_vector_string(df_jitter_s1a2["vectime"])
jitter_val_s1a1 = parse_vector_string(df_jitter_s1a1["vecvalue"])
jitter_val_s1a2 = parse_vector_string(df_jitter_s1a2["vecvalue"])

# --- Combined Plot (Latency + Jitter with Boxplots) ---
fig, axs = plt.subplots(2, 2)

# Plot E2E Time Series
axs[0, 0].plot(e2e_time_s1a1, e2e_val_s1a1, label="S1A1", color='red')
axs[0, 0].plot(e2e_time_s1a2, e2e_val_s1a2, label="S1A2", color='blue')
axs[0, 0].set_xlabel("SimulationTime [s]")
axs[0, 0].set_ylabel("E2E Delay [s]")
axs[0, 0].axvline(x=4, label="Fault", color='black', linestyle='--')
axs[0, 0].axvline(x=6, label="Recover", color='green', linestyle='--')
axs[0, 0].legend()


# Plot E2E Box Plot
axs[0, 1].boxplot([e2e_val_s1a1, e2e_val_s1a2], tick_labels=["S1A1", "S1A2"], patch_artist=True,
                  boxprops=dict(facecolor='lightgreen'), medianprops=dict(color='black'), showfliers=False)
axs[0, 1].set_ylabel("E2E Delay [s]")

# Plot Jitter Box Plot
axs[1, 0].plot(jitter_time_s1a1, jitter_val_s1a1, color='brown', label="S1A1")
axs[1, 0].plot(jitter_time_s1a2, jitter_val_s1a2, color='green', label="S1A2")
axs[1, 0].axvline(x=4, label="Fault", color='black', linestyle='--')
axs[1, 0].axvline(x=6, label="Recover", color='green', linestyle='--')
axs[1, 0].set_xlabel("SimulationTime [s]")
axs[1, 0].set_ylabel("Jitter [s]")

axs[1, 0].legend()
# Plot Jitter Box Plot
axs[1, 1].boxplot([jitter_val_s1a1, jitter_val_s1a2], tick_labels=["S1A1", "S1A2"], patch_artist=True,
                  boxprops=dict(facecolor='lightyellow'), medianprops=dict(color='black'), showfliers=False)
axs[1, 1].set_ylabel("Jitter [s]")

plt.tight_layout()
plt.savefig("ieee_latency_jitter", dpi=300)
plt.close()