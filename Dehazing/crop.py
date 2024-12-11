import os
from PIL import Image

def center_crop(image, crop_width, crop_height):
    width, height = image.size
    left = (width - crop_width) / 2
    top = (height - crop_height) / 2
    right = (width + crop_width) / 2
    bottom = (height + crop_height) / 2
    return image.crop((left, top, right, bottom))

def crop_images_in_folders(hazy_folder, gt_folder, output_hazy_folder, output_gt_folder, crop_width=1200, crop_height=800):
    if not os.path.exists(output_hazy_folder):
        os.makedirs(output_hazy_folder)
    if not os.path.exists(output_gt_folder):
        os.makedirs(output_gt_folder)
        
    hazy_files = set(os.listdir(hazy_folder))
    gt_files = set(os.listdir(gt_folder))
    common_files = hazy_files.intersection(gt_files)
    
    for file_name in common_files:
        hazy_path = os.path.join(hazy_folder, file_name)
        gt_path = os.path.join(gt_folder, file_name)
        
        with Image.open(hazy_path) as hazy_img:
            cropped_hazy_img = center_crop(hazy_img, crop_width, crop_height)
            cropped_hazy_img.save(os.path.join(output_hazy_folder, file_name))
        
        with Image.open(gt_path) as gt_img:
            cropped_gt_img = center_crop(gt_img, crop_width, crop_height)
            cropped_gt_img.save(os.path.join(output_gt_folder, file_name))

# 使用示例
hazy_folder = '/home/a/Desktop/BIT_Haze/O-HAZY/test/hazy'
gt_folder = '/home/a/Desktop/BIT_Haze/O-HAZY/test/GT'
output_hazy_folder = '/home/a/Desktop/O-HAZY_cropped/test/hazy'
output_gt_folder = '/home/a/Desktop/O-HAZY_cropped/test/GT'

crop_images_in_folders(hazy_folder, gt_folder, output_hazy_folder, output_gt_folder)
