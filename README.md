## Project name: ##
Geological Project - Investigating the use of Google TensorFlow for image recognition of satellite imagery.

#### Student info: #####
<b>Name</b>: Peter Kongstad  
<b>Field of study</b>: Geoscience - 8th semester  
<b>University</b>: Aarhus University  
<b>Contact</b>: kongstad@geo.au.dk  
<b>Primary Supervisor</b>: Christoffer Karoff - Department of Geoscience & Department of Physics.  
<b>Secondary Supervisor</b>: Rune Hylsberg - Department of Engineering.  

#### Project description: ####
This is a repository for my semester project on using Google TensorFlow for Deep Neural Network learning, Raster Vision for object detection on GeoJSON files, Rasterio for data handling and several modules. The end goal is to test the software and conclude on wether or not it is the desireable choice for the follow-up project, of which is my master thesis. Through this document, I've written the "how-to's" and given conclusions on the individual software, as well as documenting the complications that arose. A conlusion on this feasibility study can be found at the bottom of this page.

#### Software introduction: ####
- [x] Anaconda Navigator
         <details>
         <summary>Information</summary>
Anaconda makes it easier to create and manage python environments as desired. Therefore it can be useful for setting up a primary environment, with the most basic required modules installed for TensorFlow applications. Then this environment can be cloned for experimental purposes without the risk of jeopardizing the primary environment. Besides managing the python environment, this software is also very useful in terms of adding new modules and installing the Spyder IDE and Jupyter Notebook. It is not an essential product, but definitely a useful one.
         </details>
- [x] CUDA
         <details>
         <summary>Information</summary>
CUDA (Compute Unified Device Architecture) is a parallel computing platform and programming model developed by Nvidia which provides an API to the parallel computing capabilities of GPU. It has been proven that the training of DNNs can be significantly accelerated using parallel computing. This is essential to be able to try out different architectures and compare their performance. In this project, an Nvidia 1080 GPU is used. More information can be found at <a href="http://www.nvidia.com/object/io_69526.html">Nvidia's CUDA Zone</a>
         </details>
- [x] cuDNN
         <details>
         <summary>Information</summary>
cuDNN is a shortened form of CUDA Deep Neural Network library. It is a library for deep neural networks which provides GPU accelerated functionality. This library provides implementations for the common methods of DNN, such as convolutional, normalization and pooling layers, different activation functions and the most common optimization algorithms. This library streamlines processes of optimization, as the utilization of the GPU is already set up and configured to run with Tensorflow. This is essential to the project, as we otherwise would have to manually setup low-level processes in the GPU, which would require high-level knowledge about data and processor functionality. Besides, Tensorflow is already configured to perform efficiently with this library. According to Nvidia's developer page, the newest version of 7.0 and above, which is used in this project, have 3x faster training performance than previous versions.
         </details>
- [x] Python 3.6
         <details>
         <summary>Information</summary>
Python is an interpreted, object oriented, high-level programming language. It has a wide array of usages and is very often utilized in our field by scientist and researchers, but can readily be applicable by anyone. Python is relatively simple and fast programming language with a manageable learning curve. For this project version 3.6 is used. This version is the most recent major release and has proven it self to be stable and greatly backed by a large number of modules. TensorFlow recommends using Python3.5 and above for GPU-supported application.
         </details>
- [x] TensorFlow
         <details>
         <summary>Information</summary>
TensorFlow is an open-source software library for computation and displaying data flow graphs. The software architecture is very flexible, meaning that it allows for computation between several platforms such as CPU's, GPU's and TPU's(Tensor Processing Unit). Besides spanning platforms, it also allows for distributing the mathematic load over several desktops to clusters of servers and even mobile devices. TensorFlow is generally build for machine learning and deep learning, and the software is already widely applied across scientific branches. Since TensorFlow is able to display graphs of the structure of the models being build, it is easier to get the full overview of a given model. The graph is a data structure which describes the computation that a model performs. Thus it is easier to discern an outcome, study it and fine tune further development of the model. TensorFlow already provides several pre-trained models on their GitHub page. These models can be freely downloaded and applied. I have demonstrated the use of one of these pre-trained modules, in the iceberg object detection example, which is discussed further down this page.
         </details>
- [x] Spyder IDE
         <details>
         <summary>Information</summary>
