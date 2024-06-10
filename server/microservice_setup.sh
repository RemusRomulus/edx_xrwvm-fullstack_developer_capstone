echo ::Setting Working Directory::
cd /home/project/edx_xrwvm-fullstack_developer_capstone/server/djangoapp/microservices

echo ::BUILDING CONTAINER::
docker build . -t us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer

echo ::PUSHING CONTAINER::
docker push us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer

echo ::CREATING IBMCLOUD APPLICATION::
ibmcloud ce application create --name sentianalyzer --image us.icr.io/${SN_ICR_NAMESPACE}/senti_analyzer --registry-secret icr-secret --port 5000

echo ::GETTING APPLICATION LIST::
ibmcloud ce application list
