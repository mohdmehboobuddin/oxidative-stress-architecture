import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Color palette (modern minimal)
ros_color = "#c0392b"
core_color = "#2c3e50"
outcome_color = "#27ae60"

# ----------------------------
# LEFT: Oxidative Stress
# ----------------------------
ros_circle = Circle((20, 50), 12,
                    edgecolor=ros_color,
                    facecolor="white",
                    linewidth=3)
ax.add_patch(ros_circle)

ax.text(20, 58, "ROS",
        ha='center', fontsize=18,
        weight='bold', color=ros_color)

ax.text(20, 45,
        "Oxidative\nStress",
        ha='center', fontsize=12)

# ----------------------------
# CENTER: Conserved Core
# ----------------------------
core_box = FancyBboxPatch((38, 35), 24, 30,
                          boxstyle="round,pad=0.02,rounding_size=8",
                          linewidth=3,
                          edgecolor=core_color,
                          facecolor="white")
ax.add_patch(core_box)

ax.text(50, 57,
        "Conserved\nChromatin-Centred",
        ha='center', fontsize=15,
        weight='bold', color=core_color)

ax.text(50, 45,
        "Regulatory Core",
        ha='center', fontsize=14,
        weight='bold')

ax.text(50, 38,
        "(12 genes)",
        ha='center', fontsize=11)

# ----------------------------
# RIGHT: Adaptive Outcomes
# ----------------------------
out_box = FancyBboxPatch((72, 35), 24, 30,
                         boxstyle="round,pad=0.02,rounding_size=8",
                         linewidth=3,
                         edgecolor=outcome_color,
                         facecolor="white")
ax.add_patch(out_box)

ax.text(84, 58,
        "Adaptive State",
        ha='center', fontsize=16,
        weight='bold',
        color=outcome_color)

ax.text(84, 46,
        "Chromatin remodelling\nMetabolic adaptation\nStructural reorganisation",
        ha='center', fontsize=11)

# ----------------------------
# Arrows
# ----------------------------
ax.annotate("",
            xy=(38, 50), xytext=(32, 50),
            arrowprops=dict(arrowstyle="->", linewidth=2))

ax.annotate("",
            xy=(72, 50), xytext=(62, 50),
            arrowprops=dict(arrowstyle="->", linewidth=2))

# ----------------------------
# Bottom subtle statement
# ----------------------------
ax.text(50, 12,
        "12-Gene Core Separates Stress vs Control (p ≈ 1 × 10⁻¹⁶)",
        ha='center',
        fontsize=11)

plt.tight_layout()
plt.savefig("figures/Graphical_Abstract_Clean.png", dpi=600)
plt.show()
