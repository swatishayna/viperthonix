from setuptools import setup
import setuptools
import pathlib




HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md" ).read_text()
setup(
    name ="viper-thonix",
    version ="1.0.0",
    description ="Tool to perform basic operations on your Dataset",
    author="Swati Pandey",
    #url = "https://github.com/swatishayna/viperthon.git",
    long_description =README,
    long_description_content_type = "text/markdown",
    license = "MIT",
    keyword =["read csv", "basic operations on dataset","read categorical column"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    packages = ["viperthonix"],
    include_packages_data =True,
    install_requires = ["pandas","pyinputplus"],
    entry_points = {
        "console_scripts" : [
            "viperthonix = viperthonix.__main__:main",
        ]
    }







)