from enum import Enum


class Location(Enum):
    HOME = "HOME"
    AWAY = "AWAY"


class Outcome(Enum):
    WIN = "WIN"
    LOSS = "LOSS"


class Team(Enum):
    ATLANTA_HAWKS = "ATLANTA HAWKS"
    BOSTON_CELTICS = "BOSTON CELTICS"
    BROOKLYN_NETS = "BROOKLYN NETS"
    CHARLOTTE_HORNETS = "CHARLOTTE HORNETS"
    CHICAGO_BULLS = "CHICAGO BULLS"
    CLEVELAND_CAVALIERS = "CLEVELAND CAVALIERS"
    DALLAS_MAVERICKS = "DALLAS MAVERICKS"
    DENVER_NUGGETS = "DENVER NUGGETS"
    DETROIT_PISTONS = "DETROIT PISTONS"
    GOLDEN_STATE_WARRIORS = "GOLDEN STATE WARRIORS"
    HOUSTON_ROCKETS = "HOUSTON ROCKETS"
    INDIANA_PACERS = "INDIANA PACERS"
    LOS_ANGELES_CLIPPERS = "LOS ANGELES CLIPPERS"
    LOS_ANGELES_LAKERS = "LOS ANGELES LAKERS"
    MEMPHIS_GRIZZLIES = "MEMPHIS GRIZZLIES"
    MIAMI_HEAT = "MIAMI HEAT"
    MILWAUKEE_BUCKS = "MILWAUKEE BUCKS"
    MINNESOTA_TIMBERWOLVES = "MINNESOTA TIMBERWOLVES"
    NEW_ORLEANS_PELICANS = "NEW ORLEANS PELICANS"
    NEW_YORK_KNICKS = "NEW YORK KNICKS"
    OKLAHOMA_CITY_THUNDER = "OKLAHOMA CITY THUNDER"
    ORLANDO_MAGIC = "ORLANDO MAGIC"
    PHILADELPHIA_76ERS = "PHILADELPHIA 76ERS"
    PHOENIX_SUNS = "PHOENIX SUNS"
    PORTLAND_TRAIL_BLAZERS = "PORTLAND TRAIL BLAZERS"
    SACRAMENTO_KINGS = "SACRAMENTO KINGS"
    SAN_ANTONIO_SPURS = "SAN ANTONIO SPURS"
    TORONTO_RAPTORS = "TORONTO RAPTORS"
    UTAH_JAZZ = "UTAH JAZZ"
    WASHINGTON_WIZARDS = "WASHINGTON WIZARDS"

    # DEPRECATED TEAMS
    CHARLOTTE_BOBCATS = "CHARLOTTE BOBCATS"
    NEW_JERSEY_NETS = "NEW JERSEY NETS"
    NEW_ORLEANS_HORNETS = "NEW ORLEANS HORNETS"
    NEW_ORLEANS_OKLAHOMA_CITY_HORNETS = "NEW ORLEANS/OKLAHOMA CITY HORNETS"
    SEATTLE_SUPERSONICS = "SEATTLE SUPERSONICS"
    VANCOUVER_GRIZZLIES = "VANCOUVER GRIZZLIES"


class OutputType(Enum):
    JSON = "JSON"
    CSV = "CSV"


class OutputWriteOption(Enum):
    WRITE = "w"
    CREATE_AND_WRITE = "w+"
    APPEND = "a"
    APPEND_AND_WRITE = "a+"


class Position(Enum):
    POINT_GUARD = "POINT GUARD"
    SHOOTING_GUARD = "SHOOTING GUARD"
    SMALL_FORWARD = "SMALL FORWARD"
    POWER_FORWARD = "POWER FORWARD"
    CENTER = "CENTER"
    FORWARD = "FORWARD"
    GUARD = "GUARD"


class PeriodType(Enum):
    QUARTER = "QUARTER"
    OVERTIME = "OVERTIME"


class League(Enum):
    NATIONAL_BASKETBALL_ASSOCIATION = "NATIONAL_BASKETBALL_ASSOCIATION"
    AMERICAN_BASKETBALL_ASSOCIATION = "AMERICAN_BASKETBALL_ASSOCIATION"
    BASKETBALL_ASSOCIATION_OF_AMERICA = "BASKETBALL_ASSOCIATION_OF_AMERICA"


class Conference(Enum):
    EASTERN = "EASTERN"
    WESTERN = "WESTERN"


