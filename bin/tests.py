# # # imports
# # import pandas as pd
# #
# # legume = dict(['Aubergine',
# #                'Basilic',
# #                'Betterave',
# #                'Brocoli',
# #                'Carotte',
# #                'Céleri',
# #                'Chicorée',
# #                'Chou de Chine',
# #                'Concombre',
# #                'Cornichon',
# #                'Courgette',
# #                'Epinard',
# #                'Haricots grimpants',
# #                'Haricots nains',
# #                'Laitue',
# #                'Mâche',
# #                'Mesclun',
# #                'Navet',
# #                'Oignon blanc',
# #                'Poireau',
# #                'Poirée',
# #                'Pois',
# #                'Poivron',
# #                'Radis',
# #                'Tomate'])
# #
# # famille = dict(['Légume-graine',
# #                 'Légume-fruit',
# #                 'Légume-feuille',
# #                 'Légume-racine'])
# #
# # columns = ['Nom',
# #            'Famille',
# #            'Hauteur',
# #            'Icon',
# #            'Emplacement',
# #            'Exposition',
# #            'Ensoleillement',
# #            'Eloigner de',
# #            'Planter apres',
# #            'Ne pas planter apres',
# #            ]
# #
# # df_bdd = pd.DataFrame([], columns=columns)
# #
# # # GERER LES SEMIS MEEERRRDDEEE
# #
# # df0 = pd.DataFrame([['Aubergine', 'Légume-fruit', None, 'aubergine.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df1 = pd.DataFrame([['Basilic', 'Légume-feuille', None, 'basilic.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df2 = pd.DataFrame([['Betterave', 'Légume-racine', None, 'betterave.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df3 = pd.DataFrame([['Brocoli', 'Légume-feuille', None, 'brocoli.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df4 = pd.DataFrame([['Carotte', 'Légume-racine', None, 'carotte.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df5 = pd.DataFrame([['Céleri', 'Légume-racine', None, 'celeri.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df6 = pd.DataFrame([['Chicorée', 'Légume-feuille', None, 'chicoree.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df7 = pd.DataFrame([['Chou de Chine', 'Légume-feuille', None, 'choudechine.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df8 = pd.DataFrame([['Concombre', 'Légume-fruit', None, 'concombre.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df9 = pd.DataFrame([['Epinard', 'Légume-feuille', None, 'epinard.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df10 = pd.DataFrame([['Haricots grimpants', 'Légume-fruit', None, 'haricotsgrimpants.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df11 = pd.DataFrame([['Haricots nains', 'Légume-fruit', None, 'haricotsnains.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df12 = pd.DataFrame([['Laitue', 'Légume-feuille', None, 'laitue.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df13 = pd.DataFrame([['Mâche', 'Légume-feuille', None, 'mache.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df14 = pd.DataFrame([['Mesclun', 'Légume-feuille', None, 'mesclun.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df15 = pd.DataFrame([['Navet', 'Légume-racine', None, 'navet.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df16 = pd.DataFrame([['Oignon blanc', 'Légume-racine', None, 'oignonblanc.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df17 = pd.DataFrame([['Poireau', 'Légume-feuille', None, 'poireau.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df18 = pd.DataFrame([['Poirée', 'Légume-feuille', None, 'poiree.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df19 = pd.DataFrame([['Pois', 'Légume-fruit', None, 'pois.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df20 = pd.DataFrame([['Poivron', 'Légume-fruit', None, 'poivron.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df21 = pd.DataFrame([['Radis', 'Légume-racine', None, 'radis.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df22 = pd.DataFrame([['Tomate', 'Légume-fruit', None, 'tomate.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df23 = pd.DataFrame([['Cornichon', 'Légume-fruit', None, 'cornichon.png', 'Au milieu', None, 'Plein soleil', [], []]])
# # df24 = pd.DataFrame([['Courgette', 'Légume-fruit', None, 'courgette.png', 'Au milieu', None, 'Plein soleil', [], []]])
# #
# # df_bdd = df_bdd.append(df0)
# # df_bdd = df_bdd.append(df1)
# # df_bdd = df_bdd.append(df2)
# # df_bdd = df_bdd.append(df3)
# # df_bdd = df_bdd.append(df4)
# # df_bdd = df_bdd.append(df5)
# # df_bdd = df_bdd.append(df6)
# # df_bdd = df_bdd.append(df7)
# # df_bdd = df_bdd.append(df8)
# # df_bdd = df_bdd.append(df9)
# # df_bdd = df_bdd.append(df10)
# # df_bdd = df_bdd.append(df11)
# # df_bdd = df_bdd.append(df12)
# # df_bdd = df_bdd.append(df13)
# # df_bdd = df_bdd.append(df14)
# # df_bdd = df_bdd.append(df15)
# # df_bdd = df_bdd.append(df16)
# # df_bdd = df_bdd.append(df17)
# # df_bdd = df_bdd.append(df18)
# # df_bdd = df_bdd.append(df19)
# # df_bdd = df_bdd.append(df20)
# # df_bdd = df_bdd.append(df21)
# # df_bdd = df_bdd.append(df22)
# # df_bdd = df_bdd.append(df23)
# # df_bdd = df_bdd.append(df24)
# #
# #
# #
# # print(df_bdd)
#
#
import pandas as pd

bdd = pd.read_csv('../src/data/bdd.csv', delimiter=';')
a = bdd['Icon']
b = a[5]
print(a)
print(b)
# print((a['Eloigner de'][2]))
# b = b.split(', ')
# print(b)

