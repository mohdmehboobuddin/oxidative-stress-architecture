import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')  # Hide axes

# 1. Draw the Cell (Cytoplasm) - Light Blue
cell = patches.Ellipse((5, 3), width=8, height=5, facecolor='#e0f7fa', edgecolor='#006064', linewidth=3, zorder=1)
ax.add_patch(cell)

# 2. Draw the Nucleus - Darker Blue
nucleus = patches.Circle((5, 3), radius=1.5, facecolor='#b2ebf2', edgecolor='#006064', linewidth=2, zorder=2)
ax.add_patch(nucleus)

# 3. Add Arrows
# Input Arrow (Stress) - Red
ax.arrow(0.5, 3, 1.5, 0, head_width=0.3, head_length=0.3, fc='#d32f2f', ec='#d32f2f', width=0.1, zorder=3)
ax.text(1.25, 3.5, 'Oxidative Stress\n(H₂O₂)', ha='center', va='center', fontsize=12, fontweight='bold', color='#d32f2f')

# Output Arrow (Survival) - Green
ax.arrow(8, 3, 1.5, 0, head_width=0.3, head_length=0.3, fc='#388e3c', ec='#388e3c', width=0.1, zorder=3)
ax.text(8.75, 3.5, 'Adaptation &\nSurvival', ha='center', va='center', fontsize=12, fontweight='bold', color='#388e3c')

# 4. Text Annotations
# Nucleus Text
ax.text(5, 3.8, 'Rapid Nuclear Response', ha='center', va='center', fontsize=11, fontweight='bold', zorder=4)
ax.text(5, 3.4, '(Chromatin Remodeling)', ha='center', va='center', fontsize=9, style='italic', zorder=4)
ax.text(5, 2.5, 'BRD4\nSMARCA4', ha='center', va='center', fontsize=12, fontweight='bold', color='#006064', zorder=4)

# Cytoplasm Text (Structural)
ax.text(5, 5, 'Structural Reinforcement', ha='center', va='center', fontsize=11, fontweight='bold', zorder=4)
ax.text(3.5, 1.5, 'Cytoskeleton:\nWDR1', ha='center', va='center', fontsize=11, fontweight='bold', color='#004d40', zorder=4)
ax.text(6.5, 1.5, 'Nuclear Envelope:\nLMNA', ha='center', va='center', fontsize=11, fontweight='bold', color='#004d40', zorder=4)

# Title
plt.title("Conserved Transcriptional Architecture of Epithelial Oxidative Stress Response", fontsize=14, fontweight='bold', pad=20)

# Save and Show
plt.tight_layout()
plt.savefig('Graphical_Abstract.jpg', dpi=300)
plt.show()
