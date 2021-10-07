import xlearn, pandas

# read grade data file
train_path = "./data/grade_train.csv"
test_path = "./data/grade_test.csv"
model_path = "./out/model.out"

grade_train = pandas.read_csv(train_path, header=None)
grade_train.columns = ["value", "user_no", "book_no"]

grade_test = pandas.read_csv(test_path, header=None)
grade_test.columns = ["value", "user_no", "book_no"]
print("grade_test type - ", type(grade_test))

# One-hot Encoding
grade_train = pandas.get_dummies(data=grade_train, columns=["user_no", "book_no"], prefix=["user_no", "book_no"])
grade_test = pandas.get_dummies(data=grade_test, columns=["user_no", "book_no"], prefix=["user_no", "book_no"])

# get train x, y
train_x = grade_train[grade_train.columns[1:]]
train_y = grade_train[grade_train.columns[0]]

# get test x, y
test_x = grade_test[grade_test.columns[1:]]
test_y = grade_test[grade_test.columns[0]]
print("test_x - ", test_x)
print("test_y - ", type(test_y), test_y)

xdm_train = xlearn.DMatrix(train_x, train_y)
xdm_test = xlearn.DMatrix(test_x, test_y)

# training task
fm_model = xlearn.create_fm()
fm_model.setTrain(xdm_train)
fm_model.setValidate(xdm_test)

# param
param = {"task": "reg", "lr": 0.2, 
        "lambda": 0.002, "metric": "mae", "epoch": 10}

# Start to train
fm_model.disableEarlyStop()
fm_model.fit(param, model_path)

# Start to predict
fm_model.setTest(xdm_test)
result = fm_model.predict(model_path)
print(result)

print(xdm_test)
print(type(xdm_test))