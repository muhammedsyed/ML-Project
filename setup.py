from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements] 

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements



setup (
    name="ml-project",
    version='0.0.1',
    author='muhammedsyed',
    author_email='muhammedsyed21@outlook.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)