class Division(Enum):
    ATLANTIC = "ATLANTIC"
    CENTRAL = "CENTRAL"
    MIDWEST = "MIDWEST"
    NORTHWEST = "NORTHWEST"
    PACIFIC = "PACIFIC"
    SOUTHEAST = "SOUTHEAST"
    SOUTHWEST = "SOUTHWEST"


DIVISIONS_TO_CONFERENCES = {
    Division.ATLANTIC: Conference.EASTERN,
    Division.CENTRAL: Conference.EASTERN,
    Division.SOUTHEAST: Conference.EASTERN,
    Division.MIDWEST: Conference.WESTERN,
    Division.PACIFIC: Conference.WESTERN,
    Division.SOUTHWEST: Conference.WESTERN,
}


TEAM_ABBREVIATIONS_TO_TEAM = {
    'ATL': Team.ATLANTA_HAWKS,
    'BOS': Team.BOSTON_CELTICS,
    'BRK': Team.BROOKLYN_NETS,
    'CHI': Team.CHICAGO_BULLS,
    'CHO': Team.CHARLOTTE_HORNETS,
    'CLE': Team.CLEVELAND_CAVALIERS,
    'DAL': Team.DALLAS_MAVERICKS,
    'DEN': Team.DENVER_NUGGETS,
    'DET': Team.DETROIT_PISTONS,
    'GSW': Team.GOLDEN_STATE_WARRIORS,
    'HOU': Team.HOUSTON_ROCKETS,
    'IND': Team.INDIANA_PACERS,
    'LAC': Team.LOS_ANGELES_CLIPPERS,
    'LAL': Team.LOS_ANGELES_LAKERS,
    'MEM': Team.MEMPHIS_GRIZZLIES,
    'MIA': Team.MIAMI_HEAT,
    'MIL': Team.MILWAUKEE_BUCKS,
    'MIN': Team.MINNESOTA_TIMBERWOLVES,
    'NOP': Team.NEW_ORLEANS_PELICANS,
    'NYK': Team.NEW_YORK_KNICKS,
    'OKC': Team.OKLAHOMA_CITY_THUNDER,
    'ORL': Team.ORLANDO_MAGIC,
    'PHI': Team.PHILADELPHIA_76ERS,
    'PHO': Team.PHOENIX_SUNS,
    'POR': Team.PORTLAND_TRAIL_BLAZERS,
    'SAC': Team.SACRAMENTO_KINGS,
    'SAS': Team.SAN_ANTONIO_SPURS,
    'TOR': Team.TORONTO_RAPTORS,
    'UTA': Team.UTAH_JAZZ,
    'WAS': Team.WASHINGTON_WIZARDS,

    # DEPRECATED TEAMS
    'NJN': Team.NEW_JERSEY_NETS,
    'NOH': Team.NEW_ORLEANS_HORNETS,
    'NOK': Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
    'CHA': Team.CHARLOTTE_BOBCATS,
    'CHH': Team.CHARLOTTE_HORNETS,
    'SEA': Team.SEATTLE_SUPERSONICS,
    'VAN': Team.VANCOUVER_GRIZZLIES,
}

TEAM_TO_TEAM_ABBREVIATION = {v: k for k, v in TEAM_ABBREVIATIONS_TO_TEAM.items()}
TEAM_TO_TEAM_ABBREVIATION[Team.CHARLOTTE_HORNETS] = "CHO"

