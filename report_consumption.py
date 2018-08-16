#!/bin/env python
from logfile_tools import generate_dataframe_from_mpiesm_logfile, compute_effective_throughput, generate_dataframe_from_mpiesm_logfile, generate_table_walltime

import sys

logfile_df = generate_dataframe_from_mpiesm_logfile(sys.argv[1])
print(logfile_df)

generate_table_walltime(logfile_df)
generate_table_time_between_runs(logfile_df)



compute_effective_throughput(logfile_df)
