#!/bin/bash
if [ $(hostname) = "ollie1" ] || [ $(hostname) = "ollie0" ]
then
    account_settings=""
else
    account=$1
    account_settings="-A $account"
fi

list_of_users_and_runs=$(squeue $account_settings --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 4,5 | sort | grep -v NAME)
# echo ${list_of_users_and_runs}
list_of_unique_users=$(squeue $account_settings --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 5 | sort | grep -v USER | uniq )
#echo ${list_of_unique_users}
for user in ${list_of_unique_users}
do
    echo "There are $(squeue -u ${user} | tr -s ' ' | wc -l) jobs running on the squeue from ${user}!"
    echo -e "\n"
done
