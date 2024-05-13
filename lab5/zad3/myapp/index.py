import random
import string
import pyperclip
import click

@click.command()
@click.option('--length', default=12, help='Długość hasła.')
@click.option('--letters', is_flag=True, help='Włącz znaki literowe.')
@click.option('--numbers', is_flag=True, help='Włącz cyfry.')
@click.option('--special', is_flag=True, help='Włącz znaki specjalne.')
def generate_password(length, letters, numbers, special):
    """Generuje losowe hasło."""
    characters = ''
    if letters:
        characters += string.ascii_letters
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    if not characters:
        click.echo('Musisz włączyć przynajmniej jeden rodzaj znaków.')
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    click.echo('Wygenerowane hasło: {}'.format(password))
    click.echo('Skopiowano do schowka.')

if __name__ == '__main__':
    print("Cześć, działam.")
    generate_password()
