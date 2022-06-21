# Copyright (c) 2021 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#


# set up environment
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == LOAD DATA ==
fname = config['epo']
epochs = mne.read_epochs(fname)

# == GET CONFIG VALUES ==
reject_mag = config['reject_mag']
reject_grad = config['reject_grad']
reject_eeg = config['reject_eeg']
reject_eog = config['reject_eog']

flat_mag = config['flat_mag']
flat_grad = config['flat_grad']
flat_eeg = config['flat_eeg']




reject_criteria = dict(mag=reject_mag,     # 3000 fT
                       grad=reject_grad,    # 3000 fT/cm
                       eeg=reject_eeg,       # 100 µV
                       eog=reject_eog)       # 200 µV

flat_criteria = dict(mag=flat_mag,          # 1 fT
                     grad=flat_grad,         # 1 fT/cm
                     eeg=flat_eeg)           # 1 µV


epochs.drop_bad(reject=reject_criteria, flat=flat_criteria)


# == SAVE FILE ==
epochs.save(os.path.join('out_dir','meg-epo.fif'))
epochs.plot_drop_log()


# # == FIGURES ==
plt.figure(1)
fig_ep = epochs.plot_drop_log()
fig_ep.savefig(os.path.join('out_figs','meg_epoch.png'))