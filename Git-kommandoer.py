git init # Denne kommando initialiserer et nyt Git repository. Du bruger det i den mappe, hvor dit projekt er placeret.

git clone [url] # Denne kommando bruges til at kopiere et eksisterende Git repository fra en bestemt URL, som du kan finde på GitHub eller et andet sted.

git add [filnavn] eller git add . #Disse kommandoer tilføjer en fil (eller alle filer) til dit Git repository. Dette betyder ikke, at ændringerne er gemt permanent - de er bare klar til det næste trin.

git commit -m "din besked her" # Denne kommando "commit" ændringerne, du har foretaget, hvilket betyder, at de er gemt i din versionshistorik. Du skal inkludere en besked med hver commit for at beskrive, hvad du ændrede.

git push  #Denne kommando uploader dine ændringer til det remote repository (for eksempel GitHub). Andre kan nu se og bidrage til dine ændringer.

git push --set-upstream https://github.com/tyllegris/code.git master #Denne kommando uploader dine ændringer til det remote repository (for eksempel GitHub). Andre kan nu se og bidrage til dine ændringer.

git pull #Hvis du arbejder i et team, og nogen anden har lavet ændringer, bruger du denne kommando til at hente og integrere disse ændringer i dit lokale repository.