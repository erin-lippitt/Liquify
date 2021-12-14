import setuptools

setuptools.setup(
    name="liquify",
    version="0.1",
    author="Erin Lippitt",
    author_email="erin.lippitt@yale.edu",
    description="Perform preprocessing and water classification of Landsat 8 data",
    packages=["liquify","liquify/load_data","liquify/imaging"]
)