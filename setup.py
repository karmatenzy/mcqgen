from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='karma tenzy',
    author_email='karmatenzy408@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPdF2"],
    packages=find_packages()
)