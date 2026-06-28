from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from core.verify_hash import verify_hash

def display_verification_result(verification_result) :

    status = "VERIFIED" if verification_result["match"] else "NOT VERIFIED"
    algorithm = verification_result["algorithm"] if verification_result["algorithm"] else "NOT FOUND" 


    display_data = {
        "Status": status,
        "Algorithm": algorithm,
    }

    table = Table(show_header=True, header_style="bold", show_lines=False, box=box.SIMPLE_HEAD)
    table.add_column("Property") 
    table.add_column("Value") 


    for property_name, value in display_data.items() :
        table.add_row(property_name, value) 
   
        
    console = Console()
    console.print(table) 
