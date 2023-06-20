"""Function to show an example of the created points of the sampler. 
"""
import numpy as np

import matplotlib.pyplot as plt


def scatter(subspace, *samplers, dpi=False, save=False):
    """Shows (one batch) of used points in the training. If the sampler is
    static, the shown points will be the points for the training. If not
    the points may vary, depending of the sampler. 

    Parameters
    ----------
    subspace : torchphysics.problem.Space
        The (sub-)space of which the points should be plotted.
        Only plotting for dimensions <= 3 is possible.
    *samplers : torchphysics.problem.Samplers
        The diffrent samplers for which the points should be plotted.
        The plot for each sampler will be created in the order there were
        passed in.
    dpi : dpi of the saved figure.
    save : A flag to save figure.

    In future, I might use a dictionary to add more functions.

    Returns
    -------
    fig : matplotlib.pyplot.figure
        The figure handle of the plot. The Figure is created on the STDOUT, so actual return isn't required.
    """
    assert subspace.dim <= 3, "Can only scatter points in dimensions <= 3."

    #scatter_fn = _choose_scatter_function(subspace.dim)
    
    for sampler in samplers:
        points = sampler.sample_points()[:, list(subspace.keys())]
        numpy_points = points.as_tensor.detach().cpu().numpy()
        labels = _create_labels(subspace)
        #scatter_fn(numpy_points, labels)

    if subspace.dim == 1:
        _scatter_1D(numpy_points, labels, dpi, save)
    elif subspace.dim == 2:
        _scatter_2D(numpy_points, labels, dpi, save)
    else:
        _scatter_3D(numpy_points, labels, dpi, save)

def _create_labels(subspace):
    labels = []
    for var in subspace:
        if subspace[var] == 1:
            labels.append(var)
        else:
            for i in range(subspace[var]):
                labels.append(var+f'_{i+1}')
    return labels

def _choose_scatter_function(space_dim):
    
    if space_dim == 1:
        return _scatter_1D
    elif space_dim == 2:
        return _scatter_2D    
    else:
        return _scatter_3D  


def _scatter_1D(points, labels, dpi, save):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid()
    ax.scatter(points, np.zeros_like(points))
    ax.set_xlabel(labels[0])
    if save:
        plt.savefig('geom.jpg', dpi = dpi,bbox_inches='tight',transparent=True)


def _scatter_2D(points, labels, dpi, save):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid()
    ax.scatter(points[:, 0], points[:, 1])
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    if save:
        plt.savefig('geom.jpg', dpi = dpi,bbox_inches='tight',transparent=True)


def _scatter_3D(points, labels, dpi, save):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.grid()
    ax.scatter(points[:, 0], points[:, 1], points[:, 2])
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])
    if save:
        plt.savefig('geom.jpg', dpi = dpi,bbox_inches='tight',transparent=True)