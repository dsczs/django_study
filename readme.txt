1.创建项目
django-admin startproject project

2.启动项目
python manage.py runserver

3.创建应用
python manage.py startapp app

4.生成预SQL语句
python manage.py makemigrations app

5.执行预SQL语句
python manage.py sqlmigrate app 0001
python manage.py migrate

6.python django shell
python manage.py shell