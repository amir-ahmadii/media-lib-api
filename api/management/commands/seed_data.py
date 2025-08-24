import random
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import Book, Movie, Album

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=20, help='Number of items for each model')

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        Book.objects.all().delete()
        Movie.objects.all().delete()
        Album.objects.all().delete()

        fake = Faker()
        count = options['count']

        self.stdout.write(f'Creating {count} books...')
        for _ in range(count):
            Book.objects.create(
                title=fake.catch_phrase(),
                author=fake.name(),
                publication_year=random.randint(1800, 2023),
                genre=random.choice(['Science Fiction', 'Fantasy', 'Mystery']),
                isbn=fake.isbn13()
            )

        self.stdout.write(f'Creating {count} movies...')
        for _ in range(count):
            Movie.objects.create(
                title=' '.join(fake.words(nb=3)).title(),
                director=fake.name(),
                release_year=random.randint(1950, 2023),
                genre=random.choice(['Action', 'Drama', 'Sci-Fi']),
                rating=round(random.uniform(5.0, 10.0), 1)
            )

        self.stdout.write(f'Creating {count} albums...')
        for _ in range(count):
            Album.objects.create(
                title=' '.join(fake.words(nb=2)).title(),
                artist=fake.name(),
                release_year=random.randint(1960, 2023),
                genre=random.choice(['Rock', 'Pop', 'Electronic'])
            )

        self.stdout.write(self.style.SUCCESS('Database has been populated with fake data!'))