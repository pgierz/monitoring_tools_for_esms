#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import argparse
import mpiesm_logfile_tools

def parse_arguments():
    parser = argparse.ArgumentParser(description='Tells you how long you are spending in the queue')
    parser.add_argument('-p', '--plot', action="store_true")
    parser.add_argument('log_file', nargs="*")
    return parser.parse_args()


def main():
    args = parse_arguments()
    mpiesm_log_files = args.log_file
    all_means=pd.DataFrame()
    for log in mpiesm_log_files:
        log_dataframe = mpiesm_logfile_tools.generate_dataframe_from_mpiesm_logfile(log)
        time_between_starts_df = mpiesm_logfile_tools.generate_table_time_between_runs(log_dataframe)

        all_means[log.split("/")[-1].split(".")[0]] = time_between_starts_df.mean()

        if args.plot:
            time_between_starts_df.plot(legend=False)
            plt.title(log.split("/")[-1].split(".")[0])
            plt.ylabel("Time between Model Starts (minutes)")
            plt.xlabel("Date")
            plt.hold()
    all_means["Average"] = all_means.mean(axis=1)
    print(all_means.transpose())
    if args.plot: plt.show()

if __name__ == '__main__':
    main()
