name = "tbb"

version = "2020.2"

authors = ["Intel"]

requires = [
    "gcc",
    "python",
]

build_command = "python {root}/build/build.py --tbbroot {root} --prefix rezbuild --install-libs --install-devel"

def commands():
    env.TBB_ROOT = "{root}"
    env.TBB_LOCATION = "{root}"
