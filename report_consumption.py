#!/bin/env python
from mpiesm_logfile_tools import generate_dataframe_from_mpiesm_logfile, compute_effective_throughput
import sys

logfile_df = generate_dataframe_from_mpiesm_logfile(sys.argv[1])
compute_effective_throughput(logfile_df)
