"""CLI entry point for food automation system."""

import sys
from pathlib import Path

import click


@click.command()
@click.argument("photo_path", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output",
    "-o",
    type=click.Path(path_type=Path),
    help="Output file for JSON results (default: stdout)",
)
def main(photo_path: Path, output: Path | None) -> None:
    """Analyze a fridge photo and return structured inventory data."""
    click.echo(f"Processing photo: {photo_path}")

    # TODO: Implement photo analysis
    # - Load and validate image
    # - Call AI service
    # - Parse response
    # - Output structured JSON

    click.echo("Photo analysis not yet implemented", err=True)
    sys.exit(1)


if __name__ == "__main__":
    main()
