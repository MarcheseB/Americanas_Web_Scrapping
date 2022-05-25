from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    print('Habilidade a ser removida:')
    unfamiliar_skill = input('>')
    print(f"Filtrando {unfamiliar_skill}")
    html_text = requests.get('https://www.99freelas.com.br/projects?q=javascript').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='with-flag result-item')
    for index, job in enumerate(jobs):
        job_name = job.find('h1', class_='title').text
        skills = job.find('p', class_="item-text habilidades").text.replace('\n', ' ')
        publish_date = job.find('b', class_="datetime-restante")
        if unfamiliar_skill not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"Trabalho: {job_name.strip()}\n")
                f.write(f'Habilidades requeridas: {skills.strip()}\n')
            print(f"File {index} saved")
if __name__ == '__main__':
    while True:
        find_jobs()
        waiting_time = 10
        print(f"Waiting {waiting_time} minutes...")
        time.sleep(waiting_time*60)