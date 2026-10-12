import pandas
import numpy as np
import matplotlib.pyplot as plt
f=pandas.read_csv("./zadanie1.csv")

def beta_1(x_vect,y_vect):
    num=0
    den=0
    mean=np.mean(x_vect)
    for i in range(len(x_vect)):
        num+=(x_vect[i] - mean)*y_vect[i]
        den+=(x_vect[i]-mean)**2
    return num/den
def beta_0(x_vect,y_vect):
    return np.mean(y_vect) - beta_1(x_vect,y_vect)*np.mean(x_vect)

print(f"Beta 1 = {beta_1(f["godziny_nauki"],f["sredni_wynik_testow"])}")    
print(f"Beta 0 = {beta_0(f["godziny_nauki"],f["sredni_wynik_testow"])}")
print(f"np.polyfit = {np.polyfit(f["godziny_nauki"],f["sredni_wynik_testow"],1)}")

plt.scatter(f["godziny_nauki"],f["sredni_wynik_testow"])
k=lambda x: beta_0(f["godziny_nauki"],f["sredni_wynik_testow"]) + x*beta_1(f["godziny_nauki"],f["sredni_wynik_testow"])
k_vect=[]
for i in f["godziny_nauki"]:
    k_vect.append(k(i))
plt.plot(f["godziny_nauki"],k_vect,color="red")
plt.show()

def calc_resid(x_vect,y_vect):
    e=[]
    for i in range(len(x_vect)):
        e.append(y_vect[i]-(beta_0(x_vect,y_vect))-beta_1(x_vect,y_vect)*x_vect[i])
    return e
usable_resid=calc_resid(f["godziny_nauki"],f["sredni_wynik_testow"])
plt.scatter(f["godziny_nauki"],usable_resid)
plt.show()
plt.hist(usable_resid,bins=50)
plt.show()