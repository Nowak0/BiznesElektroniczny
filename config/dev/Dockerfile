FROM prestashop/prestashop:1.7.8 

RUN rm -rf /var/www/html/cache/*
COPY prestashop/themes/child_classic /var/www/html/themes/child_classic
RUN chown -R www-data:www-data /var/www/html/ 

EXPOSE 80
