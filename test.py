import unittest
import sys

from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
if sys.flags.interactive: #se r
	plt.ion()

class ProbabilityDensityFunction(InterpolatedUnivariateSpline):
    
    def __init__(self, x, y):

    	super().__init__(x,y)

class TestPdf(unittest.TestCase):

	def test_uniform(self):

		x = np.linspace(0., 1., 100)
		y = np.full(x.shape, 1.)
		#print(x,y)
		#plt.plot(x, y)
		pdf = ProbabilityDensityFunction(x, y)
		self.assertAlmostEqual(pdf(0.5), 1.)


	def test_triangular(self):
		x = np.linspace(0., 1., 100)
		y = 2 * x
		pdf = ProbabilityDensityFunction(x, y)
		plt.figure('Triangular cdf')
		plt.plot(x, y)

	def test_fancy(self):
		x = np.linspace(0., 1., 100)
		y = np.zeros(x.shape)
		y[x <= 0.5] = 2.* x[x <= 0.5]
		y[x > 0.75] = 3.

		plt.figure('Fancy pdf')
		plt.plot(x, y)
		plt.show()


if __name__ == '__main__':
	unittest.main(exit = not sys.flags.interactive)
	plt.show()
