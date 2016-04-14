#!/bin/bash

BirdID="B1235"

cubepath="mnt/cube/Ice/"

matsrc="$cubepath""$BirdID""/matfiles/"
matdest="$cubepath""kperks/""$BirdID""/matfiles/"
echo $matsrc $matdest

rsync -gloptruv $matsrc $matdest

klustaID="phy012716"
#physrc="$cubepath""$BirdID""/klusta
physrc="GitHub/NetworkCorrManipExpt/Ice/rsync/""$BirdID""/klusta/""$klustaID""/"
phydest="$cubepath""kperks/""BirdID""/klusta/""$klustaID""/"
#echo $physrc
#echo $phydest
rsync -gloptruv physrc phydest

#copy klusta files from /Users/kperks/ to Ice/kperks/bird