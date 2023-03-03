import os
from setuptools import setup, find_packages, Extension
import configparser
import importlib
import pathlib
import platform

# Import only version.py file for extracting the version
spec = importlib.util.spec_from_file_location('version', './pycodata/version.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# user dir
user_dir = pathlib.Path(os.path.expanduser("~"))

# configuration file in user home
cfg_user = configparser.RawConfigParser()
cfg_path = user_dir / "pycodata-site.cfg"
if cfg_path.exists():
    cfg_user.read(cfg_path)

# configuration file in package
cfg_package = configparser.RawConfigParser()
cfg_path = pathlib.Path("site.cfg")
if cfg_path.exists():
    cfg_package.read(cfg_path)

# Set dirs for codata library
cfg_dict = {"CODATA": {"libraries": "codata",
                       "include_dirs": "/usr/lib/include,/usr/local/include,"\
                                       +"C:/Program Files/codata/include,"\
                                       +os.path.expanduser("~")+"/codata/include,"\
                                       +os.path.expanduser("~")+"/.local/include",
                       "library_dirs": "/usr/lib,/usr/local/lib,"\
                                       +"C:/Program Files/codata/lib,"\
                                       +os.path.expanduser("~")+"/codata/lib,"\
                                       +os.path.expanduser("~")+"/.local/lib"}}

cfg = configparser.RawConfigParser()
cfg.read_dict(cfg_dict)
cfg.update(cfg_user)
cfg.update(cfg_package)

codata_include_dirs = cfg["CODATA"]["include_dirs"].split(",")
codata_library_dirs = cfg["CODATA"]["library_dirs"].split(",")
codata_libraries = cfg["CODATA"]["libraries"].split(",")

print("Looking for codata.h...")
for dir in codata_include_dirs:
    fdir = pathlib.Path(dir)
    fpath = fdir / "codata.h"
    print(f"\t{fpath}...{fpath.exists()}")

if platform.system() == "Windows":
    prefix = ""
    ext_shared = ".dll"
    ext_static = ".lib"
elif platform.system() == "Darwin":
    prefix = "lib"
    ext_shared = ".dylib"
    ext_static = ".a"
else:
    prefix = "lib"
    ext_shared = ".so"
    ext_static = ".a"
print("Looking for codata library...")
for dir in codata_library_dirs:
    fdir = pathlib.Path(dir)
    fpath = fdir / (prefix+"codata"+ext_shared)
    print(f"\t{fpath}...{fpath.exists()}")
    fpath = fdir / (prefix+"codata"+ext_static)
    print(f"\t{fpath}...{fpath.exists()}")

mod_ext = Extension(name="pycodata._codata",
                                         sources=["./pycodata/_codata.c"],
                                         libraries=codata_libraries,
                                         library_dirs=codata_library_dirs,
                                         include_dirs=codata_include_dirs)
setup(name=mod.__package_name__,
      version=mod.__version__,
      maintainer=mod.__maintainer__,
      maintainer_email=mod.__maintainer_email__,
      author=mod.__author__,
      author_email=mod.__author_email__,
      description=mod.__package_name__,
      long_description=pathlib.Path("README.rst").read_text(encoding="utf-8"),
      url='https://milanskocic.github.io/pycodata/index.html',
      download_url='https://github.com/MilanSkocic/pycodata',
      packages=find_packages(),
      include_package_data=True,
      python_requires='>=3.7',
      install_requires=pathlib.Path("requirements.txt").read_text(encoding="utf-8").split('\n'),
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 3 :: Only",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Programming Language :: Python :: 3.11",
                   "Topic :: Scientific/Engineering",
                   "Operating System :: OS Independent"],
        ext_modules=[mod_ext]
      )


# pypi
# >>> python setup.py sdist bdist_wheel
# >>> python -m twine upload dist/*
# >>> python -m twine upload --repository testpypi dist/*