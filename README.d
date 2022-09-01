We use conda to manage environments.
For this repository we create a conda environment using:
* conda create --name py_downloader python=3.9
* conda activate py_downloader
* conda install -c conda-forge requests
* conda install -c anaconda wget (only in linux/ios)

remember to make an env.txt file useful when we want to clone an environment.
* conda update -n base -c defaults conda
* conda list --explicit > ENV.txt
If you have an ENV.txt, create py_downloader using (you need to stay in the folder where have ENV.txt file):
* conda create --name py_downloader --file ENV.txt