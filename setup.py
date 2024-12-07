from setuptools import setup, find_packages
# from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT])
    return requirements



with open("README.md","r",encoding="utf-8") as f:
    long_description  = f.read()

__version__ = "0.0.1"
REPO_NAME = "Python_Package_PyPi"
PKG_NAME = "mongoDBconnector_test"
AUTHOR_NAME = "Singhal-Piyush"
AUTHOR_EMAIL = "test@gmail.com"

setup(
    name = PKG_NAME,
    version= __version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with MongoDB in initial testing phase",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements("./requirements_dev.txt")

)