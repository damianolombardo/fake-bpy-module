import os
import datetime
from setuptools import setup, find_packages

cur_dir = os.getcwd().replace("\\", "/")
#blender_version = cur_dir.split('/')[-1].split('-')[-1].replace(".", "")]
blender_version = cur_dir.split('/')[-1].split('-')[-1]
module_name = "fake-bpy-module-{}".format(blender_version)

version = datetime.datetime.today().strftime("%Y%m%d")


setup(
    name=module_name,
    version=version,
    url="https://github.com/nutti/fake-bpy-module",
    author="Nutti",
    author_email="nutti.metro@gmail.com",
    maintainer="Nutti",
    maintainer_email="nutti.metro@gmail.com",
    description="Collection of the fake Blender Python API module for the code completion.",
    long_description="",
    py_modules=[
        "bgl",
        "blf",
        "aud"
    ],
    packages=[
        "bpy",
#        "bgl",
#        "blf",
        "mathutils",
        "gpu",
        "freestyle",
        "bpy_extras",
#        "aud",
        "bmesh"
    ],
    install_requires=[],
    license="MIT",
    classifiers=[
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics :: 3D Rendering",
        "Topic :: Text Editors :: Integrated Development Environments (IDE)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)