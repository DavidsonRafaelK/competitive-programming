import os
import re
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROMAN = {1: "", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
ROMAN_LOWER = {1: "", 2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi", 7: "vii", 8: "viii", 9: "ix", 10: "x"}

BULAN = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}


def scan_files(directory, ext):
    path = os.path.join(ROOT, directory)
    if not os.path.isdir(path):
        return []
    files = sorted([
        f for f in os.listdir(path)
        if f.endswith(ext) and not f.endswith(".bak")
    ])
    return files


def filename_to_info(filename, directory):
    ext = os.path.splitext(filename)[1]
    stem = filename.replace(ext, "")

    match = re.match(r"^(.+)-(\d+)$", stem)

    if match:
        base = match.group(1)
        num = int(match.group(2))
        if num == 1:
            slug = base
            display = base.replace("-", " ").title()
        elif num in ROMAN:
            slug = f"{base}-{ROMAN_LOWER[num]}"
            display = f"{base.replace('-', ' ').title()} {ROMAN[num]}"
        else:
            slug = stem
            display = stem.replace("-", " ").title()
    else:
        slug = stem
        display = stem.replace("-", " ").title()

    url = f"https://leetcode.com/problems/{slug}/"
    file_link = f"[`{filename}`]({directory}/{filename})"

    return display, url, file_link


def generate_table(files, directory):
    if not files:
        return "_Belum ada soal._\n"

    lines = ["| # | Soal | File |", "|:-:|------|------|"]
    for i, f in enumerate(files, 1):
        display, url, file_link = filename_to_info(f, directory)
        lines.append(f"| {i} | [{display}]({url}) | {file_link} |")

    return "\n".join(lines) + "\n"


def main():
    py_easy = scan_files("python/easy", ".py")
    py_medium = scan_files("python/medium", ".py")
    py_hard = scan_files("python/hard", ".py")
    sql_files = scan_files("sql", ".sql")

    n_easy = len(py_easy)
    n_medium = len(py_medium)
    n_hard = len(py_hard)
    n_sql = len(sql_files)
    n_python = n_easy + n_medium + n_hard
    n_total = n_python + n_sql

    now = datetime.now()
    bulan = BULAN[now.month]
    tanggal = f"{now.day} {bulan} {now.year}"

    readme = f"""\
<p align="center">
  <img src="https://img.shields.io/badge/Bahasa-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Bahasa-SQL-4479A1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" />
  <img src="https://img.shields.io/badge/Total%20Soal-{n_total}-brightgreen?style=for-the-badge" />
</p>

# Competitive Programming

Kumpulan solusi soal-soal **competitive programming** dari platform [LeetCode](https://leetcode.com/), ditulis menggunakan **Python** dan **SQL**. Repository ini dibuat sebagai dokumentasi perjalanan belajar dan latihan problem solving.

---

## Statistik

| Kategori | Easy | Medium | Hard | Total |
|----------|:----:|:------:|:----:|:-----:|
| Python   | {n_easy}   | {n_medium}      | {n_hard}    | **{n_python}** |
| SQL      | {n_sql}    | -      | -    | **{n_sql}**  |
| **Total**| **{n_easy + n_sql}** | **{n_medium}** | **{n_hard}** | **{n_total}** |

---

## Struktur Proyek

```
competitive-programming/
├── python/
│   ├── easy/                # Soal Python tingkat Easy ({n_easy} soal)
│   ├── medium/              # Soal Python tingkat Medium ({n_medium} soal)
│   └── hard/                # Soal Python tingkat Hard ({n_hard} soal)
├── sql/                     # Soal SQL ({n_sql} soal)
├── scripts/                 # Script otomasi
└── README.md
```

---

## Daftar Soal

### Python - Easy ({n_easy} soal)

{generate_table(py_easy, "python/easy")}
### Python - Medium ({n_medium} soal)

{generate_table(py_medium, "python/medium")}
### Python - Hard ({n_hard} soal)

{generate_table(py_hard, "python/hard")}
### SQL ({n_sql} soal)

{generate_table(sql_files, "sql")}
---

## Cara Menjalankan

### Python

```bash
python3 python/easy/two-sum.py
```

### SQL

Import file `.sql` ke database PostgreSQL/MySQL atau jalankan langsung di platform LeetCode.

---

## Teknologi

- **Python 3** - Bahasa utama untuk menyelesaikan soal algoritma
- **SQL** - Untuk soal-soal database
- **LeetCode** - Platform utama untuk latihan
- **GitHub Actions** - Auto-update README setiap push

---

<p align="center">
  <b>Terakhir diperbarui:</b> {tanggal}
</p>
"""

    readme_path = os.path.join(ROOT, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme)

    print(f"README.md berhasil diperbarui! ({n_total} soal terdeteksi)")


if __name__ == "__main__":
    main()
