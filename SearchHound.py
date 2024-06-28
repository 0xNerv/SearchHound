#importo los modulos correspondientes
import requests
import sys
import concurrent.futures
from colorama import *
import random
import time

start_time = time.time()
comienza = random.randint(1, 2)

#Los banners estos

banner1 = f'''
                       ;\ 
                      |' \ 
   _                  ; : ; 
  / `-.              /: : | 
 |  ,-.`-.          ,': : | 
 \  :  `. `.       ,'-. : | 
  \ ;    ;  `-.__,'    `-.| 
   \ ;   ;  :::  ,::'`:.  `.         
    \ `-. :  `    :.    `.  \ 
     \   \    ,   ;   ,:    (\ 
      \   :., :.    ,'o)): ` `-. 
    ,/,' ;' ,::"'`.`---'   `.  `-._        \033[1m{Fore.RED}SearchHound {Fore.WHITE}Version 1.0{Fore.RESET}\033[0m
    /  :  ; '"      `;'          ,--`.      \033[1m{Fore.RED}Creada por {Fore.WHITE}0xNerv{Fore.RESET}\033[0m
  ;/   :; ;             ,:'     (   ,:) 
   ,.,:.    ; ,:.,  ,-._ `.     \""'/ 
    '::'     `:'`  ,'(  \`._____.-'"' 
       ;,   ;  `.  `. `._`-.  \\ 
       ;:.  ;:       `-._`-.\  \`. 
        '`:. :        |' `. `\  ) \ 
          ` ;:       |    `--\__,' 
             '`      ,' 
                  ,-' 

'''
banner = f'''
                  _,)
          _..._.-;-'
       .-'     `(
      /      ;   )
     ;.' ;`  ,;  ;
    .'' ``. (  \ ;      \033[1m{Fore.RED}SearchHound {Fore.WHITE}Version 1.0{Fore.RESET}\033[0m
   / f_ _L \ ;  )\      \033[1m{Fore.RED}Creada por {Fore.WHITE}0̳x̳N̳e̳r̳v̳{Fore.RESET}\033[0m
   \/|° °|\/;; <;/
  ((; \_/  (()     
       
'''

#banner random
if comienza == 1:
   print (banner)

if comienza == 2:
   print (banner1)

#etiquetas
new = '\033[1m['+Fore.GREEN+'>'+Fore.RESET+'] \033[0m'
info = '\033[1m['+Fore.BLUE+'?'+Fore.RESET+'] \033[0m'
found = '\033[1m['+Fore.GREEN+'+'+Fore.RESET+'] \033[0m'

try:
    target = sys.argv[1]
except IndexError:
    print('\nSeleccione el nombre objetivo, ej: ')
    print('\npython3 main.py username123\n')
    exit()

print(f'{info}Nombre objetivo: \033[1m' + target + '\033[0m')
output_file = 'osint.txt'

#url con las que prueba y al lado el nombre del servicio

