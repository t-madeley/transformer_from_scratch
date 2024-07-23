from setuptools import find_packages, setup

with open("requirements.txt", "r") as fh:
    install_requires = [req for req in fh.read().splitlines() if "==" in req]

setup(
    name="transformer_from_scratch",
    version="0.0.1",
    description="Take Home Task - Transformers and Analysis",
    author="t-madeley",
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=["pytest", "pytest-cov"],
    python_requires="==3.11.*",
    package_data={"prevayl_takehome": ["conf/*.*"]},
    include_package_data=True,
    entry_points={"console_scripts": ["transformer_from_scratch=transformer_model.__main__:cli"]}

)
