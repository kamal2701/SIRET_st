# Travaux Digital Factory 2022
# Kamal QUAZBARY

# Pour plus d'informations, lire le fichier texte Streamlit app - Mode d'emploi.docx
# streamlit run Streamlit_app.py

import streamlit as st
import pandas as pd
from api_insee import ApiInsee
import math
import numpy as np
from PIL import Image
import os


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

libelles = [
    "etablissement_uniteLegale_denominationUniteLegale",
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

mapping = pd.DataFrame({'libelles' : libelles, 'infos' : informations})
mapping['index'] = mapping.index


with st.sidebar.container():
    image = Image.open(os.path.join(os.getcwd(), 'digital.factory.png'))

    st.image(image)
    
st.sidebar.title('Hello Practice Digitale !')

st.sidebar.write('Voici une application construite sur Streamlit à propos des codes SIRET')


def flatten_dict(dd, separator ='_', prefix =''):
    return { prefix + separator + k if prefix else k : v
             for kk, vv in dd.items()
             for k, v in flatten_dict(vv, separator, kk).items()
             } if isinstance(dd, dict) else { prefix : dd }


def reglages():
    st.subheader('Sélectionnez les informations que vous souhaitez extraire')
    
    
    if st.button('Select All'):
        for info in informations:
            st.session_state['dynamic_checkbox_' + str(informations.index(info))] = True
        st.experimental_rerun()
    if st.button('UnSelect All'):
        for info in informations:
            st.session_state['dynamic_checkbox_' + str(informations.index(info))] = False
        st.experimental_rerun()
    
    for info in informations:
        st.checkbox(info, key='dynamic_checkbox_' + str(informations.index(info)), value = True)
      
    

    
    for info in informations:
        if 'dynamic_checkbox_' + str(informations.index(info)) not in st.session_state:
            st.session_state['dynamic_checkbox_' + str(informations.index(info))] = True
    
    
    
            
            
    selected_index = [i.replace('dynamic_checkbox_','') for i in st.session_state.keys() if i.startswith('dynamic_checkbox_') and st.session_state[i]]
    
    if 'selected_attributes' not in st.session_state.keys():
        st.session_state['selected_attributes'] = selected_index
    else:
        st.session_state['selected_attributes'] = selected_index
    



def menu():
    
    st.header("Extraction de données à partir de codes SIRET")    
        
        
    siret = st.text_input('Entrez le code SIRET', value = '48347855800057')
    
    if siret != "" :
        api = ApiInsee(
            key = "SvyV5c0YqjcXJXEbVYCAh2ZVfCYa",
            secret = "OzG82MAf_oL864QWoS1SCf4pmPwa")
        
        try:
            
            dict_data = flatten_dict(api.siret(siret).get())
            
            df_data = pd.DataFrame({'libelles' : dict_data.keys(), 'Resultat' : dict_data.values()})
          
            df_data = df_data[df_data['Resultat'].notnull()]
            
            df_data = df_data[~df_data.libelles.isin(['header_statut', 'header_message', 'etablissement_periodesEtablissement', 'etablissement_nombrePeriodesEtablissement'])]
            
            df_data = pd.merge(df_data, mapping, on = 'libelles', how='left',indicator=True)
            df_data['Attribut'] = np.where(df_data['_merge']== 'both', df_data['infos'], df_data['libelles'])
            df_data = df_data[['Attribut', 'Resultat', 'index']]
            
            df_data = df_data.sort_values(by=['index'])
            df_data = df_data.astype(str)
            
            list_util = [int(i) for i in st.session_state['selected_attributes']]
            n = len(df_data.index)
            
            list_util = [i for i in list_util if i<n]
            
            df_data = df_data.iloc[list_util,:]
            df_data = df_data[['Attribut', 'Resultat']]
            
            st.success('Ci-dessous les données concernant cette entreprise :')
            
            hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)

            st.table(df_data)
        
        except :
            st.warning("Ce code n'a pas été reconnu")


page_names_to_funcs = {
    "Menu": menu,
    "Réglages": reglages,
}

selected_page = st.sidebar.selectbox("Sélectionnez une page", page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()

