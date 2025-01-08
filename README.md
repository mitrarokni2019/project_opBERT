# project_opBERT


# Study of opinion change in social media for 1DL508 Project in Data Science at Uppsala University
Social media significantly shapes public opinion on critical issues such as climate change, making it crucial to understand the factors driving opinion change. This study examines the factors influencing opinion shifts on Reddit's r/ChangeMyView subreddit, a platform that allows original posters to award persuasive and influential comments with a delta symbol. Specifically, this research explores two approaches to analyzing comments:
(1) categorizing comments based on ten social intent(dimensions) as "knowledge", "trust", "similarity", "power", "status", "support", "romance", "identity","fun","conflict".
       + LSTM (Long Short-Term Memory) networks for sequence classification from ( https://github.com/lajello/tendimensions ) 
       + Zero-shot classification using BERT (Hugging Face transformers) for classification without needing labeled data.
(2) evaluating conceptual agreement between posts and comments,(conseptual semantic): agree, disagree, neutral. 
       + GPT-4: For labeling the relationship between posts and comments based on semantic content.
       + Data Augmentation:Back-translation: Using Helsinki-NLP/opus-mt models for text translation and re-translation.
                           Random word order, random deletion, and random insertion to augment the dataset.
       + BERT: Model classification, fine-tuning, and predicting labels for post-comment agreement.

Some instructions:
      - Datsets and bert_model for predicting the label can be achieved from my google drive : https://drive.google.com/drive/folders/1UWZPMsBBsylt4RbL9wc_Z9Nk5nBovWNO?usp=drive_link 
      - Dowload all embeddings from http://www.lajello.com/files/tendimensions_embeddings.zip
      - If facing issues running ttnet, compile multinet from source from https://github.com/uuinfolab/py_multinet/tree/master



[1] Monti, C., Aiello, L.M., De Francisci Morales, G. et al. The language of opinion change on social media under the lens of communicative action. Sci Rep 12, 17920 (2022). https://doi.org/10.1038/s41598-022-21720-4

[2] Vega, D., Magnani, M. Foundations of Temporal Text Networks. Appl Netw Sci 3, 25 (2018). https://doi.org/10.1007/s41109-018-0082-3
