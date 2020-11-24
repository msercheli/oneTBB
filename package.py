name = "tbb"

version = "2021.1.0"

authors = ["Intel"]

requires = [
    "gcc",
    "cmake",
]

def commands():
    env.TBB_ROOT = "{root}"
    env.TBB_LOCATION = "{root}"
