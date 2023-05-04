from setuptools import setup, find_packages

setup(
    name='functionTest',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.23.2',
        'Pillow==9.2.0',
        'torch==1.13.1',
        'torchaudio==0.13.1',
        'torchvision==0.14.1',
        'opencv-python==4.7.0.68',
    ],
)