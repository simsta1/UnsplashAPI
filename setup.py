from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Inofficial API Wrapper for Unsplash API'
LONG_DESCRIPTION = 'A package which allow python users to easily interact with the UnplashAPI'

# Setting up
setup(
    name="unsplashapi",
    version=VERSION,
    author="SimonStaehli",
    author_email="<simon.staehli@students.fhnw.ch>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'api', 'unsplash api', 'unsplash'],
    python_requires='>=3',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)