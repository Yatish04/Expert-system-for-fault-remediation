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
         ('', '', 'remedyget.krb'):
           [1508658783.2108674, 'remedyget_bc.py'],
         ('', '', 'remedies.kfb'):
           [1508658783.2108674, 'remedies.fbc'],
        },
        compiler_version)

