<p align="center">
    <img src="assets/logo.png" width="300">
</p>


## LMHaze
official implementation of paper "LMHaze: Intensity-aware Image Dehazing with a Large-scale Multi-intensity Real Haze Dataset".

### [[Paper](https://arxiv.org/abs/2410.16095)]
[Ruikun Zhang](https://scholar.google.com/citations?user=8rabqgoAAAAJ&hl=en)\*, Hao Yang, [Yan Yang](https://scholar.google.com/citations?user=IF0xw34AAAAJ&hl=en), Ying Fu, and [Liyuan Pan](https://scholar.google.com/citations?user=kAt6-AIAAAAJ&hl=en)

> **Abstract:**  Image dehazing has drawn a significant attention in recent years. Learning-based methods usually require paired hazy and corresponding ground truth (haze-free) images for training. However, it is difficult to collect real-world image pairs, which prevents developments of existing methods. Although several works partially alleviate this issue by using synthetic datasets or small-scale real datasets. The haze intensity distribution bias and scene homogeneity in existing datasets limit the generalization ability of these methods, particularly when encountering images with previously unseen haze intensities. In this work, we present LMHaze, a large-scale, high-quality real-world dataset. LMHaze comprises paired hazy and haze-free images captured in diverse indoor and outdoor environments, spanning multiple scenarios and haze intensities. It contains over 5K high-resolution image pairs, surpassing the size of the biggest existing real-world dehazing dataset by over 25 times. Meanwhile, to better handle images with different haze intensities, we propose a mixture-of-experts model based on Mamba (MoE-Mamba) for dehazing, which dynamically adjusts the model parameters according to the haze intensity. Moreover, with our proposed dataset, we conduct a new large multimodal model (LMM)-based benchmark study to simulate human perception for evaluating dehazed images. Experiments demonstrate that LMHaze dataset improves the dehazing performance in real scenarios and our dehazing method provides better results compared to state-of-the-art methods. The dataset and code are available at our project page.

## 📑 Contents
code will be released later!

- [News](#news)
- [TODO](#todo)
- [Model Summary](#model_summary)
- [Results](#results)
- [Visual Results](#visual_results)
- [Installation](#installation)
- [Training](#training)
- [Testing](#testing)
- [Citation](#cite)



![My Image](img/framework.png)


