# Compute Engine + VS Code

1. connect with your GCP project
```bash
gcloud config set project ${PROJECT}
```
2. create a GCP vm instance
```bash
gcloud compute instances create myinstance --zone=europe-west3-b


NAME        ZONE            MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
myinstance  europe-west3-b  n1-standard-1               10.156.0.2   34.141.87.167  RUNNING
```

3. create a ssh-key for the vm instance
```bash
gcloud compute config-ssh
```
4. go to the instance 
```bash
ssh myinstance.europe-west1-b.yuyatinnefeld-testing
touch a b c
exit
```

5. open SSH Configuration file (VS Code)
```bash
Host gcp-gce
    HostName <GCP External IP>
    IdentityFile ~/.ssh/google_compute_engine
    UserKnownHostsFile= ~/.ssh/google_compute_known_hosts
    HostKeyAlias=compute.123456789123456798
    IdentitiesOnly=yes
    CheckHostIP=no
    User <local-pc-user>

Host gcp-gce
    HostName 34.141.87.167
    IdentityFile /home/ytubuntu/.ssh/google_compute_engine
    UserKnownHostsFile=/home/ytubuntu/.ssh/google_compute_known_hosts
    HostKeyAlias=compute.4583265746303638803
    IdentitiesOnly=yes
    CheckHostIP=no
```
6. connect current window to host (VS Code) 