#!/usr/bin/bash.exe
if [[ -d /c/Users/Public/OneDrive/Documents/Projects/Python/packages/PyClasses/profile.d ]];
then
  PROFILE_SHELLS=`ls /c/Users/Public/OneDrive/Documents/Projects/Python/packages/PyClasses/profile.d/*.sh 2>/dev/null|wc -l`
  if [[ ${PROFILE_SHELLS} == "" ]];
  then
    echo > /dev/null
  elif [[ ${PROFILE_SHELLS} -gt 0 ]];
  then
    for pyClassesProfileFile in `ls /c/Users/Public/OneDrive/Documents/Projects/Python/packages/PyClasses/profile.d/*.sh`
    do
      source ${pyClassesProfileFile};
    done;
  fi
fi