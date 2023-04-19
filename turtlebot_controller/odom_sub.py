import math
import rclpy
from rclpy.node import Node

from nav_msgs.msg import Odometry

class PosXY:
    def __init__(self):
        self.x = 0
        self.y = 0

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.listener_callback,
            10)
        self.first_run = True
        self.origin = PosXY
        # self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: Odometry):
        distance = PosXY()
        if self.first_run:
            self.origin.x = msg.pose.pose.position.x
            self.origin.y = msg.pose.pose.position.y
            self.first_run = False

        distance.x = msg.pose.pose.position.x - self.origin.x
        distance.y = msg.pose.pose.position.y - self.origin.y

        travelled = round(math.sqrt(math.pow(distance.x, 2) + math.pow(distance.y, 2)), 2)

        self.get_logger().info(f'I have travelled {travelled} m away from spawn!', throttle_duration_sec=1.0)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
