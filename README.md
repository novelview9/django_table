## drawing table with user join info ( created_at -> in an hour)

### ========sample image========
![sample_image](https://github.com/novelview9/django_table/blob/master/sample/sample.png)
 working in python 3 +   
 
1. pip install -r requirement.txt
2. python manage.py makemigrations home
3. python mange.py migrate
4. seed.sql raw sql 에 datetime 형식이 iso 8601의 월/시간 구분에 T 를 사용하고, 타임존 형식이 no-ip 으로 Z 로 주어졌습니다.  
  * 장고에서 해당 포맷을 원활히 지원하지 않고 또 장고 filter 기능작동의 문제로 내부 별도의 작업을 필요로 합니다.
  * 이를 해결하기  위해 pre_change_raw_sql.py 으로, sql 문을 전처리해서 sqlite에 기록, 장고에서 이용 했습니다.
  * python pre_change_raw_sql.py seeds.sql result.sql
  * sqlite3 db.sqlite3 < ./result.sql  

4. 테이블의 간단한 외형 구현을 위해 CDN [pure-css](http://yui.yahooapis.com/pure/0.6.0/pure-min.css)을 이용했습니다.
