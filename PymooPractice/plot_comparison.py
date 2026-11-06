
import numpy as np
import matplotlib.pyplot as plt

# 读取实验数据
data = np.loadtxt(
    "generation_comparison.csv",
    delimiter=",",
    skiprows=1
)

generations = data[:, 0]
igd_values = data[:, 1]
hv_values = data[:, 2]

# 图1：IGD变化曲线
plt.figure(figsize=(7, 5))

plt.plot(
    generations,
    igd_values,
    marker="o",
    linewidth=2,
    label="IGD"
)

plt.xlabel("Generations")
plt.ylabel("IGD (Lower is Better)")
plt.title("NSGA-II IGD Convergence")
plt.xticks(generations)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("igd_comparison.png", dpi=300)
plt.close()

# 图2：HV变化曲线
plt.figure(figsize=(7, 5))

plt.plot(
    generations,
    hv_values,
    marker="s",
    linewidth=2,
    label="HV"
)

plt.xlabel("Generations")
plt.ylabel("HV (Higher is Better)")
plt.title("NSGA-II HV Convergence")
plt.xticks(generations)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("hv_comparison.png", dpi=300)
plt.close()

print("IGD comparison plot saved.")
print("HV comparison plot saved.")
