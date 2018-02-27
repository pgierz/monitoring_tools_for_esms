# Monitoring Tools For ESMs

`assess_queue_times.py` is a python program which tells you how long, on average, your run is spending between the state `done` and the state `start`. To use it, you must:

```bash
$ module load python # on mistral
$ module load anaconda2 # on ollie
$ FILE_LIST="/path/to/experiment/scripts/${EXPID}.log /path/to/next/experiment/scripts/${EXPID}.log ..."
$ ./assess_queue_times.py $FILE_LIST
$ ./assess_queue_times.py -p $FILE_LIST # With the optional flag -p, a plot is made
```

`report_users_and_runs.sh` is a shell script, which tells you how which users are running how many jobs. On `mistral`, give it as a parameter the account name you want to assess, on `ollie`, it lists everyone, since there are no accounts.

```bash
$ ./report_users_and_runs.sh ba0989
# Example output:
a270077 is Paul Gierz
There are 4 jobs running on the ba0989 queue from this person!


a270086 is Xun Gong
There are 16 jobs running on the ba0989 queue from this person!


m211003 is Uwe Mikolajewicz
There are 3 jobs running on the ba0989 queue from this person!


m300019 is Florian Ziemen
There are 2 jobs running on the ba0989 queue from this person!
```

Happy supercomputing!
If you need help with these tools, ask Paul: pgierz@awi.de
