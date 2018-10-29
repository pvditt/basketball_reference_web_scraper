from unittest import TestCase

from basketball_reference_web_scraper.data import Team, Position
from basketball_reference_web_scraper.parsers import player_season_totals


class TestPlayerSeasonTotals(TestCase):
    def setUp(self):
        with open('./NBA_2001_totals.html', 'r') as season_2001_totals_html:
            self.season_2001_totals = season_2001_totals_html.read()

        with open('./NBA_2018_totals.html', 'r') as season_2018_totals_html:
            self.season_2018_totals = season_2018_totals_html.read()

    def test_2001_player_season_totals(self):
        parsed_box_score = player_season_totals.parse_player_season_totals(self.season_2001_totals)
        self.assertEqual(len(parsed_box_score), 490)

        mahmoud_abdul_rauf = parsed_box_score[0]

        self.assertEqual(mahmoud_abdul_rauf["name"], "Mahmoud Abdul-Rauf")
        self.assertEqual(mahmoud_abdul_rauf["position"], Position.POINT_GUARD)
        self.assertEqual(mahmoud_abdul_rauf["team"], Team.VANCOUVER_GRIZZLIES)
        self.assertEqual(mahmoud_abdul_rauf["games_played"], 41)
        self.assertEqual(mahmoud_abdul_rauf["games_started"], 0)
        self.assertEqual(mahmoud_abdul_rauf["minutes_played"], 486)
        self.assertEqual(mahmoud_abdul_rauf["made_field_goals"], 120)
        self.assertEqual(mahmoud_abdul_rauf["attempted_field_goals"], 246)
        self.assertEqual(mahmoud_abdul_rauf["made_three_point_field_goals"], 4)
        self.assertEqual(mahmoud_abdul_rauf["attempted_three_point_field_goals"], 14)
        self.assertEqual(mahmoud_abdul_rauf["made_free_throws"], 22)
        self.assertEqual(mahmoud_abdul_rauf["attempted_free_throws"], 29)
        self.assertEqual(mahmoud_abdul_rauf["offensive_rebounds"], 5)
        self.assertEqual(mahmoud_abdul_rauf["defensive_rebounds"], 20)
        self.assertEqual(mahmoud_abdul_rauf["assists"], 76)
        self.assertEqual(mahmoud_abdul_rauf["steals"], 9)
        self.assertEqual(mahmoud_abdul_rauf["blocks"], 1)
        self.assertEqual(mahmoud_abdul_rauf["turnovers"], 26)
        self.assertEqual(mahmoud_abdul_rauf["personal_fouls"], 50)

    def test_2018_player_season_totals(self):
        parsed_box_score = player_season_totals.parse_player_season_totals(self.season_2018_totals)
        self.assertEqual(len(parsed_box_score), 605)

        alex_abrines = parsed_box_score[0]

        self.assertEqual(alex_abrines["name"], "Alex Abrines")
        self.assertEqual(alex_abrines["position"], Position.SHOOTING_GUARD)
        self.assertEqual(alex_abrines["team"], Team.OKLAHOMA_CITY_THUNDER)
        self.assertEqual(alex_abrines["games_played"], 75)
        self.assertEqual(alex_abrines["games_started"], 8)
        self.assertEqual(alex_abrines["minutes_played"], 1134)
        self.assertEqual(alex_abrines["made_field_goals"], 115)
        self.assertEqual(alex_abrines["attempted_field_goals"], 291)
        self.assertEqual(alex_abrines["made_three_point_field_goals"], 84)
        self.assertEqual(alex_abrines["attempted_three_point_field_goals"], 221)
        self.assertEqual(alex_abrines["made_free_throws"], 39)
        self.assertEqual(alex_abrines["attempted_free_throws"], 46)
        self.assertEqual(alex_abrines["offensive_rebounds"], 26)
        self.assertEqual(alex_abrines["defensive_rebounds"], 88)
        self.assertEqual(alex_abrines["assists"], 28)
        self.assertEqual(alex_abrines["steals"], 38)
        self.assertEqual(alex_abrines["blocks"], 8)
        self.assertEqual(alex_abrines["turnovers"], 25)
        self.assertEqual(alex_abrines["personal_fouls"], 124)

    def test_2018_omer_asik_player_season_totals(self):
        parsed_box_score = player_season_totals.parse_player_season_totals(self.season_2018_totals)

        new_orleans_pelicans_omer_asik = parsed_box_score[22]

        self.assertEqual(new_orleans_pelicans_omer_asik["name"], "Omer Asik")
        self.assertEqual(new_orleans_pelicans_omer_asik["position"], Position.CENTER)
        self.assertEqual(new_orleans_pelicans_omer_asik["team"], Team.NEW_ORLEANS_PELICANS)
        self.assertEqual(new_orleans_pelicans_omer_asik["games_played"], 14)
        self.assertEqual(new_orleans_pelicans_omer_asik["games_started"], 0)
        self.assertEqual(new_orleans_pelicans_omer_asik["minutes_played"], 121)
        self.assertEqual(new_orleans_pelicans_omer_asik["made_field_goals"], 7)
        self.assertEqual(new_orleans_pelicans_omer_asik["attempted_field_goals"], 16)
        self.assertEqual(new_orleans_pelicans_omer_asik["made_three_point_field_goals"], 0)
        self.assertEqual(new_orleans_pelicans_omer_asik["attempted_three_point_field_goals"], 0)
        self.assertEqual(new_orleans_pelicans_omer_asik["made_free_throws"], 4)
        self.assertEqual(new_orleans_pelicans_omer_asik["attempted_free_throws"], 12)
        self.assertEqual(new_orleans_pelicans_omer_asik["offensive_rebounds"], 7)
        self.assertEqual(new_orleans_pelicans_omer_asik["defensive_rebounds"], 30)
        self.assertEqual(new_orleans_pelicans_omer_asik["assists"], 2)
        self.assertEqual(new_orleans_pelicans_omer_asik["steals"], 1)
        self.assertEqual(new_orleans_pelicans_omer_asik["blocks"], 2)
        self.assertEqual(new_orleans_pelicans_omer_asik["turnovers"], 5)
        self.assertEqual(new_orleans_pelicans_omer_asik["personal_fouls"], 14)

        chicago_omer_asik = parsed_box_score[23]

        self.assertEqual(chicago_omer_asik["name"], "Omer Asik")
        self.assertEqual(chicago_omer_asik["position"], Position.CENTER)
        self.assertEqual(chicago_omer_asik["team"], Team.CHICAGO_BULLS)
        self.assertEqual(chicago_omer_asik["games_played"], 4)
        self.assertEqual(chicago_omer_asik["games_started"], 0)
        self.assertEqual(chicago_omer_asik["minutes_played"], 61)
        self.assertEqual(chicago_omer_asik["made_field_goals"], 2)
        self.assertEqual(chicago_omer_asik["attempted_field_goals"], 6)
        self.assertEqual(chicago_omer_asik["made_three_point_field_goals"], 0)
        self.assertEqual(chicago_omer_asik["attempted_three_point_field_goals"], 0)
        self.assertEqual(chicago_omer_asik["made_free_throws"], 0)
        self.assertEqual(chicago_omer_asik["attempted_free_throws"], 1)
        self.assertEqual(chicago_omer_asik["offensive_rebounds"], 2)
        self.assertEqual(chicago_omer_asik["defensive_rebounds"], 8)
        self.assertEqual(chicago_omer_asik["assists"], 1)
        self.assertEqual(chicago_omer_asik["steals"], 1)
        self.assertEqual(chicago_omer_asik["blocks"], 2)
        self.assertEqual(chicago_omer_asik["turnovers"], 4)
        self.assertEqual(chicago_omer_asik["personal_fouls"], 6)
