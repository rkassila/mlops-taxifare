from setuptools import find_packages
from setuptools import setup

with open("requirements_prod.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='taxifare',
      version="0.0.12",
      description="TaxiFare Model (api_pred)",
      license="MIT",
      author="Le Wagon",
      author_email="contact@lewagon.org",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      include_package_data=True,
      zip_safe=False)
