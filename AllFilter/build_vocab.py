import nltk
import pickle
import argparse
from collections import Counter
from pycocotools.coco import COCO
from Vocabulary import Vocabulary


"""此处Vocabulary无法被调用，另写"""

def build_vocab(json, threshold):
    """创建简单的词汇表包装器"""
    coco = COCO(json)
    counter = Counter()
    ids = coco.anns.keys()
    for i, id in enumerate(ids):
        caption = str(coco.anns[id]['caption'])#获取json文件里的'caption'标签内容
        """coco里包括：self.dataset,self.anns,self.cats,self.imgs四个数据对象，通过cats获取到
        ###Json数据中的"categories"，从而获取到里面的'name'标签，以自定义的数据集train.json为例;
        ###anns获取Json数据中的"annotations".
        """
        #caption = str(coco.cats[id]['name'])
        print("单词:"+caption)
        tokens = nltk.tokenize.word_tokenize(caption.lower())
        counter.update(tokens)

        if (i+1) % 1000 == 0:
            print("[{}/{}] Tokenized the captions.".format(i+1, len(ids)))

    #检测频率大于等于threshold的单词并放入词汇表
    words = [word for word, cnt in counter.items() if cnt >= threshold]

    # 创建一个词汇表包装器并添加特殊的令牌
    vocab = Vocabulary()
    vocab.add_word('<pad>')
    vocab.add_word('<start>')
    vocab.add_word('<end>')
    vocab.add_word('<unk>')

    # Add the words to the vocabulary.
    for i, word in enumerate(words):
        vocab.add_word(word)
    return vocab

def main(args):
    vocab = build_vocab(json=args.caption_path, threshold=args.threshold)
    vocab_path = args.vocab_path
    with open(vocab_path, 'wb') as f:
        pickle.dump(vocab, f)
    print("总词汇量: {}".format(len(vocab)))
    print("词汇表保存地址:'{}'".format(vocab_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--caption_path', type=str,default='coco_data/annotations/captions_train2014.json',help='注释文件地址')
    #parser.add_argument('--caption_path', type=str, default='coco_data/annotations/train.json',help='注释文件地址')
    parser.add_argument('--vocab_path', type=str, default='./coco_data/vocab.pkl',
                        help='词汇表文件地址')
    parser.add_argument('--threshold', type=int, default=4,
                        help='词汇阈值')
    args = parser.parse_args()
    main(args)