# UFO Model Generation

Here is described how to generate events including gridpacks for the VLL UFO model (or similar). These instructions were prepared for the LPC machines but it should also work on lxplus.

## GridPack Generation

Step 1. Clone the whole genproductions from git and work there. Checkout the commit that I used when I made my VLL gridpacks. This example uses a Madgraph model, so that will be the working directory.

```
mkdir MyGeneration
cd MyGeneration
git clone -b mg265UL https://github.com/cms-sw/genproductions.git
cd genproductions
cd bin/MadGraph5_aMCatNLO # working directory
```

Step 2. Clone the templates in this repository in the cards directory (includes VLL UFO model)

```
cd cards
git clone https://github.com/danielguerrero/UFOModelGeneration.git
```

Step 3. Edit the template as needed. There four files:

customizecards.dat: It sets what parameters of the model you would like to vary using the generate_grid.py script, e.g. the particle masses

extramodels.dat: It sets the model tar, e.g. vlepton_pseudoscalar_ufo.tar.gz

proc_card.dat: It contains the Madgraph commands to generate the process

run_card.dat: It is a standard Madgraph run_card used in CMS

Step 4. Generate a grid of points. This example varies both the taup and atau masses. Each variation will have its own folder, e.g. VLLs2LLPs_MVLL_200_MA_2_CTAU_850

```
cd UFOModelGeneration
python generate_grid_ctau.py
```

Step 5 Edit the gridpack_generation.sh script in the working directory to load your model properly. If the model is not online (cms-project-generators), then comment that line and add one to copy it from your local directory.

```
#wget --no-check-certificate https://cms-project-generators.web.cern.ch/cms-project-generators/$model
cp /uscms/home/guerrero/nobackup/Run2/LLPS20222/ULGeneration/genproductions/bin/MadGraph5_aMCatNLO/cards/UFOModelGeneration/$model . #mine
```

Step 6. Generate the gridpack in working directory. There are three outputs: a folder, a tarball and a log.

```
source gridpack_generation.sh VLLs2LLPs_MVLL_200_MA_2_CTAU_850 cards/UFOModelGeneration/VLLs2LLPs_MVLL_200_MA_2_CTAU_850
```
The final message should be something like this "Gridpack created successfully at Gridpack created successfully at /uscms/home/guerrero/nobackup/Run2/LLPS20222/ULGeneration/genproductions/bin/MadGraph5_aMCatNLO/VLLs2LLPs_MVLL_200_MA_2_CTAU_850_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz"

