from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

eng = create_engine("mysql+mysqldb://root:chun0225!@127.0.0.1:3306/test?charset=utf8", encoding="utf-8",  convert_unicode=False)

Session = sessionmaker(bind=eng)
ses = Session()    

'''
ses.add_all([
    UserTable(user_no=8, user_id='난희', user_pw='nanhee0225'), 
    UserTable(user_no=9, user_id='as', user_pw='juhee0318')
    ])
ses.commit()

rs = ses.query(UserTable).all()

for user in rs:
    print(user.user_no, user.user_id, user.user_pw)
'''