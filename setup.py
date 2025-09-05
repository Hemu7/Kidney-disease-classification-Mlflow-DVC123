import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
___version___ = "0.0.0"

REPO_NAME = "Kidney-disease-classification-Mlflow-DVC"
AUTHOR_USER_NAME = "hemu7"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "hemanthchowdary0766@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=___version___,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN based classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)