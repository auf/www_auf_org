# -*- encoding: utf-8 -*-

from django import forms
from django.core import validators
from project.espace_membre import models


def add_style_to_required_fields(form):
    for key in form.fields:
        if form.fields[key].required:
            if form.fields[key].label and not form.fields[key].label.endswith(" *"):
                form.fields[key].label += " *"
                form.fields[key].widget.attrs.update(
                    {'class': 'required_field'})


class EtablissementForm(forms.ModelForm):
    courriel = forms.EmailField()

    def clean(self):
        ret = super(EtablissementForm, self).clean()

        if (len(ret.get("historique")) + len(ret.get("description"))) > 800:
            raise forms.ValidationError("""
Le nombre total de caractère des textes historique et description combinés doit
être inférieur à 800.""")

        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': 'erroneous_field'})
        return ret

    class Meta:
        model = models.Etablissement
        exclude = ('membre', 'membre_adhesion_date', 'implantation',
                   'statut', 'region', 'fonction', 'actif', 'date_modification',
                   'ref', 'responsable_genre', 'responsable_nom', 'responsable_fonction',
                   'responsable_prenom', 'id', 'qualite', 'validation_sai', 'validation_com',
                   'validation_etablissement', 'date_validation_sai', 'a_valider_com', 'a_valider_sai',
                   'date_validation_etablissement', 'date_validation_com', )

    def __init__(self, *args, **kwargs):
        super(EtablissementForm, self).__init__(*args, **kwargs)

        if self.instance.qualite == u"ESR":
            self.fields['nom'].label = u"Intitulé de l'établissement"
            self.fields['nombre'].label = u"Nombre d'étudiants"
            self.fields['historique'].label = u"Historique de l'établissement"
        elif self.instance.qualite == u"CIR":
            self.fields['nom'].label = u"Intitulé du centre de recherche"
            self.fields['nombre'].label = u"Nombre de chercheurs"
            self.fields[
                'historique'].label = u"Historique du centre de recherche"
        elif self.instance.qualite == u"RES":
            self.fields['nom'].label = u"Intitulé du réseau"
            self.fields['nombre'].label = u"Nombre de membres"
            self.fields['historique'].label = u"Historique du réseau"

        self.fields['nom'].required = True
        self.fields['pays'].required = True
        self.fields['adresse'].required = True
        self.fields['ville'].required = True
        self.fields['telephone'].required = True
        self.fields['fax'].required = True
        self.fields['courriel'].required = True
        self.fields['nombre'].required = True
        self.fields['historique'].required = True
        self.fields['description'].required = True

        self.fields['fax'].label = u"Télécopie"
        self.fields['url'].label = u"Site Internet"
        self.fields['courriel'].label = u"Courriel général"

        add_style_to_required_fields(self)


class ResponsableForm(forms.ModelForm):
    courriel = forms.EmailField(required=True, label=u"Courriel")

    class Meta:
        model = models.ResponsableModification
        exclude = ('etablissement', 'responsable', 'type',
                   'modification_par', 'modification_date', 'genre')

    def __init__(self, *args, **kwargs):
        super(ResponsableForm, self).__init__(*args, **kwargs)
        self.fields["nom"].required = True
        self.fields["prenom"].required = True
        self.fields["fonction"].required = True
        add_style_to_required_fields(self)

    def clean(self):
        ret = super(ResponsableForm, self).clean()
        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': 'erroneous_field'})
        return ret


class ResponsableAutreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResponsableAutreForm, self).__init__(*args, **kwargs)
        self.fields["courriel"].required = True
        self.fields["nom"].required = False
        self.fields["prenom"].required = False
        self.fields['courriel'].label = u"Courriel du service"
        add_style_to_required_fields(self)

    def clean(self):
        ret = super(ResponsableAutreForm, self).clean()
        for f in self.errors:
            self.fields[f].widget.attrs.update({'class': 'erroneous_field'})
        return ret

    class Meta:
        model = models.ResponsableModification
        exclude = ('etablissement', 'responsable', 'type', 'genre',
                   'modification_par', 'modification_date')


class RequiredFormSet(forms.models.BaseModelFormSet):

    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        try:
            self.forms[0].empty_permitted = False
        except IndexError:
            pass
