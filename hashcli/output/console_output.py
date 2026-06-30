from rich.console import Console
from rich.table import Table
from rich import box


def display_hash_table(result) : 
    table = Table(title = "Hash Results", box=box.SIMPLE_HEAD)

    table.add_column("Algorithm", style="green")
    table.add_column("Hash", overflow="fold")

    for algorithm, hash_value in result.items() :
        table.add_row(algorithm, hash_value) 

    console = Console() 
    console.print(table) 

