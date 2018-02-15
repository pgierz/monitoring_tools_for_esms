#!/usr/bin/env python
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import argparse


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
        log_dataframe = pd.read_table(log, 
                                      sep=r" :  | -" , 
                                      skiprows=1, 
                                      infer_datetime_format=True,
                                      names=["Date", "Message", "state"], 
                                      engine='python', index_col=0)
        middle_column = log_dataframe["Message"].apply(lambda x: pd.Series(str(x).split()))
        log_dataframe.drop("Message", axis=1, inplace=True)
        middle_column.columns = ["Run Number", "Exp Date", "Job ID"]
        log_dataframe = pd.concat([log_dataframe, middle_column], axis=1)
        log_dataframe.set_index(pd.to_datetime(log_dataframe.index), inplace=True)

        data_dict={log_dataframe.index[i]: (log_dataframe.index[i+1]-log_dataframe.index[i]).total_seconds()/60.
                   for i in range(len(log_dataframe.index)-1)
                   if log_dataframe["state"][i] == " done"}

        time_between_starts_df = pd.DataFrame(data=data_dict, index=["Time between Run"]).transpose()

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
