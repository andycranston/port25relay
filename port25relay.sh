#! /bin/bash

set -u

PATH=/bin:/usr/bin
export PATH

DEBUG=1
export DEBUG

progname=`basename $0`

address="demo@cranstonhub.com"

if [ ! -d spool ]
then
  echo "$progname: no spool subdirectory" 1>&2
  exit 1
fi

cd spool

if [ $? -ne 0 ]
then
  echo "$progname: unable to change into spool subdirectory" 1>&2
  exit 1
fi

if [ $DEBUG -ne 0 ]
then
  echo "DEBUG: pwd `pwd`"
fi

while true
do
  lockfiles=`ls *.lck 2>/dev/null`

  if [ $DEBUG -ne 0 ]
  then
    echo "DEBUG: lockfiles $lockfiles"
  fi

  if [ "$lockfiles" == "" ]
  then
    if [ $DEBUG -ne 0 ]
    then
      echo "DEBUG: sleeping"
    fi

    sleep 5
  else
    for lockfile in $lockfiles
    do
      if [ $DEBUG -ne 0 ]
      then
        echo "DEBUG: lockfile $lockfile"
      fi

      datafile=`basename $lockfile .lck`

      subject=`grep '^Subject: ' $datafile | head -n 1`

      if [ "$subject" == "" ]
      then
        subject='No subject'
      fi

      if [ $DEBUG -ne 0 ]
      then
        echo "DEBUG: datafile $datafile"
        echo "DEBUG: subject \"$subject\""
      fi

      cat $datafile | ../extractcontent > body.txt

      ../pythonmail.py --address $address --subject "$subject" --content body.txt

      if [ $? -eq 0 ]
      then
        rm -f $lockfile $datafile
      fi
    done
  fi
done
