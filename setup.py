from setuptools import find_packages, setup
from typing import List

E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    ''' 
    This function will return the list of requirements.txt of all packages needed
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", " ") for req in requirements]
        
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author= 'jkumar10',
    author_email= 'jitthenkumarr29@gmail.com', 
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
    
)