TEAM_NAME_TO_TEAM = {
    "ATLANTA HAWKS": Team.ATLANTA_HAWKS,
    "BOSTON CELTICS": Team.BOSTON_CELTICS,
    "BROOKLYN NETS": Team.BROOKLYN_NETS,
    "CHARLOTTE HORNETS": Team.CHARLOTTE_HORNETS,
    "CHICAGO BULLS": Team.CHICAGO_BULLS,
    "CLEVELAND CAVALIERS": Team.CLEVELAND_CAVALIERS,
    "DALLAS MAVERICKS": Team.DALLAS_MAVERICKS,
    "DENVER NUGGETS": Team.DENVER_NUGGETS,
    "DETROIT PISTONS": Team.DETROIT_PISTONS,
    "GOLDEN STATE WARRIORS": Team.GOLDEN_STATE_WARRIORS,
    "HOUSTON ROCKETS": Team.HOUSTON_ROCKETS,
    "INDIANA PACERS": Team.INDIANA_PACERS,
    "LOS ANGELES CLIPPERS": Team.LOS_ANGELES_CLIPPERS,
    "LOS ANGELES LAKERS": Team.LOS_ANGELES_LAKERS,
    "MEMPHIS GRIZZLIES": Team.MEMPHIS_GRIZZLIES,
    "MIAMI HEAT": Team.MIAMI_HEAT,
    "MILWAUKEE BUCKS": Team.MILWAUKEE_BUCKS,
    "MINNESOTA TIMBERWOLVES": Team.MINNESOTA_TIMBERWOLVES,
    "NEW ORLEANS PELICANS": Team.NEW_ORLEANS_PELICANS,
    "NEW YORK KNICKS": Team.NEW_YORK_KNICKS,
    "OKLAHOMA CITY THUNDER": Team.OKLAHOMA_CITY_THUNDER,
    "ORLANDO MAGIC": Team.ORLANDO_MAGIC,
    "PHILADELPHIA 76ERS": Team.PHILADELPHIA_76ERS,
    "PHOENIX SUNS": Team.PHOENIX_SUNS,
    "PORTLAND TRAIL BLAZERS": Team.PORTLAND_TRAIL_BLAZERS,
    "SACRAMENTO KINGS": Team.SACRAMENTO_KINGS,
    "SAN ANTONIO SPURS": Team.SAN_ANTONIO_SPURS,
    "TORONTO RAPTORS": Team.TORONTO_RAPTORS,
    "UTAH JAZZ": Team.UTAH_JAZZ,
    "WASHINGTON WIZARDS": Team.WASHINGTON_WIZARDS,

    # DEPRECATED TEAMS
    "CHARLOTTE BOBCATS": Team.CHARLOTTE_BOBCATS,
    "NEW JERSEY NETS": Team.NEW_JERSEY_NETS,
    "NEW ORLEANS HORNETS": Team.NEW_ORLEANS_HORNETS,
    "NEW ORLEANS/OKLAHOMA CITY HORNETS": Team.NEW_ORLEANS_OKLAHOMA_CITY_HORNETS,
    "SEATTLE SUPERSONICS": Team.SEATTLE_SUPERSONICS,
    "VANCOUVER GRIZZLIES": Team.VANCOUVER_GRIZZLIES,
}

POSITION_ABBREVIATIONS_TO_POSITION = {
    "PG": Position.POINT_GUARD,
    "SG": Position.SHOOTING_GUARD,
    "SF": Position.SMALL_FORWARD,
    "PF": Position.POWER_FORWARD,
    "C": Position.CENTER,
    "F": Position.FORWARD,
    "G": Position.GUARD,
}


LOCATION_ABBREVIATIONS_TO_POSITION = {
    "": Location.HOME,
    "@": Location.AWAY,
}


OUTCOME_ABBREVIATIONS_TO_OUTCOME = {
    "W": Outcome.WIN,
    "L": Outcome.LOSS,
}

LEAGUE_ABBREVIATIONS_TO_LEAGUE = {
    "NBA": League.NATIONAL_BASKETBALL_ASSOCIATION,
    "ABA": League.AMERICAN_BASKETBALL_ASSOCIATION,
    "BAA": League.BASKETBALL_ASSOCIATION_OF_AMERICA,
}


