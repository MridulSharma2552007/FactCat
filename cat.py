import requests
import time
from rich.console import Console
console = Console()
def fetchFacts():
    Url="https://catfact.ninja/fact"
    try:
        response=requests.get(Url)
        data=response.json()

        return data['fact']
    except Exception as e:
        print(f"Error{e}")
def main():
    console.print("[bold red]🐱 Welcome To fact kitty [/bold red]")
    while True:
        fetchedData=fetchFacts()
        console.print(f"🐾[bold cyan]Fact:[/bold cyan]{fetchedData} ")
        time.sleep(2)
        console.print("[yellow]Want more (y/n)[/yellow]")
        ask=input()
        if ask.lower() != 'y':
            console.print("👋[red]Bye Bye!![/red]")       
            break
if __name__=="__main__":
    main()
