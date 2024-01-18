# Système de Location de Voitures
Ce projet est un système de location de voitures implémenté en utilisant Django. Les utilisateurs peuvent parcourir le catalogue de voitures, voir les détails de chaque voiture, effectuer des réservations et gérer les voitures.

## Fonctionnalités

- Page d'accueil :
  - Message de bienvenue et liens de navigation.

- Catalogue de Voitures :
  - Afficher une liste de voitures disponibles.
  - Cliquer sur une voiture pour plus de détails.

- Réservation :
  - Authentification utilisateur requise pour effectuer une réservation.
  - Entrer le nom du client, sélectionner une voiture et choisir la durée.
  - Voir et confirmer la réservation.

- Panneau d'administration :
  - Opérations CRUD pour les voitures.

## Configuration

1. **Installation :**
   - Assurez-vous d'avoir Python et pip installés.
   - Installez les dépendances avec `pip install -r requirements.txt`.

2. **Base de données :**
   - Appliquez les migrations avec `python manage.py migrate`.
   - Créez un superutilisateur pour accéder à l'interface admin avec `python manage.py createsuperuser`.

3. **Exécution :**
   - Lancez le serveur de développement avec `python manage.py runserver`.

4. **Accès à l'interface admin :**
   - Accédez à l'interface admin à [http://127.0.0.1:8000/admin/] en utilisant le superutilisateur (login: ramosa, mot de passe: 123).

## Utilisation

### Réservation :
1. Accédez au catalogue de voitures à [http://127.0.0.1:8000/car/catalog/].
2. Choisissez une voiture disponible.
3. Réservez la voiture en suivant le lien de réservation.

### Gestion des voitures :
1. Connectez-vous avec un compte administrateur.
2. Accédez à la page de gestion des voitures [http://127.0.0.1:8000/SupperAdmin/car_list].
3. Effectuez les opérations CRUD nécessaires :
   - Ajoutez une nouvelle voiture.
   - Modifiez les détails d'une voiture existante.
   - Supprimez une voiture.

## Testes

-Exécutez les tests avec :python manage.py test

## Installation

-Clonez le dépôt : git clone https://github.com/randamzz/LocatioDeVoiture

## Auteurs

-Mousaab Laahir - Saif-Eddin Bouchouikar -Randa El Maazouza 
