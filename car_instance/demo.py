import sys
import os
from tqdm import tqdm
sys.path.insert(0, './renderer')
sys.path.insert(0, '../')

from collections import namedtuple
from render_car_no_mesh import CarPoseVisualizer

Setting = namedtuple('Setting', ['image_name', 'data_dir'])

set_name = 'train'   #['train', 'val']
# You need to specify the dataset dir
dataset_dir = '/media/samsumg_1tb/ApolloScape/ECCV2018_apollo/train/'
img_list = [line.rstrip('\n')[:-4] for line in open(os.path.join(dataset_dir, 'split', set_name + '.txt'))]
save_dir = os.path.join(dataset_dir, 'Mesh_overlay')

setting = Setting(None, dataset_dir)
visualizer = CarPoseVisualizer(setting)
visualizer.load_car_models()

for img in tqdm(img_list):
    setting = Setting(img, dataset_dir)
    visualizer.set_dataset(setting)
    merged_image = visualizer.showAnn(setting.image_name, set_name, save_dir)

