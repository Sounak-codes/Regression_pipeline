from setuptools import find_packages,setup
from typing import List   ## return type of the packages that we are reading

HYPEN_E_DOT='-e .'        ## this will be removed when installing from requirements.txt

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='Sounak',
    author_email='bsounak2@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)