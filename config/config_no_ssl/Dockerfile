FROM prestashop/prestashop:1.7.8 

RUN rm -rf /var/www/html/cache/*
RUN rm -rf /var/www/html/var/cache/*

COPY prestashop/themes/child_classic /var/www/html/themes/child_classic
COPY config/config_no_ssl/backup/img.tar.gz /tmp/img.tar.gz
COPY config/config_no_ssl/backup/menu_module.tar.gz /tmp/menu_module.tar.gz
COPY config/config_no_ssl/backup/slider_module.tar.gz /tmp/slider_module.tar.gz

RUN tar -xzf /tmp/img.tar.gz -C /var/www/html/ \
    && tar -xzf /tmp/menu_module.tar.gz -C /var/www/html/modules/ \
    && tar -xzf /tmp/slider_module.tar.gz -C /var/www/html/modules/ \
    && rm -f /tmp/*.tar.gz

RUN chown -R www-data:www-data /var/www/html/
#  && find /var/www/html -type d -exec chmod 755 {} \; \
#  && find /var/www/html -type f -exec chmod 644 {} \;


EXPOSE 80
