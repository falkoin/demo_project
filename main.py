from typing import Annotated
import typer

app = typer.Typer()


def say_hi(name: str) -> str:
    return f"Hi, {name}! You are awesome!"


@app.command()
def greet(name: Annotated[str, typer.Argument()]):
    print(say_hi(name))


if __name__ == "__main__":
    app()
