#!/usr/bin/bash.exe
CALLED=$0
#echo $CALLED
STATUS=`git status | grep "nothing to commit" | wc -l`
if [[ ${STATUS} -eq 0 ]];
then
  git add --all
  git commit -a -m "deployed"
  git push
  git pull
  reinstallClasses.sh
fi
exit 0