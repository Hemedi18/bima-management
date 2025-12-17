import csv
from django.core.management.base import BaseCommand
from students.models import Student
import os

class Command(BaseCommand):
    help = 'Imports students from a CSV file into the database'

    def handle(self, *args, **kwargs):
        # Hakikisha faili la names.csv liko kwenye mzizi mkuu wa mradi
        file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'names.csv')
        
        self.stdout.write(self.style.SUCCESS(f'Inaanza kuingiza data kutoka {file_path}'))

        try:
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    reg_num = row.get('REG NUMBER', '').strip()
                    full_name = row.get('NAME', '').strip()
                    phone_num = row.get('PHONE NUMBER', '').strip() or None

                    if not reg_num or not full_name:
                        self.stdout.write(self.style.WARNING(f'Kuruka mstari: REG NUMBER au Jina halipo. Mstari: {row}'))
                        continue

                    student, created = Student.objects.update_or_create(
                        registration_number=reg_num,
                        defaults={
                            'full_name': full_name,
                            'phone_number': phone_num,
                            'is_registered': bool(phone_num)
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Imeongezwa: {student.full_name}'))
                    else:
                        self.stdout.write(self.style.NOTICE(f'Imesasishwa: {student.full_name}'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Hitilafu: Faili la {file_path} halijapatikana.'))
        
        self.stdout.write(self.style.SUCCESS('Uingizaji wa data umekamilika!'))

