import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-l10n-indonesia-partner",
    description="Meta package for open-synergy-ssi-l10n-indonesia-partner Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_l10n_id_partner_identification_bpjs',
        'odoo14-addon-ssi_l10n_id_partner_identification_kependudukan',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
