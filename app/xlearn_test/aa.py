import xlearn, pandas

user_no = 1
books = [2, 5, 7]

grade_test = pandas.DataFrame({"value": [0 for _ in range(len(books))], "user_no": [user_no for _ in range(len(books))], "book_no": books})
grade_test = pandas.get_dummies(data=grade_test, columns=["user_no", "book_no"], prefix=["user_no", "book_no"])
print(grade_test)

# get test x, y
test_x = grade_test[grade_test.columns[1:]]
test_y = grade_test[grade_test.columns[0]]

xdm_test = xlearn.DMatrix(test_x, test_y)

model_path = "./out/model.out"
fm_model = xlearn.create_fm()

fm_model.setTest(xdm_test)
result = fm_model.predict(model_path)
print(result)