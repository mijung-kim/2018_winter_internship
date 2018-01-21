# 2018_winter_internship @ GUGC
##Supervisor: 
  Mijung Kim

##Students: 
  Pyeong Eun Kim
  Mijeong Lee
  Ju Hyung Lee

# Table of Contents
1. Goal(#during-this-2018-winter-internship-program,-students-will-learn:)
2. Getting Ready:(#initial-steps-before-anything:)
  2.1. Introduction(#introduction)
  2.2. Installing docker(#installation-&-initialization-of-docker:)

## During this 2018 winter internship program, students will learn:

  - Basic Knowledge in Machine Learning
  - Application of machine learning for image classification.
  - Application of machine learning for STT (Speech-To-Text).
  - The concept of virtual environment, and thereby how to use docker, or any other virtual environment tools.
  - Usage of Github as sharing tool for codes.
 
  
  
## Initial steps before anything:

### Introduction:

  Just to grasp an idea what machine learning and image classification are, follow the link below:
  
  https://developer.nvidia.com/dli/onlinelabs
  
  The link will take you to NVIDIA DLI online labs. Read through the first two labs:
    - Applications of Deep Learning with Caffe, Theano, and Torch
    - Image classification with DIGITS.
  
  In order to take those labs, you need to sign up for QWIKLABS. The signing-up process is very short and simple, so no worries.

  The codes that you will see on the labs above are complicated and not informative. Make sure you do not try to UNDERSTAND, but REALIZE what you will do.


### Installation & Initiation of Docker:
  
  Docker will be the main tool you will be using throughout this program. It is a container that enables easier creation, deplyoment and running applications.
  
  The tem 'container' defines a software packaged into standardized units for development, shipment and deployment (brought from docker website). Simply speaking, it's a program you will need for coding.
  
####  1. For Linux and Mac users:
   
   **Installation**
    
     Follow the link below for general instruction of docker:
      
     https://docs.docker.com/get-started/
    
     Make sure you download the Community Edition (CE), which is free. Ofcourse, make sure the installer matches your OS.
    
   **Initiation**
   
     Make sure you open Docker application.
    
     Open Terminal and on your bash write command.
    
     $ docker login
    


####  2. For Windows users:
    
    If your computer runs a Windows 10 Pro, or has Windows Server 2016, follow the same procedures as for Linux and Mac.
    
    Else, it's a completely different story - you need to download a docker toolbox for windows from the following links:
    
      https://docs.docker.com/toolbox/toolbox_install_windows/#step-2-install-docker-toolbox
    
    Run the file to install toolbox, and then you will see three items popped up on your desktop: 
    
       - Docker Quickstart Terminal
       - Oracle VM VirtualBox
       - Kitematic (Alpha)
    
    Ignore Oracle VM VirtualBox! You won't be using this program (at least during this internship program)
    
    Run Kitematic (Alpha). You will see a page full of boxes that represent docker images. All you need is the very first item on the top left corner: 'hello-world-gnix'
    Click 'CREATE' button. It's a blue rectangular button with blue edges that every item has.
    
    Now you have the appropriate container. Close Kitematic (Alpha), and open Docker Quickstart Terminal. a command window will pop up. Wait for the program to do some initializing - when it's done, a pixel-whale will show up. After then you are ready!

    ##### *Acutally, running docker on windows is quite complicated and uncompatible with whatever you are going to do on docker. Thus, it is recommended to scroll down a bit and read the section: "Installing Ubuntu".
    
    
    
## Some lectures to go through to have a better understanding of what it is going on.

### image classification 
  
  To learn about the image classification, follow this link below for introductory explanation of image classification :
http://cs231n.github.io/classification/

### modules numpy
  
  During the internship, modules numpy in python is used that it is important to know how numpy works. It is recommended to have numpy tutorial with the link below to learn numpy and to get familiar with the modules.
http://cs231n.github.io/python-numpy-tutorial/

### machine learning
  
  Machine learning is the basis of the internship program. To have a thorough understanding of the machine learning, follow this link below :
http://www.deeplearningbook.org/contents/ml.html

### Deep learning

! [course_layout](\Users\user\Documents\workspace\intern\course_layout.png)

  For backgroud knowldege of deep learning, lectures 2-6 of Convolutional Neural Networks for Visual Recognition from Standford University can be followed. 
  http://cs231n.stanford.edu/syllabus.html
  
  After the lectures, it is recommended to attemp to solve he assignment 1.
  
  
## Github 

### Make your own Repository

Click the link and sign in https://github.com. (If you do not have account sign up! username is important because your username will be the address of your github.)

Click $start a project$ to start making your own repository. Then follow the steps
          1. write any repository name. 
          2. Check Public
          3. Check "Initializing this repository with README".
          4. You have to choose a license. License normally would be "MIT" (detailed explanation included in the link
          5. Click 'create'. Now you're ready to roll!

      


## Installing UBUNTU

### For window users: 

There is a display issue that it does not display the GUI on docker. So it is recommended to install UBUNTU to run GUI on Docker.

##To install UBUNTU :
  
  1. To download Ubuntu 16.04.3 LTS, follow this link  
          
          https://www.ubuntu.com/download/desktop
  
  2. Download the iso image for ubuntu wherever you can easily navigate. 
  
  3. Make the USB bootable with rufus. To download rufus, follow this link 
          
          https://rufus.akeo.ie/

     When you open the software, keep the default options.
     Somewhere in the bottom of the interface, you would see an option to insert the iso file you downloaded minutes ago. 
     Insert the image, then run the software so that bootable USB is created.
  
  4. To install Ubuntu, follow this link below  
          
          https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop?_ga=2.156978296.258151108.151625099           0-1540692620.1516250990#3




