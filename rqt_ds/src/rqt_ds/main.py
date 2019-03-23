import os
import rospy
import rospkg
import datetime
import threading
import time

from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget, QPushButton, QMessageBox, QTextEdit, QLineEdit
from python_qt_binding.QtCore import Qt, Signal

class DriverStationMain(Plugin):

    def __init__(self, context):
        super(DriverStationMain, self).__init__(context)
        # Give QObjects reasonable names
        self.setObjectName('MainWindow')

        # Process standalone plugin command-line arguments
        from argparse import ArgumentParser
        parser = ArgumentParser()
        # Add argument(s) to the parser.
        parser.add_argument("-q", "--quiet", action="store_true",
                      dest="quiet",
                      help="Put plugin in silent mode")
        args, unknowns = parser.parse_known_args(context.argv())
        if not args.quiet:
            print 'arguments: ', args
            print 'unknowns: ', unknowns

        # Create QWidget
        self._widget = QWidget()
        # Get path to UI file which should be in the "resource" folder of this package
        ui_file = os.path.join(rospkg.RosPack().get_path('rqt_ds'), 'resource', 'driver-station.ui')
        # Extend the widget with all attributes and children from UI file
        loadUi(ui_file, self._widget)
        # Give QObjects reasonable names
        self._widget.setObjectName('DriverStationWidget')
        # Show _widget.windowTitle on left-top of each plugin (when 
        # it's set in _widget). This is useful when you open multiple 
        # plugins at once. Also if you open multiple instances of your 
        # plugin at once, these lines add number to make it easy to 
        # tell from pane to pane.
        if context.serial_number() > 1:
            self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
        # Add widget to the user interface
        context.add_widget(self._widget)

        '''def clock_thread():
            while(True):
                # TODO: Change the way this works - current you have to ctrl + z stop the thread
                # This will probably make more sense when I figure out message listeners
                delta=str(datetime.datetime.now()-self.startTime)
                self._widget.elapsedTimeText.setText(delta[-12:])
                time.sleep(0.1)'''

        #self._widget.testButton.clicked.connect(self.test)
        '''testValue = True # TODO Theoretically, this is a boolean telling us whether we have comms
        self.commStatus(testValue)
        self.startTime=datetime.datetime.now()
        clockthread = threading.Thread(target=clock_thread)
        clockthread.start()'''



        #dateString = str(datetime.datetime.now())
        #print(dateString)
        #self._widget.elapsedTimeText.setText(dateString)

        #self.button.clicked.connect(self.on_button.clicked)

    '''def on_button_clicked():
            alert = QMessageBox()
            alert.setText('You clicked the button!')
            alert.exec_()'''
    #def setClock():


    def commStatus(self, whatever):
        if whatever:
            self._widget.comms.setText("Enabled")
        else:
            self._widget.comms.setText("Disabled")

    def shutdown_plugin(self):
        # TODO unregister all publishers here
        pass

    def save_settings(self, plugin_settings, instance_settings):
        # TODO save intrinsic configuration, usually using:
        # instance_settings.set_value(k, v)
        pass

    def restore_settings(self, plugin_settings, instance_settings):
        # TODO restore intrinsic configuration, usually using:
        # v = instance_settings.value(k)
        pass

    #def trigger_configuration(self):
        # Comment in to signal that the plugin has a way to configure
        # This will enable a setting button (gear icon) in each dock widget title bar
        # Usually used to open a modal configuration dialog