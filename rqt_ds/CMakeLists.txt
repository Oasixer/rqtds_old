cmake_minimum_required(VERSION 2.8.3)
project(rqt_ds)
find_package(catkin REQUIRED
  rospy
  rqt_gui
  rqt_gui_py
)
catkin_package()
catkin_python_setup()

install(FILES plugin.xml
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY resource
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(PROGRAMS scripts/rqt_ds
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)