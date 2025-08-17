import click 
import time



    
@click.group()
def cli():
    """This script showcases different terminal UI helpers in Click."""
    pass


@cli.command()
def menu():
    menu = "main"
    while True:
        if menu == "main":
            click.echo(click.style(
        r"""
__        _______ _     ____ ___  __  __ _____   _____ ___  
\ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
  \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/ 
                                                            
 _____ ______   _                                           
| ____|__  / | | |                                          
|  _|   / /| | | |                                          
| |___ / /_| |_| |  _   _   _                               
|_____/____|\___/  (_) (_) (_)
      """,
        fg="white",
    ))
            time.sleep(1)
            click.echo("\n")
            click.echo(click.style("Select the following options:", fg="red", bg='white'))
            click.echo("  a: Add Password")
            click.echo("  r: Read Password")
            click.echo("  d: Delete Password")
            click.echo("  x: Delete All (Everything....)")
            click.echo("  q: quit")
            char = click.getchar()
            if char == "d":
                menu = "debug"
            elif char == "q":
                menu = "quit"
            else:
                click.echo("Invalid input")
        elif menu == "debug":
            click.echo("Debug menu")
            click.echo("  b: back")
            char = click.getchar()
            if char == "b":
                menu = "main"
            else:
                click.echo("Invalid input")
        elif menu == "quit":
            return

    