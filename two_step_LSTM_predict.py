import pandas as pd
import config
from model_codes.LSTM_predict import LSTM_predict
from model_codes.SVM_with_LSTM_predict import SVM_with_LSTM_predict

def two_step_LSTM_predict(step1_model_path,
                     step2_model_path,
                     step1_tokenizer_path,
                     data_path,
                     text_variable,
                     user_variable):

    df = LSTM_predict(model_path=step1_model_path,
                      tokenizer_path=step1_tokenizer_path,
                      data_path=data_path,
                      text_variable=text_variable,
                      user_variable=user_variable,
                      maxlen=config.SEQUENCE_LENGTH,
                      batch_size=config.BATCH_SIZE)
 
    user_pred = SVM_with_LSTM_predict(df_pred = df,
                                      user_variable=user_variable,
                                      model_path=step2_model_path)
    return(user_pred)

    

if __name__ == '__main__':
    user_pred = two_step_LSTM_predict(step1_model_path=config.LSTM_MODEL_PATH,
                                 step2_model_path=config.SVM_LSTM_MODEL_PATH,
                                 step1_tokenizer_path=config.LSTM_TOKENIZER_PATH,
                                 data_path=config.DATA_PATH,
                                 text_variable=config.TEXT_COLUMN_NAME,
                                 user_variable=config.USER_COLUMN_NAME)

    user_pred.to_csv(config.USER_PRED_DATA_PATH, index=False)

