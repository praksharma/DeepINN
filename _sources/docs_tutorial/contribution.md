# Contribution
Create a `venv` in the root of the repo. Here the assumption is that the `python` is symlink to `python3`.
```sh
python -m venv .venv
```
Activate the environment.
```sh
source .venv/bin/activate
```
Confirm that the Python path is updated.
```sh
which python
```
The `STDOUT` should point to the .venv directory. Now, upgrade the pip.
```sh
python -m pip install --upgrade pip
```
Install the required packages.
```sh
pip install -r requirements.txt
```
If you want to build the docs using the same environment, then install the relevant dependencies.
```sh
pip install -r docs/requirements.txt
```

# Testing
The testing is very simple. Just run the test.py file in the current Python virtual environment.
```sh
python test.py
```
