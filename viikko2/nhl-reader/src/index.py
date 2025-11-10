from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()

    season = input("Season (esim. 2024-25): ")
    nationality = input("Nationality (esim. FIN): ")

    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality, season)

    table = Table(title=f"Season {season} playrs from {nationality}")

    table.add_column("Released", justify="left", style="cyan")
    table.add_column("teams", justify="left", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="yellow")

    for player in players:
        table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points()))

    console.print(table)

if __name__ == "__main__":
    main()
