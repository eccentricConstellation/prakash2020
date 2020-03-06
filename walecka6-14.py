# script for walecka 6.14
#Emma Rice
# 3/6/2020
from tabulate import tabulate
lamp = 2.793
lamn = -1.913
def mupos(j,lam, n=1):
	mupos = n*j - n*.5 + lam
	return mupos
def muneg(j, lam,n=1):
	muneg = n*j + j/(j+1)*(n*.5 - lam)
	return muneg

jf = 2.5
jcu = 1.5
jpd = 2.5
jin = 4.5
jfr = 4.5

muthe = [4.72, 2.14, -.61, 5.5, 4]
muexp = [mupos(jf,lamp), mupos(jcu,lamp), mupos(jpd,lamn,0), mupos(jin,lamp), muneg(jfr,lamp)]
nuclei = ["F","Cu", "Pd", "In", "Fr"]
print(tabulate({"Nuclei": nuclei,"Experimental mu)": muexp, "Theoretical mu": muthe}, headers="keys"))

