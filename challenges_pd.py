import pandas as pd
import numpy as np

# Challenge 1 

df_temp = pd.DataFrame({
    "Nom": ["Mouhamadou", "Diamanka", "Modou", "Pouye"],
    "Note1": [15, np.nan, 12, 18],
    "Note2": [np.nan, 17, 14, 19]
})

print("Avant nettoyage :\n", df_temp)
df_cleaned = df_temp.fillna(df_temp.mean(numeric_only=True))
print("\nAprès remplissage des NaN par moyenne :\n", df_cleaned)


# Challenge 2
df_finance = pd.DataFrame({
    "transaction_id": [101, 102, 103, 104, 105],
    "montant": [500, 2000, 150, 1300, 700]
})

print("Transactions > 1000 :\n", df_finance[df_finance["montant"] > 1000])


# Challenge 3 
df_ventes = pd.DataFrame({
    "region": ["Ziguinchor", "Dakar", "Sedhiou", "Rabat", "Casa", "St-louis"],
    "vente": [100, 200, 150, 300, 250, 180]
})

total_par_region = df_ventes.groupby("region")["vente"].sum().reset_index()
print("Total des ventes par region :\n", total_par_region)



# Challenge 4 
df_clients = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "nom": ["Issa", "Sarr", "Amdy"]
})

df_commandes = pd.DataFrame({
    "commande_id": [201, 202, 203, 204],
    "customer_id": [2, 1, 3, 1],
    "produit": ["Livre", "Stylo", "Sac", "Cahier"]
})

fusion = pd.merge(df_clients, df_commandes, on="customer_id")
print("Fusion clients + commandes :\n", fusion)


# Challenge 5 
df_ventes2 = pd.DataFrame({
    "produit": ["Stylo", "Stylo", "Cahier", "Livre", "Cahier", "Livre"],
    "region": ["Ziguinchor", "Dakar", "Sedhiou", "Rabat", "Casa", "St-louis"],
    "ventes": [100, 150, 200, 120, 170, 130]
})

pivot = pd.pivot_table(df_ventes2, values="ventes", index="produit", columns="region", aggfunc="sum", fill_value=0)
print("Tableau croise dynamique (somme des ventes par produit et region) :\n", pivot)
