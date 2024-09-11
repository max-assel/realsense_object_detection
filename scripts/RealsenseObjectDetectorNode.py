import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

class ObjectDetector(object):
    def __init__(self):
        print("ObjectDetector")

        self.depth_image_topic = "/camera/color/image_raw"
        self.depth_queue_size = 1
        self.buff_size = (2 ** 25)

        self.depth_img_sub = rospy.Subscriber(self.depth_image_topic,
                                                Image, 
                                                self.depth_image_callback, 
                                                queue_size=self.depth_queue_size, 
                                                buff_size=self.buff_size)

    # Currently, compressed depth images are coming in at ~20 Hz
    def depth_image_callback(self, imageData):
        # cb_start = time.time()

        # preproc_start = time.time()
        input_img = bridge.imgmsg_to_cv2(imageData, desired_encoding="passthrough")

        if (input_img is None):
            print("input img is none!")
            return

        #########################
        ## ADD CODE UNDER HERE ##
        #########################

        print("input_img: ", input_img)

        #########################
        ## ADD CODE ABOVE HERE ##
        #########################


if __name__ == '__main__':
    try:
        rospy.init_node('realsense_object_detection')

        realsenseObjectDetector = ObjectDetector()

        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("realsense_object_detection - ROSInterruptException")


