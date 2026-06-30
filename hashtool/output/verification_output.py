from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

def display_verification_result(verification_result) :

    status = "VERIFIED" if verification_result["match"] else "NOT VERIFIED"
    algorithm = verification_result["algorithm"] if verification_result["algorithm"] else "NOT FOUND" 


    display_data = {
        "Status": status,
        "Algorithm": algorithm,
    }

    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Property") 
    table.add_column("Value") 


    for property_name, value in display_data.items() :
        table.add_row(property_name, value) 
   
        
    console = Console()
    console.print(table) 
