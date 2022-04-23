import os
import shutil
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random
from PIL import Image

from com_ineuron_utils.utils import encodeImageIntoBase64

import sys
#sys.path.insert(0, 'com_ineuron_apparel/predictor_yolo_detector')

from predictor_yolo_detector.models.experimental import attempt_load
from predictor_yolo_detector.utils.datasets import LoadStreams, LoadImages
from predictor_yolo_detector.utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords,
    xyxy2xywh, plot_one_box, strip_optimizer, set_logging)
from predictor_yolo_detector.utils.torch_utils import select_device, load_classifier, \
    time_synchronized


class Detector():
    def __init__(self, filename, model_name):
        # self.weights = "./com_ineuron_apparel/predictor_yolo_detector/best.pt"
        self.conf = float(0.5)
        self.source = "inputImage.jpg"
        self.img_size = int(416)
        self.save_dir = "output.jpg"
        self.view_img = False
        self.save_txt = True
        self.device = 'cpu'
        self.augment = True
        self.agnostic_nms = True
        self.conf_thres = float(0.5)
        self.iou_thres = float(0.45)
        self.classes = 0
        self.save_conf = True
        self.update = True
        self.filename = filename
        self.pred_class = []
        self.pred_score = []
        self.pred_bbox = []
        self.pred_time = 0.0
        self.model_name = model_name

    def detect(self, save_img=False):
        out, source,  view_img, save_txt, imgsz = \
            self.save_dir, self.source,  self.view_img, self.save_txt, self.img_size
        webcam = source.isnumeric() or source.startswith(('rtsp://', 'rtmp://', 'http://')) or source.endswith('.txt')

        # Initialize
        set_logging()
        device = select_device(self.device)
        '''if os.path.exists(out):  # output dir
            shutil.rmtree(out)  # delete dir
        os.makedirs(out)  # make new dir'''
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        # model = attempt_load(weights, map_location=device)  # load FP32 model
        if self.model_name == "yolov5s":
            print('model is yolov5s')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

        elif self.model_name == "yolov5l":
            print('model is yolov5l')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5l')

        elif self.model_name == "yolov5x":
            print('model is yolov5x')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5x')

        elif self.model_name == "yolov5n":
            print('model is yolov5n')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5n')

        elif self.model_name == "yolov5m6":
            print('model is yolov5m6')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5m6')

        elif self.model_name == "yolov5n6":
            print('model is yolov5n6')
            model = torch.hub.load('ultralytics/yolov5', 'yolov5n6')

        stride, names, pt = model.stride, model.names, model.pt
        imgsz = check_img_size(imgsz, s=stride)  # check img_size
        if half:
            model.half()  # to FP16

        # Second-stage classifier
        classify = False
        if classify:
            modelc = load_classifier(name='resnet101', n=2)  # initialize
            modelc.load_state_dict(torch.load('weights/resnet101.pt', map_location=device)['model'])  # load weights
            modelc.to(device).eval()

        # Set Dataloader
        vid_path, vid_writer = None, None
        if webcam:
            view_img = True
            cudnn.benchmark = True  # set True to speed up constant image size inference
            dataset = LoadStreams(source, img_size=imgsz)
        else:
            save_img = True
            dataset = LoadImages(source, img_size=imgsz)

        # Get names and colors
        #names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        # Run inference
        t0 = time.time()
        img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
        _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            t1 = time_synchronized()
            # imgsz = img[0]

            pred = model(img, augment=self.augment)

            # Apply NMS
            pred = non_max_suppression(pred, self.conf_thres, self.iou_thres,
                                       agnostic=self.agnostic_nms)
            t2 = time_synchronized()

            # Apply Classifier
            if classify:
                pred = apply_classifier(pred, modelc, img, im0s)

            # Process detections
            for i, det in enumerate(pred):  # detections per image
                if webcam:  # batch_size >= 1
                    p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
                else:
                    p, s, im0 = path, '', im0s

                # save_path = str(Path(out) / Path(p).name)
                # txt_path = str(Path(out) / Path(p).stem) + ('_%g' % dataset.frame if dataset.mode == 'video' else '')
                s += '%gx%g ' % img.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += '%g %ss, ' % (n, names[int(c)])  # add to string

                    # Write results
                    for *xyxy, conf, cls in reversed(det):
                        if save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            line = (cls, conf, *xywh) if self.save_conf else (cls, *xywh)  # label format
                            '''with open(txt_path + '.txt', 'a') as f:
                                f.write(('%g ' * len(line) + '\n') % line)'''
                            print(f'cls:{cls}, conf:{conf}, xywh:{xywh}')
                            self.pred_class.append(cls)
                            self.pred_score.append(conf)
                            self.pred_bbox.append(xywh)

                        if save_img or view_img:  # Add bbox to image
                            label = '%s %.2f' % (names[int(cls)], conf)
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)

                # Print time (inference + NMS)
                print('%sDone. (%.3fs)' % (s, t2 - t1))


                if save_img:
                    if dataset.mode == 'images':

                        #im = im0[:, :, ::-1]
                        im = Image.fromarray(im0)

                        im.save("output.jpg")
                        # cv2.imwrite(save_path, im0)
                    else:
                        print("Video Processing Needed")


        '''if save_txt or save_img:
            # print('Results saved to %s' % Path(out))'''

        print('Done. (%.3fs)' % (time.time() - t0))
        self.pred_time = round((time.time() - t0), 3)

        return "Done"

    def detect_action(self):
        with torch.no_grad():
            self.detect()
        bgr_image = cv2.imread("output.jpg")
        im_rgb = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite('output.jpg', im_rgb)
        opencodedbase64 = encodeImageIntoBase64("output.jpg")
        result = {"image": opencodedbase64.decode('utf-8'),
                  "pred_bbox": str(self.pred_bbox),
                  "pred_score": str(self.pred_score),
                  "pred_class": str(self.pred_class),
                  "pred_time": str(self.pred_time)}
        return result

