#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload():
    url = "http://44.201.162.159:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    file_path = "/var/lib/jenkins/workspace/NewPipeline/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
    username = 'admin'
    password = 'Hasmi@jfrog7'

    with open(file_path,'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT reuquest failed with status code(response.status_code)")
        print("Response content:")
        print(response.text)

def mvnBuild():
   maven_command = "mvn clean install -DskipTests"

try:
    print("\nMaven build completed succesfully.")
except subprocess.CalledProcessError as e:
       print(f"Error: Maven build failed with exit code (e.returncode)")

def main():
    mvnBuild()
    jfrogUpload()

if __name__=="__main__":
    main()
