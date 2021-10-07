import xlearn, pandas
        
# read grade data file
train_path = "./data/grade_train.csv"
test_path = "./data/grade_test.csv"
model_path = "./out/model.out"

grade_train = pandas.read_csv(train_path, header=None)
grade_train.columns = ["value", "user_no", "book_no"]

grade_test = pandas.read_csv(test_path, header=None)
grade_test.columns = ["value", "user_no", "book_no"]

# get train x, y
grade_train = pandas.get_dummies(grade_train, columns=["user_no", "book_no"])
grade_train.to_csv("./data/grade_train_s.csv", sep=",", index=False)

# get test x, y
grade_test = pandas.get_dummies(grade_test, columns=["user_no", "book_no"])
grade_test.to_csv("./data/grade_test_s.csv", sep=",", index=False)

xdm_train = xlearn.DMatrix(grade_train[grade_train.columns[1:]], grade_train["value"])
xdm_test = xlearn.DMatrix(grade_test[grade_test.columns[1:]], grade_test["value"])

# training task
fm_model = xlearn.create_fm()
fm_model.setTrain("./data/grade_train_s.csv")
fm_model.setValidate("./data/grade_test_s.csv")

# param
param = {"task": "reg", "lr": 0.2, 
        "lambda": 0.002, "metric": "mae", "epoch": 10}

# Start to train
fm_model.disableEarlyStop()
fm_model.fit(param, model_path)

# Start to predict
fm_model.setTest("./data/grade_test_s.csv")
res = fm_model.predict(model_path, "./out/predict.txt")
print(res)
