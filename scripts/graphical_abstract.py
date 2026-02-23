import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import matplotlib.patches as patches

# Create figure
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Colors
ros_color = "#d73027"
core_color = "#4575b4"
outcome_color = "#1a9850"

# -----------------------------
# Left: Oxidative Stress
# -----------------------------
ros_box = FancyBboxPatch((5, 35), 25, 30,
                         boxstyle="round,pad=0.02,rounding_size=5",
                         linewidth=2,
                         edgecolor=ros_color,
                         facecolor="white")
ax.add_patch(ros_box)

ax.text(17.5, 58, "Oxidative Stress",
        ha='center', fontsize=16, weight='bold', color=ros_color)

ax.text(17.5, 45,
        "Reactive Oxygen Species (ROS)\nHydrogen Peroxide (H₂O₂)",
        ha='center', fontsize=12)

# -----------------------------
# Middle: Conserved Core
# -----------------------------
core_box = FancyBboxPatch((37, 25), 26, 50,
                          boxstyle="round,pad=0.02,rounding_size=5",
                          linewidth=2,
                          edgecolor=core_color,
                          facecolor="white")
ax.add_patch(core_box)

ax.text(50, 70,
        "Conserved Chromatin-Centred\nRegulatory Core (12 genes)",
        ha='center', fontsize=14, weight='bold', color=core_color)

genes = [
    "BRD4", "SMARCA4", "NSD2",
    "STAT2", "EIF4G1",
    "LMNA", "ITGA3",
    "SLC2A1", "MBOAT7",
    "GANAB", "PTPRF", "WDR1"
]

ax.text(50, 50,
        "\n".join(genes),
        ha='center', fontsize=10)

# -----------------------------
# Right: Functional Outcomes
# -----------------------------
out_box = FancyBboxPatch((70, 35), 25, 30,
                         boxstyle="round,pad=0.02,rounding_size=5",
                         linewidth=2,
                         edgecolor=outcome_color,
                         facecolor="white")
ax.add_patch(out_box)

ax.text(82.5, 58, "Adaptive Outcomes",
        ha='center', fontsize=16, weight='bold', color=outcome_color)

ax.text(82.5, 45,
        "Chromatin remodelling\nMetabolic adaptation\nStructural reorganisation\nStress signalling",
        ha='center', fontsize=12)

# -----------------------------
# Arrows
# -----------------------------
ax.annotate("",
            xy=(37, 50), xytext=(30, 50),
            arrowprops=dict(arrowstyle="->", linewidth=2))

ax.annotate("",
            xy=(70, 50), xytext=(63, 50),
            arrowprops=dict(arrowstyle="->", linewidth=2))

# -----------------------------
# Bottom predictive statement
# -----------------------------
ax.text(50, 10,
        "12-Gene Core Alone Separates Stress vs Control (p ≈ 1 × 10⁻¹⁶)",
        ha='center',
        fontsize=13,
        weight='bold')

plt.tight_layout()
plt.savefig("figures/Graphical_Abstract.png", dpi=600)
plt.show()
