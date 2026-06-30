from rich.table import Table
from rich.console import Console
from rich import box


def display_detect_result(result):
    
    algorithms = ", ".join(result["algorithms"])
    length = str(result["length"])

    display_data = {
        "Possible Algorithm(s)": algorithms,
        "Hash Length": length,
    }

    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Property") 
    table.add_column("Value") 

    for property_name, value in display_data.items():
        table.add_row(property_name, value)

    console = Console()
    console.print(table) 