## Project name: ##
Geological Project - TensorFlow for interpretating satellite imagery

#### Description: ####
This is a repository for a semester course on using TensorFlow for image recognition of satellite imagery.  

### Project overview: ###

#### February 2018: ####
--------------------------------------------------------------
- [x] Project startup approved
- [x] Basic TensorFlow tutorials completed
- [x] Progress documented in /files/process.docx

#### March 2018: ####
--------------------------------------------------------------
- [ ] TensorFlow succesfully operational with GPU Support:
  - [x] OS: Linux Ubuntu 16.04
       <details>
       <summary>Modification</summary>
       <p>A slight modification in the Software & Updates panel is required. In the sub-menu <b>Additional drivers</b>, I had to disable the Ubuntu Nouveau display driver and instead opt for the program to the setting: <b>Using Nvidia binary - driver</b>. This makes sure that there is no driver conflict.</p>
       </details>
  - [x] Handler: Anaconda Navigator 4.5.0
       <details>
       <summary>Installation</summary>
       <p>Anaconda Navigator was downloaded from <a href="https://www.anaconda.com/download/#linux">their website</a> and    thereafter updated to version 4.5.0 by using the navigator automatic updating platform. Then I proceeded to create a new  python environment in the Anaconda directory, to install TensorFlow into - which I name tensorflow. This was done by the using the command <b>"conda create -n tensorflow pip python=3.6" </b>. I then activate the newly created environment by typing <b>source activate tensorflow</b>. Now Anaconda is primed for TensorFlow to be installed. However, CUDA and CuDNN should installed first. </p>
      </details>
  - [x] Python: 3.6 - Installed in the Anaconda environment.
  - [x] CUDA: 
       <details>
       <summary>Installation</summary>
       <p>I've proceeded to the CUDA 9.0 website to download this specific version, as it should work better with this setup. I've downloaded CUDA 9.0 from <a href="https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal">here</a>. I've chosen the Linux version, with x86_64, for Ubuntu 16.04 and the installer as a deb(local) type. Then I've launched the following terminal commands for download and correct installation<br> 
         <b>
         1. Set the directory to the folder with the downloaded CUDA file.<br>
         2. sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb<br> 
         3. sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub<br> 
         4. sudo apt-get update<br> 
         5. sudo apt-get install cuda</b>
  </p>
       </details>
  - [ ] CuDNN: 
       <details>
       <summary>Installation</summary>
       <p>Anaconda</p>
       </details>
  - [ ] TensorFlow:
       <details>
       <summary>Installation</summary>
       <p>Now TensorFlow can be installed into the Anaconda environment, previously created and named tensorflow. Remember to activate the environment before doing this by using the command <b>source activate tensorflow</b>. Now the use the following terminal command to install the GPU supported version of tensorflow. <b>pip install --ignore-installed --upgrade https: //storage.googleapis.c om/tensorflow/linux/gpu/tensorflow_gpu-1.6.0-cp36-cp36m-linux_x86_64.whl</b> Note that this is the correct tensorflow for python 3.6, by its denomination cp36.</p>
       </details>
- [ ] Geological feature chosen for experiment
- [ ] Sufficient satellite imagery collected

#### April 2018: ####
--------------------------------------------------------------
- [ ] Image recognition code produced
- [ ] Algorithm trained and producing scores
- [ ] Algortihm capable of identifying objects in images.

#### May 2018: ####
--------------------------------------------------------------
- [ ] Conclusion of project and finishing of GitHub setup


##### Student info: #####
Name: Peter Kongstad  
Field of study: Geoscience - 10th semester  
University: Aarhus University
Contact: kongstad@geo.au.dk
