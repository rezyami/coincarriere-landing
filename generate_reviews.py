import json

reviews = [
    ("Capgemini", "Des candidats très pertinents et un accompagnement de qualité.", "https://companieslogo.com/img/orig/CAP.PA-9b4110b0.png?t=1720244491"),
    ("Atos", "Plateforme incontournable pour nos recrutements IT au Maroc.", "https://icon.horse/icon/atos.net"),
    ("CGI", "Une sélection de profils tech de haut niveau. Très satisfaits.", "https://icon.horse/icon/cgi.com"),
    ("SQLI", "CoinCarrière simplifie grandement notre processus de recrutement.", "https://icon.horse/icon/sqli.com"),
    ("IBM", "Excellente source de talents spécialisés en développement.", "https://icon.horse/icon/ibm.com"),
    ("Leyton", "Interface intuitive et CVs toujours très qualifiés.", "https://icon.horse/icon/leyton.com"),
    ("Sofrecom", "Des profils rares trouvés en un temps record.", "https://icon.horse/icon/sofrecom.com"),
    ("Accenture", "Notre partenaire privilégié pour l'acquisition de talents.", "https://icon.horse/icon/accenture.com"),
    ("Deloitte", "Une base de données très riche et des profils vérifiés.", "https://icon.horse/icon/deloitte.com"),
    ("Alten", "Très bonne expérience, nous recrutons régulièrement via le site.", "https://icon.horse/icon/alten.com"),
    ("DXC Technology", "Les candidats correspondent parfaitement à nos exigences techniques.", "https://icon.horse/icon/dxc.com"),
    ("Orange Business", "Un gain de temps énorme dans nos campagnes de recrutement.", "https://icon.horse/icon/orange-business.com"),
    ("Inetum", "La meilleure plateforme pour sourcer des ingénieurs expérimentés.", "https://icon.horse/icon/inetum.com"),
    ("Intelcia", "Un flux constant de candidats de grande qualité.", "https://icon.horse/icon/intelcia.com"),
    ("Thales", "Très professionnels, les profils proposés sont toujours excellents.", "https://icon.horse/icon/thalesgroup.com")
]

output = ""
for name, review, src in reviews:
    encoded_name = name.replace(' ', '+')
    output += f"""                <div class="relative mx-8 flex flex-col items-center gap-3 group/logo cursor-pointer">
                    <!-- Tooltip -->
                    <div class="absolute bottom-[100%] left-1/2 -translate-x-1/2 mb-4 w-[220px] bg-white p-4 rounded-xl shadow-[0_15px_35px_rgba(0,0,0,0.15)] border border-[#eaeaea] opacity-0 invisible group-hover/logo:opacity-100 group-hover/logo:visible group-hover/logo:-translate-y-2 transition-all duration-300 z-50 pointer-events-none text-center whitespace-normal">
                        <div class="flex items-center justify-center gap-1 text-accent mb-2">
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                            <svg class="w-4 h-4 fill-current" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
                        </div>
                        <p class="text-[0.85rem] text-text-main font-medium italic">"{review}"</p>
                        <!-- Pointer -->
                        <div class="absolute top-full left-1/2 -translate-x-1/2 border-[6px] border-transparent border-t-white z-10"></div>
                        <div class="absolute top-full left-1/2 -translate-x-1/2 border-[7px] border-transparent border-t-[#eaeaea] mt-[1px]"></div>
                    </div>
                    <img src="{src}" alt="{name}" class="h-12 w-auto object-contain grayscale opacity-60 group-hover/logo:grayscale-0 group-hover/logo:opacity-100 transition-all duration-300" onerror="this.src='https://ui-avatars.com/api/?name={encoded_name}&background=fff&color=0077B6&size=128'">
                    <span class="text-[0.85rem] font-semibold text-text-light opacity-60 group-hover/logo:opacity-100 group-hover/logo:text-primary transition-all duration-300">{name}</span>
                </div>\n"""

with open('reviews.html', 'w') as f:
    f.write(output)
