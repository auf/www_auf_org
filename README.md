# Mise en place d'un environnement de développement

Créer un environnement virtuel:

    virtualenv env
    . env/bin/activate

Installer les dépendances:

    pip install MySQL-python
    pip install Pillow
    pip install lxml==2.2.8

Télécharger le [SDK](http://test-www.auf.org/static/auf-django-sdk.tar.gz) et
le décompresser dans le répertoire parent du projet.

Modifier la configuration dans `project/settings/10-local.py`.

Créer la base de données:

    mysqladmin create <nom de la BD>
    python manage.py syncdb
