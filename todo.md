# TODO list

Last work : `DeepINN/constraint/gradients.py`
## Geometry
- [ ] Geometry added but lot of bloats from TorchPhysics. Clean up geometry folder.
- [ ] Clean up utils folder.
- [ ] Implement gradient for multiple output neurons.
- [ ] Do we need retain_graph=True

## Constraints
- [X]  Implement the prescribed BC part in constraint/ boundary_loss dirichletBC.
- [X] Implement PDE loss constraint.
- [ ] Implement gradients.
- [ ] Implement lazy evaluation of gradients.

## Architectures
- [ ]  Implement fully connected NN.

## Tutorials
- [x] Basic geometry tutorials.
- [ ] Constraints tutorials.

## Misc
- [ ] Migrate to JupyterBooks. 
- [ ] Move everything after contribution in the [readme.md](readme.md) to the docs.