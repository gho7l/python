# Nous créons une variable en écrivant le nom de la variable que nous voulons suivie
# par un signe égal, suivi de la valeur que nous voulons stocker dans la
# variable. Par exemple, la ligne suivante crée une variable appelée
# hello_str, contenant la chaîne Hello World.
hello_str = "Hello World"

# La ligne suivante crée une variable entière appelée hello_int avec la valeur # de 21.
# Notez comment elle n'a pas besoin d'être mise entre guillemets
hello_int = 21

# Le même principe est vrai pour les opérateurs booléens
hello_bool = True

# Nous créeons un tuple de la manière suivante
hello_tuple = (21,32)

hello_list = ["Hello,","ceci","est","une","liste"]
# Cette liste contient maintenant 5 chaînes. Notez qu'il n'y a pas d'espaces
# entre ces chaînes, donc si vous deviez les rejoindre pour faire une phrase
# il faudrait ajouter un espace entre chaque élément

# Vous pouvez également créer la même liste comme suit
hello_list = list()
hello_list.append("Hello,")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

# La première ligne crée une liste et les lignes suivantes utilisent l'ajout
# du type de liste pour ajouter des éléments à la liste. Cette façon d'utiliser un
# listee n'est pas très utile lorsque vous travaillez avec des chaînes que vous connaissez
# à l'avance, mais elle peut être utile lorsque vous travaillez avec des données dynamiques
# Cette liste écrasera la première liste sans aucun avertissement car nous
# utilisons le même nom de variable que la liste précédent.

# Nous pourrions créer un dictionnaire tant que nous y sommes. Notez comment nous avons
# aligné les colonnes ci-dessous pour rendre le code propre
hello_dict = {"first_name":"Liam","last_name":"Fraser","eye_colour":"Blue"}

# Accédons à certains éléments dans nos ensembles de données
# Nous allons commencer par changer la valeur de la dernière chaîne dans notre hello_list
# et ajouter un point d'exclamation à la fin. La chaîne "list" est le 5ème élément
# dans la liste. Cependant, les index dans Python sont basés sur zéro, ce qui signifie que
# le premier élément a un indice de 0.

# Notez qu'il y a aura maintenant deux signes d'exclamation à l'affichage de l'élément
print(hello_list[4])
hello_list[4] += "!"
# hello_list[4] = hello_list[4] + "!"
print(hello_list[4])

# Rappelez-vous que les tuples sont immuables, bien que nous puissions avoir accès à
# leurs éléments individuellement
print(str(hello_tuple[0]))
# Nous ne pouvons pas changer la valeur des éléments comme nous l'avons fait avec la liste
# Notez l'utilisation de la fonction str ci-dessus pour convertir explicitement la valeur
# du nombre entier contenu dans le tuple en chaîne de caractères avant de l'afficher.

# Créeons une phrase en utilisant les données contenues dans hello_dict
print(hello_dict["first_name"]+" "+hello_dict["last_name"]+" has "+hello_dict["eye_colour"]+" eyes.")

# Une façon plus ordonnée de le faire serait d'utiliser le formatteur de chaînes de Python
print("{0} {1} has {2} eyes.".format(hello_dict["first_name"],hello_dict["last_name"],hello_dict["eye_colour"]))