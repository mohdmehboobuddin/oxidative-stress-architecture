import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import matplotlib.patches as patches

# 16:9 canvas (Elsevier compatible)
fig, ax = plt.subplots(figsize=(16, 9))
ax.set_xlim(0, 160)
ax.set_ylim(0, 90)
ax.axis('off')

# -----------------------
# Color Scheme
# -----------------------
neutral = "#34495e"
ros_color = "#e74c3c"
core_color = "#2c3e50"
highlight = "#2980b9"
outcome_color = "#27ae60"

# -----------------------
# LEFT — Trigger
# -----------------------
ros_circle = Circle((30, 45), 14,
                    edgecolor=ros_color,
                    facecolor="white",
                    linewidth=3)
ax.add_patch(ros_circle)

ax.text(30, 53, "ROS",
        ha='center', fontsize=18,
        weight='bold', color=ros_color)

ax.text(30, 40,
        "Oxidative\nStress",
        ha='center', fontsize=12)

# Arrow 1
ax.annotate("",
            xy=(60, 45), xytext=(44, 45),
            arrowprops=dict(arrowstyle="->", linewidth=2))

# -----------------------
# CENTER — Mechanism
# -----------------------
core_box = FancyBboxPatch((60, 25), 40, 40,
                          boxstyle="round,pad=0.02,rounding_size=8",
                          linewidth=3,
                          edgecolor=core_color,
                          facecolor="white")
ax.add_patch(core_box)

ax.text(80, 58,
        "Chromatin-Centred",
        ha='center', fontsize=16,
        weight='bold', color=core_color)

ax.text(80, 50,
        "Regulatory Reorganisation",
        ha='center', fontsize=15,
        weight='bold')

ax.text(80, 38,
        "Conserved 12-Gene Core",
        ha='center', fontsize=12, color=highlight)

# Arrow 2
ax.annotate("",
            xy=(115, 45), xytext=(100, 45),
            arrowprops=dict(arrowstyle="->", linewidth=2))

# -----------------------
# RIGHT — Outcome
# -----------------------
out_box = FancyBboxPatch((115, 25), 35, 40,
                         boxstyle="round,pad=0.02,rounding_size=8",
                         linewidth=3,
                         edgecolor=outcome_color,
                         facecolor="white")
ax.add_patch(out_box)

ax.text(132, 58,
        "Adaptive State",
        ha='center', fontsize=16,
        weight='bold',
        color=outcome_color)

ax.text(132, 46,
        "Metabolic\nStructural\nSignalling",
        ha='center', fontsize=12)

ax.text(132, 32,
        "Predictive Separation\n(p ≈ 1 × 10⁻¹⁶)",
        ha='center', fontsize=11, weight='bold')

# -----------------------
# Bottom subtitle
# -----------------------
ax.text(80, 8,
        "Oxidative stress reorganises chromatin architecture to define a conserved regulatory state across cell types",
        ha='center', fontsize=11, color=neutral)

plt.tight_layout()
plt.savefig("figures/Graphical_Abstract_Final.png", dpi=300)
plt.savefig("figures/Graphical_Abstract_Final.svg")
plt.show()
