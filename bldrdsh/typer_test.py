from datetime import datetime

import typer


def typer_test(
    launch_date: datetime = typer.Argument(
        ..., formats=["%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%d/%m/%Y"]
    )
):
    typer.echo(f"Launch will be at: {launch_date}")


if __name__ == "__main__":
    typer.run(typer_test)