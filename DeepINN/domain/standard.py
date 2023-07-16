from .base import Dataset

class Generic(Dataset):
    """
    Very generic dataset loader. It loads the entire dataset in one go, which can lead to overfitting in stiff-PDEs.

    Parameters
    ----------
    pde_equation: a method which returns the PDE equation as tensor object (not numpy)
    collocation_object: A PDE sampler. 
        Instance of DeepINN.constraint.PDE()
    bc_object: A BC sampler.
        Instance of dp.constraint.DirichletBC() or Neumann BC (to be implemented).
    """
    def __init__(self, pde_equation, collocation_object, bc_object) -> None:
        super().__init__()

        self.pde = pde_equation
        self.pde_sampler = collocation_object
        # if the bcs is not list, then make it a list
        self.bc_sampler = bc_object if isinstance(bc_object, (list)) else [bc_object]

        self.bc_list_len = len(self.bc_sampler)
    
    def sample_collocation_points(self):
        # returns the collocation points as tensor.
        # the DeepINN.constraint.PDE() takes care of the missing column in 1D tensor. See tutorials/4. dataset/ 1.basic.ipynb 
        return self.pde_sampler.sampler_object().sample_points().as_tensor
    
    def sample_collocation_labels(self):
        # returns the collocation points using the above function.
        # also returns the collocation points labels i.e. the residual of the PDE as tensor.
        self.collocation_points = self.sample_collocation_points() # returns a tensor of sampled collocation points
        return self.collocation_points, self.pde_sampler.sample_labels(self.collocation_points).unsqueeze(1)
    
    def sample_boundary_points(self):
        # returns a list of boundary points on each boundary as tensor
        self.bc_points_list =[]
        for bc in self.bc_sampler:
            self.bc_points_list.append(bc.sampler_object().sample_points().as_tensor)
        return self.bc_points_list
    
    def sample_boundary_labels(self):
        # returns the list of boundary points on each boundary using the above function.
        # returns a list of tensor boundary conditions on each boundary.
        self.bc_labels_list = []
        self.bc_points = self.sample_boundary_points() # returns a list of boundary points on each boundary as tensor
        for bc_number in range(0, self.bc_list_len):
            self.bc_labels_list.append(self.bc_sampler[bc_number].sample_labels(self.bc_points[bc_number]).unsqueeze(1))
        return self.bc_points, self.bc_labels_list