Spyder is an open source cross-platform Integrated Development Environment, tailored for scientific programming in conjunction with the Python language. It comes with advanced editing, interactive testing and debuggig. Spyder also hosts a numerical computing environment, due to the support of IPython, which is an enhanced interactive python interpreter. Spyder further integrates well-known modules such as NumPy(Linear Algebra), SciPy(Signal and image processing), Matplotlib(interactive 2D/3D plotting) and much more. It is also an integral part of the Anaconda Navigator, which allows for easy interplay between environments and Spyder can therefore be installed into each environment as required.
         </details>
         
### Project Timeline: ###

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
         <p> This module enables an easy way of importing one or multiple images from ESA, based on a GeoJSON file. Essentially using https://geojson.io (Note: The website may show up as unsafe, thus you have to bypass the security in your browser window), you mark a polygon of the desired region. Then save it as a geoJSON file, which sentinelsat module in python can import and recognize. Details on Sentinelsat module can be found <a href="http://sentinelsat.readthedocs.io/en/stable/api.html">here</a>
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
        For this project there are two satellite series of primary interest. The Sentinel-1 and the Sentinel-2 satellites. The Sentinel-1 satellites provide Synthetic Aperature Radar(SAR) images. Whilst the Sentinel-2 satellites are Multi Spectrum Imaging(MSI) satellites. Thanks to S1's SAR system, it is able to see through clouds and gather data without daylight. It is not desirable to use these maps for the testing purpose of the TensorFlow software in this part of the project. On the other hand, the S2 satellites provides 13 bands ranging from 443 nm and up to 2190 nm. This provides an array of tools for detection of several things such as biosphere, visible light, aerosols and much more. However for the sake of image recognition, band 2,3 and 4 - the RGB bands, will be used in this project. Its also of interest to note that the images comes at different processing levels. I have used the level 1C images here, as they are most suitable for the current project. They include radiometric and geometric corrections, ortho-rectification and spatial registration on a global reference system. Also cloud and land/water masks are generated. For the follow-up project, the level-2A may be of more interest, as it comes with more processed masks and several outputs. On the other hand, raw pictures can be shaped as required. This requires more investigation in the follow up project. More information about Level 1 and Level 2 processed images can be found <a href="https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi/processing-levels/level-2">here</a>
        </details>
- [x] Create and import GeoJSON files to script
        <details>
        <summary>Information</summary>
        GeoJSON file can very easily be created at this website: https://geojson.io. (Note: The website may show up as unsafe, thus you have to bypass the security in your browser window). Once a desirable shape have been drawn up and saved, the file can be imported into python. I have created a 4-sided polygon, defining the region of which I am interested in, in regards to downloading satellite imagery. Once the script executes, it will only import images that have a georeference within this polygon.
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
            I have changed the object detection tutorial as provided by the RasterVision library to run a satellite image with a large ice sheet flowing. Initially it was problematic as the models didn't seem to recognize anything, as it did in the demo tutorial (the object detection tutorial notebook mentioned earlier). I realised a different model was required and tried changing between several different models. These models can be found at the TensorFlow github page right <a href="https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md">here</a>. By switching the model to "faster_rcnn_inception_resnet_v2_atrous_oid_2018_01_28", I was finally able to get the large icesheet framed. I've produced a jupyter notebook of it which can be found at <b>/Files/jupyter-notebooks/TF_IR_tut.ipynb </b>
             </details>
- [x] Follow-up investigation   
    - [x] Semantic Segmentation vs. Object recognition
          <details>
          <summary>Information</summary> 
          For this project I've investigated both semantic segmentation and object recognition. For simplicity the object recognition seems at first to be the easiest method. By simply creating a bounding box around the ice in the images. However, for the follow-up project, it seems evident that the semantic segmentation is the way forward. This is due to the complexity of the follow up project. Whilst identifying 1 or 5 classes in a picture may be preferential in simplistic images. Working with large satellite imagery and trying to define small features, then pixelwise recognition may prove more fruitful. In comparision, visually, this means that when we want to detect an object, it will not be covered by a bounding box, but rather the entire object will be marked - pixel by pixel. <br>
