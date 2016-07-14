#!/bin/sh


for i in $(ls -1 *.htm); do ~/bin/wkhtmltopdf file:///net/nfs-authnss.b.ca.auf/home/gustavo.espinosa/sites/site_institutionnel/project/static/organigramme/fiches/$i pdf2/$i.pdf ;done
