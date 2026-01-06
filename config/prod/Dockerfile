FROM prestashop/prestashop:1.7.8

RUN a2enmod ssl rewrite headers

COPY ssl.conf /etc/apache2/sites-available/000-default.conf

COPY certs /etc/apache2/ssl

COPY child_classic /var/www/html/themes/child_classic

COPY backup/img.tar.gz /tmp/img.tar.gz
RUN tar -xzf /tmp/img.tar.gz -C /var/www/html/ \
 && rm /tmp/img.tar.gz

COPY backup/menu_module.tar.gz /tmp/menu_module.tar.gz
RUN tar -xzf /tmp/menu_module.tar.gz -C /var/www/html/modules \
 && rm /tmp/menu_module.tar.gz

COPY backup/slider_module.tar.gz /tmp/slider_module.tar.gz
RUN tar -xzf /tmp/slider_module.tar.gz -C /var/www/html/modules \
 && rm /tmp/slider_module.tar.gz

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80 443
