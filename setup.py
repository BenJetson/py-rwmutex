import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rwmutex",  # Replace with your own username
    version="1.0",
    author="Ben Godfrey",
    author_email="BenJetson@users.noreply.github.com",
    description="Provides a read/write mutex lock usable with context managers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BenJetson/py-rwmutex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
