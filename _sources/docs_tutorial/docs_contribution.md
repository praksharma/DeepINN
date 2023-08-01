
# Documentation compilation
The doc is created using [Jupyter-book](https://jupyterbook.org/en/stable/intro.html).

### Setting up Jupyter-books
These steps will allows you to create a basic setup. For more details visit [here](https://jupyterbook.org/en/stable/start/your-first-book.html). 
1. Create a new Python virtual environment or use an existing one.

```sh
python3 -m venv jupyter_env
```

2. Install Jupyter-book.
```sh
pip3 install -U jupyter-book
```

3. Create a template for quick start.
```sh
jupyter-book create docs/
```
This will create a directory in the ```$PWD``` named ```docs/```. The table of contents are stored in ```_toc.yml``` and the configuration is stored in ```_config.yml```.

4. Building a project

```
jupyter-book build docs/
```

For a full rebuild:

```
jupyter-book build --all docs/
```

If the toc doesn't update. This will update the entire project.

5. Publish the docs in the new branch.

```
ghp-import -n -p -f docs/_build/html
```

6. Deploy website
Go to "Settings->Pages" of the repo. Set the "Source" to "Deploy from a branch". In the "Branch", select the "gh-pages" branch and location as the "/root".

7. GitHub pages force build
GitHub pages is known for its laziness. To force deploy the website go to "Setting->Pages". Here, search for the following line:

> Your site was last deployed to the github-pages environment by the pages build and deployment workflow.

Click on "pages build and deployment" and click on the button "Re-run all jobs" on the top right corner.

8. Include notebooks outside the docs/ directory
You can create a soft link in the book directory to the directory with the notebooks you want to include:
```sh
ln -s ../Tutorials ./Tutorials   
```

You can also link to a document as follows:

```sh
ln -s ../../README.md ./README.md
```