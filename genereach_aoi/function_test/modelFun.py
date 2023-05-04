import torch
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from model_architecture import Basic_CNN, resnet18, pre_resnet18

def check_if_placed(img_path, model_path, block_num):
    
    device =  "cuda" if torch.cuda.is_available() else "cpu"
    #load model
    if "basic_CNN" in model_path:
        model = Basic_CNN().to(device)
        model.load_state_dict(torch.load(model_path, map_location = torch.device(device)))
    elif "pre" in model_path:
        model = pre_resnet18.to(device)
        model.load_state_dict(torch.load(model_path, map_location = torch.device(device)))
    else: 
        model = resnet18.to(device)
        model.load_state_dict(torch.load(model_path, map_location = torch.device(device)))

    #Make the test set
    #1.partition img
    partitioned_img = partition_blocks(img_path, block_num)

    #2.load the img
    test_set = ImageDataset(partitioned_img)
    test_loader = DataLoader(test_set, batch_size=1, shuffle=False, num_workers=0, pin_memory=True)
    # print(f"length: {len(test_set)}")

    #model judgement
    model.eval()
    with torch.no_grad():
        for data in test_loader:
            pred = model(data)
            test_label = np.argmax(pred.cpu().data.numpy(), axis=1)
    return True if test_label[0] else False

def partition_blocks(img_path, block_num):
    #list = [left, upper, right, lower]
    #formal edition
    block_position = {
        "block1":[964, 660, 1182, 1092],
        "block2":[1222, 667, 1713, 1014],
        "block3":[1853, 667, 2359, 1022],
        "block4":[2866, 704, 3115, 1101],
        "block5":[1025, 1332, 1090, 1397],
        "block6":[1017, 1403, 1083, 1470],
        "block7":[1015, 1476, 1092, 1539],
        "block8":[1025, 1545, 1084, 1606],
        "block9":[1013, 1605, 1087, 1675],
        "block10":[1097, 1332, 1184, 1390],
        "block11":[1084, 1394, 1189, 1462],
        "block12":[1098, 1469, 1185, 1539],
        "block13":[1104, 1536, 1188, 1599],
        "block14":[1087, 1603, 1180, 1675],
        "block15":[1209, 1301, 1331, 1667],
        "block16":[1331, 1317, 1451, 1656],
        "block17":[1554, 1368, 1638, 1448],
        "block18":[1561, 1451, 1633, 1519],
        "block19":[1561, 1522, 1631, 1582],
        "block20":[1551, 1583, 1632, 1657],
        "block21":[1652, 1376, 1725, 1446],
        "block22":[1639, 1449, 1731, 1520],
        "block23":[1643, 1514, 1721, 1590],
        "block24":[1647, 1591, 1724, 1653],
        "block25":[1746, 1373, 1812, 1441],
        "block26":[1742, 1443, 1817, 1518],
        "block27":[1745, 1515, 1811, 1587],
        "block28":[1740, 1589, 1809, 1656],
        "block29":[1836, 1336, 1872, 1636],
        "block30":[1873, 1333, 1910, 1631],
        "block31":[1971, 1159, 2190, 1614],
        "block32":[2450, 1130, 2953, 1473],
        "block33":[3025, 1184, 3828, 1703],
        "block34":[954, 1767, 1201, 2153],
        "block35":[1242, 1743, 1459, 2157],
        "block36":[1522, 1730, 1740, 2154],
        "block37":[1834, 1887, 1900, 1996],
        "block38":[1838, 1995, 1905, 2022],#[1831, 1996, 1905, 2065],
        "block39":[1831, 2058, 1890, 2079],#[1825, 2065, 1904, 2128],
        "block40":[1795, 2134, 1910, 2159],#[1826, 2129, 1907, 2159],
        "block41":[2019, 1820, 2129, 2159],
        "block42":[2364, 1831, 2484, 2156],
        "block43":[2483, 1826, 2604, 2156],
        "block44":[2638, 1811, 2759, 2157],
        "block45":[2982, 1850, 3102, 2158],
    }#46, 47 Not Yet
    coordination = block_position["block" + f"{block_num}"]

    img = Image.open(img_path)
    partitioned_img = img.crop((coordination[0], coordination[1], coordination[2], coordination[3]))

    return partitioned_img 

class ImageDataset(Dataset):
    def __init__(self, partitioned_img):
        super(ImageDataset).__init__()
        self.transform = transforms.Compose([
            transforms.Resize((128, 128)),
            transforms.ToTensor()
        ])
        self.im = partitioned_img
  
    def __len__(self):
        return 1
  
    def __getitem__(self,idx):
        im = self.transform(self.im)
        return im

if __name__ == "__main__":
    
    block_num = input("Please input the target block: ")
    model = "basic_CNN"
    img_path = "./imgs_data/1/1_1.jpg"
    model_path = f"./best_model/block{block_num}/"+model+"_best.ckpt"
    
    print(check_if_placed(img_path, model_path, block_num))
