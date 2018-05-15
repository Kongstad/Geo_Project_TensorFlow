## Project name: ##
Geological Project - Investigating the use of Google TensorFlow for image recognition of satellite imagery.

#### Description: ####
This is a repository for my semester project on using Google TensorFlow for Deep Neural Network learning, Raster Vision for object detection on GeoJSON files, Rasterio for data handling and several others. The end goal is to test the software and conclude on wether or not it is the desireable choice for the follow-up project. Through this readme document, I've written how-to's and conclusions on using the individual software, as well as documenting the complications that arose. A conlusion on this feasibility study can be found at the bottom of this page.

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
         <p>A slight modification in the Software & Updates panel is required. In the sub-menu <b>Additional drivers</b>, I had to disable the Ubuntu Nouveau display driver and instead set it to: <b>Using Nvidia binary - driver</b>. This makes sure that there is no driver conflict.</p>
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
         <p> This module enables an easy way of importing one or multiple images from ESA, based on a GeoJSON file. Essentially using https://geojson.io, you mark a polygon of the desired region. Then save it as a geoJSON file, which sentinelsat module in python can import and recognize. Details on Sentinelsat module can be found <a href="http://sentinelsat.readthedocs.io/en/stable/api.html">here</a>
          </p>
         </details>
- [x] RasterVision
         <details>
         <summary>Information</summary>
  <p> This module is found <a href="https://github.com/azavea/raster-vision">here</a>. It is currently under development and expected to be released in Summer 2018. The goal is to train and run deep learning models of satellite imagery and being able to make object detection viable through the TensorFlow Object Detection API. The reason for using this deep learning library is, that this one can handle GeoTIFF files and annotations/predictions are represented in geospatial coordinates, using the previously mentioned GeoJSON files. Installation of this module has to be done manually and there are several dependencies and documents to be downloaded manually through their github site <a href="https://github.com/azavea/raster-vision/tree/develop/src/tf/object_detection">here</a>. Required libraries besides TensorFlow and Jupyter notebook are, Protobuf 2.6, Pillow 1.0, lxml, tf Slim (which is included in the "tensorflow/models" checkout) and Matplotlib. The process is inadequately described and requires tinkering around and downloading their entire library. Later note: The PIL install doesn't work right unless activating the correct environment in the terminal and then proceeding to install image by <b>pip install image</b>. See the folder <b>Files/jupyter-notebooks/</b> for a jupyter file of the object detection tutorial output. I've not authored this notebook, it's provided on the RasterVision github page. However, I did succesfully run it on my machine, indicating the install and object detection works as expected. Yet running it with satellite imagery doesn't seem fruitful at this stage, as the model used in this tutorial, doesn't seem to box in icebergs very well. 
          </p>
         </details>
- [x] Rasterio
         <details>
         <summary>Information</summary>
        Rasterio is a tool for importing large Geo imbedded satellite images and can be installed by following this <a href="https://rasterio.readthedocs.io/en/latest/installation.html">link</a> <p> 
  The module essentially allows for manipulation of the images. The RasterVision module is expecting to be able to provide this feature as well. But for the sake of exhausting all possibilities, I've tested this module on images imported through the Sentinelsat plugin. See the file <b>rasterotest.py</b> in the files section. I've created a notebook that shows the imported data (via the Sentinel API module), applied straight into the Rasterio module, where I decode the image and display it in it's varios bands. The notebook is found at <b>/Files/jupyter-notebooks/RasterioTest.ipynb</b>
         </details>
- [x] Run premade scripts to ensure succesful application of all software
    - [x] TensorFlow with GPU Support
    - [x] Sentinelsat API Import
    - [x] RasterVision
    - [x] Rasterio
- [x] Geological feature chosen for experiment
        <details>
        <summary>Information</summary> 
        So far this has proven to be slightly difficult. The region of choice has a lot of ice even though I have chosen the summer periods. The high albedo of the snow makes the images appear extremely white. I'm working on culling the intensity. But essentially icebergs in the fjord is the target for this study. I've come to discover that the region have a period of ca. 2.5 months from late july to mid october, where in the ice is at a minimum as well as the cloud cover is reduced. I've designated 15 days of perfect conditions and have therefore stored 15 images in the images folder.
        </details>
- [x] Satellite Research
        <details>
        <summary>Information</summary> 
        For this project there are two satellite series of primary interest. The Sentinel-1 and the Sentinel-2 satellites. The Sentinel-1 satellites provide Synthetic Aperature Radar(SAR) images. Whilst the Sentinel-2 satellites are Multi Spectrum Imaging(MSI) satellites. Whilst S1 can provide height information, see through clouds and gather data without light. It is not desirable to use these maps for the testing purpose of the TensorFlow software in this part of the project. On the other hand, the S2 satellites provides 13 bands ranging from 443 nm and up to 2190 nm. This provides an array of tools for detection of several things such as biosphere, visible light, aerosols and much more. However for the sake of image recognition, band 2,3 and 4 - the RGB bands, will be used in this project. Its also of interest to note that the images comes at different processing levels. I have used the level 1C images here, as they are most suitable for the current project. They include radiometric and geometric corrections, ortho-rectification and spatial registration on a global reference system. Also cloud and land/water masks are generated. For the follow-up project, the level-2A may be of more interest, as it comes with more processed masks and several outputs. More information about Level 1 and Level 2 processed images can be found <a href="https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-2">here</a>
        </details>
