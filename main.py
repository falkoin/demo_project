from typing import Annotated
import typer

app = typer.Typer()

def say_reverse(name: str) -> str:
    name_reverse = name[::-1]
    return f"Hi, {name_reverse}! You are awesome!"

def say_hi(name: str) -> str:
    return f"Hi, {name}! You are awesome!"


@app.command()
def greet(name: Annotated[str, typer.Argument()]):
    print(say_hi(name))

@app.command()
def teerg(name: Annotated[str, typer.Argument()]):
    print(say_reverse(name))

if __name__ == "__main__":
    app()
