"""
Author: J0hNnY1ee joh1eenny@gmail.com
Date: 2025-03-10 17:22:27
LastEditors: J0hNnY1ee joh1eenny@gmail.com
LastEditTime: 2025-03-11 13:10:46
FilePath: /Language-Independent-Named-Entity-Recognition/main.py
Description:

Copyright (c) 2025 by J0hNnY1ee joh1eenny@gmail.com, All Rights Reserved.
"""

# 创建标签到数字的映射
unique_tags = set(tag for target in targets for tag in target)
tag_to_id = {tag: idx for idx, tag in enumerate(unique_tags)}
id_to_tag = {idx: tag for tag, idx in tag_to_id.items()}  # 创建数字到标签的映射

# 将标注列表转换为数字列表
numeric_targets = []
for target in targets:
    numeric_target = [tag_to_id[tag] for tag in target]
    numeric_targets.append(numeric_target)

self.numeric_targets = numeric_targets
self.id_to_tag = id_to_tag
self.tag_to_id = tag_to_id

unique_words = set(word for sentence in sentences for word in sentence)
word_to_id = {word: idx for idx, word in enumerate(unique_words)}
id_to_word = {idx: word for word, idx in word_to_id.items()}
tokenized_sentences = []
for sentence in sentences:
    tokenized_sentence = [word_to_id[word] for word in sentence]
    tokenized_sentences.append(tokenized_sentence)
self.tokenized_sentences = tokenized_sentences
self.word_to_id = word_to_id
self.id_to_word = id_to_word
self.vocab_size = len(word_to_id)