urls_with_names = {
    f'https://www.youtube.com/@{target}': 'YouTube',
    f'https://www.1337x.to/user/{target}': '1337x',
    f'https://www.7cups.com/@{target}': '7Cups',
    f'https://8tracks.com/{target}': '8tracks',
    f'https://www.9gag.com/u/{target}': '9GAG',
    f'https://about.me/{target}': 'About.me',
    f'https://airbit.com/{target}': 'Airbit',
    f'https://www.airliners.net/user/{target}/profile/photos': 'Airliners.net',
    f'https://allmylinks.com/{target}': 'AllMyLinks',
    f'https://aminoapps.com/u/{target}': 'Amino',
    f'https://developer.apple.com/forums/profile/{target}': 'Apple Developer Forums',
    f'https://discussions.apple.com/profile/{target}': 'Apple Discussions',
    f'https://archiveofourown.org/users/{target}': 'Archive of Our Own',
    f'https://asciinema.org/~{target}': 'Asciinema',
    f'https://ask.fm/{target}': 'Ask.fm',
    f'https://audiojungle.net/user/{target}': 'AudioJungle',
    f'https://github.com/{target}': 'GitHub',
    f'https://facebook.com/{target}': 'Facebook',
    f'https://www.twitch.tv/{target}': 'Twitch',
    f'https://x.com/{target}': 'Twitter',
    f'https://www.chess.com/member/{target}': 'Chess.com',
    f'https://clapperapp.com/{target}': 'Clapper',
    f'https://www.duolingo.com/profile/{target}': 'Duolingo',
    f'https://giphy.com/{target}': 'Giphy',
    f'https://gitlab.com/{target}': 'GitLab',
    f'https://www.roblox.com/user.aspx?username={target}': 'Roblox',
    f'https://steamcommunity.com/groups/{target}': 'Steam Community Groups',
    f'https://steamcommunity.com/id/{target}': 'Steam Community ID',
    f'https://t.me/{target}': 'Telegram',
    f'https://www.pinterest.com/{target}/': 'Pinterest',
    f'https://soundcloud.com/{target}': 'SoundCloud',
    f'https://www.reddit.com/user/{target}': 'Reddit',
    f'https://www.quora.com/profile/{target}': 'Quora',
    f'https://www.vimeo.com/{target}': 'Vimeo',
    f'https://www.blogger.com/profile/{target}': 'Blogger',
    f'https://www.wattpad.com/user/{target}': 'Wattpad',
    f'https://www.last.fm/user/{target}': 'Last.fm',
    f'https://www.behance.net/{target}': 'Behance',
    f'https://www.discogs.com/user/{target}': 'Discogs',
    f'https://mix.com/{target}': 'Mix',
    f'https://imgur.com/user/{target}': 'Imgur',
    f'https://www.okcupid.com/profile/{target}': 'OkCupid',
    f'https://www.zoosk.com/profile/{target}': 'Zoosk',
    f'https://www.deviantart.com/{target}': 'DeviantArt',
    f'https://www.slideshare.net/{target}': 'SlideShare',
    f'https://ello.co/{target}': 'Ello',
    f'https://keybase.io/{target}': 'Keybase',
    f'https://www.bandcamp.com/{target}': 'Bandcamp',
    f'https://www.tripadvisor.com/Profile/{target}': 'TripAdvisor',
    f'https://www.goodreads.com/{target}': 'Goodreads',
    f'https://www.hackerone.com/{target}': 'HackerOne',
    f'https://www.producthunt.com/@{target}': 'Product Hunt',
    f'https://www.vk.com/{target}': 'VK',
    f'https://www.myspace.com/{target}': 'MySpace',
    f'https://www.flickr.com/people/{target}': 'Flickr',
    f'https://www.minds.com/{target}': 'Minds',
    f'https://www.livejournal.com/{target}': 'LiveJournal',
    f'https://www.gaana.com/artist/{target}': 'Gaana',
    f'https://www.jiosaavn.com/artist/{target}': 'JioSaavn',
    f'https://www.scribd.com/{target}': 'Scribd',
    f'https://www.academia.edu/{target}': 'Academia.edu',
    f'https://www.edmodo.com/{target}': 'Edmodo',
    f'https://www.badoo.com/en/{target}': 'Badoo',
    f'https://www.meetup.com/members/{target}': 'Meetup',
    f'https://www.couchsurfing.com/people/{target}': 'Couchsurfing',
    f'https://www.wanelo.com/{target}': 'Wanelo',
    f'https://www.instructables.com/member/{target}/': 'Instructables',
    f'https://www.houzz.com/user/{target}': 'Houzz',
    f'https://www.gumroad.com/{target}': 'Gumroad',
    f'https://www.patreon.com/{target}': 'Patreon',
    f'https://www.behance.net/{target}': 'Behance',
    f'https://www.dribbble.com/{target}': 'Dribbble',
    f'https://www.artstation.com/{target}': 'ArtStation',
    f'https://www.cgtrader.com/{target}': 'CGTrader',
    f'https://www.turbosquid.com/Search/Artists/{target}': 'TurboSquid'
}

print(f'{new}Iniciando hilos ...')
print(f'{info}Método usado en esta herramienta: GET')
print(f'{new}Buscando ...')

#funcion principal (busqueda)

def buscar(url, name):
    try:
        with requests.Session() as session:
            response = session.get(url, timeout=4)

        if response.status_code == 200:
            print(f'{found}{Fore.RED}\033[1m{name}{Fore.RESET}:\033[0m {url}')
            return name, url

    except requests.RequestException as e:
        pass

    return None

resultados_encontrados = []

with open(output_file, 'w') as a, concurrent.futures.ThreadPoolExecutor(max_workers=13) as executor:
    future_to_url = {executor.submit(buscar, url, name): url for url, name in urls_with_names.items()}
    
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]

        try:
            result = future.result()

            if result:                                                                                                                                                                  #no veas .secreto
                name, url = result
                resultados_encontrados.append((name, url))
                a.write(f'{name}: {url}\n')

        except Exception as e:
            pass

#chequea el tiempo de principio a fin

end_time = time.time()
elapsed_time = end_time - start_time 

print(f'{new}Numero total de cuentas encontradas: \033[1m{Fore.BLUE}{len(resultados_encontrados)}\033[0m{Fore.RESET}')
print(f"{info}Logs guardados en '{output_file}'")
print(f'{info}Tiempo transcurrido: {elapsed_time:.2f} segundos')
