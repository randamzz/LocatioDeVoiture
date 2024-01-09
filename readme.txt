# Location de Voiture
HAD SHI KHSO ITBDL BUT HADA GHI EX
Ce projet Django permet à un utilisateur de consulter un catalogue de voitures, de choisir une voiture disponible, et de la réserver pour une période spécifique.

## Fonctionnalités

- Catalogue de voitures avec des détails tels que le modèle et l'année.
- Possibilité de réserver une voiture disponible.

## Configurationpi

1. **Installation :**
   - Assurez-vous d'avoir Python et pip installés.
   - Installez les dépendances avec `pip install -r requirements.txt`.

2. **Base de données :**
   - Appliquez les migrations avec `python manage.py migrate`.
   - Créez un superutilisateur pour accéder à l'interface admin avec `python manage.py createsuperuser`.

3. **Exécution :**
   - Lancez le serveur de développement avec `python manage.py runserver`.

4. **Accès à l'interface admin :**
   - Accédez à l'interface admin à [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) en utilisant le superutilisateur créé.

## Utilisation

1. Accédez au catalogue de voitures à [http://127.0.0.1:8000/location/catalogue/](http://127.0.0.1:8000/location/catalogue/).
2. Choisissez une voiture disponible.
3. Réservez la voiture en suivant le lien de réservation.

## Contribution

1. Forkez le projet.
2. Créez une branche pour vos modifications : `git checkout -b feature/nouvelle-fonctionnalite`.
3. Committez vos modifications : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`.
4. Poussez votre branche : `git push origin feature/nouvelle-fonctionnalite`.
5. Créez une pull request.

## Licence

Ce projet est sous licence [Nom de la licence]. Voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## Auteurs

-Mousaab Laahir - Saif-Eddin Bouchouikar -Randa El Maazouza 
