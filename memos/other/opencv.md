#### system
```
sudo apt-get update
sudo apt-get upgrade
```

#### tools
Remove any previous installations of x264


```
sudo apt-get remove x264 libx264-dev
```

We will Install dependencies now

``` 
sudo apt-get install build-essential checkinstall cmake pkg-config yasm
sudo apt-get install git gfortran
sudo apt-get install libjpeg8-dev libjasper-dev libpng12-dev
```

If you are using Ubuntu 14.04
```
sudo apt-get install libtiff4-dev
```
If you are using Ubuntu 16.04
```
sudo apt-get install libtiff5-dev
```

```
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev
sudo apt-get install libxine2-dev libv4l-dev
sudo apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get install qt5-default libgtk2.0-dev libtbb-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
sudo apt-get install libvorbis-dev libxvidcore-dev
sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
sudo apt-get install x264 v4l-utils
```
###### Optional dependencies
```
sudo apt-get install libprotobuf-dev protobuf-compiler
sudo apt-get install libgoogle-glog-dev libgflags-dev
sudo apt-get install libgphoto2-dev libeigen3-dev libhdf5-dev doxygen
```

#### install python package
```
pip install python3-dev numpy
```

#### compile
```
cd opencv && mkdir build && cd build
cmake CMAKE_BUILD_TYPE=RELEASE \
      CMAKE_INSTALL_PREFIX=/usr/local \
      INSTALL_C_EXAMPLES=ON \
      INSTALL_PYTHON_EXAMPLES=ON \
      WITH_TBB=ON \
      WITH_V4L=ON \
      WITH_QT=ON \
      WITH_OPENGL=ON \
      OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      BUILD_EXAMPLES=ON ..

make -j4
sudo make install
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```
