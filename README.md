## Project name: ##
Geological Project - Employing Google TensorFlow for image recognition of satellite imagery.

#### Description: ####
This is a repository for my semester project on using Google TensorFlow for Deep Neural Learning, Raster Vision for object detection on GeoJSON files and Rasterio for data handling. The end goal is to create a script that allows for image recognition of satellite imagery and documenting the process here.  

### Project overview: ###

#### February 2018: ####
--------------------------------------------------------------
- [x] Project startup approved
- [x] Basic TensorFlow tutorials completed
- [x] Initial progress documented in /files/process.pdf

#### March 2018: ####
--------------------------------------------------------------
- [x] Complete hardware reset and reinstallation to bypass previous issues - See process.docx.
- [x] TensorFlow succesfully operational with GPU Support:
  - [x] OS: Linux Ubuntu 16.04
         <details>
         <summary>Modification</summary>
         <p>A slight modification in the Software & Updates panel is required. In the sub-menu <b>Additional drivers</b>, I had to disable the Ubuntu Nouveau display driver and instead opt for the program to the setting: <b>Using Nvidia binary - driver</b>. This makes sure that there is no driver conflict.</p>
         </details>
  - [x] Anaconda Navigator: 4.5.0
         <details>
         <summary>Installation</summary>
        <p>Anaconda Navigator was downloaded from <a href="https://www.anaconda.com/download/#linux">their website</a> and    thereafter updated to version 4.5.0 by using the navigator automatic updating platform.</p>
        </details>
  - [x] CUDA: 9.0
         <details>
        <summary>Installation</summary>
        <p>I've proceeded to the CUDA 9.0 website to download this specific version, as it should work better with this setup. I've downloaded CUDA 9.0 from <a href="https://developer.nvidia.com/cuda-90-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=deblocal">here</a>. I've chosen the Linux version, with x86_64, for Ubuntu 16.04 and the installer as a deb(local) type. Then I've launched the following terminal commands for download and correct installation<br> 
         <b>
         1. Set the directory to the folder with the downloaded CUDA file.<br>
         2. sudo dpkg -i cuda-repo-ubuntu1604-9-0-local_9.0.176-1_amd64.deb<br> 
         3. sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub<br> 
         4. sudo apt-get update<br> 
         5. sudo apt-get install cuda</b><br>
         I then proceed to the <a href="http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html">CUDA installation documentation</a>, which states at point 7.1, that some actions must be taken after the installation before the CUDA Toolkit and Driver can be used.<br> The PATH variable needs to include /usr/local/cuda-9.1/bin, so to add this path to the PATH variable, the following command needs to be entered in the terminal window:<br>
         <b> export PATH=/usr/local/cuda-9.1/bin${PATH:+:${PATH}}</b> In addition, when using the runfile installation method, the LD_LIBRARY_PATH variable needs to contain /usr/local/cuda-9.1/lib64 on a 64-bit system.To change the environment variables for 64-bit operating systems, enter the following in a terminal window:<br>
         <b> export LD_LIBRARY_PATH=/usr/local/cuda-9.1/lib64\
           ${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}</b>
         </p>
         </details>
  - [x] cuDNN: 7.0.5
         <details>
         <summary>Installation</summary>
         <p>In order to download cuDNN, a Nvidia developer membership is required. This can freely be obtained by simply registrating on their website. I've done so and proceed to download the file at this <a href="https://developer.nvidia.com/rdp/cudnn-download">website</a>. The file I've used for this is the one labelled <a href="https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.0.5/prod/9.0_20171129/Ubuntu16_04-x64/libcudnn7_7.0.5.15-1+cuda9.0_amd64">cuDNN v7.0.5 Runtime Library for Ubuntu16.04 (Deb)</a>. Once this file is downloaded. I double click it to initiate the software installer.</p>
         </details>
  - [x] Python: 3.6
        <details>
        <summary>Installation</summary>
        <p>I have installed python3.6 through Anaconda Navigator by creating a new  python environment in the Anaconda directory, to install TensorFlow into - which I named tensorflow. This was done by the using the command <b>"conda create -n tensorflow pip python=3.6" </b>. I then activate the newly created environment by typing <b>source activate tensorflow</b>. I then launch the Anaconda Navigator and install the Spyder editor in the tensorflow environment. With Anaconda now all set up, Tensorflow can be installed </p>
         </details>
  - [x] TensorFlow:
          <details>
         <summary>Installation</summary>
         <p>Now in order to install Tensorflow, I use the following terminal command to install the GPU supported version <b>pip install --ignore-installed --upgrade https: //storage.googleapis.c om/tensorflow/linux/gpu/tensorflow_gpu-1.6.0-cp36-cp36m-linux_x86_64.whl</b> Note that this is the correct TensorFlow for python 3.6, by its denomination cp36.</p>
         </details>
  - [x] Spyder Test:
          <details>
         <summary>Code Compilation</summary>
         <p>In order to test whether TensorFlow is sucessfully working, I now compile a short "Hello, TensorFlow" test as given <a href="https://www.tensorflow.org/install/install_linux#run_a_short_tensorflow_program">here</a>.<br>
            The code looks like this:<br>
            <i>#Python<br>
            import tensorflow as tf<br>
            hello = tf.constant('Hello, TensorFlow!')<br>
            sess = tf.Session()<br>
            print(sess.run(hello))<br>
            Which succesfully prints<br>
              'Hello, TensorFlow!'</i>
          </p>
         </details>
         
