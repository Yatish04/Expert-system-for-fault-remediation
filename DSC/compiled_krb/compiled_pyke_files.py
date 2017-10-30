# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'Remedy.kfb'):
           [1509376379.984834, 'Remedy.fbc'],
         ('', '', 'Remedyrule.krb'):
           [1509376380.0161219, 'Remedyrule_bc.py'],
        },
        compiler_version)

