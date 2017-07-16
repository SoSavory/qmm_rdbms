from django.core.management.base import BaseCommand, CommandError
from search.models import Article
import os
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        for fn in os.listdir('search/imports'):
            if os.path.isfile(fn):
                with open(fn) as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if row[0] != 'Dimension (1,2,3)':
                            if row[1] == 'F':
                                i_particles = 'fr'
                            else:
                                i_particles = 'bs'
                            if row[2] == 'N':
                                i_trap = False
                            else:
                                i_trap = True
                            if row[3] == 'FT':
                                i_gs_ft = 'ft'
                            else:
                                i_gs_ft = 'gs'
                            if row[4] == 'N':
                                i_spin = False
                            else:
                                i_spin = True
                            if row[5] == 'N':
                                i_mass = False
                            else:
                                i_mass = True

                            _, created = Article.objects.get_or_create(
                                dimension=row[0],
                                particles=i_particles,
                                trap=i_trap,
                                gs_ft=i_gs_ft,
                                spin_imbalance=i_spin,
                                mass_imbalance=i_mass,
                                title=row[7],
                                authors=row[8],
                                link=row[9],
                            )
