# -*- coding: utf-8 -*-		

import requests
import sys
from bs4 import BeautifulSoup

class Finder:

    def conab(self):
        try:
            page = requests.get('http://www.conab.gov.br/conteudos.php?a=1696&t=&Pagina_objcmsconteudos=3#A_objcmsconteudos')
            soup = BeautifulSoup(page.content, 'html.parser')

            rows = soup.find_all('tr', id = 'listagemItens')

            for row in rows:
                columns = row.find_all('td')
                title = columns[0].a.get_text().strip()

                if 0 < title.find('28'):
                    link = columns[1].a['href']

                    return {'title': title, 'link': link}

                pass

            return None
        except:
            return None