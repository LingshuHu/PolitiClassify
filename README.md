# PolitiClassify
A python package for classifying Twitter users' political orientation with two-step deep learning models.

Two models can be chosen for the first step of the method: LSTM and BERT. The trained BERT model will be automatically downloaded.The LSTM model need to be downlaoded from [here](https://drive.google.com/file/d/1uqw9rjmDyDtJ-Z827O85SiE3lY00l1ed/view?usp=drive_link). After downloading the trained LSTM model, you can store the model in the "trained_models" folder, or you can specify the path of the model in the function argument "step1_model_path".

The accuracy of using this two-step mothod to classify non-politician Twitter users' political orientation based on their 200 tweets is around 96.33%.

Please cite this paper:
@article{HuL,
    author = {Lingshu Hu},
    title = {A Two-Step Method for Classifying Political Partisanship Using Deep Learning Models},
    journal = {Social Science Computer Review},
    year = {2023},
}
