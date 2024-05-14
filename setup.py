import setuptools
with open('README.md','r',encoding="utf-8") as f:
    long_description=f.read()

__version__= "0.0.0"

REPO_NAME= "Text_Summariser"
AUTHOR_USER_NAME= 'Vikash'
SRC_REPO= 'textsummarizer'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="text summarization project",
    long_description_content= "text/makdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url={
        "BUG tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)