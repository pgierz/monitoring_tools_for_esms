import pandas as pd

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

def generate_table_time_between_runs(log_dataframe):
    data_dict={log_dataframe.index[i]: (log_dataframe.index[i+1]-log_dataframe.index[i]).total_seconds()/60.
               for i in range(len(log_dataframe.index)-1)
               if log_dataframe["State"][i] == " done"}
    return pd.DataFrame(data=data_dict, index=["Time between Run"]).transpose()
