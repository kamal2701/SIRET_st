# Kamal QUAZBARY
# 2023


# streamlit run Streamlit_app.py

import streamlit as st
import pandas as pd
from api_insee import ApiInsee
import numpy as np
from PIL import Image
import os
import io

buffer = io.BytesIO()


informations = [
"Dénomination usuelle de l’unité légale",
"Numéro Siren",
"Numéro interne de classement de l'établissement",
"Numéro Siret",
"Statut de diffusion de l’établissement",
"Date de création de l’établissement",
"Tranche d’effectif salarié de l’établissement",
"Année de validité de la tranche d’effectif salarié de l’établissement",
"Activité exercée par l’artisan inscrit au registre des métiers",
"Date du dernier traitement de l’établissement dans le répertoire Sirene",
"Qualité de siège ou non de l’établissement",
"État administratif de l’unité légale",
"Statut de diffusion de l’unité légale",
"Date de création de l'unité légale",
"Catégorie juridique de l’unité légale",
"Dénomination de l’unité légale",
"Sigle de l’unité légale",
"Dénomination usuelle de l’unité légale deuxième champ",
"Dénomination usuelle de l’unité légale troisième champ",
"Caractère féminin ou masculin de la personne physique",
"Nom de naissance de la personnes physique",
"Nom d’usage de la personne physique",
"Premier prénom déclaré pour un personne physique",
"Deuxième prénom déclaré pour un personne physique",
"Troisième prénom déclaré pour un personne physique",
"Quatrième prénom déclaré pour un personne physique",
"Prénom usuel de la personne physique",
"Pseudonyme de la personne physique",
"Activité principale de l’unité légale",
"Nomenclature d’activité de la variable activitePrincipaleUniteLegale",
"Numéro au Répertoire National des Associations",
"Appartenance au champ de l’économie sociale et solidaire",
"Caractère employeur de l’unité légale",
"Tranche d’effectif salarié de l’unité légale",
"Année de validité de la tranche d’effectif salarié de l’unité légale",
"Numéro interne de classement (Nic) de l’unité légale",
"Date du dernier traitement de l’unité légale dans le répertoire Sirene",
"Catégorie à laquelle appartient l’entreprise",
"Année de validité de la catégorie d’entreprise",
"Complément d’adresse",
"Numéro de voie",
"Indice de répétition dans la voie",
"Type de voie",
"Libellé de voie",
"Code postal",
"Libellé de la commune",
"Libellé de la commune pour un établissement situé à l’étranger",
"Distribution spéciale de l’établissement",
"Code commune de l’établissement",
"Code cedex",
"Libellé du code cedex",
"Code pays de l’adresse secondaire pour un établissement situé à l’étranger",
"Libellé du pays pour un établissement situé à l’étranger",
"Complément d’adresse secondaire",
"Numéro de la voie de l’adresse secondaire",
"Indice de répétition dans la voie pour l’adresse secondaire",
"Type de voie de l’adresse secondaire",
"Libellé de voie de l’adresse secondaire",
"Code postal de l’adresse secondaire",
"Libellé de la commune de l’adresse secondaire",
"Code commune de l’adresse secondaire",
"Distribution spéciale de l’adresse secondaire de l’établissement",
"Code cedex de l’adresse secondaire",
"Libellé du code cedex de l’adresse secondaire",
"Code pays pour un établissement situé à l’étranger",
"Libellé du pays de l’adresse secondaire pour un établissement situé à l’étranger"]

