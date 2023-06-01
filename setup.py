import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Pytrace_EyeOfThePython",
    version = "0.0.1",
    author = "Erik Frandofer",
    author_email = "erik.frandofer.365@gmail.com",
    description = "Python tracing application",
    # long_description = long_description,
    # long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)
