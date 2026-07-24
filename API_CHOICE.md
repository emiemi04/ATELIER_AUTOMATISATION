# API Choice

- Étudiant : Emilie
- API choisie : NVD (National Vulnerability Database)
- URL base : https://services.nvd.nist.gov/rest/json/cves/2.0
- Documentation officielle / README :
  https://nvd.nist.gov/developers/start-here

- Auth :
  None (API Key recommandée pour augmenter les limites)

- Endpoints testés :
  - GET /cves/2.0?keywordSearch=flask

- Hypothèses de contrat (champs attendus, types, codes) :
  - HTTP 200 attendu pour une requête valide.
  - Réponse au format JSON.
  - Présence du champ vulnerabilities (liste).
  - Chaque vulnérabilité contient un objet cve.
  - Chaque CVE possède :
    - id : string
    - descriptions : liste
    - metrics : informations de sévérité

- Limites / rate limiting connu :
  - Sans clé API : environ 5 requêtes toutes les 30 secondes.
  - Avec clé API : limites augmentées.
  - Un délai entre les requêtes est nécessaire.

- Risques :
  - Volume important de données JSON.
  - Modification possible du schéma dans le futur.
  - Indisponibilité temporaire du service NVD.
  - Nécessité de gérer les erreurs HTTP 403, 429 et 5xx.
