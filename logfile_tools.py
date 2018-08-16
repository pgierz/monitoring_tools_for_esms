import pandas as pd
import datetime

def generate_dataframe_from_mpiesm_logfile(log):
    log_dataframe = pd.read_table(log,
                                  sep=r" :  | -" ,
                                  skiprows=1,
                                  infer_datetime_format=True,
                                  names=["Date", "Message", "State"],
                                  engine='python', index_col=0)
    middle_column = log_dataframe["Message"].apply(lambda x: pd.Series(str(x).split()))
    log_dataframe.drop("Message", axis=1, inplace=True)
    middle_column.columns = ["Run Number", "Exp Date", "Job ID"]
    log_dataframe = pd.concat([log_dataframe, middle_column], axis=1)
    log_dataframe.set_index(pd.to_datetime(log_dataframe.index), inplace=True)
    return log_dataframe

def remove_duplicate_starts(log_dataframe):
        for JOB_ID in log_dataframe:
                pass



def generate_table_walltime(log_dataframe):
    remove_duplicate_starts(log_dataframe)
    starts = log_dataframe[log_dataframe.State == " start"][["Run Number"]]; ends = log_dataframe[log_dataframe.State == " done"][["Run Number"]]
    print(ends.index - starts.index) 

def generate_table_time_between_runs(log_dataframe):
    starts = log_dataframe[log_dataframe.State == " start"][["Run Number"]]; ends = log_dataframe[log_dataframe.State == " done"][["Run Number"]]
    print(starts-ends)

def compute_effective_throughput(log_dataframe, verbose=True):
    starts = log_dataframe[log_dataframe.State == " start"]; ends = log_dataframe[log_dataframe.State == " done"]
    starts = starts.index.to_datetime().tolist(); ends = ends.index.to_datetime().tolist()
    starts = starts[:len(ends)]  # FIXME: the needs to be checked in both directions, and always norm to the shorter list
    diffs = [ends[i] - starts[i] for i in range(len(ends))]
    average_timedelta = sum(diffs, datetime.timedelta(0)) / len(diffs)
    DAY = datetime.timedelta(1)
    throughput = DAY / average_timedelta
    if verbose:
        print("Your run is taking %s on average" % average_timedelta)
        print("this is an effective throughput of %s simulated runs per day, assuming no queue time" % throughput)
    return average_timedelta, throughput
