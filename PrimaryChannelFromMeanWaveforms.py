import sys
import os

# os.chdir('/mnt/cube/Ice/kperks/B1087/klusta/phy040116/Pen03_Lft_AP0_ML500__Site01_Z2200__B1087_cat_P03_S01_1/')
pwd_path=os.getcwd()
print pwd_path
BirdID=pwd_path.split('/')[7]
klustaID=pwd_path.split('/')[9]
SiteID=pwd_path.split('/')[10]
# BirdID=pwd_path.split('/')[5]
# klustaID=pwd_path.split('/')[7]
# SiteID=pwd_path.split('/')[8]
phydir=SiteID[SiteID.find(BirdID):len(SiteID)] + '.phy/'
subj_dir_path=pwd_path[0:pwd_path.find(BirdID)]

print BirdID, klustaID, SiteID
import numpy as np
from os import mkdir, listdir
from os.path import join, splitext, exists
import time
import scipy.io as sio
import imp
import array

numchannels_array = sys.argv
numchannels = int(numchannels_array[1])

def file_list(folder):
    return [(folder, filename) for filename in listdir(folder)]

klustadir= subj_dir_path + '/'.join((BirdID, "klusta", klustaID, SiteID))
phymetadir= '/'.join((klustadir, phydir, "cluster_store/0/main/"))
filesphy = file_list(phymetadir)
is_mean_waveform = [file_entry[1] for file_entry in filesphy if '.mean_waveform' in file_entry[1]]
cluster_id = np.zeros((len(is_mean_waveform)))
# primary_prb_port = np.zeros((len(is_mean_waveform)))
prb_location_microns = np.zeros((len(is_mean_waveform),2))
filesklusta = file_list(klustadir)
prb_file_arr = [file_entry[1] for file_entry in filesklusta if '.prb' in file_entry[1]]
prb_file_name = prb_file_arr[0]
a = '/'.join((klustadir,prb_file_name))

# -*- coding: utf-8 -*-
prb_info = imp.load_source('probe_file','/'.join((klustadir,prb_file_name)))
chan_index_order = prb_info.channel_groups[0]['channels']
chan_geometry = prb_info.channel_groups[0]['geometry']
waveform_filename = is_mean_waveform[0]
cluster_id = waveform_filename.split('.')[0]

cluster_id = np.zeros((len(is_mean_waveform)))
for idx, waveform_filename in enumerate(is_mean_waveform):
    cluster_id[idx] = waveform_filename.split('.')[0]
    
    waveformsfile = phymetadir + waveform_filename
    arr = np.fromfile(waveformsfile, dtype=np.float32)
    arr = np.reshape(arr, (1,-1,numchannels))

    allvars = arr.var(axis=1)
    
    primary_chan_index = allvars[0].argmax()
    prb_geometry_index = chan_index_order[primary_chan_index]
    prb_location_microns[idx] = chan_geometry[prb_geometry_index]
    
makedict = {'cluster_id':cluster_id,'prb_location_microns':prb_location_microns}
savename = '/'.join((klustadir, 'cluster_info.mat'))
sio.savemat(savename,makedict)
print 'saved to:  ' + savename