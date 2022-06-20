import typer


def main(lastname: str = typer.Option(..., prompt=True)):
    aa = lastname
    typer.echo(f"Hello {lastname}")
    print("Your names is:", aa)


if __name__ == "__main__":
    typer.run(main)