class TeamTotal:
    def __init__(self, team_abbreviation, totals):
        self.team_abbreviation = team_abbreviation
        self.totals = totals

    @property
    def minutes_played(self):
        return self.totals.minutes_played

    @property
    def made_field_goals(self):
        return self.totals.made_field_goals

    @property
    def attempted_field_goals(self):
        return self.totals.attempted_field_goals

    @property
    def field_goals_percentage(self):
        return self.totals.field_goals_percentage

    @property
    def made_three_point_field_goals(self):
        return self.totals.made_three_point_field_goals

    @property
    def attempted_three_point_field_goals(self):
        return self.totals.attempted_three_point_field_goals

    @property
    def three_point_field_goals_percentage(self):
        return self.totals.three_point_field_goals_percentage

    @property
    def made_free_throws(self):
        return self.totals.made_free_throws

    @property
    def attempted_free_throws(self):
        return self.totals.attempted_free_throws

    @property
    def free_throws_percentage(self):
        return self.totals.free_throws_percentage

    @property
    def offensive_rebounds(self):
        return self.totals.offensive_rebounds

    @property
    def defensive_rebounds(self):
        return self.totals.defensive_rebounds

    @property
    def assists(self):
        return self.totals.assists

    @property
    def steals(self):
        return self.totals.steals

    @property
    def blocks(self):
        return self.totals.blocks

    @property
    def turnovers(self):
        return self.totals.turnovers

    @property
    def personal_fouls(self):
        return self.totals.personal_fouls

    @property
    def points(self):
        return self.totals.points

    @property
    def date(self):
        return self.totals.date

    @property
    def outcome(self):
        return self.totals.outcome

    @property
    def opponent(self):
        return self.totals.opponent

    @property
    def total_rebounds(self):
        return self.totals.total_rebounds

    @property
    def opponent_points(self):
        return self.totals.opponent_points

    @property
    def opponent_field_goals(self):
        return self.totals.opponent_field_goals

    @property
    def opponent_field_goal_attempts(self):
        return self.totals.opponent_field_goal_attempts

    @property
    def opponent_field_goal_percentage(self):
        return self.totals.opponent_field_goal_percentage

    @property
    def opponent_three_point_field_goals(self):
        return self.totals.opponent_three_point_field_goals

    @property
    def opponent_three_point_field_goal_attempts(self):
        return self.totals.opponent_three_point_field_goal_attempts

    @property
    def opponent_free_throws(self):
        return self.totals.opponent_free_throws

    @property
    def opponent_free_throw_attempts(self):
        return self.totals.opponent_free_throw_attempts

    @property
    def opponent_free_throw_percentage(self):
        return self.totals.opponent_free_throw_percentage

    @property
    def opponent_offensive_rebounds(self):
        return self.totals.opponent_offensive_rebounds

    @property
    def opponent_total_rebounds(self):
        return self.totals.opponent_total_rebounds

    @property
    def opponent_assists(self):
        return self.totals.opponent_assists

    @property
    def opponent_steals(self):
        return self.totals.opponent_steals

    @property
    def opponent_blocks(self):
        return self.totals.opponent_blocks

    @property
    def opponent_turnovers(self):
        return self.totals.opponent_turnovers

    @property
    def opponent_personal_fouls(self):
        return self.totals.opponent_personal_fouls


class AdvancedTeamTotal:
    def __init__(self, team_abbreviation, totals):
        self.team_abbreviation = team_abbreviation
        self.totals = totals

    @property
    def playing_time(self):
        return self.totals.playing_time

    @property
    def true_shooting_percentage(self):
        return self.totals.true_shooting_percentage

    @property
    def effective_field_goal_percentage(self):
        return self.totals.effective_field_goal_percentage

    @property
    def attempted_three_point_field_goals_per_field_goal_percent(self):
        return self.totals.attempted_three_point_field_goals_per_field_goal_percent

    @property
    def attempted_free_throws_per_field_goal_percent(self):
        return self.totals.attempted_free_throws_per_field_goal_percent

    @property
    def offensive_rebound_percentage(self):
        return self.totals.offensive_rebound_percentage

    @property
    def defensive_rebound_percentage(self):
        return self.totals.defensive_rebound_percentage

    @property
    def total_rebound_percentage(self):
        return self.totals.total_rebound_percentage

    @property
    def assist_percentage(self):
        return self.totals.assist_percentage

    @property
    def steal_percentage(self):
        return self.totals.steal_percentage

    @property
    def block_percentage(self):
        return self.totals.block_percentage

    @property
    def turnover_percentage(self):
        return self.totals.turnover_percentage

    @property
    def offensive_rating(self):
        return self.totals.offensive_rating

    @property
    def defensive_rating(self):
        return self.totals.defensive_rating

    @property
    def pace(self):
        return self.totals.pace

    @property
    def free_throw_rate(self):
        return self.totals.free_throw_rate

    @property
    def opponent_effective_field_goal_rate(self):
        return self.totals.opponent_effective_field_goal_rate

    @property
    def opponent_turnover_rate(self):
        return self.totals.opponent_turnover_rate

    @property
    def opponent_free_throw_rate(self):
        return self.totals.opponent_free_throw_rate


class PlayerData:
    def __init__(self, name, resource_location, league_abbreviations):
        self.name = name
        self.resource_location = resource_location
        self.league_abbreviations = set(league_abbreviations)
