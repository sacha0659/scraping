from turtle import title
from numpy import array
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests_cache

requests_cache.install_cache('demo_cache')

def get_page(url):
    page = requests.get(url).text
    return BeautifulSoup(page, 'html.parser')

def get_stats(page_data):
    data_stats = []
    array = []

    title = page_data.find('h2').text
    data_stats.append(title)

    table = page_data.find('tbody')
    for row in table.find_all('tr'):
        player = {
          'joueur': {
            'nom': row.find('th', {"data-stat" : "player"}).text,
            'nation': row.find('td', {"data-stat" : "nationality"}).text,
            'pos': row.find('td', {"data-stat" : "position"}).text,
            'age': row.find('td', {"data-stat" : "age"}).text,
          },
          'tempsDeJeu': {
            'mj': row.find('td', {"data-stat" : "games"}).text,
            'titulaire': row.find('td', {"data-stat" : "games_starts"}).text,
            'min': row.find('td', {"data-stat" : "minutes"}).text,
            '90': row.find('td', {"data-stat" : "minutes_90s"}).text,
          },
          'performance': {
            'buts': row.find('td', {"data-stat" : "goals"}).text,
            'pd': row.find('td', {"data-stat" : "assists"}).text,
            'b-penm': row.find('td', {"data-stat" : "goals_pens"}).text,
            'penm': row.find('td', {"data-stat" : "pens_made"}).text,
            'pent': row.find('td', {"data-stat" : "pens_att"}).text,
            'cj': row.find('td', {"data-stat" : "cards_yellow"}).text,
            'cr': row.find('td', {"data-stat" : "cards_red"}).text,
          },
          'par90Minutes-1': {
            'buts': row.find('td', {"data-stat" : "goals_per90"}).text,
            'pd': row.find('td', {"data-stat" : "assists_per90"}).text,
            'b+pd': row.find('td', {"data-stat" : "goals_assists_per90"}).text,
            'b-penm': row.find('td', {"data-stat" : "goals_pens_per90"}).text,
            'b+pd-penm': row.find('td', {"data-stat" : "goals_assists_pens_per90"}).text,
          },
          'attendu': {
            'xg': row.find('td', {"data-stat" : "xg"}).text,
            'npxg': row.find('td', {"data-stat" : "npxg"}).text,
            'xa': row.find('td', {"data-stat" : "xa"}).text,
            'npgxg+xa': row.find('td', {"data-stat" : "npxg_xa"}).text,
          },
          'par90Minutes-2': {
            'xg': row.find('td', {"data-stat" : "xg_per90"}).text,
            'xa': row.find('td', {"data-stat" : "xa_per90"}).text,
            'xg+xa': row.find('td', {"data-stat" : "xg_xa_per90"}).text,
            'npxg': row.find('td', {"data-stat" : "npxg_per90"}).text,
            'npxg+xa': row.find('td', {"data-stat" : "npxg_xa_per90"}).text,
          },
          'matchs': f"https://fbref.com{row.find('td', {'data-stat' : 'matches'}).find('a')['href']}",
        }
        array.append(player)
    data_stats.append(array)
    return data_stats


def get_calendars(page_data):
    data_calendar= []
    array = []

    title = page_data.find_all('h2')[1].text
    data_calendar.append(title)
    table = page_data.find_all('tbody')[1]
    for row in table.find_all('tr'):
      match = {
        'date': row.find('th', {"data-stat" : "date"}).text,
        'heure': row.find('td', {"data-stat" : "time"}).text,
        'comp': row.find('td', {"data-stat" : "comp"}).text,
        'tour': row.find('td', {"data-stat" : "round"}).text,
        'jour': row.find('td', {"data-stat" : "dayofweek"}).text,
        'tribune': row.find('td', {"data-stat" : "venue"}).text,
        'résultat': row.find('td', {"data-stat" : "result"}).text,
        'BM': row.find('td', {"data-stat" : "goals_for"}).text,
        'BE': row.find('td', {"data-stat" : "goals_against"}).text,
        'adversaire': row.find('td', {"data-stat" : "opponent"}).text,
        'xG': row.find('td', {"data-stat" : "xg_for"}).text,
        'xGA': row.find('td', {"data-stat" : "xg_against"}).text,
        'poss': row.find('td', {"data-stat" : "possession"}).text,
        'affluence': row.find('td', {"data-stat" : "attendance"}).text,
        'capitaine': row.find('td', {"data-stat" : "captain"}).text,
        'formation': row.find('td', {"data-stat" : "formation"}).text,
        'arbitre': row.find('td', {"data-stat" : "referee"}).text,
        'rapport': row.find('td', {"data-stat" : "match_report"}).text
      }
      array.append(match)
      data_calendar.append(array)
    return data_calendar

def get_tirs(page_data):
  data_tirs = []
  array = []
  title = page_data.find_all('h2')[4].text
  data_tirs.append(title)
  table = page_data.find_all('tbody')[4]
  for row in table.find_all('tr'):
    players = {
      'Joueur': row.find('th', {"data-stat" : "player"}).text,
      'Nation': row.find('td', {"data-stat" : "nationality"}).text,
      'Pos': row.find('td', {"data-stat" : "position"}).text,
      'Age': row.find('td', {"data-stat" : "age"}).text,
      '90': row.find('td', {"data-stat" : "minutes_90s"}).text,
      'Standard':{
        'Buts': row.find('td', {"data-stat" : "goals"}).text,
        'Tirs': row.find('td', {"data-stat" : "shots_total"}).text,
        'Tc': row.find('td', {"data-stat" : "shots_on_target"}).text,
        'TC % ': row.find('td', {"data-stat" : "shots_on_target_pct"}).text,
        'TC/90': row.find('td', {"data-stat" : "shots_on_target_per90"}).text,
        'B/TIR': row.find('td', {"data-stat" : "goals_per_shot"}).text,
        'B/TC': row.find('td', {"data-stat" : "goals_per_shot_on_target"}).text,
        'Dist': row.find('td', {"data-stat" : "average_shot_distance"}).text,
        'CF': row.find('td', {"data-stat" : "shots_free_kicks"}).text,
        'PénM': row.find('td', {"data-stat" : "pens_made"}).text,
        'PénT': row.find('td', {"data-stat" : "pens_att"}).text,
      },
       'Attendu':{
         'xg': row.find('td', {"data-stat" : "xg"}).text,
         'npxG': row.find('td', {"data-stat" : "npxg"}).text,
         'npxg/sh': row.find('td', {"data-stat" : "npxg_per_shot"}).text,
         'G-xg': row.find('td', {"data-stat" : "xg_net"}).text,
         'np': row.find('td', {"data-stat" : "npxg_net"}).text,
       }, 
       'Match': row.find('td', {"data-stat" : "matches"})

    }
    

    array.append(players)
  data_tirs.append(array)
  return data_tirs 


if __name__ == "__main__":
    path = r'https://fbref.com/fr/equipes/361ca564/Statistiques-Tottenham-Hotspur'
    page_data = get_page(path)

    data_stats = get_stats(page_data)
    data_calendars = get_calendars(page_data)
    data_tirs = get_tirs(page_data)

    data_export = []
    data_export.append(data_stats)
    data_export.append(data_calendars)
    data_export.append(data_tirs)
print(data_export)
