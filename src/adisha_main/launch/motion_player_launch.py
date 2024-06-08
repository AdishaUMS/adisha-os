import os
import yaml
from launch import LaunchDescription
from launch_ros.actions import Node


CORE_CONFIG_PATH    = os.path.join(os.getcwd(), 'src/adisha_data/config/core_config.yaml')
JOINT_CONFIG_PATH   = os.path.join(os.getcwd(), 'src/adisha_data/config/joint_config.yaml')
ROBOT_CONFIG_PATH   = os.path.join(os.getcwd(), 'src/adisha_data/config/robot_config.yaml')
POSE_PATH           = os.path.join(os.getcwd(), 'src/adisha_data/data/pose_studio')
MOTION_PATH         = os.path.join(os.getcwd(), 'src/adisha_data/data/motion_sequencer')


with open(ROBOT_CONFIG_PATH, 'r') as file:
    ROBOT_CONFIG    = yaml.safe_load(file)
    ROBOT_ID        = ROBOT_CONFIG['id']
    MASTER_CLOCK    = ROBOT_CONFIG['master_clock']


with open(JOINT_CONFIG_PATH, 'r') as file:
    JOINT_CONFIG    = yaml.safe_load(file)
    DXL_BAUDRATE    = JOINT_CONFIG['dxl_baudrate']
    DXL_U2D2_PORT   = JOINT_CONFIG['dxl_u2d2_port']
    DXL_NUM         = JOINT_CONFIG['dxl_num']
    DXL_ID          = JOINT_CONFIG['dxl_id']
    DXL_TYPE        = JOINT_CONFIG['dxl_type']
    JOINT_NAME      = JOINT_CONFIG['joint_name']


def generate_launch_description():
    
    motion_player_node = Node(
        package     = 'adisha_controllers',
        executable  = 'motion_player',
        name        = f'{ROBOT_ID}_motion_player',
        parameters  = [
            {'id': ROBOT_ID},
            {'dxl_baudrate': DXL_BAUDRATE},
            {'dxl_u2d2_port': DXL_U2D2_PORT},
            {'dxl_num': DXL_NUM},
            {'dxl_id': DXL_ID},
            {'dxl_type': DXL_TYPE},
            {'joint_name': JOINT_NAME},
            {'master_clock': MASTER_CLOCK},
            {'pose_path': POSE_PATH},
            {'motion_path': MOTION_PATH}, 
            {'motions': [
                'motion01'
            ]}
        ]
    )

    return LaunchDescription([
        motion_player_node
    ])