Semantic segmentation works by understanding an image at the pixel level. Thus by assigning each pixel in an image to an object class. 
           </details>
    - [x] GPU vs. CPU
          <details>
          <summary>Information</summary> 
          Graphics Processing Units and Central Processing Units works in different ways, and therefore it is also situationally dependent, which one will perform best. Generally it can be said that CPUs handle algorithms such as GLMs better than a GPU would, and is generally more flexible. This is due to CPU's working more sequential. Where as the GPUs are parallelised and less flexible. This makes GPU preferential in machine learning cases such as with DNN. To go more in depth in understanding the difference, it is helpful to know the broadly simplified architecture of both processing units. A typical CPU is constructed for a more generic computing workload, as such that software is to be executed sequentially, implying one line/command at a time. However, this method places a limit to how fast a CPU can function. Secondly a CPU have fewer, but more complex cores to work with. Therefore CPU's do not function very well in gaming, multimedia application or with big data. This is where GPUs perform better with their parallelised architecture and large amount of simpler cores. The GPU are build as such, that it executes as many instructions as possible in parallel, but at the cost of slow sequential execution. GPU's primary weakness is memory capacity. Whilst they can draw a much higher memory bandwidth than a CPU, they tend to stretch the latency - meaning it is slower in transferring data. Another architectural difference is that CPU's are often clocked much higher than GPU's. Sequential tasks on a GPU is therefore not expected to match that of a CPU. The GPU provided for this project has 2560 CUDA cores, and can therefore computate massive amount of data, of the sort that can be parallelized (Matrix-matrix multiplications for example). This is why GPUs are significantly faster in deep learning applications. As mentioned this is just a broad overview of some cons and pros of the two types of processing units. A detailed description of this topic would exceed the scope of this report. The conlusion is that the GPU is simply able to juggle massive amounts of data simultaneously, in comparison to a CPU and therefore can shorten DNN methods down by days if not weeks, depending on the task. GPUs simply have more resources in form of its number of cores, its faster bandwidth to memory and the fact that DNN computations fit well with the GPU architecture.
           </details>
    - [x] U-net Architecture
          <details>
          <summary>Information</summary> 
          U-Net architecture is a convolutional network architecture for quick and exact segmentation of images. It works by inputting a raw image and it essentially outputs a segmentation map of the image, highlighting features. One of the remarkable things about this architecture is, that the researchers who developed it for the biomedical field, was able to produce very good results with as few as 30 annotated images per application. The images also featured objects of the same class touching each other, in some cases overlapping or even with invisible borders, meaning that it was required that the model could distinguish and seperate these objects. The architecture of the convolutional network contains several convolutional and max pooling operations and can be seen <a href="https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/u-net-architecture.png">here</a>. The network is fed an image, then the data is propagated and resized along all possible paths through the multichannel feature maps, eventually producing a segmented output image with 2 classes. A background and foreground image. The structure is relatively complex and for the sake of understanding its setup, I've provided a link to a 5 minute video explaining the model in its entirety <a href="https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/">here</a>. I strongly recommend watching it.
           </details>
    - [x] QGIS
          <details>
          <summary>Information</summary> 
          QGIS is an cross-platform, open-sourced and free Geographic Information System(GIS) application. The software allows for the analysis and editing of geospatial data, and provides the tools for composing and exporting graphical maps. QGIS supports both raster and vector layers, allowing for drawing points and polygonal features on satellite imagery. It also supports a wide variety of raster image formats, can work with layers and it can manage georeferenced images. The software can, as with conventional GIS programs, combine geophysical data with map and satellite data. With the addition of local geophysical data retrieved from Greenland, added on top of Sentinel satellite images and possibly additional Digital Elevation Maps(DEM), it could be a powerful tool for combining all the data into a single comprehensible visual product. QGIS is also able to connect directly to python through plugins. Whether or not QGIS is entirely relevant for machine learning processes can be debated, but it could have potential in working with geologicals areas of interest and with pre-existing geological data.
           </details>
           
#### Conclusion: ####
--------------------------------------------------------------
   <b>Introduction</b><br>
