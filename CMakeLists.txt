cmake_minimum_required(VERSION 3.0.2)
project(realsense_object_detection)

## Compile as C++11, supported in ROS Kinetic and newer
find_package(catkin REQUIRED)

###################################
## catkin specific configuration ##
###################################

catkin_package(
  CATKIN_DEPENDS realsense2_camera
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
catkin_install_python(PROGRAMS
   scripts/RealsenseObjectDetectorNode.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)