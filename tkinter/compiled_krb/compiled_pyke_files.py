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
           [1510041704.128401, 'Remedy.fbc'],
         ('', '', 'Remedyrule.krb'):
           [1510041704.1384315, 'Remedyrule_bc.py'],
        },
        compiler_version)

