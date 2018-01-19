# 2018_winter_internship @ GUGC
supervisor: Mijung Kim

Students: Pyeong Eun Kim
          Mijeong Lee
          Ju Hyung Lee

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
    
    Now you have the appropriate container. Close Kitematic (Alpha), and open Docker Quickstart Terminal. a command window will pop up. Wait for the program to do some initializing - when it's done, a pixel-whale will show up. 
    
    
    
## Before starting the coding, there are some lectures to go through to have a better understanding of what it is going on.

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

! [Alt text](\Users\user\Documents\workspace\intern\course_layout.png)

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
          4. License normally would be "MIT" (about the license go to this link 
          5. 

      
      
## Installing UBUNTU
### For window users      : 
  There is a display issue that it does not display the GUI on docker. So it is recommended to install UBUNTU to run GUI on Docker.
##To install UBUNTU  :
  1. To download Ubuntu 16.04.3 LTS, follow this link  
          https://www.ubuntu.com/download/desktop
  2. Move the Ubuntu file into USB.  
  3. Make the USB bootable with rufus. To download rufus, follow this link 
          https://rufus.akeo.ie/
  4. To install Ubuntu, follow this link below  
          https://tutorials.ubuntu.com/tutorial/tutorial-install-ubuntu-desktop?_ga=2.156978296.258151108.1516250990-1540692620.1516250990#3
