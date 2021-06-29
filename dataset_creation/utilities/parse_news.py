from datetime import datetime
import numpy as np
import regex as re

def format_string(input_string):
    '''
    Remove spaces at the beginning and replace multiple withe spaces by one.
    '''
    return re.sub(' +', ' ', input_string).strip()

def obtain_information_elconfidencial(t_id, soup):
    '''
    Given the soup (html) of a new from the webpage of 'elconfidencial' returns a list of
    fields to store the new's info in NewsML-G2 format (xml)
    '''
    news_uri = soup.find("link", {'rel': 'canonical'})['href']
    try:
        news_author = soup.find('a', class_='news-def-author').get_text()
        news_provider = "Blogs, El Confidencial"
        news_creation_datetime = soup.find('time', class_='news-def-date')['datetime']

        news_title = soup.find('h1', class_='news-header-tit').get_text()
        news_headline = soup.find('h2', class_='news-header-opening-txt').get_text()

        news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

        text = soup.find_all('div', class_='news-body-center cms-format')
        paragraphs = []
        for i in np.arange(0, len(text)):
            for part in text[i].find_all("p"):
                paragraphs.append(part.get_text())

        news_article = format_string(" ".join(paragraphs))

    except:
        news_author = format_string(soup.find_all("div", class_="authorSignature")[0].get_text().replace('Por', ''))
        news_provider = "Vanitatis, El Confidencial"
        news_creation_datetime = format_string(soup.find_all("div", class_="dateTime")[0].find('time')['datetime'])

        news_title = format_string(soup.find_all("title")[0].get_text())
        news_headline = format_string(soup.find_all("meta", {'name': 'description'})[0]['content'])

        news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

        text = soup.find_all("div", class_="newsType__content")
        paragraphs = []
        for i in np.arange(0, len(text)):
            for part in text[i].find_all("p"):
                paragraphs.append(part.get_text())

        news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_20m(t_id, soup):
    '''
    Given the soup (html) of a new from the webpage of '20m' returns a list of
    fields to store the new's info in NewsML-G2 format (xml)
    '''
    news_author = format_string(soup.find_all("span", class_="article-author")[0].get_text())
    news_provider = format_string(soup.find_all("meta", {"name": "author"})[0]["content"])
    news_creation_datetime = format_string(soup.find_all("meta", {"property": "article:published_time"})[0]["content"])
    news_uri = soup.find_all("link", {'rel': 'canonical'})[0]['href']

    news_title = format_string(soup.find_all("meta", {"name": "title"})[0]["content"])
    news_headline = format_string(soup.find_all("meta", {"name": "description"})[0]["content"])

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all("div", class_="article-text")
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_A3Noticias(t_id, soup):
    '''
    Given the soup (html) of a new from the webpage of 'A3Noticias' returns a list of
    fields to store the new's info in NewsML-G2 format (xml)
    '''
    news_author = format_string(soup.find_all('div', class_='article-author__name')[0].get_text())
    news_provider = format_string(soup.find('meta', {'property': 'og:site_name'})['content'])
    news_creation_datetime = format_string(soup.find_all('time', class_='article__time')[0]['datetime'])
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = format_string(soup.find_all('h1', class_='article-main__title')[0].get_text())
    news_headline = format_string(soup.find_all('h2', class_='article-main__description')[0].get_text())

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all("div", class_="article-main")
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_abc_es(t_id, soup):
    '''
    Given the soup (html) of a new from the webpage of 'abc_es' returns a list of
    fields to store the new's info in NewsML-G2 format (xml)
    '''

    news_author = format_string(soup.find('span', class_='autor').find('a', class_='nombre').get_text())
    news_provider = 'ABC.es'
    news_creation_datetime = format_string(soup.find('span', class_='fecha').find('time')['datetime'])
    news_uri = soup.find("link", {'rel': 'canonical'})['href']

    news_title = format_string(soup.find('span', class_='titular').get_text())
    news_headline = format_string(soup.find('h2', class_='subtitulo').get_text())

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('span', class_='cuerpo-texto')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_elmundoes(t_id, soup):
    '''
    Given the soup (html) of a new from the webpage of 'abc_es' returns a list of
    fields to store the new's info in NewsML-G2 format (xml)
    '''

    news_author = soup.find('div', class_='ue-c-article__byline-name').get_text()
    news_provider = 'EL MUNDO'
    news_creation_datetime = soup.find('meta', {'name': 'date'})['content']
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1').get_text()
    news_headline = soup.find('p', class_='ue-c-article__standfirst').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', {'data-section': 'articleBody'})
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_elperiodico(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'el periodico' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('meta', {'name': 'author'})['content']
    news_provider = 'El periodico'
    news_creation_datetime = soup.find('meta', {'property': 'article:published_time'}).get('content')
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1', class_='title').get_text()
    news_headline = soup.find('h2', class_='subtitle').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='ep-detail-body')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_informativost5(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'el periodico' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = 'Not specified'
    continue_ = True
    for author_field in soup.find_all('span'):
        try:
            if 'authorComponent__gray-1sqs' in author_field.get('class')[0] and continue_:
                news_author = author_field.get_text()
                continue_ = False
        except:
            pass
    news_provider = 'Informativos T5'
    news_creation_datetime = soup.find('time').get('datetime')
    news_uri = soup.find('link', {'rel': 'canonical'}).get('href')

    news_title = soup.find('h1').get_text()
    news_headline = " ".join([element.get_text() for element in soup.find_all('h2')])

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='article__paragraph-lSRh embeddedBodyItem__container_list-Etoy')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_La_SER(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'Cadena SER' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('div', class_='autor').get_text()
    news_provider = 'Cadena SER'
    news_creation_datetime = soup.find('time').get('datetime')
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1').get_text()
    news_headline = soup.find('h2').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='cuerpo')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_larazon_es(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'La razon' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('div', class_="byline__autor-wrapper first-author").get_text()
    news_provider = 'La razon'
    news_creation_datetime = soup.find('time').get('datetime')
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1').get_text()
    news_headline = soup.find('h2').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='article__body-container')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_laVanguardia(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'La razon' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('div', class_='author-name').get_text()
    news_provider = 'La vanguardia'
    news_creation_datetime = soup.find('time').get('datetime')
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1', class_='title').get_text()
    news_headline = ". ".join([elem.get_text() for elem in soup.find_all('h2', class_='epigraph')])

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='article-modules')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))
    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_okdiario(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'La razon' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('li', class_='author-name').get_text()
    news_provider = 'OKDIARIO'
    try:
        news_creation_datetime = datetime.strptime(soup.find('time', class_='date')['datetime'],
                                                   '%Y-%m-%d %H:%M').strftime("%Y-%m-%dT%H:%M:%S+02:00")
    except:
        news_creation_datetime = 'Not found'
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1').get_text()
    news_headline = soup.find('h2').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='entry-content')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            if part.get('class') is None and part.find('span') is None: paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))
    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_rtve(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'La razon' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('span', {'itemprop': 'author'}).get_text()
    news_provider = 'rtve'
    news_creation_datetime = soup.find('time')['datetime']
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('span', class_='maintitle').get_text()
    news_headline = ". ".join([elem.get_text() for elem in soup.find_all('div', class_='summary')])

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', {'itemprop': 'articleBody'})
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))
    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article


def obtain_information_sextaNoticias(t_id, soup):
    # Given the soup (html) of a new from the webpage of 'La razon' returns a list of
    # fields to store the new's info in NewsML-G2 format (xml)

    news_author = soup.find('div', class_='article-author__name').get_text()
    news_provider = 'La sexta'
    news_creation_datetime = soup.find('time', class_='article__time')['datetime']
    news_uri = soup.find('link', {'rel': 'canonical'})['href']

    news_title = soup.find('h1', class_='title-new').get_text()
    news_headline = soup.find('sumary', class_='entradilla').get_text()

    news_guid = "urn:newsml:{}:{}:{}".format(news_provider, datetime.now().strftime("%Y%m%d"), t_id)

    text = soup.find_all('div', class_='articleBody')
    paragraphs = []
    for i in np.arange(0, len(text)):
        for part in text[i].find_all("p"):
            paragraphs.append(part.get_text())

    news_article = format_string(" ".join(paragraphs))

    return news_author, news_provider, news_creation_datetime, news_uri, news_title, news_headline, news_guid, news_article
