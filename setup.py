from setuptools import setup
import os
from glob import glob

package_name = 'turtlebot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yml'))
    ],
    install_requires=[
        'setuptools',
        'os',
        'glob'
    ],
    zip_safe=True,
    maintainer='frie',
    maintainer_email='frie.krause@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'odom_listener = turtlebot_controller.odom_sub:main',
            'scan_listener = turtlebot_controller.scan_sub:main'
        ],
    },
)
