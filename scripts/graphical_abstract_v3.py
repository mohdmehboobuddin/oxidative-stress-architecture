import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import matplotlib.patches as patches
import numpy as np

fig, ax = plt.subplots(figsize=(16, 10))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Color palette (professional scientific)
ros_color = "#d62728"
chromatin_color = "#1f77b4"
signal_color = "#9467bd"
structure_color = "#2ca02c"
neutral = "#2c3e50"

# ---------------------------
# TOP: Oxidative Stress
# ---------------------------
ax.text(50, 92, "Oxidative Stress (ROS Burst)",
        ha='center', fontsize=18, weight='bold', color=ros_color)

# Lightning bolt symbol
bolt_x = [48, 52, 49, 53]
bolt_y = [88, 80, 80, 72]
ax.plot(bolt_x, bolt_y, linewidth=4, color=ros_color)

# ---------------------------
# Layer 1: Chromatin Regulation
# ---------------------------
box1 = FancyBboxPatch((25, 68), 50, 12,
                      boxstyle="round,pad=0.02,rounding_size=6",
                      linewidth=2,
                      edgecolor=chromatin_color,
                      facecolor="white")
ax.add_patch(box1)

ax.text(50, 74,
        "Chromatin Regulatory Layer\n(BRD4 • SMARCA4 • NSD2)",
        ha='center', fontsize=14, weight='bold', color=chromatin_color)

# ---------------------------
# Layer 2: Signal Integration
# ---------------------------
box2 = FancyBboxPatch((30, 52), 40, 12,
                      boxstyle="round,pad=0.02,rounding_size=6",
                      linewidth=2,
                      edgecolor=signal_color,
                      facecolor="white")
ax.add_patch(box2)

ax.text(50, 58,
        "Signal Integration Layer\n(STAT2 • Regulatory TFs)",
        ha='center', fontsize=13, weight='bold', color=signal_color)

# ---------------------------
# Layer 3: Structural–Metabolic
# ---------------------------
box3 = FancyBboxPatch((20, 36), 60, 12,
                      boxstyle="round,pad=0.02,rounding_size=6",
                      linewidth=2,
                      edgecolor=structure_color,
                      facecolor="white")
ax.add_patch(box3)

ax.text(50, 42,
        "Structural & Metabolic Adaptation\n(ITGA3 • SLC2A1 • LMNA • EIF4G1 • MBOAT7)",
        ha='center', fontsize=13, weight='bold', color=structure_color)

# ---------------------------
# Arrows Between Layers
# ---------------------------
arrow_style = dict(arrowstyle="->", linewidth=2)

ax.annotate("", xy=(50, 68), xytext=(50, 84), arrowprops=arrow_style)
ax.annotate("", xy=(50, 52), xytext=(50, 68), arrowprops=arrow_style)
ax.annotate("", xy=(50, 36), xytext=(50, 52), arrowprops=arrow_style)

# ---------------------------
# Bottom: Predictive Separation
# ---------------------------
bottom_box = FancyBboxPatch((30, 12), 40, 10,
                            boxstyle="round,pad=0.02,rounding_size=6",
                            linewidth=2,
                            edgecolor=neutral,
                            facecolor="white")
ax.add_patch(bottom_box)

ax.text(50, 17,
        "12-Gene Core Separates Stress vs Control\n(p ≈ 1 × 10⁻¹⁶)",
        ha='center', fontsize=12, weight='bold')

# Final formatting
plt.tight_layout()
plt.savefig("figures/Graphical_Abstract_Layered_Model.png", dpi=600)
plt.show()
