from setuptools import setup, find_packages
import codecs
import os

# pwd
here = os.path.abspath(os.path.dirname(__file__))

# Long description of the project
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="DeepINN",
    version='{{VERSION_PLACEHOLDER}}',
    author="Prakhar Sharma",
    author_email="prakhars962@gmail.com",
    description="A Physics-informed neural network (PINN) library.",
    url = "https://deepinn.readthedocs.io/en/latest/index.html",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords = ["Differential equations", "Physics-informed neural networks"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)