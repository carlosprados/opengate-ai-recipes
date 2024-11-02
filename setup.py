from setuptools import setup, find_packages

setup(
    name="mlflowx-recipes",
    version="0.1.0",
    author="Carlos Prados",
    author_email="carlos.prados@gmail.com",
    description="An extensible fork of MLflow Recipes that allows easy integration of new machine learning workflows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/carlosprados/mlflowx-recipes",
    packages=find_packages(),
    install_requires=[
        "mlflow>=1.25.0",  # Ensure compatibility with MLflow
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "mlflowx-recipes = mlflowx_recipes.cli:main",  # Example of adding a CLI entry point
        ],
    },
)