For this feasibility project, I have utilized the TensorFlow DNN software and it’s associated products, enabling the usage of GPU support for faster calculation of the algorithms. This with the aim, of using Convolutional Neural Network techniques in image recognition. To start out with, I was tasked with making the TensorFlow software run along with its associated software and modules. Secondly I was tasked with testing out different methods of data retrieval and management, which I will conclude on in this section. Lastly I was to attempt simple image recognition of the satellite imagery obtained. Through this section I comment superficially on the important aspects and take-aways. For a more thorough comment on process, complications and solutions, check the individual points in the above section of this readme file.<br><br>
     <b>Installation:</b><br>
The first task of this project, was to get the GPU support up and running with TensorFlow, which is from here on denoted simply as “TF”. As there is little to no direct guidance provided by the TF team, this is not a trivial task. The different softwares have to be installed in a specific order, or conflict can arise. 
First step here was to make a system modification to the Linux Ubuntu setup, in order to avoid display driver conflict. 
Next was the installation of the CUDA 9.0 software, which enables the use of the Nvidia GPU in the TF module and associated modules. Also not a trivial task, but in this case, there was adequate documentation provided by Nvidia. The third requirement for the setup, was the cuDNN software. In order to utilize this software, which is an essential component, membership at the Nvidia developer page was required. Once obtained, the correct version could be installed without any hassle. Next requirement was the installation of Python 3.6 and creating the environment for the TF modules. Once the environment was configured, it was simple to install TF into this environment.<br><br>
   <b>Data Import:</b><br>
As my progress indicates in the sections above, there are several ways to retrieve the data. The simplest is by accessing the <a href=”https://apps.sentinel-hub.com/eo-browser/”>EO browser</a>. This website offers an easy-to-use browser interface, where the desired parameters can easily be entered and then an output is generated in a equally easy to use format. The page requires registration and subsequently payment. However, new profiles with trial periods can be used. The second way is the proper way to do this, and in the follow-up project the way I would advice us to proceed. By utilizing the ESA Sentinel API, a script will connect directly to the ESA server and retrieve the images in bulk, provided the script feeds them a GeoJSON file with coordinates of the desired region. The image retrieval can be customized to a given preference dictated by parameters in the script. There are slight issues with this method though. The files are rather large, as all 13 bands and pre-processed images are contained within the file. Secondly the server is being throttled by ESA. Decreasing download speed severely. It would be interesting to consider approaching ESA and put in a request for a university pipe, that could offer increased download speeds. Regardless of this, I recommend we proceed with this method of obtaining Sentinel data. Especially for the L2A images.<br><br>
<b>Rasterio:</b><br>
The Rasterio module is, as previously mentioned, a tool for importing and editing large Geo-imbedded satellite images. This module lived up to its expectations and was relatively easy to use. I’m not convinced this module is essential to the follow up project. However it does seem to make some image manipulation easier and thus faster, rather than have to do it manually. I would not sign this particular module off yet, neither would I declare it essential. I recommend keeping it in the toolbox for now. <br><br>
<b>RasterVision:</b><br>
This module is under strong development and have changed entirely twice over this semester. This has made it slightly difficult to work with, since their github contents have changed over night. As it looks now, they are aiming at a major bundle release in the summer of 2018. Further investigation of their product reveals that they are working on releasing a stand-alone client, which seems to be their main focus. Regardless thereof, I was able to apply their previous image recognition code into one of the satellite images that I retrieved. By adjusting their initial model to a different TF released model, the code successfully identified a large ice sheet in a image and framed it. This proves what they are working on, works to a certain degree. However, after consulting PhD. Jacob at Engineering, I was advised to look in a different direction. Rather than using Object Orientated recognition, which RasterVision now specializes in, I was advised to investigate the Semantic Segmation method. 
Upon following this direction, I must concur with Jacob. By semantically segmented images, the image is divided up into pixels which are then assigned classes. This allows for creating pixel wise boundaries in the satellite images. Giving incredible precision. I’ve included two images in the image folder, showing an example output of both techniques.
This will obviously require more computational power, rather than doing object orientated recognition. However, by using Fully Convolutional Network(FCN) and the U-net architecture, which only requires very few annotated images, this should be reasonable to do on the new hardware acquired for this project. A complete understanding of the application of FCN, U-net architecture and perhaps others, should be investigated in the follow-up project. But for now I suggest shelfing the RasterVision module, in favor of semantic segmentation. Its also important to note, that we have in-house experience with this method and cases where this exact method have been implemented(Jacob). Therefore diminishing the learning curve of the follow-up project slightly by utilizing in-house capabilities.<br><br>
<b>Testing:</b><br>
Once TF, Sentinel API Import, RasterVision and Rasterio was successfully installed. I commenced the testing of them by running provided tutorials. I then modified the code in these tutorials to comply with satellite images of the Scoresbysund Fjord in Eastern Greenland. As can be seen in the Files/jupyter-notebooks/ folder, the modules interacted as intended with the imagery.<br> - The RasterioTest.ipynb illustrates the Sentinel API Import in action, as well as the image manipulation by the Rasterio module.<br> - The TF_IR_tut.ipynb is a modified TF official tutorial, where the satellite image is connected to the ImageNet 2012 challenge database. Herein the model attempts to predict objects in the image by outputting the object and its error score. This method is not of interest this project, but serves just as an investigative turn in trying out different methods.<br>- The object_detection_tutorial_iceberg.ipynb is of little more interest. In this I was able to use an old iteration of RasterVision, to identify the large ice sheet in the image with a bounding box. This is the object orientated recognition described in the paragraph above. This particular model fails at identifying the minor ice sheets though. <br><br>
<b>Summary:</b><br>
Through this feasibility study I have configured and applied all the software, thus successfully produce results in all of the software and modules included. I have speculated and argued on what works and what should be brought forward to the follow-up project. This has also lead to the, for now, dismissal of the RasterVision module. Regardless, as object orientation is not immediately useful for the follow-up project, I see no reason to continue investigation in this module for now.
The positive take away from this project have been as follows:<br>   
    -  Proof-of-concept with regards to TensorFlow Image Recognition.<br>
    -  Successful API data import methods.<br>
    -  Successful image manipulation in Rasterio.<br>
    -  Dismissal of RasterVision.<br>
    -  A better idea of how to proceed from here on.<br>
    -  Experience with the whole method of operation <br><br>
