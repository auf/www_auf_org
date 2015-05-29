/*
Sources des données:
* http://openlayers.org/en/master/examples/data/geojson/countries.geojson
* http://techslides.com/demos/country-capitals.json
 */

var Carte = (function() {
    "use strict";
    var PAYS_SANS_DONNEES = 'SANS_DONNEES';

    var SQUARE_STYLE = new ol.style.RegularShape({
        fill: new ol.style.Fill({color: 'gray'}),
        stroke: new ol.style.Stroke({color: 'white', width: 1}),
        points: 4,
        radius: 6,
        angle: Math.PI / 4
    });

    var lieux_implantations_styles = {};

    function get_lieu_implantation_style(nom, lat, lon) {
        var key = lat.toString() + ';' + lon.toString();
        var style;
        if (!(key in lieux_implantations_styles)) {
            style = new ol.style.Style({
                image: SQUARE_STYLE,
                text: new ol.style.Text({
                        font: '12px Calibri,sans-serif',
                        fill: new ol.style.Fill({
                            color: 'black'
                        }),
                        stroke: new ol.style.Stroke({
                            color: 'white',
                            width: 1
                        }),
                        text: nom,
                        offsetX: 10,
                        textAlign: 'left'
                    }
                )
            });
            lieux_implantations_styles[key] = style;
        } else {
            style = lieux_implantations_styles[key];
        }
        return style;
    }


    function make_marker_icon_style(icon_url, rotation) {
        if (rotation === undefined) rotation = 0;
        return new ol.style.Style({
            image: new ol.style.Icon(({
                anchor: [0.5, 50],
                anchorXUnits: 'fraction',
                anchorYUnits: 'pixels',
                opacity: 1,
                scale: 0.5,
                src: icon_url,
                rotation: rotation
            }))
        });
    }

    function make_styles_pays(couleurs_bureaux) {
        var styles= {};
        $.each(couleurs_bureaux, function (code_bureau, couleur) {
            styles[code_bureau] = new ol.style.Style({
                fill: new ol.style.Fill({color: couleur}),
                stroke: new ol.style.Stroke({color: 'black', width: 1}),
                text: new ol.style.Text({
                    font: '12px Calibri,sans-serif',
                    fill: new ol.style.Fill({
                        color: '#000'
                    }),
                    stroke: new ol.style.Stroke({
                        color: 'white',
                        width: 1
                    })
                })
            });
        });
        styles[PAYS_SANS_DONNEES] = new ol.style.Style({
            fill: new ol.style.Fill({color: 'gray'}),
            stroke: new ol.style.Stroke({color: 'gray', width: 1})
        });
        return styles;
    }

    function point_from_lon_lat(lon, lat) {
        var coords = ol.proj.fromLonLat([lon, lat]);
        return new ol.geom.Point(coords);
    }

    function get_pays_par_bureau(donnees_pays) {
        var par_bureau = {};
        $.each(donnees_pays, function(code_pays, pays) {
            var liste_pays_bureau;
            var code_bureau = pays.bureau;
            if (!(code_bureau in par_bureau)) {
                liste_pays_bureau = [];
                par_bureau[code_bureau] = liste_pays_bureau;
            } else {
                liste_pays_bureau = par_bureau[code_bureau];
            }
            liste_pays_bureau.push(pays)
        });
        return par_bureau;
    }

    function get_pays_par_type(donnees_pays) {
        var pays_implantations = {};
        var pays_etablissements = {};
        $.each(donnees_pays, function(code_pays, pays) {
            if (pays.implantations.length > 0) {
                pays_implantations[code_pays] = pays;
            }
            if (pays.nb_etablissements > 0) {
                pays_etablissements[code_pays] = pays;
            }
        });
        return {'pays_etablissements': pays_etablissements,
                'pays_implantations': pays_implantations}
    }

    function make_marker_pays_feature(country_code, code_bureau, capitale_lon_lat) {
        var point = point_from_lon_lat(capitale_lon_lat.lon, capitale_lon_lat.lat);
        return new ol.Feature({
            geometry: point,
            name: country_code,
            code_pays: country_code,
            code_bureau: code_bureau
        });
    }

    function make_marker_pays_features(capitales, donnees_pays) {
        var marker_features = [];
        $.each(donnees_pays, function (code_pays, pays) {
            var capitale_lon_lat = capitales[code_pays];
            if (pays.presence_auf) {
                marker_features.push(make_marker_pays_feature(
                    code_pays, pays.bureau, capitale_lon_lat))
            }
        });
        return marker_features;
    }

    function marker_pays_etablissement_style(
        pays_implantations, filtre_code_bureau, etablissement_marker_style,
        etablissement_marker_style_skewed, feature, resolution) {
        var code_pays = feature.get('code_pays');
        var code_bureau = feature.get('code_bureau');
        if (filtre_code_bureau === 'tous' || filtre_code_bureau === code_bureau) {
            if (code_pays in pays_implantations) {
                return [etablissement_marker_style_skewed];
            } else {
                return [etablissement_marker_style];
            }
        } else {
            return [];
        }
    }

    function marker_pays_implantation_style(
        filtre_code_bureau, implantation_marker_style, feature, resolution) {
        var code_bureau = feature.get('code_bureau');
        if (filtre_code_bureau === 'tous' || filtre_code_bureau === code_bureau) {
            return [implantation_marker_style];
        } else {
            return [];
        }
    }

    function make_lieu_implantation_feature(lieu) {
        return new ol.Feature({
            geometry: point_from_lon_lat(lieu.lon, lieu.lat),
            lieu: lieu
        });
    }

    function make_lieux_implantations_features(lieux_implantations) {
        var features = [];
        $.each(lieux_implantations, function(i, lieu) {
            features.push(make_lieu_implantation_feature(lieu)) });
        return features;
    }

    function make_map(container_id, layers) {
        return new ol.Map({
            target: container_id,
            layers: layers,
            view: new ol.View({
                center: ol.proj.transform([0, 0], 'EPSG:4326', 'EPSG:3857'),
                zoom: 2
            })
        });

    }

    function make_bureaux_geometries(pays_marker_layer_list, donnees_pays) {
        /**
         * Renvoie un ol.geom.GeometryCollection contenant les geométries de
         * tous les marqueurs pays de chaque bureau. Utile pour centrer la
         * carte sur une région.
         * */
        var bureaux_geometry_lists = {};

        $.each(pays_marker_layer_list, function(i, pays_marker_layer) {
            pays_marker_layer.getSource().forEachFeature(function (feature) {
                var code_pays = feature.get('code_pays');
                var pays = donnees_pays[code_pays];
                if (pays) {
                    var bureau_geometries;
                    var code_bureau = pays.bureau;
                    if (code_bureau in bureaux_geometry_lists) {
                        bureau_geometries = bureaux_geometry_lists[code_bureau];
                    } else {
                        bureau_geometries = [];
                        bureaux_geometry_lists[code_bureau] = bureau_geometries;
                    }
                    bureau_geometries.push(feature.getGeometry());
                }
            });
        });

        var bureaux_geometries = {};
        $.each(bureaux_geometry_lists, function (code_bureau, list) {
            bureaux_geometries[code_bureau] = new ol.geom.GeometryCollection(list);
        });
        return bureaux_geometries;
    }

    function get_lieu_style(filtre_code_bureau, feature, resolution) {
        var lieu = feature.get('lieu');
        var code_bureau = lieu.code_bureau;
        if (resolution < 10000 &&
            (filtre_code_bureau === 'tous' || filtre_code_bureau === code_bureau)) {
            return [get_lieu_implantation_style(lieu.nom, lieu.lat, lieu.lon)];
        } else {
            return [];
        }
    }

    /**
     * Callback appelé lorsque le popup va être affiché afin que son contenu soit
     * mis à jour
     * @callback setPopupContentCallback
     * @param {string} nom Nom du pays
     * @param {string} code_pays Code iso3 du pays
     * @param {Array} implantations Liste des implantations du pays
     * @param {Number} nb_etablissements Nombre d'établissements dans le pays
     * @param {Number} nb_cnfp Nombre de CNF Partenaires dans le pays
     */

    /**
     *
     * @param options
     * @param options.container_id L'élément dans lequel on va dessiner la carte
     * @param options.donnees_cartes Données sur les pays, les bureaux,
     * les capitales, les lieux d'implantation
     * @param options.implantation_marker_url Image servant de marqueur pour les
     * pays où il y a au moins une implantation
     * @param options.membre_marker_url Image servant de marqueur pour les pays
     * où il y a des membres mais pas d'implantation
     * @param options.popup_id Id de l'élément qui sert de popup
     * @param {setPopupContentCallback} options.set_popup_content Callback appelé
     * lorsque le popup va être affiché
     * @param options.couleurs_bureaux Dictionnaire donnant la couleur pour
     * chaque code de bureau régional
     * @param options.filtre_region Code d'un bureau si on ne veut afficher que
     * celui-là
     */
    function init(options) {
        var implantation_marker_style = make_marker_icon_style(options.implantation_marker_url);
        var etablissement_marker_style = make_marker_icon_style(options.membre_marker_url);
        var etablissement_marker_style_skewed = make_marker_icon_style(options.membre_marker_url, 0.25);
        var donnees_pays = options.donnees_carte.donnees_pays;
        var styles_pays = make_styles_pays(options.couleurs_bureaux);

        function get_capitale_style(pays) {
            return pays.implantations.length ? implantation_marker_style
                : etablissement_marker_style;
        }

        var pays_par_type = get_pays_par_type(donnees_pays);
        var pays_par_bureau = get_pays_par_bureau(donnees_pays);

        var markers_pays_implantations = make_marker_pays_features(
            options.donnees_carte.capitales,
            pays_par_type.pays_implantations);
        var markers_pays_etablissements = make_marker_pays_features(
            options.donnees_carte.capitales,
            pays_par_type.pays_etablissements);


        var markers_pays_implantations_layer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: markers_pays_implantations
            }),
            style: implantation_marker_style
        });

        var markers_pays_etablissements_layer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: markers_pays_etablissements
            }),
            style: marker_pays_etablissement_style.bind(undefined,
                pays_par_type.pays_implantations, 'tous',
                etablissement_marker_style,
                etablissement_marker_style_skewed)
        });

        var pays_format = new ol.format.GeoJSON({
            defaultDataProjection:"EPSG:4326"});

        var paysLayer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: pays_format.readFeatures(
                    options.donnees_carte.countries_geojson,
                    {featureProjection: "EPSG:3857"})
            }),
            style: function (feature, resolution) {
                var pays_iso3 = feature.getId();
                var infos_pays = donnees_pays[pays_iso3];
                var style_key = infos_pays ? infos_pays.bureau : PAYS_SANS_DONNEES;
                var style = styles_pays[style_key];
                var style_text = style.getText();
                if (style_text) {
                    style_text.setText(resolution < 5000 ? infos_pays.nom : '');
                }
                return [style];
            },
            opacity: 0.5
        });

        var lieux_layer = new ol.layer.Vector({
            source: new ol.source.Vector({
                features: make_lieux_implantations_features(
                    options.donnees_carte.lieux_implantations)
            }),
            style: get_lieu_style.bind(undefined, 'tous')
        });

        var map = make_map(options.container_id, [paysLayer, lieux_layer,
            markers_pays_etablissements_layer, markers_pays_implantations_layer]);

        var element = document.getElementById(options.popup_id);
        var popup = new ol.Overlay({
            element: element,
            positioning: 'bottom-center',
            stopEvent: false
        });
        map.addOverlay(popup);
        map.on('click', feature_click.bind(undefined, map, donnees_pays, popup,
            options.set_popup_content));

        function filter_map(code_bureau, type) {
            // lieux, markers pays impl, markers pays etab
            lieux_layer.setStyle(get_lieu_style.bind(undefined, code_bureau));
            if (type === 'tous' || type === 'etablissements') {
                var etablissement_et_implantation_marker_style =
                    type === 'tous' ? etablissement_marker_style_skewed
                        : etablissement_marker_style;
                markers_pays_etablissements_layer.setStyle(
                    marker_pays_etablissement_style.bind(undefined,
                        pays_par_type.pays_implantations, code_bureau,
                        etablissement_marker_style,
                        etablissement_et_implantation_marker_style));
            } else {
                markers_pays_etablissements_layer.setStyle(
                    function() { return []; })
            }
            if (type === 'tous' || type === 'implantations') {
                markers_pays_implantations_layer.setStyle(
                    marker_pays_implantation_style.bind(undefined, code_bureau,
                        implantation_marker_style));
            } else {
                markers_pays_implantations_layer.setStyle(
                    function () {
                        return [];
                    })
            }
        }

        var bureaux_geometries = make_bureaux_geometries(
            [markers_pays_etablissements_layer,
                markers_pays_implantations_layer], donnees_pays);
        var zoom_to_region_fn = zoom_to_region.bind(undefined, map, bureaux_geometries);

        return {
            filter_map: filter_map,
            zoom_to_region: zoom_to_region_fn,
            ol_map: map
        }
    }

    function zoom_to_region(map, bureaux_geometries, code_bureau) {
        var region_geometry = bureaux_geometries[code_bureau];
        var view = map.getView();
        view.fitExtent(region_geometry.getExtent(), map.getSize());
        var zoom = view.getZoom();
        if (zoom > 4) {
            view.setZoom(zoom - 1);
        }
    }

    function feature_click(map, donnees_pays, popup, set_popup_content, evt) {
        var feature = map.forEachFeatureAtPixel(evt.pixel,
            function (feature, layer) {
                return feature;
            });
        if (feature) {
            var code_pays = feature.get('code_pays');
            if (code_pays) {
                var geometry = feature.getGeometry();
                var coord = geometry.getCoordinates();
                var donnees_du_pays = donnees_pays[code_pays];
                set_popup_content(code_pays,
                    donnees_du_pays.nom,
                    donnees_du_pays.implantations,
                    donnees_du_pays.nb_etablissements,
                    donnees_du_pays.nb_cnfp);
                popup.setPosition(coord);
            } else {
                popup.setPosition(undefined);
            }
        } else {
            popup.setPosition(undefined);
        }
    }

    return {
        init: init
    }
})();
