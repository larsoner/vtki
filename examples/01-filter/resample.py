"""
Resampling Data Sets
~~~~~~~~~~~~~~~~~~~~

Resample one mesh's point/cell arrays onto another meshes nodes.
"""
###############################################################################
# This example will resample a volumetric mesh's  scalar data onto the surface
# of a sphere contained in that volume.

# sphinx_gallery_thumbnail_number = 1
import vtki
from vtki import examples
import numpy as np

###############################################################################
# Querry a grids points onto a sphere
mesh = vtki.Sphere(center=(4.5,4.5,4.5), radius=4.5)
data_to_probe = examples.load_uniform()

###############################################################################
# Plot the two datasets
p = vtki.Plotter()
p.add_mesh(mesh, color=True)
p.add_mesh(data_to_probe, opacity=0.5)
p.show()

###############################################################################
# Run the algorithm and plot the result
result = mesh.interpolate(data_to_probe)

# Plot result
name = 'Spatial Point Data'
result.plot(scalars=name, clim=data_to_probe.get_data_range(name))