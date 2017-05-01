from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

try:
  import seaborn as sns
except ImportError:
  pass


def pca_plot(dist):
  """Create a 2 or 3D PCA visulization of a higher dimensional distribution.

  Parameters
  ----------
  dist : RandomVariable
    takes an input first class edward RandomVariable object, representing the distribution to visualize.
  dimensions:
    

  Returns
  -------
  matplotlib axes
  """
 

