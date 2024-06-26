import sys

import pandas as pd

print(sys.argv)  # prints the command line arguments passed to the script

day = sys.argv[1]

# some fancy stuff with pandas

print(f"job finished successfully for day = f{day}")