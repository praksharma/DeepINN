Search.setIndex({"docnames": ["Tutorials/1. Geometry/Basic_domains", "Tutorials/1. Geometry/UKAEA SUT", "Tutorials/1. Geometry/different sampling", "Tutorials/1. Geometry/domain_creation", "Tutorials/1. Geometry/polygons_external_objects", "Tutorials/2. BC/1. dirichlet", "Tutorials/2. BC/2. pde", "Tutorials/3. Gradients/1. Gradients", "Tutorials/3. Gradients/2. higher derivative", "Tutorials/4. Dataset/1. basic", "Tutorials/5. FCNN/1. basic", "Tutorials/5. FCNN/2. test", "Tutorials/5. FCNN/3. model", "Tutorials/6. 2D heat conduction/1. model", "docs_tutorial/contribution", "docs_tutorial/docs_contribution", "docs_tutorial/installation", "intro"], "filenames": ["Tutorials/1. Geometry/Basic_domains.ipynb", "Tutorials/1. Geometry/UKAEA SUT.ipynb", "Tutorials/1. Geometry/different sampling.ipynb", "Tutorials/1. Geometry/domain_creation.ipynb", "Tutorials/1. Geometry/polygons_external_objects.ipynb", "Tutorials/2. BC/1. dirichlet.ipynb", "Tutorials/2. BC/2. pde.ipynb", "Tutorials/3. Gradients/1. Gradients.ipynb", "Tutorials/3. Gradients/2. higher derivative.ipynb", "Tutorials/4. Dataset/1. basic.ipynb", "Tutorials/5. FCNN/1. basic.ipynb", "Tutorials/5. FCNN/2. test.ipynb", "Tutorials/5. FCNN/3. model.ipynb", "Tutorials/6. 2D heat conduction/1. model.ipynb", "docs_tutorial/contribution.md", "docs_tutorial/docs_contribution.md", "docs_tutorial/installation.md", "intro.md"], "titles": ["Basic domain", "UKAEA SUT", "Basic sampling techniques", "Domain Basics", "Polygons and External Objects", "Dirichlet BC", "PDE constraint", "Gradient basics", "Gradients in DeepINN", "Training dataset", "Basics of network design", "Forward pass", "FCNN training", "FCNN training", "Contribution", "Documentation compilation", "Installation", "DeepINN"], "terms": {"thi": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16], "i": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], "onli": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "valid": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "when": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "packag": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "instal": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], "import": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15], "sy": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "path": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "append": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "two": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "folder": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "up": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "deepinn": [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 16], "dp": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "us": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17], "default": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16], "backend": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "pytorch": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "2": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "0": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "1": [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13], "cu117": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "t": [0, 3, 4, 7, 9, 10, 15], "space": [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13], "r1": [0, 3, 9, 10, 12], "we": [0, 1, 3, 4, 7, 13], "need": [0, 2, 3, 4, 7, 13], "one": [0, 3, 4, 15, 16], "dimension": [0, 3], "interv": [0, 3, 9, 10, 12], "5": [0, 2, 3, 4, 7, 10, 11, 12, 13], "from": [1, 4, 7, 15], "geometri": [1, 2, 3, 4], "domain": [1, 2, 4, 5, 6, 7, 9, 10, 12, 13], "domain2d": [1, 3, 4], "shapely_polygon": [1, 4], "shapelypolygon": [1, 4], "polygon": 1, "creator": [1, 4], "domain3d": [1, 4], "trimesh_polyhedron": [1, 4], "trimeshpolyhedron": [1, 4], "torch": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], "r3": [1, 4], "p": [1, 4, 15, 16], "file_nam": [1, 4], "home": [1, 2, 3, 4, 9, 10, 12], "hell": [1, 2, 3, 4, 9, 10, 12], "desktop": [1, 2, 3, 4, 9, 10, 12], "phd": 1, "work": [1, 4], "pinn": [1, 17], "10": [1, 2, 5, 6, 7, 9, 10, 12, 13], "june": 1, "2022": 1, "4": [1, 4, 7, 9, 16], "week": 1, "3": [1, 4, 7, 11], "nvidia": [1, 16], "modulu": 1, "7": 1, "modifi": 1, "fourier": 1, "sampl": [1, 3, 5, 6, 7], "adapt": 1, "activ": [1, 11, 12, 13, 14], "stl_file": 1, "stl": [1, 4], "file_typ": [1, 4], "just": [1, 14], "boundari": [1, 2, 3, 4, 5, 12, 13], "p_sampler": [1, 4], "sampler": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12], "lhssampler": [1, 2], "n_point": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12], "200": 1, "randomuniformsampl": [1, 2, 4, 5, 6, 7], "util": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13], "scatter": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13], "10000": 1, "filter_fn": [1, 2, 5, 9, 10, 12, 13], "lambda": [1, 2, 3, 5, 6, 7, 9, 10, 12, 13], "ab": 1, "9": [1, 3, 4], "matplotlib": [1, 5, 6, 7, 12, 13], "pyplot": [1, 5, 6, 7, 12, 13], "plt": [1, 5, 6, 7, 12, 13], "p_point": 1, "sample_point": [1, 5, 6, 7, 9], "as_tensor": [1, 5, 6, 7, 9], "detach": 1, "cpu": 1, "numpi": [1, 13], "fig": 1, "figur": [1, 12, 13], "ax": 1, "add_subplot": 1, "project": [1, 4, 15], "3d": [1, 4], "set_ylim": 1, "The": [1, 3, 4, 5, 6, 7, 14, 15, 16], "last": [1, 3, 4, 15], "point": [1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 13, 14], "tutori": [1, 2, 3, 4, 9, 10, 12, 15, 16], "possibl": [1, 3, 4], "transform": [1, 4], "either": [1, 4], "slice": [1, 4], "plane": [1, 4], "also": [1, 3, 4, 15], "function": [1, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13], "implement": [1, 3, 4], "trimesh": [1, 4], "mai": [1, 2, 3, 4], "problem": [1, 4, 17], "should": [1, 3, 4, 9, 10, 14], "first": [1, 4, 7, 9, 10, 12, 16], "research": [1, 4], "2d": [1, 4, 5, 6, 13], "which": [1, 3, 4, 7, 14], "most": [1, 4], "time": [1, 3, 4, 12, 13, 16], "less": [1, 4], "expens": [1, 4], "For": [1, 3, 4, 15], "have": [1, 3, 4], "choos": [1, 4], "how": [1, 4], "want": [1, 3, 4, 14, 15], "creat": [1, 2, 3, 4, 7, 14, 15, 16], "represent": [1, 4], "here": [1, 3, 4, 7, 14, 15, 16], "same": [1, 3, 4, 7, 14], "new_spac": [1, 4], "r2": [1, 2, 3, 4, 5, 6, 7, 13], "new": [1, 4, 15], "object": [1, 3, 8], "p_z": 1, "slice_with_plan": [1, 4], "plane_origin": [1, 4], "plane_norm": [1, 4], "100": [1, 2, 3, 4, 5, 6, 7, 13], "1000": 1, "p_x": 1, "325": 1, "25": [1, 2], "05": 1, "r": [2, 3, 5, 6, 7, 14], "parallelogram": [2, 3, 4, 5, 6, 7, 13], "unit": [2, 3, 13], "squar": [2, 3, 13], "c": [2, 3, 5, 6, 7, 13], "circl": [2, 3], "random_r": 2, "50": [2, 3, 5, 9, 10, 12, 13], "random": [2, 3, 5, 6, 7, 9, 10, 12], "grid_c": 2, "gridsampl": [2, 3, 4], "densiti": [2, 3, 4], "grid": [2, 9, 10, 12, 13], "intersect": [2, 3], "500": [2, 12], "random_intersect": 2, "repo": [2, 3, 4, 9, 10, 12, 14, 15], "domainoper": [2, 3], "sampler_help": [2, 3], "py": [2, 3, 4, 9, 10, 12, 14], "userwarn": [2, 3, 4, 9, 10, 12], "Will": [2, 3, 9, 10, 12], "oper": [2, 4, 7], "loop": [2, 3], "over": [2, 3], "all": [2, 3, 4, 15], "input": [2, 3, 7, 9, 10, 11], "paramet": [2, 3], "total": [2, 3], "slow": [2, 3], "down": [2, 3], "train": [2, 3, 4], "warn": [2, 3, 9, 10, 12], "f": [2, 3, 15, 16], "163": [2, 3], "cut": [2, 3], "107": [2, 3], "exact": [2, 3], "volum": [2, 3, 4], "known": [2, 3, 15], "estim": [2, 3], "domain_a": [2, 3], "domain_b": [2, 3], "If": [2, 3, 4, 7, 14, 15], "you": [2, 3, 4, 9, 10, 12, 13, 14, 15, 16], "set_volum": [2, 3], "right_boundari": 2, "left_boundari": [2, 5], "sign": 2, "In": [3, 15], "file": [3, 4, 14], "explain": [3, 4], "usag": 3, "class": [3, 4, 7], "everi": 3, "child": 3, "main": 3, "follow": [3, 15, 16], "method": [3, 4], "properti": [3, 4], "contain": [3, 16], "check": [3, 8], "lai": 3, "insid": [3, 4], "comput": [3, 4, 7], "set": 3, "bounding_box": 3, "get": 3, "bound": [3, 4], "box": [3, 4], "given": [3, 9, 10, 12], "return": [3, 4, 7, 8, 9, 10, 12, 13], "itself": 3, "know": 3, "normal": [3, 4, 11, 12, 13], "vector": [3, 4], "But": [3, 4], "ha": [3, 4], "explicit": 3, "document": 3, "each": [3, 16], "see": 3, "doc": [3, 14, 15], "some": 3, "pre": [3, 4, 16], "ar": [3, 4, 7, 9, 10, 12, 13, 15], "focu": 3, "now": [3, 4, 14, 16], "creation": [3, 4], "differ": [3, 4], "To": [3, 4, 15], "belong": 3, "definit": 3, "were": 3, "part": [3, 4], "previou": 3, "interval_sampl": 3, "plot": [3, 12, 13], "someth": 3, "dpi": [3, 9, 10, 12, 13], "300": 3, "save": 3, "true": [3, 7, 8, 9, 10, 11, 12, 13], "r_bound": 3, "c_bound": 3, "would": 3, "nice": 3, "look": [3, 4], "directli": 3, "r_sampler": 3, "c_sampler": 3, "venv": [3, 4, 14, 15], "lib": [3, 4], "python3": [3, 4, 14, 15], "site": [3, 4, 15], "504": [3, 4], "meshgrid": [3, 4], "an": [3, 4, 7, 15, 16], "upcom": [3, 4], "releas": [3, 4, 16], "requir": [3, 4, 14], "pass": [3, 4, 7], "index": [3, 4], "argument": [3, 4], "trigger": [3, 4], "intern": [3, 4], "aten": [3, 4], "src": [3, 4], "nativ": [3, 4], "tensorshap": [3, 4], "cpp": [3, 4], "3483": [3, 4], "_vf": [3, 4], "tensor": [3, 4, 5, 8, 9, 10, 11, 12, 13], "kwarg": [3, 4], "type": [3, 4], "ignor": [3, 4], "attr": [3, 4], "defin": [3, 4, 7], "134": [3, 4], "dimens": [3, 4, 5], "other": [3, 4], "than": [3, 4], "revers": [3, 4], "shape": [3, 4, 13], "deprec": [3, 4], "throw": [3, 4], "error": [3, 4, 13], "futur": [3, 4], "consid": [3, 4], "mt": [3, 4], "transpos": [3, 4], "batch": [3, 4], "matric": [3, 4], "permut": [3, 4], "arang": [3, 4], "ndim": [3, 4], "3571": [3, 4], "bary_coord": [3, 4], "stack": [3, 4], "y": [3, 4, 7, 8, 9, 10, 12, 13], "reshap": [3, 4], "wai": [3, 4], "until": 3, "simpl": [3, 5, 6, 7, 9, 10, 12, 13, 14], "complex": [3, 4], "union": 3, "A": [3, 9, 10, 12, 13], "cup": 3, "b": 3, "cap": 3, "setminu": 3, "cartesian": 3, "product": 3, "cdot": 3, "aspect": 3, "previous": [3, 4], "mention": [3, 4], "can": [3, 4, 9, 10, 12, 13, 15, 16], "arbitrari": 3, "number": 3, "possibli": 3, "becom": 3, "costli": 3, "union_domain": 3, "intersection_domain": 3, "cut_domain": 3, "again": [3, 4, 7, 9, 10, 12], "call": [3, 4], "sinc": 3, "voluem": 3, "alwai": [3, 4, 13], "valu": 3, "correspond": 3, "union_sampl": 3, "inter_sampl": 3, "cut_sampl": 3, "142": 3, "30": 3, "boundary_a": 3, "bounadry_b": 3, "cylind": 3, "exampl": [3, 4], "abov": 3, "product_sampl": 3, "20": [3, 9, 10, 12], "variabl": [3, 4], "e": 3, "g": 3, "grow": 3, "rotat": 3, "end": 3, "radiu": 3, "origin": 3, "right": [3, 15], "depend": [3, 4, 14], "anoth": 3, "so": 3, "solut": [3, 16], "stai": [3, 4], "replac": 3, "desir": 3, "These": [3, 15], "like": [3, 4], "appli": 3, "new_domain": 3, "thank": 4, "soft": [4, 15], "polyhedron": 4, "addit": 4, "exist": [4, 15], "thei": 4, "combin": 4, "featur": 4, "mean": 4, "what": 4, "chang": 4, "vertic": 4, "find": [4, 9, 10, 12], "under": 4, "construct": 4, "through": 4, "your": [4, 15], "own": 4, "yourself": 4, "constructor": 4, "befor": 4, "therefor": 4, "pointsampl": 4, "next": 4, "sai": [4, 7], "side": 4, "simplex": 4, "face": 4, "show": 4, "pde": [4, 7, 9, 10, 17], "alreadi": 4, "support": [4, 16], "ascii": 4, "obj": 4, "mani": 4, "more": [4, 7, 9, 10, 12, 13, 15], "do": [4, 7], "specifi": 4, "l_plate": 4, "where": 4, "l": 4, "useabl": 4, "let": [5, 6, 7], "u": [5, 6, 7, 15], "make": [5, 6, 7], "rectangl": [5, 6, 7], "stencil": [5, 6, 7], "collocation_point": [5, 6, 7], "without": 5, "filter": [5, 9, 10, 12], "bc_point": 5, "constraint": [5, 7, 8, 9, 10, 12, 13], "dirichletbc": [5, 9, 10, 12, 13], "geom": [5, 6, 7, 9, 10, 12, 13], "sampling_strategi": [5, 6, 7, 9, 10, 12, 13], "no_point": [5, 6, 7, 9, 10, 12, 13], "bc_points_right": 5, "sampler_object": [5, 6, 7, 9, 10, 12, 13], "manual": [5, 7], "bc_points_sampl": 5, "size": [5, 6, 7, 8, 9, 10, 16], "bc_points_right_sampl": 5, "label": [5, 9, 10, 12, 13], "unsqueez": [5, 6, 7, 9], "add": 5, "result": [5, 7], "bc_points_sampled_label": 5, "sample_label": [5, 6, 7, 9], "bc_points_sampled_right_label": 5, "variat": [5, 6, 7], "base": [5, 6, 7], "provid": [5, 6, 7], "cmap": [5, 6, 7, 13], "get_cmap": [5, 6, 7, 13], "plasma": [5, 6, 7, 13], "colorbar": [5, 6, 7, 13], "0x7fe83c7ed3a0": 5, "0x7fe83c6df730": 5, "collcoc": [6, 7], "collocation_points_sampl": [6, 7], "collocation_points_label": [6, 7], "bc": [6, 7, 12, 13], "0x7ff085fec070": 6, "nn": [7, 11, 12, 13], "requires_grad": [7, 8, 9, 10], "print": [7, 8], "grad_fn": [7, 8, 10, 11], "addbackward0": 7, "frac": 7, "dy": 7, "dx": 7, "2x": 7, "calcul": 7, "autograd": 7, "grad": 7, "create_graph": 7, "retain_graph": 7, "mulbackward0": 7, "jacobian": [7, 8, 9, 10, 12, 13], "jacobian_matrix": 7, "graph": [7, 9, 10], "investig": 7, "whether": 7, "confirm": [7, 14], "both": [7, 9, 10], "neural": [7, 9, 10, 17], "network": [7, 9, 17], "demonstr": 7, "net": [7, 11, 12, 13], "modul": 7, "def": [7, 8, 9, 10, 12, 13], "__init__": 7, "self": [7, 9, 10, 12], "super": 7, "linear": [7, 11, 12, 13], "automat": 7, "weight": [7, 11], "initialis": [7, 11, 12, 13], "forward": [7, 17], "instanti": 7, "4514": 7, "3535": 7, "6050": 7, "squeezebackward1": 7, "verifi": 7, "give": [7, 13], "prop": 7, "fun": 7, "bias": 7, "bia": [7, 11, 12, 13], "output": [7, 9, 10, 13], "matmul": 7, "notic": 7, "ok": 7, "am": 7, "stupid": [7, 9, 10, 12, 13], "n": [7, 9, 10, 12, 15], "func": 7, "sin": 7, "8415": 7, "9093": 7, "1411": 7, "7568": 7, "sinbackward0": 7, "grad_output": 7, "ones_lik": 7, "5403": 7, "4161": 7, "9900": 7, "6536": 7, "column": 7, "denot": 7, "coodin": 7, "second": 7, "coordint": 7, "coordin": 7, "indexbackward0": [7, 8, 10], "0x7f750007aa90": 7, "enabl": [7, 9, 10], "chain": [7, 9, 10], "rule": [7, 9, 10], "differenti": 7, "take": 7, "2930": [7, 13], "0000": [7, 11, 12], "0825": 7, "5305": 7, "9212": 7, "6438": 7, "9175": 7, "7091": 7, "9677": 7, "7350": 7, "6300": 7, "4992": 7, "9642": 7, "3607": 7, "9573": 7, "0166": 7, "8906": 7, "1743": 7, "9489": 7, "0287": 7, "3507": 7, "4230": 7, "9440": 7, "6972": 7, "5564": 7, "2747": 7, "8570": 7, "0975": 7, "6516": 7, "6687": 7, "3874": 7, "5045": 7, "9092": 7, "5228": 7, "5527": 7, "4221": 7, "9412": 7, "9828": 7, "7495": 7, "3001": [7, 13], "0497": 7, "0901": 7, "2823": 7, "9442": 7, "2218": 7, "9692": 7, "5136": 7, "5020": 7, "2023": 7, "3678": 7, "7819": 7, "7172": 7, "0191": 7, "3216": 7, "4669": 7, "5493": 7, "2346": 7, "3253": 7, "7525": 7, "6583": 7, "8198": 7, "6443": 7, "0415": 7, "1759": 7, "8441": 7, "4261": 7, "4104": 7, "6782": 7, "8920": 7, "1505": 7, "7075": 7, "7404": 7, "9070": 7, "1176": 7, "4098": 7, "0612": 7, "1286": 7, "0742": 7, "6482": 7, "9419": 7, "4051": 7, "8317": 7, "3231": 7, "0585": 7, "3959": 7, "1475": 7, "9752": 7, "3819": 7, "4927": 7, "0505": 7, "3465": 7, "9483": 7, "2960": 7, "3112": 7, "1125": 7, "8214": 7, "3367": 7, "5440": 7, "7444": 7, "2778": 7, "j": [7, 8, 9, 10, 12, 13], "hessian": 7, "laplac": [8, 12, 13], "1d": [8, 12, 13], "equat": [8, 12, 13], "u__x": [8, 9, 10, 12, 13], "dy_x": [8, 9, 10, 12, 13], "associ": 8, "dy_xx": [8, 9, 10, 12, 13], "boundary_point_label": [8, 9, 10], "boundary_point_sampl": [8, 9, 10, 12, 13], "0x7f6b65325040": 8, "len": [8, 9, 10], "line": [9, 10, 12, 15], "left_bc": [9, 10, 12, 13], "condit": [9, 10, 12, 13], "deal": [9, 10, 12, 13], "right_bc": [9, 10, 12, 13], "interior_point": [9, 10, 12, 13], "debug": 9, "grid_sampl": [9, 10, 12], "78": [9, 10, 12], "iter": [9, 10, 12, 13], "did": [9, 10, 12], "ani": [9, 10, 12], "try": [9, 10, 12], "Or": [9, 10, 12], "els": [9, 10, 12], "temp": 9, "gener": [9, 10, 12, 13], "don": [9, 10], "collocation_point_label": [9, 10], "collocation_point_sampl": [9, 10, 12, 13], "sample_collocation_point": 9, "sample_collocation_label": [9, 10], "sample_boundary_label": [9, 10], "sample_boundary_point": [9, 10], "neuron": [9, 10], "hypothet": [9, 10], "connect": [9, 10], "fcnn": 10, "tanh": [11, 12, 13], "xavier": [11, 12, 13], "layer_s": [11, 12, 13], "fullyconnect": [11, 12, 13], "modulelist": [11, 12, 13], "in_featur": [11, 12, 13], "out_featur": [11, 12, 13], "data": 11, "randn": 11, "0735": 11, "2387": 11, "4911": 11, "1239": 11, "1970": 11, "addmmbackward0": 11, "0734": 11, "2342": 11, "4551": 11, "loss_metr": 11, "mse": [11, 12, 13], "mseloss": [11, 12, 13], "1445": 11, "mselossbackward0": 11, "model": [12, 13], "optimis": [12, 13], "adam": [12, 13], "lr": [12, 13], "001": [12, 13], "metric": [12, 13], "compil": [12, 13], "devic": [12, 13], "cuda": [12, 13], "optimiser_funct": [12, 13], "optim": [12, 13], "loss": [12, 13], "6431": [], "51": 12, "4550": [], "101": 12, "3263": [], "151": 12, "2451": [], "201": 12, "1962": [], "251": 12, "1659": [], "301": 12, "1442": [], "351": 12, "1258": [], "401": 12, "1085": [], "451": 12, "0919": [], "501": [12, 13], "0761": [], "finish": [12, 13], "2000": [12, 13], "coordinates_list": [12, 13], "tensor2numpi": [12, 13], "solution_list": [12, 13], "collocation_forward": [12, 13], "bc_forward": [12, 13], "histori": [12, 13], "training_histori": [12, 13], "colloc": [12, 13], "color": 12, "red": 12, "blue": 12, "minor": [12, 13], "xlabel": [12, 13], "ylabel": [12, 13], "text": [12, 13], "root": [14, 15], "assumpt": 14, "python": [14, 15], "symlink": 14, "m": [14, 15], "environ": [14, 15], "sourc": [14, 15], "bin": [14, 16], "updat": [14, 15, 16], "stdout": 14, "directori": [14, 15], "upgrad": 14, "pip": 14, "txt": 14, "build": [14, 15], "relev": 14, "veri": 14, "run": [14, 15, 16], "current": 14, "virtual": [14, 15], "step": 15, "allow": 15, "basic": 15, "setup": 15, "detail": 15, "visit": 15, "jupyter_env": 15, "pip3": 15, "templat": 15, "quick": 15, "start": 15, "pwd": [15, 16], "name": 15, "tabl": 15, "content": 15, "store": 15, "_toc": 15, "yml": 15, "configur": 15, "_config": 15, "full": 15, "rebuild": 15, "toc": 15, "doesn": 15, "entir": 15, "publish": 15, "branch": 15, "ghp": 15, "_build": 15, "html": 15, "deploi": 15, "websit": 15, "go": 15, "page": 15, "select": 15, "gh": 15, "locat": 15, "github": 15, "forc": 15, "its": 15, "lazi": 15, "search": 15, "wa": 15, "deploy": 15, "workflow": 15, "click": 15, "button": 15, "re": 15, "job": 15, "top": 15, "corner": 15, "includ": 15, "notebook": 15, "outsid": 15, "link": 15, "ln": 15, "": 15, "readm": 15, "md": 15, "via": 16, "command": 16, "pull": 16, "suitabl": 16, "tagnam": 16, "avail": 16, "prakhars962": 16, "open": 16, "jupyt": 16, "server": 16, "8888": 16, "overrid": 16, "entrypoint": 16, "bash": 16, "guid": 16, "bind": 16, "workspac": 16, "lab": 16, "v": 16, "altern": 16, "interact": 16, "session": 16, "old": 16, "repositori": 16, "tag": 16, "id": 16, "886808706155": 16, "minut": 16, "ago": 16, "6": 16, "99gb": 16, "none": 16, "0bb744f6159e": 16, "38": 16, "4ffbb67f8447": 16, "about": 16, "hour": 16, "8gb": 16, "fe16ca34f9d9": 16, "delet": 16, "them": 16, "image_id": 16, "rm": 16, "deep": 17, "learn": 17, "framework": 17, "solv": 17, "invers": 17, "involv": [13, 17], "physic": 17, "inform": 17, "1876": 12, "0990": 12, "0583": 12, "0352": 12, "0205": 12, "0112": 12, "0057": 12, "0027": 12, "0011": 12, "0004": 12, "0002": 12, "taken": [12, 13], "trainer": [12, 13], "9356": 12, "sec": [12, 13], "np": 13, "rect": 13, "bug": 13, "somehow": 13, "otherwis": 13, "latinhypercub": 13, "u__i": 13, "zero": 13, "becaus": 13, "dy_i": 13, "dy_yi": 13, "5000": 13, "0018": 13, "150": 13, "6618": 13, "6636": 13, "2732": 13, "9934": 13, "2665": 13, "1001": 13, "3051": 13, "0254": 13, "3305": 13, "1501": 13, "2981": 13, "0206": 13, "3187": 13, "2001": 13, "0178": 13, "3108": 13, "2501": 13, "2885": 13, "0154": 13, "3039": 13, "2842": 13, "0133": 13, "2975": 13, "3501": 13, "2801": 13, "0113": 13, "2914": 13, "4001": 13, "2759": 13, "0094": 13, "2854": 13, "4501": 13, "2718": 13, "0076": 13, "2794": 13, "5001": 13, "2676": 13, "0058": 13, "2734": 13, "28": 13, "5579": 13}, "objects": {}, "objtypes": {}, "objnames": {}, "titleterms": {"basic": [0, 2, 3, 7, 10], "domain": [0, 3], "ukaea": 1, "sut": 1, "sampl": 2, "techniqu": 2, "oper": 3, "chang": 3, "polygon": 4, "extern": 4, "object": 4, "dirichlet": 5, "bc": 5, "pde": [6, 12, 13], "constraint": 6, "gradient": [7, 8], "test": [7, 14], "1": 7, "A": 7, "note": 7, "futur": 7, "1d": [7, 9, 10], "tensor": 7, "multipl": 7, "valu": 7, "2d": 7, "actual": 7, "geometri": [7, 9, 10, 12, 13], "deepinn": [8, 17], "train": [9, 12, 13], "dataset": [9, 10], "laplac": [9, 10], "equat": [9, 10], "network": [10, 12, 13], "design": 10, "forward": 11, "pass": 11, "fcnn": [12, 13], "contribut": 14, "document": 15, "compil": 15, "set": 15, "up": 15, "jupyt": 15, "book": 15, "instal": 16, "us": 16, "pip": 16, "docker": 16, "imag": 16, "cpu": 16, "onli": 16, "gpu": 16, "passthrough": 16, "tagless": 16, "copi": 16}, "envversion": {"sphinx.domains.c": 3, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 9, "sphinx.domains.index": 1, "sphinx.domains.javascript": 3, "sphinx.domains.math": 2, "sphinx.domains.python": 4, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.intersphinx": 1, "sphinxcontrib.bibtex": 9, "sphinx": 60}, "alltitles": {"Basic domain": [[0, "basic-domain"]], "UKAEA SUT": [[1, "ukaea-sut"]], "Basic sampling techniques": [[2, "basic-sampling-techniques"]], "Domain Basics": [[3, "domain-basics"]], "Domain Operations": [[3, "domain-operations"]], "Changing Domains": [[3, "changing-domains"]], "Polygons and External Objects": [[4, "polygons-and-external-objects"]], "Polygons": [[4, "polygons"]], "External Objects": [[4, "external-objects"]], "Dirichlet BC": [[5, "dirichlet-bc"]], "PDE constraint": [[6, "pde-constraint"]], "Gradient basics": [[7, "gradient-basics"]], "Test 1": [[7, "test-1"]], "A note for the future.": [[7, "a-note-for-the-future"]], "1D tensor with multiple values.": [[7, "d-tensor-with-multiple-values"]], "2D tensor": [[7, "d-tensor"]], "Gradients with actual geometry": [[7, "gradients-with-actual-geometry"]], "Gradients in DeepINN": [[8, "gradients-in-deepinn"]], "Training dataset": [[9, "training-dataset"]], "Geometry": [[9, "geometry"], [10, "geometry"], [12, "geometry"], [13, "geometry"]], "1D Laplace equation": [[9, "d-laplace-equation"], [10, "d-laplace-equation"]], "Dataset": [[9, "dataset"], [10, "dataset"]], "Basics of network design": [[10, "basics-of-network-design"]], "Forward pass": [[11, "forward-pass"]], "Contribution": [[14, "contribution"]], "Testing": [[14, "testing"]], "Documentation compilation": [[15, "documentation-compilation"]], "Setting up Jupyter-books": [[15, "setting-up-jupyter-books"]], "Installation": [[16, "installation"]], "Using pip": [[16, "using-pip"]], "Docker image": [[16, "docker-image"]], "CPU Only": [[16, "cpu-only"]], "GPU passthrough": [[16, "gpu-passthrough"]], "Tagless copy": [[16, "tagless-copy"]], "DeepINN": [[17, "deepinn"]], "FCNN training": [[12, "fcnn-training"], [13, "fcnn-training"]], "PDE": [[12, "pde"], [13, "pde"]], "Network": [[12, "network"], [13, "network"]]}, "indexentries": {}})