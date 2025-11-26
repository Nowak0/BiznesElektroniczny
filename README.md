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

| Component            | Technologies / details            |
| -------------------- | --------------------------------- |
| Store engine         | PrestaShop 1.7.8                  |
| Frontend / templates | Smarty (theme + child theme)      |
| Backend / extensions | PHP + PrestaShop modules          |
| Styling              | CSS                               |
| Helper scripts       | Shell                             |
| Tooling / automation | Docker, docker-compose            |
| Database             | MySQL (container `prestashop-db`) |

Languages used in the repository (according to GitHub):  
Smarty • Python • CSS • PHP

## Structure (excerpt)

```
/
├─ config/
│  ├─ docker-compose.yml
│  ├─ (container configuration files)
├─ themes/
│  ├─ child_theme/          (custom child theme)
├─ modules/                 (optional custom modules)
├─ restore.sh               (script restoring data and assets)
├─ prestashop.sql           (database dump)
├─ img.tar.gz               (images archive for /var/www/html/img)
├─ cod_module.tar.gz        (Cash On Delivery module archive)
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

   ```bash
   cd config
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
- Extraction of the Cash On Delivery module
- Setting permissions for the module

Core operations (for reference):

```bash
# Database import
type prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop

# Extract images
type img.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/img
docker exec prestashop chown -R www-data:www-data /var/www/html/img/p

# Extract COD module
type cod_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules
docker exec prestashop chown -R www-data:www-data /var/www/html/modules/ps_cashondelivery
```

If you use Linux/macOS and encounter issues with `type`, you can use `cat` equivalents:

```bash
cat prestashop.sql | docker exec -i prestashop-db mysql --default-character-set=utf8mb4 -u root -pprestashop prestashop
cat img.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/img
cat cod_module.tar.gz | docker exec -i prestashop tar xzf - -C /var/www/html/modules
```

## PrestaShop configuration

After restoring the data:

1. Open the back office (URL depends on container settings; e.g., http://localhost:8080/admin123).
2. Verify:
   - The `child_theme` theme is active
   - The `ps_cashondelivery` module is available
   - Product thumbnails and images display correctly
3. If needed, clear the cache:
   - Back office -> Advanced Parameters -> Performance -> Clear cache
   - Or manually: `docker exec prestashop rm -rf /var/www/html/var/cache/*`

## Useful commands

```bash
# List containers
docker ps

# Shell into the app container
docker exec -it prestashop bash

# Database backup (example)
docker exec prestashop-db mysqldump -u root -pprestashop prestashop > backup.sql

# Restart services
docker compose restart
```

## Common issues

| Issue                    | Possible cause                              | Solution                                                     |
| ------------------------ | ------------------------------------------- | ------------------------------------------------------------ |
| Missing product images   | Archive not extracted or wrong permissions  | Re-run the restore.sh part related to `img.tar.gz`           |
| Theme not active         | DB not imported or theme not switched       | Activate `child_theme` in the back office                    |
| COD module not working   | Incorrect extraction or missing permissions | Check `modules/ps_cashondelivery` and set proper permissions |
| 500 error in back office | Cache or missing PHP extensions             | Clear cache, check container logs                            |

## Roadmap / further development

- Add CI/CD (GitHub Actions) for image builds
- Automatic seeding of demo data
- Integration with external payment services
- Automated tests (e.g., Playwright / Cypress for frontend, PHPUnit for modules)

## License

(Insert license information – e.g., MIT / none / institutional. If no formal license, it’s good to clarify.)

## Contact

For project-related matters, please contact the team members (Jakub, Oliwier, Artur, Paweł) or open an Issue in the repository.
