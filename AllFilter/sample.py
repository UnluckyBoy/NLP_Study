import json

import torch
import matplotlib.pyplot as plt
import numpy as np
import argparse
import pickle
import os
import pandas as pd
from torchvision import transforms
from build_vocab import Vocabulary
from model import EncoderCNN, DecoderRNN
from PIL import Image
import cv2

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def load_image(image_path, transform=None):
    image = Image.open(image_path).convert('RGB')
    image = image.resize([224, 224], Image.LANCZOS)

    if transform is not None:
        image = transform(image).unsqueeze(0)
    return image

def main(args):
    # Image preprocessing
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406),
                             (0.229, 0.224, 0.225))])

    # Load vocabulary wrapper
    with open(args.vocab_path, 'rb') as f:
        vocab = pickle.load(f)

    # Build models
    encoder = EncoderCNN(args.embed_size).eval()  # eval mode (batchnorm uses moving mean/variance)
    decoder = DecoderRNN(args.embed_size, args.hidden_size, len(vocab), args.num_layers)
    encoder = encoder.to(device)
    decoder = decoder.to(device)

    # Load the trained model parameters
    encoder.load_state_dict(torch.load(args.encoder_path))
    decoder.load_state_dict(torch.load(args.decoder_path))

    # Prepare an image
    image = load_image(args.image, transform)
    image_tensor = image.to(device)

    # Generate an caption from the image
    feature = encoder(image_tensor)
    sampled_ids = decoder.sample(feature)
    sampled_ids = sampled_ids[0].cpu().numpy()  # (1, max_seq_length) -> (max_seq_length)

    # Convert word_ids to words
    #通过词汇id键值在词汇表中创建一句话
    #sampled_caption = []
    #for word_id in sampled_ids:
        #word = vocab.idx2word[word_id]
        #sampled_caption.append(word)
        #if word == '<end>':
            #break
    #sentence = ' '.join(sampled_caption)

    #不需要一句话，只需要识别出生物
    #sentence = vocab.idx2word[sampled_ids[1]]+' '+vocab.idx2word[sampled_ids[2]]
    sentence = vocab.idx2word[sampled_ids[2]]

    ###转换中英文
    with open(args.Json_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        for Key in json_data:
            mWord=json_data[Key]
            #mValue = mWord[0][sentence]
            #print(mValue)
            for i in range(len(mWord)):
                mDic_word=mWord[i]
                #print(mDic_word)
                for key in mDic_word.keys():
                    #print(key)
                    if sentence==key:
                        #print(mDic_word[key])
                        sentence=mDic_word[key]
                        break
                    else:
                        break
                    pass
                pass
            pass

    # Print out the image and the generated caption
    # 打印出最终识别结果并绘制
    print(args.image + "_最终识别结果：" + sentence)
    # 绘制原图
    image = Image.open(args.image)
    # 解决中文显示问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title("原图")  # title
    plt.imshow(np.asarray(image))

    ###以openCV绘制
    # img1 = cv2.imread(args.image, flags=1)  # flags=1读取彩色图像(BGR)
    # imageRGB = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # 图片格式转换：BGR(OpenCV) -> RGB(PyQt5)
    # plt.imshow(imageRGB)  # matplotlib 显示彩色图像(RGB格式)

    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True, help='图像输入参数')
    parser.add_argument('--encoder_path', type=str, default='coco_models/encoder-5-3000.ckpt',
                        help='训练编码器路径')
    parser.add_argument('--decoder_path', type=str, default='coco_models/decoder-5-3000.ckpt',
                        help='训练解码器路径')
    parser.add_argument('--vocab_path', type=str, default='coco_data/vocab.pkl', help='单词包装器地址')

    # Model parameters (should be same as paramters in train.py)
    parser.add_argument('--embed_size', type=int, default=256, help='词嵌入向量的维数')
    parser.add_argument('--hidden_size', type=int, default=512, help='LSTM隐藏状态的维数')
    parser.add_argument('--num_layers', type=int, default=1, help='LSTM中的层数')
    parser.add_argument('--Json_path',type=str,default='./coco_data/WordTransition.json',help='中英文转换Json文件地址')
    args = parser.parse_args()
    main(args)
