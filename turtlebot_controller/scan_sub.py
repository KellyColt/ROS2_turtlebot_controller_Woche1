import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        topic = self.declare_parameter('topic_name', 'topic')
        q_size = self.declare_parameter('queue_size', 0)
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            q_size.value)
        # self.subscription  # prevent unused variable warning

    def listener_callback(self, msg: LaserScan):
        self.get_logger().info('I heard: "%s"' % msg.header.frame_id)


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
