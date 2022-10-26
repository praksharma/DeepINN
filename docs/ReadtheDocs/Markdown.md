# A Markdown example

We can't preview a markdown file in RST preview too, so we need to download a separate makrdown preview tool in VS Code.

We can write code:

```python
import numpy as np
a = np.array([1,2,3])
```

We can also use Latex I guess.

$$u_{xx}=\alpha \frac{\partial u^2}{\partial ^2 x}$$

I think we can't type equations this way. but we can use `nbsphinx` to include `ipynb` files. Then we cna simply write Iron Python files and include it in the `.. toctree`.

First we need to install `nbsphinx`.

```bash
pip install nbsphinx
```
If you have Jupyter Lab installed then also install the Pandoc using

```python
conda install -c conda-forge pandoc
```

but first check if you have `pandoc` already installed.

```python
pip list | grep nbconvert 
```

Add the following in the `conf.py`.
```bash
extensions = ['myst_parser','nbsphinx']
```

Now you can add `ipynb` files without the extension in the `.. toctree`. 