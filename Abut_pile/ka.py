import matplotlib.pyplot as plt
import abut_foundation as af
import input_sheet as isp
import numpy as np

def plot_ka_diagram(C432, D431, C437, top_pile_cap, bot_pile_cap, top_form_lev, earth_pressure_base_pile_cap, earth_pressure_abutment_base):
    # Draw the right-angled triangle
    xpoints = np.array([5, (5 + earth_pressure_base_pile_cap), 5, 5])
    ypoints = np.array([5, 5, 5 + C432, 5])

    # Hide axis
    plt.axis('off')

    # Plot the right_angled triangle
    plt.plot(xpoints, ypoints)

    # Plot the dotted lines
    # Extend the base to the left using dotted lines
    extended_x = np.array([0, 5])
    extended_y = np.array([5, 5])
    plt.plot(extended_x, extended_y, linestyle='dotted')

    # Extend the line from (5, 5 + C432) to the left using dotted lines
    extended_x_parallel = np.array([0, 5])
    extended_y_parallel = np.array([5 + C432, 5 + C432])
    plt.plot(extended_x_parallel, extended_y_parallel, linestyle='dotted')

    # Extend the line from (5, 5 + C432) to the left using dotted lines
    extended_x_parallel = np.array([0, 5 + earth_pressure_base_pile_cap])
    extended_y_parallel = np.array([5 + C437, 5 + C437])
    plt.plot(extended_x_parallel, extended_y_parallel, linestyle='dotted')

    # Add double-headed arrows
    arrow_props = dict(arrowstyle='<->', color='black')

    # Arrow between top line and middle line
    plt.annotate('', xy=(2, 5 + C437), xytext=(2, 5 + C432), arrowprops=arrow_props)

    # Arrow between top line and bottom line
    plt.annotate('', xy=(1, 5 + C432), xytext=(1, 5), arrowprops=arrow_props)

    # Arrow between middle and bottom line
    plt.annotate('', xy=(2, 5 + C437), xytext=(2, 5), arrowprops=arrow_props)

    # Add measurement texts
    plt.text(2.2, 5 + (C432 + C437) / 2, f'{D431}', ha='left', va='center')
    plt.text(0, 5.5, f'{C437}', ha='left', va='center')
    plt.text(0, 5 + (C437 + 5) / 2, f'{C432}', ha='left', va='center')

    # Bottom of pile cap text
    plt.text(3.5, 4 + C437, 'BOTTOM OF PILE CAP', ha='center', va='bottom', fontsize=8)
    plt.text(3.5, 3.8 + C437, f'{bot_pile_cap}m', ha='center', va='bottom', fontsize=8)

    # Top of pile cap text
    plt.text(3.5, 6 + C437, 'TOP OF PILE CAP', ha='center', va='bottom', fontsize=8)
    plt.text(3.5, 5.8 + C437, f'{top_pile_cap}m', ha='center', va='bottom', fontsize=8)

    # Top of formation level text
    plt.text(3.5, 3.8 + C437 + C432, 'TOP OF FORMATION LEVEL', ha='center', va='bottom', fontsize=8)
    plt.text(3.5, 3.6 + C437 + C432, f'{top_form_lev}m', ha='center', va='bottom', fontsize=8)

    plt.text(3.5, 8.8 + C437, f'{earth_pressure_abutment_base}T/m²', ha='center', va='bottom', fontsize=8)

    # Earth pressure text
    
    plt.text(4.5 + (earth_pressure_base_pile_cap / 2), 3.7 + C432 / 2, f'{earth_pressure_base_pile_cap} T/m', ha='center', va='bottom', fontsize=8)


    # Show plot
    plt.show()

    # Example usage
C432 = af.C432  # 6.582
D431 = af.D431  # 4.782
C437 = af.C437  # 1.8
top_pile_cap = isp.top_pile_cap
bot_pile_cap = isp.bot_pile_cap_lev
top_form_lev = isp.prop_rail_form_level
earth_pressure_base_pile_cap = af.earth_pressure_base_pile_cap
earth_pressure_abutment_base = af.earth_pressure_abutment_base

plot_ka_diagram(C432, D431, C437, top_pile_cap, bot_pile_cap, top_form_lev, earth_pressure_abutment_base, earth_pressure_base_pile_cap)