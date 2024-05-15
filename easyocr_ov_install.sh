#! /bin/bash

git clone https://github.com/avbelova/EasyOCR.git
git checkout feature/openvino-backend
pip install wheel
cd EasyOCR/
python setup.py bdist_wheel
pip install dist/easyocr-1.7.1-py3-none-any.whl
echo "EasyOCR OpenVINO is successfully installed."
