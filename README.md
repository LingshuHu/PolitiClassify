# PolitiClassify
A python package for classifying Twitter users' political orientation with two-step deep learning models.

Two models can be chosen for the first step of the method: LSTM and BERT. The trained BERT model will be automatically downloaded.The LSTM model need to be downlaoded from [here](https://drive.google.com/file/d/1uqw9rjmDyDtJ-Z827O85SiE3lY00l1ed/view?usp=drive_link). After downloading the trained LSTM model, you can store the model in the "trained_models" folder, or you can specify the path of the model in the function argument "step1_model_path".

The accuracy of using this two-step mothod to classify non-politician Twitter users' political orientation based on their 200 tweets is around 96.33%.

To use this Python package, you can download it from GitHub, store your dataset into the data folder, change the name of the dataset in the `config.py` file, and then run either `two_step_BERT_predict.py` or `two_step_LSTM_predict.py` in your terminal. Alternatively, you can also import two_step_BERT_predict or two_step_LSTM_predict and use their functions as follows: 

```Python
from two_step_BERT_predict import two_step_BERT_predict
user_pred = two_step_BERT_predict(step2_model_path="trained_models/step2_model_svm_200tweets_bert.sav",
                                  data_path="data/example_tweets.csv",
                                  text_variable="text",
                                  user_variable="user_id")
```

Please cite this paper:

@article{HuL,\
&nbsp;&nbsp;&nbsp;&nbsp;    author = {Lingshu Hu},\
&nbsp;&nbsp;&nbsp;&nbsp;    title = {A Two-Step Method for Classifying Political Partisanship Using Deep Learning Models},\
&nbsp;&nbsp;&nbsp;&nbsp;    journal = {Social Science Computer Review},\
&nbsp;&nbsp;&nbsp;&nbsp;    DOI = {10.1177/08944393231219685},\
&nbsp;&nbsp;&nbsp;&nbsp;    year = {2023}\
}

The training dataset can be obtained from [kaggle](https://www.kaggle.com/datasets/lingshuhu/political-partisanship-tweets).
