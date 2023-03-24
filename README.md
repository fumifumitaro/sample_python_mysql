PythonでMySQLを操作することを目的としたサンプルプログラムです。

Dockerをインストールして利用してください。

本ディレクトリで実行してください。
```shell
ls
```
を実行したときに、実行結果が以下の場所です。
```shell
README.md  docker  docker-compose.yml  src
```


以下でコンテナを立ち上げます。
```shell
docker-compose up -d
```
そのあと、コンテナ内に入るため下記を実行、
```shell
docker-compose run app bash
```
でPythonコマンドの実行が可能となります。
上記状態で立ち上げたMySQLへの接続もできます。

```shell
python main_table.py

python main.py 1
```

を実行して下記がでたら環境が問題なく環境ができています。
`子猫ちゃんは朝食にサンプルを食べました。`

MySQL接続情報
```
Host: localhost
Port: 3306
User: user
Password: password
Database: db
```
