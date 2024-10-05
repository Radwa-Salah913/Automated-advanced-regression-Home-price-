import pandas as pd
import streamlit as st
import pickle
import os

file_path="C:\\Users\\dell\\OneDrive\\Desktop\\ML\\Preprocessing\\Home price.sav"
if os.path.exists(file_path):
        model = pickle.load(open(file_path, 'rb'))
else:
    st.error(f"File not found: {file_path}")


st.title("Predict Home Price")


cols=[ 'bsmtunfsf','openporchsf', 'wooddecksf', 'bsmtfullbath', 'fireplaces','overallcond', 'halfbath', 'bsmtfinsf1']

appear=['Unfinished square feet of basement area','Open porch area in square feet','Wood deck area in square feet','Basement full bathrooms',
        'Number of fireplaces','Rates the overall condition of the house from 10','Half baths above grade','Type 1 finished square feet']

lst=['BrDale', 'BrkSide', 'ClearCr', 'Crawfor', 'Edwards',
       'IDOTRR', 'MeadowV', 'NoRidge', 'NridgHt', 'OldTown', 'SawyerW',
       'Somerst', 'StoneBr', 'Timber', 'Veenker','other']    

dic_bsmtexposure ={'No':3,'Gd':1,'Mn':2,'Av':0}
dic_bsmtqual ={'Gd':2,'TA':3,'Ex':0,'Fa':1}
dic_mszoning ={'RL':3,'RM':4,'C (all)':0,'FV':1,'RH':2}
dic_bsmtfintype1 ={'GLQ':2,'ALQ':0,'Unf':5,'Rec':4,'BLQ':1,'LwQ':3}
dic_kitchenqual ={'Gd':2,'TA':3,'Ex':0,'Fa':1,}

dic_mssubclass={'1-STORY 1946 & NEWER ALL STYLES':20,'1-STORY 1945 & OLDER':30,
        	'1-STORY W/FINISHED ATTIC ALL AGES':40,'1-1/2 STORY - UNFINISHED ALL AGES':45,
        	'1-1/2 STORY FINISHED ALL AGES':50,'2-STORY 1946 & NEWER':60,
            '2-STORY 1945 & OLDER':70,'2-1/2 STORY ALL AGES':75,
        	'SPLIT OR MULTI-LEVEL':80,'SPLIT FOYER':85,
        	'DUPLEX - ALL STYLES AND AGES':90,'1-STORY PUD (Planned Unit Development) - 1946 & NEWER':120,
         	'1-1/2 STORY PUD - ALL AGES':150,'2-STORY PUD - 1946 & NEWER':160,
           	'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER':180,'2 FAMILY CONVERSION - ALL STYLES AND AGES':190
            }
lst2=['1-STORY 1946 & NEWER ALL STYLES','1-STORY 1945 & OLDER',
        	'1-STORY W/FINISHED ATTIC ALL AGES','1-1/2 STORY - UNFINISHED ALL AGES',
        	'1-1/2 STORY FINISHED ALL AGES','2-STORY 1946 & NEWER',
            '2-STORY 1945 & OLDER','2-1/2 STORY ALL AGES',
        	'SPLIT OR MULTI-LEVEL','SPLIT FOYER',
        	'DUPLEX - ALL STYLES AND AGES','1-STORY PUD (Planned Unit Development) - 1946 & NEWER',
         	'1-1/2 STORY PUD - ALL AGES','2-STORY PUD - 1946 & NEWER',
           	'PUD - MULTILEVEL - INCL SPLIT LEV/FOYER','2 FAMILY CONVERSION - ALL STYLES AND AGES'
            ]

dic={}
dic['mssubclass']=dic_mssubclass[st.selectbox('the type of dwelling involved in the sale',lst2)]
dic['bsmtexposure']=dic_bsmtexposure[st.selectbox('garden level walls',['No','Gd','Mn','Av'])]
dic['bsmtqual']=dic_bsmtqual[st.selectbox('the height of the basement',['TA','Gd','Ex','Fa'])]
dic['mszoning']=dic_mszoning[st.selectbox('zoning classification of the sale',['RH','RM','RL','FV','C (all)'])]
dic['bsmtfintype1']=dic_bsmtfintype1[st.selectbox('Rating of basement finished area',['GLQ','ALQ','Unf','Rec','BLQ','LwQ'])]
dic['kitchenqual']=dic_kitchenqual[st.selectbox('Kitchen quality',['Gd','TA','Ex','Fa'])]

for i,j in zip(cols,appear):
     temp=st.text_input(j)
     dic[i] = [float(temp)] if temp else [0]

CemntBd=st.selectbox('Exterior covering on house',['Cement Board','other'])    
RoofStyle=st.selectbox('Roof Style',['Hip','other'])
BuiltIn=st.selectbox('Garage location',['BuiltIn','other'])
Foundation=st.selectbox('Type of foundation',['Poured Contrete', 'Slab','other'])
HouseStyle=st.selectbox('House Style',['Two and one-half story: 2nd level finished','Two and one-half story: 2nd level unfinished',	'Split Foyer','SLvl	Split Level','other'])
LotConfig=st.selectbox('Lot configuration',['Cul-de-sac','Frontage on 2 sides of property','other'])
Neighborhood=st.selectbox('Neighborhood',lst)

if CemntBd=='Cement Board':
     dic['CemntBd']=1
else:
     dic['CemntBd']=0
if RoofStyle=='Hip':
     dic['Hip']=1
else:
     dic['Hip']=0
if BuiltIn=='BuiltIn':
     dic['BuiltIn']=1
else:
     dic['BuiltIn']=0
if Foundation=='Poured Contrete':
     dic['PConc']=1
     dic['Slab']=0
elif Foundation=='Slab':
     dic['PConc']=0
     dic['Slab']=1
else:
     dic['PConc']=0
     dic['Slab']=0

for item in lst:
    if Neighborhood== item:
      dic[item]=1
    else:
       dic[item]=0

if LotConfig=='Cul-de-sac':
     dic['CulDSac']=1
     dic['FR2']=0
elif LotConfig=='Frontage on 2 sides of property':
     dic['CulDSac']=0
     dic['FR2']=1
else:
     dic['CulDSac']=0
     dic['FR2']=0

if HouseStyle=='Two and one-half story: 2nd level finished':
     dic['2.5Fin']=1
     dic['2.5Unf']=0
     dic['2Story']=0
     dic['SLvl']=0
elif HouseStyle=='Two and one-half story: 2nd level unfinished':
     dic['2.5Fin']=0
     dic['2.5Unf']=1
     dic['2Story']=0
     dic['SLvl']=0
elif HouseStyle=='Split Foyer':
     dic['2.5Fin']=0
     dic['2.5Unf']=0
     dic['2Story']=1
     dic['SLvl']=0
elif HouseStyle=='SLvl	Split Level':
     dic['2.5Fin']=0
     dic['2.5Unf']=0
     dic['2Story']=0
     dic['SLvl']=1
else:
     dic['2.5Fin']=0
     dic['2.5Unf']=0
     dic['2Story']=0
     dic['SLvl']=0

train_df=pd.read_csv("C:\\Users\\dell\\OneDrive\\Desktop\\ML\\Preprocessing\\arranged_df.csv")
df=pd.DataFrame(dic,index=[0])
df = df[train_df.columns]



con=st.button('Confirm')

if con:
   result=model.predict(df)
   st.write(result)
