#Java GCP API

## Setup

### 1. create GCP project and activate cloud storage & cloud storage API

### 2. create GCP service account (From the Role list, select Project > Owner.)

### 3. download the service account json key and move to conf repository

```bash
mkdir java/conf
mv YOUR_SERVICE_JSON_KEY.json java/conf/service_account.json
```

### 4. provide authentication credentials to your application code by setting the environment variable
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/.../java/conf/service_account.json
```
### 5. create maven project

### 6. pom.xml update

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>20.6.0</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>

<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>

```
### 6. create test class
touch java/cloudStorage.java

### 7. update cloudStorage.java

```java
import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.storage.Bucket;
import com.google.cloud.storage.BucketInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;

import java.io.FileInputStream;
import java.io.InputStream;

public class cloudStorage {
    public static void main(String[] args) throws Exception {
        String PROJECT_ID = "YOUR_PROJECT_ID";
        String SERVICE_ACCOUNT = "conf/service_account.json"; // mkdir java/conf/

        InputStream input = new FileInputStream(SERVICE_ACCOUNT);


        Storage storage = StorageOptions.newBuilder()
                .setProjectId(PROJECT_ID)
                .setCredentials(GoogleCredentials.fromStream(input))
                .build()
                .getService();


        String BUCKET_NAME = "java-api-bucket";
        Bucket bucket = storage.create(BucketInfo.newBuilder(BUCKET_NAME).build());
        System.out.println("Created bucket " + bucket.getName());
    }
}
```
### 8. test run in the IDE and terminal

```bash
java -cp target/java-1.0.jar cloudStorage
```

### 9. read Java API examples

> https://github.com/googleapis/google-cloud-java/tree/master/google-cloud-examples/src/main/java/com/google/cloud/examples/storage/buckets
