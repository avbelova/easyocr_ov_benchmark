# easyocr_ov_benchmark
Scripts for benchmarking of [OpenVINO integration into EasyOCR](https://github.com/avbelova/EasyOCR)  
This repo helps to benchmark OpenVINO integration into EasyOCR and compare it with an original one based on Pytorch (on CPU).

## Installation
1. Create a virtual environment or use an existing one:
On Linux:
```bash
python3 -m venv env
source env/bin/activate
```
On Windows:
```bash
python -m venv env
env\Scripts\activate
```
2. Clone the repo:
```bash
git clone https://github.com/avbelova/easyocr_ov_benchmark.git
cd easyocr_ov_benchmark
```
4. Install OpenVINO integration into EasyOCR:
```bash
pip install git+https://github.com/avbelova/EasyOCR.git
```
## Run benchmarking
```bash
python easyocr_ov_benchmark.py <PATH-TO-AN-INPUT-IMAGE> <LANGUAGE>
```
Additianally you can specify an inference device for OpenVINO (default one is CPU) and a number of iterations (default is 10).  
For example the following command runs 20 benchmarking iterations of English language recognition on Intel(R) Processor Graphics:
```bash
python easyocr_ov_benchmark.py EasyOCR/examples/english.png en -n 20 -d ov_gpu
```
Running Chinese+English text recognition benchmarking on Intel(R) Discrete Graphics:
```bash
python easyocr_ov_benchmark.py EasyOCR/examples/chinese.jpg ch_sim en -d ov_gpu.1
```


