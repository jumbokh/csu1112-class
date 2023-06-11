### download oracle virtualbox: https://www.virtualbox.org/wiki/Downloads
### download preinstalled vm: https://www.osboxes.org/ubuntu/#ubuntu-22-10-info
### configure:
* sudo passwd osboxes
* time zone: sudo dpkg-reconfigure tzdata
    * Asia/Taipei
* sudo apt update
* sudo apt upgrade
* sudo apt install git wget 
* sudo apt install libopencv-dev python3-opencv
### test opencv
* python3 -c "import cv2; print(cv2.__version__)"
* sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
    gfortran openexr libatlas-base-dev python3-dev python3-numpy \
    libtbb2 libtbb-dev libdc1394-22-dev libopenexr-dev \
    libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
### env
* sudo apt-get install python3-pip
* sudo pip3 install virtualenv
* sudo pip3 install virtualenvwrapper
* mkvirtualenv cv 
* source  ~/.virtualenvs/cv/bin/activate
* vi ~/.bashrc
```
export WORKON_HOME=~/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```
* source ~/.bashrc
* workon cv
* pip install numpy
* pip install scipy
* pip install scikit-image
### reference
* [opencv install](https://vegastack.com/tutorials/how-to-install-opencv-on-ubuntu-20-04/)
* [virtualenv](https://medium.com/@scofield44165/ubuntu-20-04%E4%B8%AD%E5%AE%89%E8%A3%9D%E4%B8%A6%E4%BD%BF%E7%94%A8virtualenv%E8%99%9B%E6%93%AC%E7%92%B0%E5%A2%83-install-and-use-virtualenv-in-ubuntu-20-04-7849091ea8e0)
