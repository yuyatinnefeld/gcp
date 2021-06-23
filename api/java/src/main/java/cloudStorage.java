import com.google.api.gax.paging.Page;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.storage.Bucket;
import com.google.cloud.storage.BucketInfo;
import com.google.cloud.storage.Storage;
import com.google.cloud.storage.StorageOptions;

import java.io.FileInputStream;
import java.io.InputStream;

public class cloudStorage {
    public static void main(String[] args) throws Exception {
        String PROJECT_ID = "xxxxxx-yyy"; //"YOUR_PROJECT_ID";
        String SERVICE_ACCOUNT = "conf/service_account.json"; //java/conf/service_account.json
        String BUCKET_NAME = "java-api-bucket223";
        String REGION="EUROPE-WEST3";
        String STORAGE_CLASS="STANDARD";

        InputStream input = new FileInputStream(SERVICE_ACCOUNT);

        Storage storage = StorageOptions.newBuilder()
                .setProjectId(PROJECT_ID)
                .setCredentials(GoogleCredentials.fromStream(input))
                .build()
                .getService();

        Bucket new_bucket = storage.create(BucketInfo.newBuilder(BUCKET_NAME).build());
        System.out.println("Created bucket " + new_bucket.getName());

        System.out.println("Bucket List");
        Page<Bucket> buckets = storage.list();

        for (Bucket bucket : buckets.iterateAll()) {
            System.out.println(bucket.getName());
        }
    }
}
        