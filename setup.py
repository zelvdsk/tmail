import setuptools

setuptools.setup(
    author= 'Ipan (zelvdsk)',
    description= 'Free temporary email',
    entry_points= {'console_scripts': ['tmail=tmail:TMail']},
    install_requires= [
        'requests', 
        'bs4'
    ],
    long_description= open("README.md").read(),
    long_description_content_type= "text/markdown",
    url= "https://github.com/zelvdsk/tmail",
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords= [
        'tmail', 'temporary email', 'email sementara', 'gmail', 'temp mail',
        '10 minute mail', 'free temporary email', 'free temp mail'
    ],
    name= 'tmail',
    packages=setuptools.find_packages(),
    version='1.0.9'
)
