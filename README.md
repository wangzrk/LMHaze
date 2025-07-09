<p align="center">
    <img src="img/logo.png" width="300">
</p>


## LMHaze
[ACM MM Asia 2024 Oral] Official implementation of our paper "LMHaze: Intensity-aware Image Dehazing with a Large-scale Multi-intensity Real Haze Dataset".

### [[Paper](https://dl.acm.org/doi/abs/10.1145/3696409.3700178)][[arxiv](https://arxiv.org/abs/2410.16095)]
[Ruikun Zhang](https://scholar.google.com/citations?user=8rabqgoAAAAJ&hl=en), [Hao Yang](https://github.com/noxsine), [Yan Yang](https://scholar.google.com/citations?user=IF0xw34AAAAJ&hl=en), Ying Fu, and [Liyuan Pan](https://scholar.google.com/citations?user=kAt6-AIAAAAJ&hl=en)\*

> **Abstract:**  Image dehazing has drawn a significant attention in recent years. Learning-based methods usually require paired hazy and corresponding ground truth (haze-free) images for training. However, it is difficult to collect real-world image pairs, which prevents developments of existing methods. Although several works partially alleviate this issue by using synthetic datasets or small-scale real datasets. The haze intensity distribution bias and scene homogeneity in existing datasets limit the generalization ability of these methods, particularly when encountering images with previously unseen haze intensities. In this work, we present LMHaze, a large-scale, high-quality real-world dataset. LMHaze comprises paired hazy and haze-free images captured in diverse indoor and outdoor environments, spanning multiple scenarios and haze intensities. It contains over 5K high-resolution image pairs, surpassing the size of the biggest existing real-world dehazing dataset by over 25 times. Meanwhile, to better handle images with different haze intensities, we propose a mixture-of-experts model based on Mamba (MoE-Mamba) for dehazing, which dynamically adjusts the model parameters according to the haze intensity. Moreover, with our proposed dataset, we conduct a new large multimodal model (LMM)-based benchmark study to simulate human perception for evaluating dehazed images. Experiments demonstrate that LMHaze dataset improves the dehazing performance in real scenarios and our dehazing method provides better results compared to state-of-the-art methods. The dataset and code are available at our github page.

![My Image](img/framework.png)


## 📑 Contents
code will be released later!

- [News](#news)
- [TODO](#todo)
- [Dataset](#dataset)
- [Results](#results)
- [Installation](#installation)
- [Training](#training)
- [Testing](#testing)
- [Citation](#cite)



## <a name="news"></a> 🆕 News

- **2024-10-04:** :fire: :fire: :fire: Congratulations! Our paper has been accepted by **ACM MMAsia 2024**！
- **2024-10-21:** arXiv paper available.
- **2024-10-22:** Congratulations! Our paper has been selected as an Oral presentation at **ACM MMAsia 2024**! 🎉
- **2024-10-24:** This repo is released.
- **2024-11-24:** The LMHaze training and test sets have been released! 🎉 We will release training and test code soon~
- **2024-12-10:** The LMHaze training and test codes have been released! 


## <a name="todo"></a> ☑️ TODO

- [x] Build the repo
- [x] arXiv version
- [x] Release code
- [x] Release dataset
- [x] Release logit generation code

## <a name="todo"></a> 📂 Dataset
Due to storage capacity limitations, we have initially released the complete dataset at a resolution of 1200x800. The dataset has been divided into training and test sets following the settings described in the paper. The download instructions are as follows:

| Dataset                                       |                         BaiduNetDisk link                    |                         extraction code                      | Google Drive link                                            |
| :-------------------------------------------- | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| train set                                     | [train set](https://pan.baidu.com/s/1IfNMVB16vfLY6nlNjgXqdQ) (3925 image pairs) | 52zz | https://drive.google.com/file/d/10BiQF9oTexwo3EdRKeyqhY39Q_qAAAc2/view?usp=sharing |
| test set                                      | [test set](https://pan.baidu.com/s/1LTntZHargILIQSsdCLe69Q) (1115 image pairs)  | 52zz | https://drive.google.com/file/d/1V-PwHbLfNgg1nF64bPK9HHUlc93bDSGs/view?usp=sharing |

## <a name="installation"></a> ⚙️ Installation

This codebase was tested with the following environment configurations:

- Ubuntu 20.04
- CUDA 11.7
- Python 3.9
- PyTorch 2.0.1 + cu117

### Previous installation
To use the selective scan with efficient hard-ware design, the `mamba_ssm` library is needed to install with the folllowing command.

```
pip install causal_conv1d==1.0.0
pip install mamba_ssm==1.0.1
```

One can also create a new anaconda environment, and then install necessary python libraries with "./requirement.txt" and the following command: 
```
pip install -r requirements.txt
```

## <a name="training"></a>  🔥 Training

### Train on LMHaze dataset

1. Please download the corresponding training datasets and put them in the folder `./datasets/LMHaze/train`. Download the testing datasets and put them in the folder `./datasets/LMHaze/test`.

2. Please check the `Dehazing/options/train_MoEMamba_LMHaze.yml` file to modify the dataset path and training/testing settings.

3. Follow the instructions below to begin training our model.

```

python -m torch.distributed.launch --nproc_per_node=4 --master_port=1234 Dehazing/basicsr/train.py -opt Dehazing/options/train_MoEMamba_LMHaze.yml --launcher pytorch

```
if you want to test on other dataset, please change the `Dehazing/options/train_MoEMamba_LMHaze.yml` file.

## <a name="testing"></a> 🔥 Testing

### Test on LMHaze dataset

1. Please download the corresponding training datasets and put them in the folder `./datasets/LMHaze/train`. Download the testing datasets and put them in the folder `./datasets/LMHaze/test`.

2. Please check the `Dehazing/options/test_MoEMamba_LMHaze.yml` file to modify the dataset path and testing settings.

3. Follow the instructions below to begin testing our model.
```

python Dehazing/basicsr/test.py -opt Dehazing/options/test_MoEMamba_LMHaze.yml

```
if you want to test on other dataset, please change the `Dehazing/options/test_MoEMamba_LMHaze.yml` file.


## <a name="cite"></a> 🥰 Citation

```
@article{zhang2024lmhaze,
  title={LMHaze: Intensity-aware Image Dehazing with a Large-scale Multi-intensity Real Haze Dataset},
  author={Zhang, Ruikun and Yang, Hao and Yang, Yan and Fu, Ying and Pan, Liyuan},
  journal={arXiv preprint arXiv:2410.16095},
  year={2024}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Acknowledgement

The code is borrowed from the following repositories, thanks for sharing.
- [BasicSR](https://github.com/XPixelGroup/BasicSR)
- [ART](https://github.com/gladzhang/ART)
- [VMamba](https://github.com/MzeroMiko/VMamba)
- [MambaIR](https://github.com/csguoh/MambaIR)

## Contact

Feel free to contact me at **ruikun.zhang@bit.edu.cn** if you have any questions.