- [x] Create and import GeoJSON files to script
        <details>
        <summary>Information</summary>
        GeoJSON file can very easily be created at this website: https://geojson.io. Once a desirable shape have been drawn up and saved, the file can be imported into python. I have created a 4-sided polygon, defining the region of which I am interested in, in regards to downloading satellite imagery. Once the script executes, it will only import images that have a georeference within this polygon.
        </details>

#### May 2018: ####
--------------------------------------------------------------
- [x] Satellite Imagery Challenges
        <details>
        <summary>Information</summary> 
        The initial technique of using the Sentinelsat API tool for image retrieval, seems to be undesirable at this point in time. There are three major hurdles in using this technique so far. 1) The immense file size of requesting 1 photo at a given location. In these zipped folders, there are all 13 bands, as well as several datafiles. This can easily produce file sizes above 1.3 gb. When in reality the desired product was an image at the size of 122 mb. 2) ESA throttles their servers download speed. Putting a 1.3 gb file download time to more than 30 minutes, at a very reasonable broadband connection (50/50 mbit). They are simply limiting the outgoing server speeds. 3) The images are often extremely bright as a product of the snow albedo. Image brightness can ofcourse be reduced. Conclusion: I suggest for this pilot project, that the focus is on getting the image recognition going, rather than dealing with image retrieval and editing technicalities. Hence I've concluded it is better to use their online sentinel hub website (EO Browser). The images I require can be loaded up in less than 10 seconds and several parameters can be defined. Such as format, with or without georeference, quality, coordinate system and band/layers. I've decided to proceed with this method. 15 images have been selected so far and can be found here /Files/images/. 
        </details>
- [x] Image recognition methods used on ice sheet images
    - [x] TensorFlow Image Recognition by ImageNet
            <details>
             <summary>Information</summary> 
             I've used the image classifier tutorial listed on the TensorFlow website and then applied their code to the retrieved satellite imagery. This is a simple test where only 1 image is chosen, then compared to a large online database. The trick here is for TensorFlow to categorise as much as possible, then listing the top 5 objects and how often the algorithm guessed it right - Actually the error % rate. Testing on several images, it was able to say that the image contained icebergs and seashores. However it also misclassified other objects as killer whales, geysers and a Newfoundland Dog. To the algorithms credit, it guessed the seashore wrong only 2 % of the time. I've uploaded a Jupyter Notebook about with a little more details. It can be found at <b>/Files/jupyter-notebooks/TF_IR_tut.ipynb</b>
             </details>
     - [x] Object Detection in action
            <details>
             <summary>Information</summary> 
            I have changed the object detection tutorial as provided by the RasterVision library to run a satellite image with a large ice sheet flowing. Initially it was problematic as the models didn't seem to recognize anything, as it did in the demo tutorial (the object detection tutorial notebook mentioned earlier). I realised a different model was required and tried changing between several different models. These models can be found at the TensorFlow github page right <a href="https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md">here</a> By switching the model to "faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28", I was finally able to get the large icesheet framed. I've produced a jupyter notebook of it which can be found at <b>/Files/jupyter-notebooks/TF_IR_tut.ipynb </b>
             </details>
- [x] Follow-up investigation   
    - [x] Semantic Segmentation vs. Object recognition
          <details>
          <summary>Information</summary> 
          For this project I've investigated both semantic segmentation and object recognition. For simplicity the object recognition seems at first to be the easiest method. By simply creating a bounding box around the ice in the images. However, for the follow-up project, it seems evident that the semantic segmentation is the way forward. This is due to the complexity of the follow up project. Whilst identifying 1 or 5 classes in a picture may be preferential in simplistic images. Working with large satellite imagery and trying to define small features, then pixelwise recognition may prove more fruitful. In comparision, visually, this means that when we want to detect an object, it will not be covered by a bounding box, but rather the entire object will be marked - pixel by pixel. <br>
Semantic segmentation works by understanding an image at the pixel level. Thus by assigning each pixel in an image to an object class. 
           </details>
- [ ] Project Conclusion
      <details>
      <summary>Information</summary> 
      I've 
      </details>


#### Student info: #####
<b>Name</b>: Peter Kongstad  
<b>Field of study</b>: Geoscience - 8th semester  
<b>University</b>: Aarhus University  
<b>Contact</b>: kongstad@geo.au.dk  
<b>Primary Supervisor</b>: Christoffer Karoff - Department of Geoscience & Department of Physics.  
<b>Secondary Supervisor</b>: Rune Hylsberg - Department of Engineering.  
