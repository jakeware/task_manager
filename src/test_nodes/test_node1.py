#!/usr/bin/env python
# Copyright 2018 Massachusetts Institute of Technology

import rospy

from test_nodes import test_process_ros

if __name__ == '__main__':
    rospy.init_node('test_node1')
    test_process1 = test_process_ros.TestProcessRos('1')
    test_process1.Run()