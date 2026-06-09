from rich.console import Console
from rich.table import Table


def display_hash_table(result) : 
    table = Table(title = "Hash Results")

    table.add_column("Algorithm", style="green")
    table.add_column("Hash", overflow="fold")

    for algorithm, hash_value in result.items() :
        table.add_row(algorithm, hash_value) 

    console = Console()
    console.print(table)