from __future__ import print_function

import os

debug = os.environ.get("DEBUG", False)
input_directory = "."
output_directory = "."
skip_shows = False
# should be one of raise, warn, skip
assertions = "raise"
show_timings = True
# should be one of periods, functions, procedures (deprecated), processes
log_level = "functions"
autodump = None
autodump_file = None
autodiff = None