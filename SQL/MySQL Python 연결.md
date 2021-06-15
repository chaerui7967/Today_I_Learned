# MySQL Python 연결



## 라이브러리 설치

```python
import pandas as pd
import pymysql.cursors
```

 pymysql 라이브러리에서 cursors함수를 이용하여 MySQL와 연결한다



## sql 접근

```python 
connection = pymysql.connect(host='127.0.0.1', # == localhost
        user='root', # 유저이름 생성했으면 유저이름
        password='----',
        db='테이블 이름',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor) # -- dictionary 형태로 받아옴
```

 접근하고 싶은 db 내용을 작성한 후 연결한다.



> **cursor?**
>
> ![image-20210615173054225](C:\Users\j\AppData\Roaming\Typora\typora-user-images\image-20210615173054225.png)
>
> MySQL 내부 테이블에서 다음과 같은 화살표를 cursor라고 한다



```python
try:
    with connection.cursor() as cursor:
        
#         sql = "select count(total_bill) from tips where tip >= 7;" # 메모리 사용 제한을 위해 먼저 카운트값을 가져온다
        sql = "select total_bill from tips where tip >= 7;" # 변수에 문자열로 sql문을 작성
        cursor.execute(sql)  # 해당 sql 적용
        result = cursor.fetchone()  # fetchone() 함수는 해당 커서 하나를 가져옴
        print(result)
        # fetchone() 을 통해서 여러개 열을 가져오는 방법
#         for _ in range(3):
#             result = cursor.fetchone()
#             print(result)
finally:
    connection.close()  # 연결을 끊음, 메모리 절약을 위해서 db 연결을 끊는게 좋음
```



### 한번에 가져오는 방법

```python
import pandas as pd

# MySQL DB에서 데이터 받아와서 DataFrame에 저장

conn = pymysql.connect(host='localhost', user='이름', 
                       password='----', db='테이블 이름', charset='utf8',
                       autocommit=True, cursorclass=pymysql.cursors.DictCursor)
try:

   with conn.cursor() as curs:
      sql = "select total_bill from tips where tip >= 7;"
      curs.execute(sql)
      rs = curs.fetchall()  # fetchall을 통해서 모든 열을 가져옴

      # DB에서 받아온 값을 DataFrame에 넣음

      df = pd.DataFrame(rs)
      print(df)
    # df.to_csv('파일명.csv')
finally:

   conn.close()
```



### 기타

```python
df.isnull().count() # null 개수 확인
df['total_bill'].hist() # 해당 컬럼의 히스토그램 확인
```

