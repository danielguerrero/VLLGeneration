# UFO Model Generation

Here is described how to generate events including gridpacks for the VLL UFO model (or similar). These instructions were prepared for the LPC machines but it should also work on lxplus.

## GridPack Generation

Step 1. Clone the whole genproductions from git and work there. Checkout the commit I used to make the VLL gridpacks. This example uses a Madgraph model, so that will be the working directory.

```
mkdir MyGeneration
cd MyGeneration
git clone -n https://github.com/cms-sw/genproductions.git
cd genproductions
git checkout -b mygenbranch 60944bc193e0df84dd58a01d3e41e5a9a8e21e24
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

Step 4. Generate a grid of points. This example varies both the taup and atau masses. Each variation will have its own folder, e.g. VLLs2LLPs_MVLL_100_MA_10

```
python generate_grid.py
```

Step 5 Edit the gridpack_generation.sh script in the working directory to load your model properly. If the model is not online (cms-project-generators), then comment that line and add one to copy it from your local directory.

```
#wget --no-check-certificate https://cms-project-generators.web.cern.ch/cms-project-generators/$model
cp /uscms/home/guerrero/nobackup/Run2/LLPS20222/MyGeneration/genproductions/bin/MadGraph5_aMCatNLO/cards/UFOModelGeneration/$model . #mine
```

Step 6. Generate the gridpack in working directory. There are three outputs: VLLs2LLPs_MVLL_100_MA_10 (folder), VLLs2LLPs_MVLL_1000_MA_10_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz and VLLs2LLPs_MVLL_100_MA_10.log.

```
source gridpack_generation.sh VLLs2LLPs_MVLL_100_MA_10 cards/UFOModelGeneration/VLLs2LLPs_MVLL_100_MA_10
```

