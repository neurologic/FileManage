#!/bin/bash

BirdID="B1224"
SiteID="Pen01_Lft_AP200_ML1200__Site01_Z2000__B1224_cat_P01_S01_1"
klustaID="phy021216"

cubepath="/Users/kperks/mnt/cube/Ice/"
# diskpath="/Volumes/BookDrive/GitHub/NetworkCorrManipExpt/Ice/rsync/"

matsrc="$cubepath""$BirdID""/matfiles/""$SiteID""/"
physrc="$cubepath""kperks/""$BirdID""/klusta/""$klustaID""/""$SiteID""/"

merge_stim_kwik "$matsrc" "$physrc" 

python /Users/kperks/mnt/cube/Ice/FileManage/PrimaryChannelFromMeanWaveforms.py
