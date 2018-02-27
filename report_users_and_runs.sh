#!/bin/bash
if [ $(hostname) = "ollie1" ] || [ $(hostname) = "ollie0" ]
then

list_of_users_and_runs=$(squeue --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 4,5 | sort | grep -v NAME)
# echo ${list_of_users_and_runs}
list_of_unique_users=$(squeue --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 5 | sort | grep -v USER | uniq )
#echo ${list_of_unique_users}
for user in ${list_of_unique_users}
do
    echo "There are $(squeue -u ${user} | tr -s ' ' | wc -l) jobs running on the squeue from ${user}!"
    echo -e "\n"
done

else

account=$1
list_of_users_and_runs=$(squeue -A $account --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 4,5 | sort | grep -v NAME)
# echo ${list_of_users_and_runs}
list_of_unique_users=$(squeue -A $account --format='%.18i %.9P %.30j %.8u %.2t %.10M %.6D %R' | tr -s ' ' | cut -d ' ' -f 5 | sort | grep -v USER | uniq )
#echo ${list_of_unique_users}
for user in ${list_of_unique_users}
do
    echo "${user} is $(finger ${user} | awk '{printf("%s %s\n", $4, $5);}' | head -n 1)"
    echo "There are $(squeue -A $account -u ${user} | tr -s ' ' | wc -l) jobs running on the $account queue from this person!"
    echo -e "\n"
done
fi
