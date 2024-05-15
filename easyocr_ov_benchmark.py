import cv2
import numpy as np
import easyocr
from time import perf_counter
import argparse

def benchmark(reader, img, niter):
    times = []
    for i in range(0, niter):
        start_time = perf_counter()
        result = reader.readtext(img, detail=0)
        exec_time = perf_counter()-start_time
        time_ms = round(exec_time*1000,2)
        print('Execution time: ',time_ms, "ms")
        times.append(time_ms)
        print("OCR result:")
        print(result)
    avg_time = round(np.average(times),2)
    return avg_time

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help = "Path to input image")
    parser.add_argument("language", help = "Language in easyOCR format: en for English, hi for Hindi, etc. ", nargs = '+')
    parser.add_argument("-d", "--device_ov", help = "Inference device in OpenVINO format", default = "ov_cpu")
    parser.add_argument("-n", "--iterations_number", help = "Number of benchmarking iterations", type = int, default = 10)
    args = parser.parse_args()
    img = cv2.imread(args.image)
    language = args.language
    ov_device = args.device_ov
    niter = args.iterations_number
    reader_pt = easyocr.Reader(language,"cpu")
    latency_pt = benchmark(reader_pt, img, niter)
    reader_ov = easyocr.Reader(language, ov_device)
    latency_ov = benchmark(reader_ov, img, niter)

    print("------------------------------------------------------")
    print("Language: ", language)
    print("Image shape: ", img.shape)
    print("Latency Pytorch CPU : ", latency_pt, "MS")
    print("Latency OpenVINO", ov_device, ": ",  latency_ov, "MS")


if __name__ == "__main__":
    main()
