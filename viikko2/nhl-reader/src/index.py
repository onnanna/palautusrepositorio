from rich.console import Console
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def get_inputs():
    season = input("Season (esim. 2024-25): ")
    nationality = input("Nationality (esim. FIN): ")
    return season, nationality

def create_table(players, season, nationality):

    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", justify="left", style="cyan")
    table.add_column("teams", justify="left", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="yellow")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points())
                 )
    return table

def main():
    console = Console()
    season, nationality = get_inputs()

    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality, season)

    table = create_table(players, season, nationality)
    console.print(table)

if __name__ == "__main__":
    main()
