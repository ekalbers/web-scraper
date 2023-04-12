from bs4 import BeautifulSoup
import requests


def get_citations_needed_count(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    text = soup.select('p')
    counter = 0
    for x in text:
        if x.sup:
            if x.sup.i:
                if x.sup.i.a:
                    if x.sup.i.a.span.text == 'citation needed':
                        counter += 1

    return counter


def get_citations_needed_report(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    text = soup.select('p')
    return_string = ''
    for x in text:
        if x.sup:
            if x.sup.i:
                if x.sup.i.a:
                    if x.sup.i.a.span.text == 'citation needed':
                        return_string += f'{x.text}\n'

    return return_string




def main():
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_Mexico'))
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico'))


if __name__ == '__main__':
    main()
