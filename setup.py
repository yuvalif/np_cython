from distutils.core import setup, Extension
from Cython.Build import cythonize

extensions = [
        Extension("compute_cy", ["compute_cy.pyx"]),
        Extension("compute_type_cy", ["compute_type_cy.pyx"])
]
#define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')]

setup(ext_modules=cythonize(extensions, language_level = "3"))

