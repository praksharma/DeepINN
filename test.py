import DeepINN as dp

# Let us make a simple rectangle
X = dp.spaces.R2('x') #  2D space stencil
R = dp.domains.Parallelogram(X, [0,0], [1,0], [0,1])

bc_points = dp.constraint.DirichletBC(geom = R,
                                    function = lambda X: X[:,0]**2,
                                    sampling_strategy = "random",
                                    no_points = 100 )

bc_points_sampled = bc_points.sampler_object().sample_points().as_tensor
print(f"bc _points shape : {bc_points_sampled.size()}")

bc_points_sampled_labels = bc_points.sample_labels(bc_points_sampled).unsqueeze(1)
print (f"bc labels shape : {bc_points_sampled_labels.size()}")