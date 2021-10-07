import xlearn, pandas, os

os.system("cls")

def convert(df_train, df_test, column_name: str):
        column_max = max(max(df_train[column_name]), max(df_test[column_name]))
        # col_list = 
        df_train[column_name] = pandas.DataFrame(map(int, str(bin(value))[2:].zfill(column_max)) for value in df_train[column_name])
        df_test[column_name] = pandas.DataFrame(map(int, str(bin(value))[2:].zfill(column_max)) for value in df_test[column_name])

# read grade data file
train_path = "./data/grade_train.csv"
test_path = "./data/grade_test.csv"

grade_train = pandas.read_csv(train_path, header=None)
grade_train.columns = ["value", "user_no", "book_no"]

grade_test = pandas.read_csv(test_path, header=None)
grade_test.columns = ["value", "user_no", "book_no"]

# convert
convert(grade_train, grade_test, "user_no")
convert(grade_train, grade_test, "book_no")

print(type(grade_train), grade_train)
print(grade_train["user_no", "book_no"])

xdm_train = xlearn.DMatrix(grade_train[grade_train.columns["user"]], grade_train["value"])
xdm_test = xlearn.DMatrix(grade_test[grade_test.columns[1:]], grade_test["value"])

# training task
fm_model = xlearn.create_fm()
fm_model.setTrain(xdm_train)
fm_model.setValidate(xdm_test)

# param
param = {"task": "reg", "lr": 0.2, 
        "lambda": 0.002, "metric": "mae", "epoch": 10}

# Start to train
model_path = "./out/model.out"

fm_model.disableEarlyStop()

# Start to predict
predict_path = "./out/predict.txt"

fm_model.setTest("./data/grade_test_s.csv")
res = fm_model.predict(model_path, xdm_test)
print(res)
