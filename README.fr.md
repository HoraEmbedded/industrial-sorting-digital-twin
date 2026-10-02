# Jumeau numérique d'une ligne de tri industrielle

Jumeau numérique et contrôle par automate d'une ligne de tri industrielle, réalisés avec Siemens TIA Portal, S7-PLCSIM et Factory I/O.

![Statut](https://img.shields.io/badge/statut-en%20cours-yellow)
![Licence](https://img.shields.io/badge/licence-MIT-blue)
![Automate](https://img.shields.io/badge/automate-Siemens%20S7--1200-blue)
![Jumeau](https://img.shields.io/badge/jumeau-Factory%20I%2FO-green)

🇫🇷 Français (actuel) | 🇬🇧 [English](README.md)

## Présentation

Ce projet couvre l'ensemble du cycle d'ingénierie d'une ligne de tri automatisée :

- Spécifications fonctionnelles et table d'affectation des entrées et sorties
- Programmation de l'automate dans TIA Portal (S7-1200, langage à contacts)
- Configuration du jumeau numérique dans Factory I/O
- Co-simulation entre S7-PLCSIM et Factory I/O
- Schéma électrique
- Définition et suivi des indicateurs de performance
- Vidéo de démonstration et rapport technique final

Il est conçu comme un projet de portfolio pour les métiers de l'automatisation industrielle et de la programmation d'automates.

## La ligne simulée

Le jumeau numérique est la scène Factory I/O **Sorting by Height (Advanced)**. Des caisses de deux hauteurs différentes arrivent sur un convoyeur d'entrée et sont mesurées par un rideau lumineux. Un plateau tournant oriente ensuite chaque caisse vers le convoyeur de sortie gauche ou droit. Un pupitre opérateur fournit les boutons Start, Stop et Reset, l'arrêt d'urgence, un sélecteur Manuel/Auto et un compteur de caisses.

## Technologies

| Outil | Version ou modèle | Rôle |
| --- | --- | --- |
| Siemens TIA Portal | V18 | Programmation de l'automate |
| Siemens S7-1200 | CPU 1214C DC/DC/DC, firmware V4.6 | Automate cible |
| S7-PLCSIM | Même génération que TIA Portal | Automate virtuel |
| Factory I/O | v2.5.10, Ultimate Edition | Jumeau numérique |
| QElectroTech | - | Schéma électrique |
| Git et GitHub | - | Gestion de versions |

## Structure du dépôt

```
.
├── docs/          Documentation technique (en/, fr/, images/)
├── factory-io/    Notes et configuration de la scène
├── plc/           Exports lisibles du programme (XML, PDF)
├── tia-portal/    Archives des projets TIA Portal
├── electrical/    Schéma électrique (QElectroTech)
├── kpi/           Définition et résultats des KPI
├── screenshots/   Captures d'écran du portfolio
├── videos/        Vidéo de démonstration et liens
├── report/        Rapport PDF final et ressources
└── scripts/       Contrôles du dépôt et hooks Git
```

## Documentation

- Index de la documentation en anglais : [docs/en](docs/en/README.md)
- Index de la documentation en français : [docs/fr](docs/fr/README.md)
- Journal de dépannage : [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Historique des changements : [CHANGELOG.md](CHANGELOG.md)

## Avancement du projet

| Phase | Contenu | Statut |
| --- | --- | --- |
| 1 | Fondations : périmètre, architecture, audit du poste, table d'E/S | Terminé |
| 2 | Sécurité et modes de l'automate (`FB_ModeManager`) | Terminé |
| 3 | Nettoyage du dépôt et documentation bilingue | En cours |
| 4 | Logique de tri pour la scène Advanced | Prévu |
| 5 | Tests de co-simulation (S7-PLCSIM et Factory I/O) | Prévu |
| 6 | Schéma électrique | Prévu |
| 7 | KPI, vidéo de démonstration et captures | Prévu |
| 8 | Rapport final et version 1.0 | Prévu |

## Prise en main

1. Cloner le dépôt.
2. Suivre la [procédure de co-simulation](docs/en/runbook-co-simulation.md) (en anglais) pour démarrer TIA Portal, S7-PLCSIM et Factory I/O dans le bon ordre.
3. Les étapes complètes de reproduction seront publiées avec la version 1.0.

## Politique de langue

L'anglais est la langue de référence. Les traductions françaises sont ajoutées progressivement dans `docs/fr` et dans ce fichier.

## Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Publié sous licence MIT. Voir [LICENSE](LICENSE).

## Auteur

[HoraEmbedded](https://github.com/HoraEmbedded)