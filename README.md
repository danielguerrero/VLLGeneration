# VLLGeneration

Here is described how to generate events including gridpacks for the VLL UFO model (or similar)

## GridPack Generation

Step 1. Clone the whole genproductions from git and work there. This example uses a Madgraph model, so that will be the working directory.
```
mkdir VLLGeneration
cd VLLGeneration
git clone https://github.com/cms-sw/genproductions.git
cd /VLLGeneration/genproductions/bin/MadGraph5_aMCatNLO # working directory
```

Step 2. Clone the templates in this repository in the cards directory
```
cd cards
git clone https://github.com/danielguerrero/UFOModelGeneration.git
```

Step 3. Edit the template as needed. There four files:

customizecards.dat: It sets what parameters of the model you would like to vary using the generate_grid.py script, e.g. the particle masses.
extramodels.dat: It sets the model tar, e.g. vlepton_pseudoscalar_ufo.tar.gz
proc_card.dat: It contains the Madgraph commands to generate the process
run_card.dat: It is a standard Madgraph run_card used in CMS

Step 4. Generate a grid of points. This example varies both the taup and atau masses. Each variation will have its own folder, e.g. VLLs2LLPs_MVLL_100_MA_10

```
python generate_grid.py
```
Step 5. Generate the gridpack in working directory. There are three outputs: VLLs2LLPs_MVLL_100_MA_10 (folder), VLLs2LLPs_MVLL_1000_MA_10_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz and VLLs2LLPs_MVLL_100_MA_10.log.
```
cd ../../
source gridpack_generation.sh VLLs2LLPs_MVLL_100_MA_10 cards/UFOModelGeneration/VLLs2LLPs_MVLL_100_MA_10
```

