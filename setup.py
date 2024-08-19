from setuptools import find_packages, setup
from typing import List

# HYPHEN_E_DOT = "-e ."


# def get_requirements(filename):

#     requirements = []
#     with open(filename) as f1:
#         requirements = f1.readlines()
#         requirements = [req.replace["\n"," "] for req in requirements]
        
#         if HYPHEN_E_DOT == requirements:
#             requirements.remove(HYPHEN_E_DOT)

#     return requirements


setup(
    
    name ="MLProject1",
    version = "0.0.1",
    author = "Soham",
    author_email= "sohamjagrit@gmail.com",
    packages = find_packages(),
    install_requires = ['pandas', 'numpy']
)