In the following months I will partake in Deep Learning course CS231n as recommended by PhD. Jacob Høxbroe Jeppesen, as well as study exercises provided by him. I would also argue that it might be beneficial to add QGIS to the toolbox, as this could become useful when data from the exploration company is added. Therefore I'll conduct a self-study on the QGIS software before engaging in the follow-up project.
After the initial meeting with the mineral exploration company 21st North, of which the follow-on project is intertwined with, more information have been given on the data. 21st North have around 250.000 different types of samples acquired in the Ammassalik region of Greenland. This data spans several methods in the geophysical and geochemical realm, and have been accumulated over the past 15+ years. The older data are of varying quality, thus they need to be assessed before application. 

These data samples will be connected with Copernicus satellite imagery from the region. This means that a geochemical sample containing data such as coordinates and mineral content, will be interlinked with small scale high-resolution satellite images on those exact coordinates. This will be applied into a TensorFlow script, where a model will be developed for anticipating, at first, nickel content in other nearby regions of known quantities and thus provide us with a score of its predictability rating. When this has been achieved, more minerals can be added from the geochemical data, to give a more complex image of the region. Eventually the model can be used to attempt prediction of mineral content in unknown regions, which may be investigated by 21st North on their expedition in 2019.

The region of interest has already shown rich nickel deposits in the geochemical samples, however the current localities are difficult to exploit, as the landscape consist of steep cliffsides in a relatively inhospitable region. It is also of interest that copper deposition may have occured in the the northern region, yet there is next to no data availible in this region other than the general structure geology. The entire ammassalik region can be geologically related to specific regions of Canda and Norway. These regions are already producing world class deposits of nickel ore and are being commercially exploited. This is significant, as it is geologically established that Greenland were once landlocked with Laurentia(North America) and Baltica during the last supercontinent amalgamation, commonly reffered to as Pangaea. With the geological history in mind, it is probable that the same processes of which enriched the soil with nickel in Canada and Norway, did the same to Greenland. With this geological background, data samples of several methods, satellite imagery and the powerfull application of the TensorFlow software, I hope to be able to create a meaningful link between the data and the geology. Optimally, the algorithm would be able to infer where the large deposits may be localised. 21st North is returning to the region in 2019, for additional sampling. This could potentially test the viability of the result of the follw-up project, as the company can attempt sampling in regions that the software may flag as interesting.





