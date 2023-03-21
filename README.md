# Veri Mühendisliği - Case Study

1. Git üzerinden dosyayı clonelayın veya .zip olarak indirin.

2. `airflow` isimli dosyanın içerisinde girin ve burada bir terminal açın.

3. `"docker-compose up airflow-init"` komutunu girerek container'ı kurun. Container için gerekli olan config dosyalarının hepsi `docker-compose.yaml` dosyası içerisindedir.

4. `"docker-compose up"` ile container ve içeriklerini ayağa kaldırın. (`localhost:8080` üzerinden Airflow ayağa kalkıyor ancak mysql ayağa kalksa da `localhost:3306` üzerinden kendi makinemde erişemedim)

## Tabloları incelemek için:

   1. Docker desktop üzerinden `"mysql-1"` üzerinde tıklayıp terminal kısmına geçin ve `"mysql -u root -p"` yazdıktan sonra gerekli olan şifreyi (`kartaca`) girin.
       
   2. `"database_queries_for_tables.txt"` dosyası içerisinde olan her bir SQL query'sini tek tek (Kod bloğu halinde) çalıştırın. Kodlar aşağıda verilmiştir.
   
   ``` sql
   -- country_currency isminde bir database oluşturuyoruz.
   CREATE DATABASE country_currency;
   
   ```
   ```sql
   -- country isminde bir table oluşturuyoruz
   CREATE TABLE country (
     code VARCHAR(2) NOT NULL PRIMARY KEY,
     name VARCHAR(255) NOT NULL
   );
   ```
   ```sql
   -- currency isminde bir table oluşturuyoruz
   CREATE TABLE currency (
     code VARCHAR(2) NOT NULL PRIMARY KEY,
     currency VARCHAR(3) NOT NULL,
     FOREIGN KEY (code) REFERENCES country (code)
   );
   ```
   ```sql
   -- data_merge isminde bir table oluşturuyoruz
   CREATE TABLE data_merge (
     code VARCHAR(2) PRIMARY KEY,
     name VARCHAR(255),
     currency VARCHAR(3)
   );
   ```

## Airflow üzerinde:

   1. Admin > Connections kısmından yeni bir connection oluşturun.

   2. Aşağıdaki inputları girin:

       - Conn Id : `mysql_default`
       - Conn Type: `MySQL`
       - Host: `mysql`
       - Schema: `airflow`
       - Login: `root`
       - Password: `kartaca` (Eğer olmazsa `root` deneyebilirsiniz.)
       - Port: `3306`

   Sonrasında Save ederek connection oluşturmuş olacaksınız.

DAG'ları, yanlarındaki butonlara tıklayarak aktifleştirdikten sonra manuel olarak triggerlayabilirsiniz.
