from fastapi import Depends
from sqlalchemy.orm import Session
from datetime import datetime
import xlearn 

from db.session import get_db

class fm_model():
    def __init__(self):
        self.model = xlearn.create_fm()

    def pre(sele, user_no: int, book_no: list):
        pass


def xl_data(db: Session=Depends(get_db)):
    # SHOW VARIABLES LIKE "secure_file_priv"; 명령어로 확인한 경로 아래에 파일을 저장
    timestr = datetime.now().strftime("%Y%m%d_%H%M%S")
    data_path = f"'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/xl_data_{timestr}.csv'"
    query = f"SELECT user_no, book_no, grade FROM grade INTO OUTFILE {data_path} fields terminated by ',';"
    data = db.execute(query)
    print(data)

    br_model = xlearn.create_fm()
    br_model.setTrain(data_path) # training data
    # br_model.disableNorm() # 최적화

    # param = {"task": "reg", "lr": 0.0002, "lambda": 0.00001, "metrics": "rmse", "epoch": 100}

    # br_model.fit(param, "./model.out")