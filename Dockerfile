FROM odoo:15.0

USER root

RUN apt-get update && apt-get install -y git && apt-get install -y python3-pip && pip3 install --upgrade pip
RUN pip install git+https://github.com/OCA/openupgradelib.git@master#egg=openupgradelib

COPY ./work/custom /mnt/extra-addons
COPY ./work/official /mnt/extra-addons
COPY install-module.sh .
COPY scaffold.sh .
COPY odoo.conf /etc/odoo/odoo.conf

RUN chown -R odoo:odoo /mnt/extra-addons

USER odoo