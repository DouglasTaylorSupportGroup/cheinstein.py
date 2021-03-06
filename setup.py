import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="cheinsteinpy",
    version="0.1.6",
    author="jckli & okinahiru",
    description="A Python library to get information from Chegg.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DouglasTaylorSupportGroup/cheinstein.py",
    packages=setuptools.find_packages(),
    install_requires=["requests", "beautifulsoup4"]
)