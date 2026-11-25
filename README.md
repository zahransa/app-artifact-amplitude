<h1 align="center">app-artifact-amplitude</h1>

<p align="center">
  Rejects MEG/EEG epochs whose peak-to-peak amplitude exceeds reject thresholds or falls below flat thresholds per channel type, with MNE-Python drop_bad, and outputs the cleaned epochs and a drop-log plot.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.653"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.653-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Rejects MEG/EEG epochs whose peak-to-peak amplitude exceeds reject thresholds or falls below flat thresholds per channel type, with MNE-Python drop_bad, and outputs the cleaned epochs and a drop-log plot.**

Parses reject and flat criteria given as 'type=value' pairs separated by semicolons (e.g. grad=4000e-13;mag=4e-12;eeg=150e-6) and calls epochs.drop_bad. Use it as a simple amplitude-based artifact rejection after epoching. Both criteria strings must list the same channel types in the same order, because the flat thresholds are keyed by the reject criteria's channel types.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/epochs` |
| **Outputs** | `neuro/meeg/mne/epochs` · `generic/image/png` |
| **Container** | `brainlife/mne:0.23dev` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.653](https://doi.org/10.25663/brainlife.app.653) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `epo` | `neuro/meeg/mne/epochs` | yes | Epoched MEG/EEG data in MNE epochs .fif format. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/epochs` | Epochs (meg-epo.fif) after dropping those that violate the amplitude criteria. |
| `out_figs` | `generic/image/png` | Drop-log plot showing why epochs were rejected. |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `flat_criteria` | string |  | a string that contains the flat criteria (minimum acceptable peak-to-peak amplitudes for each channel type in an epoch) |
| `reject_criteria` | string |  | a string that contains the reject criteria (maximum acceptable peak-to-peak amplitudes for each channel type in an epoch) |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.653](https://doi.org/10.25663/brainlife.app.653), choose `neuro/meeg/mne/epochs` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/epochs`, `generic/image/png`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:0.23dev`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "epo": "/path/to/epo/epo",
       "flat_criteria": "",
       "reject_criteria": ""
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- app-artifact-amplitude. brainlife.io App. [doi:10.25663/brainlife.app.653](https://doi.org/10.25663/brainlife.app.653)
- Taulu S. and Kajola M. Presentation of electromagnetic multichannel data: The signal space separation method. Journal of Applied Physics, 97 (2005). [https://doi.org/10.1063/1.1935742](https://doi.org/10.1063/1.1935742)
- Taulu S. and Simola J. Spatiotemporal signal space separation method for rejecting nearby interference in MEG measurements. Physics in Medicine and Biology, 51 (2006). [https://doi.org/10.1088/0031-9155/51/7/008](https://doi.org/10.1088/0031-9155/51/7/008)
- Gramfort et al. MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience* 7 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Saeed Zahran

**Contributors**

- Saeed Zahran

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>