libelles = ["etablissement_uniteLegale_denominationUniteLegale",
"etablissement_siren",
"etablissement_nic",
"etablissement_siret",
"etablissement_statutDiffusionEtablissement",
"etablissement_dateCreationEtablissement",
"etablissement_trancheEffectifsEtablissement",
"etablissement_anneeEffectifsEtablissement",
"etablissement_activitePrincipaleRegistreMetiersEtablissement",
"etablissement_dateDernierTraitementEtablissement",
"etablissement_etablissementSiege",
"etablissement_uniteLegale_etatAdministratifUniteLegale",
"etablissement_uniteLegale_statutDiffusionUniteLegale",
"etablissement_uniteLegale_dateCreationUniteLegale",
"etablissement_uniteLegale_categorieJuridiqueUniteLegale",
"etablissement_uniteLegale_sigleUniteLegale",
"etablissement_uniteLegale_denominationUsuelle1UniteLegale",
"etablissement_uniteLegale_denominationUsuelle2UniteLegale",
"etablissement_uniteLegale_denominationUsuelle3UniteLegale",
"etablissement_uniteLegale_sexeUniteLegale",
"etablissement_uniteLegale_nomUniteLegale",
"etablissement_uniteLegale_nomUsageUniteLegale",
"etablissement_uniteLegale_prenom1UniteLegale",
"etablissement_uniteLegale_prenom2UniteLegale",
"etablissement_uniteLegale_prenom3UniteLegale",
"etablissement_uniteLegale_prenom4UniteLegale",
"etablissement_uniteLegale_prenomUsuelUniteLegale",
"etablissement_uniteLegale_pseudonymeUniteLegale",
"etablissement_uniteLegale_activitePrincipaleUniteLegale",
"etablissement_uniteLegale_nomenclatureActivitePrincipaleUniteLegale",
"etablissement_uniteLegale_identifiantAssociationUniteLegale",
"etablissement_uniteLegale_economieSocialeSolidaireUniteLegale",
"etablissement_uniteLegale_caractereEmployeurUniteLegale",
"etablissement_uniteLegale_trancheEffectifsUniteLegale",
"etablissement_uniteLegale_anneeEffectifsUniteLegale",
"etablissement_uniteLegale_nicSiegeUniteLegale",
"etablissement_uniteLegale_dateDernierTraitementUniteLegale",
"etablissement_uniteLegale_categorieEntreprise",
"etablissement_uniteLegale_anneeCategorieEntreprise",
"etablissement_adresseEtablissement_complementAdresseEtablissement",
"etablissement_adresseEtablissement_numeroVoieEtablissement",
"etablissement_adresseEtablissement_indiceRepetitionEtablissement",
"etablissement_adresseEtablissement_typeVoieEtablissement",
"etablissement_adresseEtablissement_libelleVoieEtablissement",
"etablissement_adresseEtablissement_codePostalEtablissement",
"etablissement_adresseEtablissement_libelleCommuneEtablissement",
"etablissement_adresseEtablissement_libelleCommuneEtrangerEtablissement",
"etablissement_adresseEtablissement_distributionSpecialeEtablissement",
"etablissement_adresseEtablissement_codeCommuneEtablissement",
"etablissement_adresseEtablissement_codeCedexEtablissement",
"etablissement_adresseEtablissement_libelleCedexEtablissement",
"etablissement_adresseEtablissement_codePaysEtrangerEtablissement",
"etablissement_adresseEtablissement_libellePaysEtrangerEtablissement",
"etablissement_adresse2Etablissement_complementAdresse2Etablissement",
"etablissement_adresse2Etablissement_numeroVoie2Etablissement",
"etablissement_adresse2Etablissement_indiceRepetition2Etablissement",
"etablissement_adresse2Etablissement_typeVoie2Etablissement",
"etablissement_adresse2Etablissement_libelleVoie2Etablissement",
"etablissement_adresse2Etablissement_codePostal2Etablissement",
"etablissement_adresse2Etablissement_libelleCommune2Etablissement",
"etablissement_adresse2Etablissement_libelleCommuneEtranger2Etablissement",
"etablissement_adresse2Etablissement_distributionSpeciale2Etablissement",
"etablissement_adresse2Etablissement_codeCedex2Etablissement",
"etablissement_adresse2Etablissement_libelleCedex2Etablissement",
"etablissement_adresse2Etablissement_codePaysEtranger2Etablissement",
"etablissement_adresse2Etablissement_libellePaysEtranger2Etablissement"]

mapping = pd.DataFrame({'libelles' : libelles, 'Attributs' : informations})
mapping['index'] = mapping.index

api = ApiInsee(
    key = st.secrets["key"],
    secret = st.secrets["secret"])

    

st.sidebar.write('Application construite autour des codes SIRET')


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


uploaded_file = st.sidebar.file_uploader("Insérez les SIRET dans la même colonne d'un fichier Excel vide")


st.header("Extraction de données à partir de codes SIRET")    
    
if uploaded_file is not None:
    input_sirets = pd.read_excel(uploaded_file, header=None, names = ['Sirets'])
    input_sirets = input_sirets['Sirets'].tolist()
    
    if len(input_sirets) ==0:
        st.success("Veuillez mettre des codes SIRET dans le fichier")
    
    else:
        df_final = pd.DataFrame(informations, columns=['Attributs'])
        
        for siret in input_sirets:
            siret = str(siret)
            if siret != "" :
                try:
                    # Récupération des données et retraitement pour les avoir au format dataframe
                    dict_data = flatten_dict(api.siret(siret).get())
                    df_siret = pd.DataFrame({'libelles' : dict_data.keys(), siret : dict_data.values()})
                    df_siret = df_siret[~df_siret.libelles.isin(['header_statut', 'header_message', 'etablissement_periodesEtablissement', 'etablissement_nombrePeriodesEtablissement'])]
                    df_siret = df_siret[df_siret.libelles.isin(libelles)]
                    # Jointure pour récupérer les bons noms des champs, ou les attributs
                    df_siret = pd.merge(df_siret, mapping, on = 'libelles', how='left',indicator=True)
                    df_siret = df_siret[["Attributs", siret]]
                    df_siret = df_siret.astype(str)
                    
                    # Affichage du résultat en cas de réussite
                    name_company = dict_data['etablissement_uniteLegale_denominationUniteLegale']
                    st.success(f'Le SIRET {siret} correspond à {name_company}')
                    
                    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
            
                    df_final = pd.merge(df_final, df_siret, on=["Attributs"])
                    df_final.replace(to_replace=['None'], value=np.nan, inplace=True)
                    
                except :
                    st.warning(f"Le SIRET {siret} n'a pas été reconnu")
        
        
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df_final.to_excel(writer, sheet_name='Resultat', index=False)
            
            worksheet = writer.sheets['Resultat']  # pull worksheet object
            for idx, col in enumerate(df_final):  # loop through all columns
                series = df_final[col]
                max_len = max((
                    series.astype(str).map(len).max(),  # len of largest item
                    len(str(series.name))  # len of column name/header
                    )) + 1  # adding a little extra space
                worksheet.set_column(idx, idx, max_len)
            
            writer.save()
            
            st.download_button(
                label="Télécharger les données en Excel",
                data=buffer,
                file_name="Resultats_SIRET.xlsx",
                mime="application/vnd.ms-excel")


