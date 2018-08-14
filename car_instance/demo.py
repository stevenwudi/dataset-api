import sys
sys.path.insert(0, './renderer')
sys.path.insert(0, '../')

from collections import namedtuple
import render_car_no_mesh as rci

Setting = namedtuple('Setting', ['image_name', 'data_dir'])
setting = Setting('180116_053947113_Camera_5', '/home/wudi/Data/3d_car_instance_sample/')

visualizer = rci.CarPoseVisualizer(setting)
visualizer.load_car_models()
merged_image = visualizer.showAnn(setting.image_name)
