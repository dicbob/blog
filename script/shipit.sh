#!/bin/bash
#This script assumes you have git, pelican (http:/getpelican.com), python, and its respective dependencies installed

GITREPO='https://github.com/dicbob/blog.git'
WEBROOT=/usr/share/nginx/www  #Webserver Root Dir
#WEBROOT=/usr/share/nginx/www  #Webserver Root Dir
PHP_CONFIG=$1  #Location of the private config.php
STATUS=0
DATE=`date +%Y%b%d%s`
#Make a temp dir for the git clone or FAIL
TMPDIR=$(mktemp -d /tmp/shipit.XXXXX) || { echo "Failed to create temp file"; exit 1; }
TMPFILE=$TMPDIR/log.out

##mail function
sendmail() {
STATUS_TXT="$1"
SUBJECT="Push Status:$STATUS_TXT"
EMAIL="me@dicbo.bz"
EMAILMESSAGE="$TMPFILE"
/usr/bin/mail -s "$SUBJECT" "$EMAIL" < $EMAILMESSAGE
}

#Move to the temp dir, clone blog repo, and copy local private files
cd $TMPDIR && git clone $GITREPO &>> $TMPFILE && cd blog && mkdir -p output && STATUS=1

#Im relying on the exit code of the Makefile html target,  anything other than exit 0 breaks the script.

if [ $STATUS = 1 ] #See if clone was succesful
then	
	make html &>> $TMPFILE && cp -R $TMPDIR/blog/output/* $WEBROOT && cp -R $TMPDIR/blog/yourls/* $WEBROOT && cp $PHP_CONFIG $WEBROOT/user/ && STATUS=2
fi
#did Make and publish run properly?
if  [ $STATUS = 2 ] 
then
	echo "Push Complete $DATE" &>> $TMPFILE
        sendmail Success || { echo "Mail=Fail Push=Succuess\n" &>> $TMPFILE; cp $TMPFILE ~/log.out.$DATE; }
        rm -rf $TMPDIR	
elif [ $STATUS = 0 ]
then	
	echo "Error\n" &>> $TMPFILE
	echo "Push Incomplete $DATE" &>> $TMPFILE
        sendmail Make-Fail || { echo "Mail=Fail Push=Fail\n" &>> $TMPFILE; cp $TMPFILE ~/log.out.$DATE; }
        rm -rf $TMPDIR
else 
	echo "Unknown Error\n" &>> $TMPFILE
        echo "Push Incomplete $DATE" &>> $TMPFILE
        sendmail Unknown-Fail || { echo "Mail=Fail Push=Fail\n" &>> $TMPFILE; cp $TMPFILE ~/log.out.$DATE; }
        rm -rf $TMPDIR
fi


