# API Choice

- Étudiant : Emilie
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle / README : https://agify.io/documentation/api/reference
- Auth : None

- Endpoints testés :
  - GET /?name=lucas

- Hypothèses de contrat (champs attendus, types, codes) :
  - Le endpoint doit répondre avec un code HTTP 200 en cas de requête valide.
  - La réponse doit être au format JSON.
  - Le JSON doit contenir les champs suivants :
    - name : string (prénom recherché)
    - age : integer ou null (âge estimé)
    - count : integer (nombre de personnes utilisées pour l'estimation)
  - Le paramètre "name" est obligatoire pour obtenir une estimation pertinente.
  - Une requête avec un prénom valide doit retourner une structure JSON conforme.

- Limites / rate limiting connu :
  - L'API est publique et accessible sans clé d'authentification.
  - Le nombre de requêtes doit rester raisonnable afin d'éviter une surcharge du service.
  - Aucun quota précis n'est indiqué dans la documentation publique.
  - Un système de timeout doit être utilisé côté client pour éviter de bloquer l'application.

- Risques (instabilité, downtime, CORS, etc.) :
  - L'API dépend d'un service externe : une indisponibilité du fournisseur peut provoquer des erreurs.
  - Les temps de réponse peuvent varier selon la disponibilité du service.
  - Une erreur réseau ou un problème serveur peut retourner un code HTTP différent de 200.
  - L'application Flask doit gérer les erreurs HTTP et les timeouts.
  - Le CORS n'est pas un problème car l'appel API est réalisé côté serveur avec Python (requests).
