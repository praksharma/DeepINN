# TODO list

Last work : `DeepINN/constraint/gradients.py`
## Geometry
- [ ] Geometry added but lot of bloats from TorchPhysics. Clean up geometry folder. In progress in "DeepINN/geometry_refactor".
- [ ] Clean up utils folder.
- [ ] Implement anchor points.
- [ ] Add prediction plot function.

## Gradients
- [x] Implement basic gradients.
- [ ] Implement gradient for multiple output neurons.
- [x] Do we need retain_graph=True?

## Constraints
- [X] Implement the prescribed BC part in constraint/ boundary_loss dirichletBC.
- [X] Implement PDE loss constraint.
- [x] Implement gradients.
- [ ] Implement lazy evaluation of gradients.
- [ ] Implement more constraint.

## Architectures
- [x] Implement fully connected NN.
- [ ] Implement more neural networks

## Tutorials
- [x] Basic geometry tutorials.
- [x] Constraints tutorials.
- [ ] Add template PDE in constraint directory.
- [x] There was some problem with FCNN tutorial. It was incorrect PDE.
- [x] Add 2D discontinuous heat conduction problem
- [x] Add Fourier neural network and Deep Galerkin method architecture.

## Misc
- [x] Migrate to JupyterBooks. 
- [x] Move everything after contribution in the [readme.md](readme.md) to the docs.

## Technical stuff
- [ ] Substitute `raise NotImplementedError` to `@abc.abstractmethod` for better ABC implementation on concrete classes (classes where the member function are actually implemented).
- [ ] Use `functool.wraps` so that the decorator doesn't loose the metadata such as docsting.