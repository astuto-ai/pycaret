def version():
    from onelens.onelens_pycaret import version_

    return version_


# Hack to lazy import __version__ from `onelens_pycaret`.
# Needed to avoid a circular dependency.
def __getattr__(name):
    if name in ("__version__", "version_"):
        return version()
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
