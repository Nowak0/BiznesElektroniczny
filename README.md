# Electronic Business – Team Project (PrestaShop 1.7.8)

This project is developed for the course **Electronic Business (Biznes Elektroniczny)**. The application is an online store based on **PrestaShop 1.7.8**, running in Docker containers using the `docker-compose.yml` file located in the `config/` subfolder.

## Team

- Jakub Nowak ([Nowak0](https://github.com/Nowak0))
- Oliwier Komorowski ([ol1c](https://github.com/ol1c))
- Artur Szlędak ([DokkaDok](https://github.com/DokkaDok))
- Paweł Demski ([Esce-gh](https://github.com/Esce-gh))

## Project foundation

The store is based on the concepts and layout of: [monocerus.pl](https://monocerus.pl)  
The project uses a **custom child theme**: `child_theme`.

## Tech stack

| Component              | Technologies / details                                   |
| ---------------------- | -------------------------------------------------------- |
| Store engine           | PrestaShop 1.7.8                                         |
| Frontend / templates   | Smarty + HTML (theme + child theme)                      |
| Backend / extensions   | PHP + PrestaShop modules                                 |
| Styling                | CSS                                                      |
| Helper scripts         | Shell (`restore.sh`)                                     |
| Tooling / automation   | Docker, docker-compose (configs in `config/`)            |
| Mail / dev tooling     | MailHog (directory `mailhog/`)                           |
| Automated testing      | Python (directory `automatic_testing/`)                  |
| Scraping / data helper | Scraper (directory `scraper/`)                           |
| Analytics              | Google Analytics (tracking: purchase, user registration) |
| Database               | MySQL (container `prestashop-db`)                        |

Languages used in the repository (according to GitHub):  
HTML • Smarty • Python • CSS • PHP • Shell

## Structure (excerpt)

```
/
├─ config/              (env / docker config: dev, prod)
├─ prestashop/          (PrestaShop project files)
│  └─ themes/           (themes)
├─ mailhog/             (MailHog setup)
├─ scraper/             (scraper + assets/results)
├─ automatic_testing/   (automated tests)
└─ README.md
```

## Prerequisites

- Docker Engine installed
- Docker Compose installed (plugin or integrated in newer Docker versions)
- OS: Linux / macOS / Windows (WSL recommended on Windows)
- Sufficient RAM (min. ~2 GB free for smooth operation)

## Getting started (quick start)

1. Clone the repository:

   ```bash
   git clone https://github.com/Nowak0/BiznesElektroniczny.git
   cd BiznesElektroniczny
   ```

2. Go to the directory with `docker-compose.yml`:

   e.g.

   ```bash
   cd config/dev
   ```

3. Build and start the containers:

   ```bash
   docker compose build
   docker compose up -d
   ```

   After startup:

   - App container: `prestashop`
   - Database container: `prestashop-db`

4. (Optional) Check logs:

   ```bash
   docker compose logs -f prestashop
   ```

5. When the store is up (both back office and front office respond), go back to the project root (if needed) and run the restore script:

   ```bash
   bash restore.sh
   ```

   If you are using Windows PowerShell, you can run the commands from inside the script manually (see below).

## Data restore script: restore.sh

The script performs:

- Import of the database dump (`prestashop.sql`) into the MySQL container
- Extraction of product images/assets into `/var/www/html/img`
- Setting correct file permissions
- Extraction of the used modules
- Setting permissions for the modules

## PrestaShop configuration

After restoring the data:

1. Open the back office (URL depends on container settings; e.g., http://localhost:8081/admin123).
2. Verify:
   - The `child_theme` theme is active
   - Product thumbnails and images display correctly
3. If needed, clear the cache:
   - Back office -> Advanced Parameters -> Performance -> Clear cache
   - Or manually: `docker exec prestashop rm -rf /var/www/html/var/cache/*`

## Common issues

| Issue                    | Possible cause                             | Solution                                           |
| ------------------------ | ------------------------------------------ | -------------------------------------------------- |
| Missing product images   | Archive not extracted or wrong permissions | Re-run the restore.sh part related to `img.tar.gz` |
| Theme not active         | DB not imported or theme not switched      | Activate `child_theme` in the back office          |
| 500 error in back office | Cache or missing PHP extensions            | Clear cache, check container logs                  |

## Contact

For project-related matters, please contact the team members (Jakub, Oliwier, Artur, Paweł) or open an Issue in the repository.
