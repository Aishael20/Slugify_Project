Yon pwojè Python ki fasilite konvèti nenpòt chenn karaktè an "slug"

pip install slugify
Itilizasyon

from slugify import text_to_slug
slug = text_to_slug("Nenpòt Tèks La") 
# nenpot-teks-la

slug = text_to_slug("Nenpòt Tèks La", seperator='*') 
# nenpot*teks*la