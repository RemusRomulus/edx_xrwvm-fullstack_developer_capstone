# Overview
The steps used to deploy  the application on containers and in kubernetes

## Clean-up Old Environments
* Perform these commands in a lab terminal
    * `kubectl get deployments`
    * `kubectl delete deployment dealership`
    * `ibmcloud cr images`
    * `ibmcloud cr image-rm us.icr.io/${SN_ICR_NAMESPACE}/dealership:latest`
* Sign out of SN Labs
* Clear browser cache

## Setup
* clone repo
* Start the **Database** application
    * See `BUILD.md > Running Database Service` for steps
* Start the **Sentiment Analyzer** in *Code Engine*
    * See `BUILD.md > Sentiment Analyzer Service` for steps
* Build the **REACT Frontend** 
    * See `BUILD.md > Buildingn Frontend` for steps