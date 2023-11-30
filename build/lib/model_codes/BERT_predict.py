from transformers import BertTokenizer, BertModel, TFBertForSequenceClassification
import pandas as pd
import numpy as np
from processing.text_preprocessing import preprocess

def input_output(text_array, tokenizer, max_length):
    input_ids=[]
    attention_masks=[]

    for i in range(len(text_array)):
        if isinstance(text_array[i], str):
            bert_inp = tokenizer.encode_plus(text_array[i],
                                             add_special_tokens = True,
                                             max_length = max_length,
                                             #truncation=True,
                                             #padding=True,
                                             pad_to_max_length = True,
                                             return_attention_mask = True)
            input_ids.append(bert_inp['input_ids'])
            attention_masks.append(bert_inp['attention_mask'])

    input_ids=np.asarray(input_ids)
    attention_masks=np.array(attention_masks)
    return(input_ids, attention_masks)

def BERT_predict(data_path,
                 text_variable,
                 user_variable):
    # load the data
    df = pd.read_csv(data_path)

    # clean data
    df[text_variable] = df[text_variable].apply(lambda x: preprocess(x, remove_stop_words = False))
    df = df[df[text_variable].notna()]

    # import model and tokenizer
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = TFBertForSequenceClassification.from_pretrained("LingshuHu/BEpaRTy", num_labels=2)
    inp, mask = input_output(df[text_variable].values, tokenizer, max_length=64)

    # prediction
    pred = model.predict([inp, mask])
    pred_proba = [p[1]-p[0] for p in pred[0]]

    df_pred = pd.DataFrame(zip(df[user_variable].values, pred_proba), columns=[user_variable, 'pred_proba'])
    
    return(df_pred)
