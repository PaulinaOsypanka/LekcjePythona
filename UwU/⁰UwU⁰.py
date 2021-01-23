def to_police(netto, vat):
    brutto = netto + netto*vat
    return brutto

coca_cola = to_police(10, 0.23)

carrots_in_the_field_are_dying = to_police(2, 0.08) 

Agata_Christie_trzecia_lokatorka = to_police(15, 0)
print(coca_cola, carrots_in_the_field_are_dying, Agata_Christie_trzecia_lokatorka)