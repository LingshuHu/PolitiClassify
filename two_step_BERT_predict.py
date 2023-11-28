import pandas as pd
import config
from model_codes.BERT_predict import BERT_predict
from model_codes.SVM_with_BERT_predict import SVM_with_BERT_predict

def two_step_BERT_predict(
                     step2_model_path,
                     data_path,
                     text_variable,
                     user_variable):

    df = BERT_predict(
                      
                      data_path=data_path,
                      text_variable=text_variable,
                      user_variable=user_variable)
 
    user_pred = SVM_with_BERT_predict(df_pred = df,
                                      user_variable=user_variable,
                                      model_path=step2_model_path)
    return(user_pred)

    

if __name__ == '__main__':
    user_pred = two_step_BERT_predict(
                                 step2_model_path=config.SVM_BERT_MODEL_PATH,
                                 
                                 data_path=config.DATA_PATH,
                                 text_variable=config.TEXT_COLUMN_NAME,
                                 user_variable=config.USER_COLUMN_NAME)

    user_pred.to_csv(config.USER_PRED_DATA_PATH, index=False)