#### April 2018: ####
--------------------------------------------------------------
- [x] Sentinelsat python module for ESA API Hub retrieval
         <details>
         <summary>Information</summary>
         <p> This module enables an easy way of importing one or multiple images from ESA, based on a GeoJSON file. Essentially using https://geojson.io, one marks a polygon of the desired region. Then save it as a geoJSON file, which sentinelsat module in python can import and recognize. Details on Sentinelsat module can be found at: http://sentinelsat.readthedocs.io/en/stable/api.html
          </p>
         </details>
- [x] RasterVision
         <details>
         <summary>Information</summary>
         <p> This module is found at https://github.com/azavea/raster-vision. It is currently under development and expected to be released in Summer 2018. The goal is to train and run deep learning models of satellite imagery and being able to make object detection viable through the TensorFlow Object Detection API. The reason for using this deep learning library is, that this one can handle GeoTIFF files and annotations/predictions are represented in geospatial coordinates, using the previously mentioned GeoJSON files. Installation of this module has to be done manually and there are several dependencies and documents to be downloaded manually through their github site here: https://github.com/azavea/raster-vision/tree/develop/src/tf/object_detection. Required libraries besides TensorFlow and Jupyter notebook are, Protobuf 2.6
Pillow 1.0, lxml, tf Slim (which is included in the "tensorflow/models" checkout) and Matplotlib. The process is inadequately described and requires tinkering around and downloading their entire library. Later note: The PIL install doesn't work right unless activating the correct environment in the terminal and then proceeding to install image by pip install image. See the folder Files/src/testing/ for a jupyter file of the object detection tutorial output. I've succesfully ran it on my machine. 
          </p>
         </details>
- [x] Rasterio
         <details>
         <summary>Information</summary>
        Rasterio is a tool for importing large Geo imbedded satellite images and can be installed by following this link -https://rasterio.readthedocs.io/en/latest/installation.html. <p> 
  The module essentially allows for manipulation of the images. The RasterVision module is expecting to be able to provide this feature as well. But for the sake of exhausting all possibilities, I've tested this module on images imported through the Sentinelsat plugin. See the file rasterotest.py in the files section.
         </details>
- [x] Run premade scripts to ensure succesful application of all software
    - [x] TensorFlow with GPU Support
    - [x] Sentinelsat API Import
    - [x] RasterVision
    - [x] Rasterio
- [ ] Geological feature chosen for experiment
- [x] Satellite Research
        <details>
        <summary>Information</summary> 
        For this project there are two satellite series of primary interest. The Sentinel-1 satellites and the Sentinel-2 satellites. The Sentinel-1 satellites provide Synthetic Aperature Radar(SAR) images. Whilst the Sentinel-2 satellites are Multi Spectrum Imaging(MSI) satellites. Whilst S1 can provide height information, see through clouds and gather data without light. It is not desirable to use these maps for the testing purpose of the TensorFlow software in this part of the project. On the other hand, the S2 satellites provides 13 bands ranging from 443 nm and up to 2190 nm. This provides an array of tools for detection of several things such as biosphere, visible light, aerosols and much more. However for the sake of image recognition, band 2,3 and 4 - the RGB bands, will be used in this project.
        </details>
- [x] Create and import GeoJSON files to script
- [ ] Image recognition code produced
- [ ] Algorithm trained and producing scores
- [ ] Algortihm capable of identifying objects in images.

#### May 2018: ####
--------------------------------------------------------------
- [ ] Conclusion of project and finishing of GitHub setup


#### Student info: #####
<b>Name</b>: Peter Kongstad  
<b>Field of study</b>: Geoscience - 8th semester  
<b>University</b>: Aarhus University  
<b>Contact</b>: kongstad@geo.au.dk  
<b>Primary Supervisor</b>: Christoffer Karoff - Department of Geoscience & Department of Physics.  
<b>Secondary Supervisor</b>: Rune Hylsberg - Department of Engineering.  
