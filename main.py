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

import matplotlib.image


#workaround for -- _tkinter.TclError: invalid command name ".!canvas"
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == LOAD DATA ==
fname = config['epo']
epochs = mne.read_epochs(fname)




reject_criteria_c = config['reject_criteria']
reject_criteria = dict(x.split("=") for x in reject_criteria_c.split(";"))
reject_criteria_n = dict(zip(reject_criteria.keys(), [float(value) for value in reject_criteria.values()]))

flat_criteria_c = config['flat_criteria']
flat_criteria = dict(x.split("=") for x in flat_criteria_c.split(";"))
flat_criteria_n = dict(zip(reject_criteria.keys(), [float(value) for value in flat_criteria.values()]))


epochs.drop_bad(reject=reject_criteria_n, flat=flat_criteria_n)


# == SAVE FILE ==
epochs.save(os.path.join('out_dir','meg-epo.fif'))
epochs.plot_drop_log()


# # == FIGURES ==
plt.figure(1)
fig_ep = epochs.plot_drop_log()
fig_ep.savefig(os.path.join('out_figs','meg_epoch.png'))
