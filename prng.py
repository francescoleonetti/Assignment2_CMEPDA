# -*- coding: utf-8 -*-
#
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

"""Core logic for the probability density function (pdf) definition.
"""


import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit



class ProbabilityDensityFunction(InterpolatedUnivariateSpline):

    """Class describing our pdf.

    Parameters
    ----------
    x : array-like
        The array of x values to be passed to the pdf, assumed to be sorted.
    
    y : array-like
        The array of y values to be passed to the pdf.

    k : int
        The order of the splines to be created.
    """

    def __init__(self, x, y, k=3):
        """Constructor.
        """
        # Normalize the pdf, if it is not (and probably it is npt!)
        norm = InterpolatedUnivariateSpline(x, y, k=k).integral(x[0], x[-1])
        y /= norm
        super().__init__(x, y, k=k)
        ycdf = np.array([self.integral(x[0], xcdf) for xcdf in x])
        self.cdf = InterpolatedUnivariateSpline(x, ycdf, k=k)
        # Need to make sure that the vector I am passing to the ppf spline as
        # the x values (here we are interchanging x and y: the ppf is the inverse 
        # function of the cdf!) has no duplicates---and need to filter the y 
        # accordingly! We can only invert bijective functions!
        xppf, ippf = np.unique(ycdf, return_index=True)
        yppf = x[ippf]
        self.ppf = InterpolatedUnivariateSpline(xppf, yppf, k=k)
        
        
    def prob(self, x1, x2):
        """Return the probability for the random variable to be included
        between x1 and x2.
        """
        return self.cdf(x2) - self.cdf(x1)

    
    def prng(self, size = 1000):
        """Return an array of random values distributed accordingly 
        to the pdf. Number of values in the array = 'size'. 
        """
        return self.ppf(np.random.uniform(size = size))


if __name__ == '__main__':
    x = np.linspace(0., np.pi, 2000)
    y = np.sin((np.cos(np.sin(x)))**2)
    pdf = ProbabilityDensityFunction(x, y)
    print(pdf.prng())


    
















