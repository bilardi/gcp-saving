"""GCP saving package

This package contains the modules for managing your services timelife and costs.
The package works if you have added some tags on your objects:
see the documentation on https://gcp-saving.readthedocs.io/en/latest/

It is part of the educational repositories (https://github.com/pandle/materials)
to learn how to write stardard code and common uses of the TDD.

Package contents two main classes: Saving, the main class, and Service,
the class extended by each class that implements an GCP service.

    >>> import gcp_saving
    >>> help(gcp_saving)
    >>> import gcp_saving.saving as Saving
    >>> help(Saving)

# license MIT
# support https://github.com/bilardi/gcp-saving/issues
"""
__version__ = '0.0.1'
__author__ = 'Alessandra Bilardi'
