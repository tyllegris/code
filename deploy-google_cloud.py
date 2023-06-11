#Installer Google Cloud SDK på din lokale maskine: Følg instruktionerne her: https://cloud.google.com/sdk/docs/install

#Log ind på din Google Cloud-konto og sæt dit projekt: 

gcloud auth login gcloud config set project <PROJECT_ID>

#Byg din Docker-container og push den til Google Container Registry (GCR):
gcloud builds submit --tag gcr.io/<PROJECT_ID>/<APP_NAME> .

#Deploy din Streamlit-app til Google Cloud Run:

gcloud run deploy <APP_NAME> --image gcr.io/<PROJECT_ID>/<APP_NAME> --platform managed --region <REGION> --allow-unauthenticated --port 8080

#Her er en kort oversigt over de anvendte kommandoer:

pip install #Installerer Python-pakker.
gcloud auth login #Logger ind på din Google Cloud-konto.
gcloud config set project #Indstiller det aktive projekt i Google Cloud SDK.
docker build -t <fil_navn> . #Bygger en et Docker billede Husk mellemrum og punktum efter filnavn
docker images  #Tjek om du har bygget et Docker billede
gcloud builds submit #Bygger og pusher Docker-containeren til GCR.
gcloud run deploy #Deployer din Streamlit-app til Google Cloud Run.