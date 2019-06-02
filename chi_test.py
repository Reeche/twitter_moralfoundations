import pandas as pd
import numpy as np
from scipy.stats import chisquare, chi2_contingency

data = pd.read_csv('scores_relative.csv', header = 0)
print(data)



# Generally for all parties
#stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 1], data.iloc[:, 2], data.iloc[:, 3], data.iloc[:, 4]]))
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0]*100, data.iloc[:, 1]*100, data.iloc[:, 2]*100,data.iloc[:, 3]*100, data.iloc[:, 4]*100]))
print("for all parties ", "stats", stats, "p-value", p, "dof", dof)

## For pairs:
for i in range(0, 6):
    for j in range(1, 6):
        p1 = data.iloc[:, i]*100
        p2 = data.iloc[:, j]*100
        stats, p, dof, expected = chi2_contingency(np.array([p1, p2]))
        # stats2, p2 = chisquare(np.array([data.iloc[:, i], data.iloc[:, j]]).T)
        print("Party 1 ", i, "Party 2 ", j, "stats", stats, "p-value", p, "degrees of freedom", dof)

"""
# Afd 0 - CDU 1
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 1]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 1]]).T)
print("AFD - CDU :", "stats", stats, "p-value", p)
print("AFD - CDU :", "stats 2", stats2, "p-value 2", p2)

# Afd 0 - FDP 2
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 2]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("AFD - FDP :", "stats", stats, "p-value", p)
print("AFD - FDP :", "stats", stats2, "p-value", p2)

# Afd 0 - Grüne 3
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 3]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("AFD - Grüne :", "stats", stats, "p-value", p)

# Afd 0 - Linke 4
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 4]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("AFD - Linke :", "stats", stats, "p-value", p)

# Afd 0 - SPD 5
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 0], data.iloc[:, 5]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("AFD - SPD :", "stats", stats, "p-value", p)

# CDU 1 - FDP 2
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 1], data.iloc[:, 2]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("CDU - FDP :", "stats", stats, "p-value", p)

# CDU 1 - Grüne 3
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 1], data.iloc[:, 3]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("CDU - Grüne :", "stats", stats, "p-value", p)

# CDU 1 - Linke 4
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 1], data.iloc[:, 4]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("CDU - Linke :", "stats", stats, "p-value", p)

# CDU 1 - SPD 5
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 1], data.iloc[:, 5]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("CDU - SPD :", "stats", stats, "p-value", p)

# FDP 2 - Grüne 3
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 2], data.iloc[:, 3]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("FDP - Grüne :", "stats", stats, "p-value", p)

# FDP 2 - Linke 4
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 2], data.iloc[:, 4]]))
stats2, p2 = chisquare(np.array([data.iloc[:, 0], data.iloc[:, 2]]).T)
print("FDP - Linke :", "stats", stats, "p-value", p)

# FDP 2 - SPD 5
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 2], data.iloc[:, 5]]))
print("AFD - SPD :", "stats", stats, "p-value", p)

# Grüne 3 - Linke 4
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 3], data.iloc[:, 4]]))
print("Grüne - Linke :", "stats", stats, "p-value", p)

# Grüne 3 - SPD 5
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 3], data.iloc[:, 5]]))
print("Grüne - SPD :", "stats", stats, "p-value", p)

# Linke 4 - SPD 5
stats, p, dof, expected = chi2_contingency(np.array([data.iloc[:, 4], data.iloc[:, 5]]))
print("Linke - SPD :", "stats", stats, "p-value", p)
"""

