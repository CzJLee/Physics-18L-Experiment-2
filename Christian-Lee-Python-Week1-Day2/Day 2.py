from numpy import loadtxt
from matplotlib import pyplot
from scipy.optimize import curve_fit
from math import sqrt

fvdata = loadtxt("fvdata.csv", dtype="int, float", delimiter=",", usecols=(0,1),unpack=True)

fdata = list(fvdata[0])
vdata = list(fvdata[1])

def linear_fxn(x, m, b):
	return m*x + b

popt, pcov = curve_fit(linear_fxn, fdata, vdata)

print(pcov)

he_value = round(popt[0], 17)
wf_value = round(popt[1], 2)

x = list(range(0, 10**15+1, 10**14))
y = [linear_fxn(i,he_value,wf_value) for i in x]

he_uncertainty = sqrt(pcov[0,0])
wf_uncertainty = sqrt(pcov[1,1])

print(he_uncertainty*wf_uncertainty)

pyplot.scatter(fdata, vdata, color = "red")
pyplot.plot([0,10**15],[0,0],"b")
pyplot.plot(x,y,color="orange", label="Best linear fit")
pyplot.legend(loc="upper left")
pyplot.title("Plot of Stopping Potential (V) vs Frequency (Hz)")
pyplot.axis([0,10**15, -2,3])
pyplot.xlabel("Frequency (Hz)")
pyplot.ylabel("Stopping Potential (V)")
pyplot.text(0.5*10**14,2,"h/e = ( {} ± {} ) x10 ^ -15 eV*s \nw/e = ( {} ± {} ) eV".format(round(he_value*10**15,2),round(he_uncertainty*10**15,2),abs(round(wf_value,2)),round(wf_uncertainty,2)))
pyplot.show()
