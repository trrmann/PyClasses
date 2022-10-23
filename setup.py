import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "PyClasses",
    version = "0.0.1",
    author = "Tracy Mann",
    author_email = "trmann70@hotmail.com",
    description = "my PyClasses library package",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/trrmann/PyClasses",
    project_urls = {
#        "Math": "https://github.com/trrmann/cse110-27/tree/master/classes/Math"
    },
    license = "GNU GPLv3",
    #packages = ["cse110-27"],
    packages = ["ClassesPackage", "CodeTestingPackage", "SciencePackage", "MathPackage"],
    #install_requires = ["Math"],
    install_requires = []
)
