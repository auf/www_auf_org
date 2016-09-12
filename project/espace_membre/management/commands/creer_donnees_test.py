# -*- encoding: utf-8 -*-
from django.core.management import BaseCommand
from django.db import connection
from project.espace_membre.models import Responsable, Etablissement, \
    RESPONSABLE_ETABLISSEMENT, RESPONSABLE_COMMUNICATION, \
    RESPONSABLE_RELATIONS_INTERNATIONALES


class Command(BaseCommand):

    def handle(self, *args, **options):
        c = connection.cursor()
        c.execute("DELETE FROM espace_membre_courriellog")
        c.execute("DELETE FROM espace_membre_acces")
        c.execute("""DELETE FROM
        `site_inst`.`espace_membre_responsablemodification`""")
        c.execute("""DELETE FROM `site_inst`.`espace_membre_responsable`
        """)
        c.execute("""DELETE FROM
        `site_inst`.`espace_membre_etablissementmodification`""")
        c.execute("""DELETE FROM `site_inst`.`espace_membre_etablissement`
        """)
        c.execute("""
        INSERT INTO `site_inst`.`espace_membre_etablissement`
            (`actif`, `nom`, `sigle`, `pays`, `region`,
            `implantation`, `description`, `historique`,
            `membre`, `membre_adhesion_date`, `statut`,
            `qualite`, `responsable_genre`, `responsable_nom`,
            `responsable_prenom`, `responsable_fonction`,
            `adresse`, `code_postal`, `cedex`,
            `ville`, `province`, `telephone`,
            `fax`, `url`, `date_modification`,
            `commentaire`, `ref_id`,
            `courriel`, `chiffres_cles`, `publication_papier`,
            `publication_electronique`, `nombre_etudiants`, `nombre_chercheurs`,
            `nombre_enseignants`, `nombre_membres`, `responsable_courriel`
            )
            SELECT
            `actif`, `nom`, `sigle`, `pays`, `region`, `implantation`,
            `description`, `historique`, `membre`, `membre_adhesion_date`,
            `statut`, `qualite`, `responsable_genre`, `responsable_nom`,
            `responsable_prenom`, `responsable_fonction`, `adresse`,
            `code_postal`, `cedex`, `ville`, `province`, `telephone`,
            `fax`, `url`, `date_modification`, `commentaire`, `id`,
            CONCAT('courriel@etab', `id`, '.com'), 'blablachiffres',
            0, 0, 12, 33, 142, 253, `responsable_courriel`
            from datamaster.ref_etablissement
        """)
        etablissements = Etablissement.objects.filter(actif=True, membre=True)
        e = etablissements[0]
        Responsable.objects.create(
            etablissement=e, genre='M', nom='RespPlusHaut{}'.format(e.id),
            prenom='Arianne', type=RESPONSABLE_ETABLISSEMENT,
            fonction='Cheuf', courriel="arianne@ok.com")
        Responsable.objects.create(
            etablissement=e, genre='M', nom='RespComm{}'.format(e.id),
            prenom='Blandine', type=RESPONSABLE_COMMUNICATION,
            fonction='Communique', courriel="blandine@jou.cd")
        Responsable.objects.create(
            etablissement=e, genre='M', nom='RespInt{}'.format(e.id),
            prenom='Louise', type=RESPONSABLE_RELATIONS_INTERNATIONALES,
            fonction='Internationalise', courriel="louise@poil.de")
        e = etablissements[1]
        Responsable.objects.create(
            etablissement=e, genre='M', nom='RespComm{}'.format(e.id),
            prenom='Pauline', type=RESPONSABLE_COMMUNICATION,
            fonction='Communique', courriel="pauline@boui.com")
        Responsable.objects.create(
            etablissement=e, genre='M', nom='RespInt{}'.format(e.id),
            prenom='Domi', type=RESPONSABLE_RELATIONS_INTERNATIONALES,
            fonction='Internationalise', courriel="domi@ppp.com")
        e = etablissements[2]
        Responsable.objects.create(
            etablissement=e, genre='M', nom='SeulRespInt{}'.format(e.id),
            prenom='Béatrice', type=RESPONSABLE_RELATIONS_INTERNATIONALES,
            fonction='Internationalise', courriel="beatrice@free.fr")
        e = etablissements[3]
        Responsable.objects.create(
            etablissement=e, genre='M', nom='SeulRespPlusHaut{}'.format(e.id),
            prenom='Chantal', type=RESPONSABLE_ETABLISSEMENT,
            fonction='Cheuf', courriel="chantal@kim.cn")
