FROM registry.fedoraproject.org/fedora:31
ENV PYTHONPATH=/usr/share/koschei
EXPOSE 8080

RUN : \
 && dnf -y --refresh update \
 && dnf -y install \
      python3-sqlalchemy \
      python3-psycopg2 \
      python3-rpm \
      python3-flask \
      python3-flask-sqlalchemy \
      python3-flask-wtf \
      python3-wtforms \
      python3-humanize \
      python3-jinja2 \
      python3-memcached \
      python3-mod_wsgi \
      python3-fedora-messaging \
      httpd \
      js-jquery \
      mod_auth_openidc \
      python3-koji \
      python3-hawkey \
      python3-librepo \
      python3-dogpile-cache \
      python3-alembic \
      postgresql \
 && dnf -y clean all \
 && useradd koschei \
 && :

COPY bin/ /usr/bin/
COPY ./ /usr/share/koschei/

RUN : \
 && chmod -R a+rwX /usr/share/koschei/ \
 && mkdir -m 777 /var/cache/koschei/ /var/cache/koschei/repodata/ \
 && :

USER koschei
