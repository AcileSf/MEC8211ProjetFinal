# =============================================================================
# ====================== MEC 8211 - PROJET FINAL V&V - H24 ====================
# Redigé par:
# Acile Sfeir
# Mohammed Mahdi Sahbi Ben Daya
# Alexandre Deschenes
#______________________________________________________________________________
# Adapted from @author:Jean-Yves Trepanier
# =============================================================================
# =============================================================================

import math
import csv
from scipy import stats  
import numpy as np  
import matplotlib.pylab as plt

def ConfidenceInterval(series, n, confiance):
     """Retourne l'intervalle de confiance sur la moyenne"""
     mean_val = series.mean()
     stdev = series.std()
     test_stat = stats.t.ppf((confiance + 1)/2, n)
     lower_bound = mean_val - test_stat * stdev / math.sqrt(n)
     upper_bound = mean_val + test_stat * stdev / math.sqrt(n)
     return lower_bound, upper_bound
 
# create some normal random data
mean = 150.
sd = 2.5
n = 100
np.random.seed(0)
serie = np.random.normal(mean,sd,n)
print("serie=", serie)
# plot histogram
plt.hist(serie, 30)
plt.show()
# statistiques
moyenne = serie.mean() # moyenne 
print ('moyenne voulue: ',mean)
print ('moyenne échantillon: ',moyenne)
stddev = serie.std() # standard deviation 
print ('deviation standard voulue: ',sd)
print ('deviation standard échantillon: ',stddev)
#Intervalles de confiance
confiance = 0.95
lower_bound, upper_bound = ConfidenceInterval(serie,serie.size,confiance)
print('Intervalle de confiance à ',100*confiance,'% : ', lower_bound, upper_bound)



# Export generated data to csv
with open('FORCES_random_seed0_150.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Forces distribution normale'])
    for i in range(len(serie)):
         filewriter.writerow([serie[i]])

    filewriter.writerow(['moyenne voulue: ',mean])
    filewriter.writerow(['moyenne échantillon: ',moyenne])
    filewriter.writerow(['deviation standard voulue: ',sd])
    filewriter.writerow(['deviation standard échantillon: ',stddev])
    filewriter.writerow(['Intervalle de confiance à ',100*confiance,'% : ', lower_bound, upper_bound])
     
     
