#!/usr/bin/env python
# Copyright (C) 2022 francescoleonetti
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Second assignment for the CMEPDA course, 2022/23"""

from scipy.interpolate import InterpolatedUnivariateSpline
import random
import numpy as np
import matplotlib.pyplot as plt



class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    
    def __init__(self, x, y, k = 3):

    	super().__init__(x,y)
    	ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x]) #sto calcolando per punti la funzione cumulativa
    	self.cdf = InterpolatedUnivariateSpline(x, ycdf)

    	xppf, ippf = np.unique(ycdf, return_index = True) #np.unique prende un array e mi restituisce i valori unici dell'array, ritornandomi anche i rispettivi indici con index
    	yppf = x[ippf]
    	self.ppf 



if __name__ == '__main__':

	x = np.linspace(0., np.pi, 100)
	y = np.sin(x) + np.log((np.cos(x))**2)
	f = ProbabilityDensityFunction(x, y)

	plt.figure('Grafico 1')
	plt.title('Grafico 1')
	plt.plot(x, y, 'o', color = 'green')
	_x = np.linspace(0., np.pi, 1000)
	plt.plot(_x, f(_x), color = 'red')
	plt.show()
