# SQL

## define ENV variables
```bash
REGION="xxxxx"
ZONE="xxxxx"
PROJECT_ID="xxxxx"
PASSWORD="xxxxx"
CPU_NUM=y #1,2,3
MEMORY_SIZE="xxxxx" #7680MB
DB_VERSION="xxxxx" #MYSQL_8_0 / POSTGRES_12
INSTANCE_NAME="xxxxx"
DB_NAME="xxxxx"
BUCKET_NAME="xxxxx"
FILE_NAME_1="xxxxx"
TABLE_NAME="xxxxx"
```

## create a postgres db
```bash
gcloud sql instances create ${INSTANCE_NAME}  \
--database-version=${DB_VERSION} --cpu=${CPU_NUM} --memory=${MEMORY_SIZE}  \
--zone=${ZONE} --root-password=${PASSWORD}
```

## check the db
```bash
gcloud sql databases list
```

## check the SQL setup
```bash
gcloud sql instances describe ${INSTANCE_NAME} 
```

## open GCP Console, click the Cloud Shell icon
```bash
gcloud sql connect ${INSTANCE_NAME} --user=root
```
## password setup

## create a db
```roomsql
CREATE DATABASE shop_db;
```
## create a shop table & insert data into the table

```roomsql
USE shop_db;
CREATE TABLE mst_shops (shop_cd INTEGER, shop_name VARCHAR(255),
entryID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(entryID));
```
```roomsql
INSERT INTO mst_shops (shop_cd, shop_name) values (779, "Jimmys");
INSERT INTO mst_shops (shop_cd, shop_name) values (941, "ナカハラストアー");
INSERT INTO mst_shops (shop_cd, shop_name) values (2640, "丸大");
INSERT INTO mst_shops (shop_cd, shop_name) values (5394, "Aコープ");
INSERT INTO mst_shops (shop_cd, shop_name) values (6427, "サンエー");
INSERT INTO mst_shops (shop_cd, shop_name) values (6532, "ユニオン");
INSERT INTO mst_shops (shop_cd, shop_name) values (7746, "りうぼう");
```
```roomsql
SELECT * FROM mst_shops;
```
## create a product table & insert data into the table
```roomsql
USE shop_db;
CREATE TABLE mst_products (jancd BIGINT, name_prod VARCHAR(255), name_bender VARCHAR(255), category VARCHAR(255), price DOUBLE);
```

```roomsql
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4514062284934, "ＵＨＡピピン　ｅ－ｍａのど飴鬼滅の刃　袋　４０ｇ", "ユーハピピン", "キャンディ・キャラメル", 150.64);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660503620, "バンダイ　鬼滅の刃ディフォルメシールウエハース１枚", "バンダイ", "玩具菓子", 98.67);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660503637, "バンダイ　鬼滅の刃ウエハース２　１枚", "バンダイ", "玩具菓子", 116.92);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660504306, "バンダイ　鬼滅の刃ＣＡＮＤＹ缶２　１９ｇ", "バンダイ", "キャンディ・キャラメル", 381.33);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660504757, "バンダイ　鬼滅の刃名場面チョコスナック　２０ｇ", "バンダイ", "玩具菓子", 177.23);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660504764, "バンダイ　鬼滅の刃禰豆子のチョコバー　１個", "バンダイ", "玩具菓子", 158.46);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4549660504771, "バンダイ　鬼滅の刃全員集中アクリルチャーム　１個", "バンダイ", "玩具菓子", 477.98);
INSERT INTO mst_products (jancd, name_prod, name_bender, category, price) values (4580036210100, "フォルテ　鬼滅の刃コレクターズＣ　１枚", "フォルテ", "玩具菓子", 116.83);
```

```roomsql
SELECT * FROM mst_products;
```

## setup iam & role
```bash
cd iam 
bash iam_setup_sa.sh
```



## importing cloud storage data into cloud SQL table
0) create DB and table
```roomsql
CREATE DATABASE mydb123;
```

```roomsql
USE mydb123;
CREATE TABLE ratings (userId INTEGER, movieId INTEGER, rating DOUBLE, timestamp VARCHAR(255));
```
1) Go to your Cloud SQL Instance and copy service account of instance (Cloud SQL->{instance name}->OVERVIEW->Service account)
   xxxxxxxxx@gcp-sa-cloud-sql.iam.gserviceaccount.com

2) Go the Cloud Storage Bucket > permission > add member > add the copied service account

3) run SDK cmd
```bash
gcloud sql import csv ${INSTANCE_NAME} \
gs://${BUCKET_NAME}/${FILE_NAME} \
--database=${DB_NAME} \
--table=${TABLE_NAME}                             
```
4) check data in GCP Console shell
```bash
SELECT * FROM ratings;                         
```