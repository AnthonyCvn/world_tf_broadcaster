#!/usr/bin/env python
import roslib
import rospy

import tf

def world_tf_broadcaster_node():
    rospy.init_node('world_tf_broadcaster', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        br = tf.TransformBroadcaster()
        br.sendTransform((2, 2, 3),
                         (0, 0, 0, 1),
                         rospy.Time.now(),
                         "camera_1",
                         "world")

        br.sendTransform((5, 2, 3),
                         (0, 0, 0, 1),
                         rospy.Time.now(),
                         "camera_2",
                         "world")
        rate.sleep()

if __name__ == '__main__':
    try:
        world_tf_broadcaster_node()
    except rospy.ROSInterruptException:
        pass
