name = "tbb"

version = "2020.2"

authors = [
    "Intel"
]

description = \
    """
    Intel Threading Blocks
    """

requires = [
    "gcc",
]

build_command = "export TBBROOT={root}; make -f {root}/Makefile"

def pre_build_commands():
    pass

def commands():
    pass
