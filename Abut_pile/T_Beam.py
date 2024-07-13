import matplotlib.pyplot as plt
import numpy as np

# Define dimensions of the T-beam cross-section

D = 400  # overall height of the beam
bw = 100 
bf = 650
df = 100

# Define coordinates for the T-beam cross-section
x = np.array([(bf-bw)/2, (bf-bw)/2 + bw, (bf-bw)/2 + bw, bf, bf, 0, 0, (bf-bw)/2, (bf-bw)/2])
y = np.array([0, 0, D-df, D-df, D, D, D-df, D-df, 0])

# Plot the T-beam cross-section
# plt.figure(figsize=(10, 12))
plt.plot(x, y, color='black')
# plt.fill(x, y, 'b', alpha=0.1)  # Fill the T-beam cross-section
plt.title('T-beam Cross-section')
plt.xlabel('Width (mm)')
plt.ylabel('Height (mm)')
plt.axis('off')


plt.annotate('', xy=(-10,D ), xytext=(-10, 0), arrowprops=dict(arrowstyle='<->',color='black', linewidth=2), label='Arrow Line')
plt.text(-25,D/2, f"D({D}mm)",rotation='vertical', va = 'center')

plt.annotate('', xy=(0, D+10), xytext=(bf, D+10), arrowprops=dict(arrowstyle='<->', color='black', linewidth=2), label='Arrow Line')
plt.text(bf/2,D+15,  f"b-f({bf}mm)", ha = 'center',)

plt.annotate('', xy=(bf+10, D-df), xytext=(bf+10, D), arrowprops=dict(arrowstyle='<->', color='black', linewidth=2), label='Arrow Line')
plt.text(bf+15,(D-df+D)/2, f"d-f({df}mm)", rotation = 'vertical', va = 'center' )


plt.annotate('', xy=((bf-bw)/2, D/2), xytext=((bf-bw)/2 + bw, D/2), arrowprops=dict(arrowstyle='<->', color='black', linewidth=2), label='Arrow Line')
# plt.text((bf-bw)/2, (D/2)+15, f"b-w({bw}mm)", )
plt.text((bf)/2, (D/2)+15, f'bw: {bw}',ha = 'center',  fontsize=12)


plt.tight_layout()
plt.show()
