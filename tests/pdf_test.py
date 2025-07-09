import shutil
import subprocess
from pathlib import Path

BUILD_DIR = Path('_build/test_pdf')

if BUILD_DIR.exists():
    shutil.rmtree(BUILD_DIR)

subprocess.check_call([
    'sphinx-build', '-c', 'tests/pdf_sample', '-b', 'latex',
    'tests/pdf_sample', str(BUILD_DIR / 'latex')
])
subprocess.check_call(['make', '-C', str(BUILD_DIR / 'latex')])

pdfs = list((BUILD_DIR / 'latex').glob('*.pdf'))
if not pdfs:
    raise SystemExit('PDF not generated')
print('PDF generated:', pdfs[0])
