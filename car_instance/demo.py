import sys
from tqdm import tqdm
sys.path.insert(0, './renderer')
sys.path.insert(0, '../')

from collections import namedtuple
import render_car_no_mesh as rci
#import render_car_instances as rci

Setting = namedtuple('Setting', ['image_name', 'data_dir'])

set_name = 'val'   #['train', 'val']
img_list = [line.rstrip('\n')[:-4] for line in
            open('/media/samsumg_1tb/ApolloScape/ECCV2018_apollo/3d_car_instance_sample/split/' + set_name + '.txt')]

#img_list = ['180116_053947113_Camera_5']

for img in tqdm(img_list):
    setting = Setting(img, '/home/wudi/Data/3d_car_instance_sample/')
    visualizer = rci.CarPoseVisualizer(setting)
    visualizer.load_car_models()
    merged_image = visualizer.showAnn(setting.image_name, set_name)

