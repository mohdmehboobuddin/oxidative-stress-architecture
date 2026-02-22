import matplotlib.pyplot as plt

plt.figure(figsize=(7,9))

steps = [
"Oxidative Injury",
"Stress Transcription Factors\n(ATF3 / AP-1 / STAT)",
"Chromatin Remodeling\n(BRD4 – SMARCA4)",
"Metabolic + Structural Adaptation\n(SLC2A1, LMNA, ITGA3, MBOAT7)",
"Cellular Survival State"
]

for i,step in enumerate(steps):
    plt.text(0.5,1-i*0.2,step,ha='center',va='center',
             bbox=dict(boxstyle="round,pad=0.5"))

for i in range(len(steps)-1):
    plt.arrow(0.5,1-i*0.2-0.07,0,-0.08,length_includes_head=True,
              head_width=0.02)

plt.axis('off')
plt.title("Conserved Regulatory Architecture of Oxidative Stress Response")
plt.savefig("Figure12_Mechanistic_Model.png",dpi=300,bbox_inches='tight')
print("Model figure created")
