import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="conga_office",
    version="0.2.0",
    author="Jose Mielgo",
    author_email="mielgosez@gmail.com",
    description="Python library thought to active conga-office in order to appear online to your employer while "
                "grabbing a coffee or having creativity sessions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mielgosez/conga_office",
    project_urls={
        "Bug Tracker": "https://github.com/mielgosez/conga_office/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["pyautogui",
                      "requests",
                      "numpy"]
)
