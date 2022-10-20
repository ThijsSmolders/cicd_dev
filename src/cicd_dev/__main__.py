"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Cicd_Dev."""


if __name__ == "__main__":
    main(prog_name="cicd_dev")  # pragma: no cover
