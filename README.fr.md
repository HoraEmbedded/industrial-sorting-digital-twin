# Jumeau numérique d'une ligne de tri industrielle

Jumeau numérique et commande par automate d'une ligne de tri industrielle de caisses, réalisés avec Siemens TIA Portal, S7-PLCSIM et Factory I/O.

![Statut](https://img.shields.io/badge/statut-termin%C3%A9-green)
![Licence](https://img.shields.io/badge/licence-MIT-blue)
![Automate](https://img.shields.io/badge/automate-Siemens%20S7--1200-blue)
![Jumeau](https://img.shields.io/badge/jumeau-Factory%20I%2FO-green)
![Tests](https://img.shields.io/badge/tests-29%20valid%C3%A9s-green)

🇫🇷 Français (actuel) | 🇬🇧 [English](README.md)

## Présentation

Ce projet couvre l'ensemble du cycle d'ingénierie d'une ligne de tri automatisée, des exigences à la conception de l'armoire électrique, et valide entièrement le programme de commande en simulation.

- Spécifications fonctionnelles et table d'affectation des entrées-sorties
- Programmation de l'automate dans TIA Portal (S7-1200, langage à contacts)
- Configuration du jumeau numérique dans Factory I/O
- Co-simulation entre S7-PLCSIM et Factory I/O
- Étude électrique de l'armoire de commande
- Indicateurs de performance embarqués dans l'automate
- Plan de tests documenté et rapport technique final

Il est conçu comme un projet de portfolio pour les métiers de l'automatisation industrielle et de la programmation d'automates.

## Résultats clés

| Résultat | Valeur |
| --- | --- |
| Tests validés | **29** (13 modes et sécurité, 12 logique de tri, 4 émission pipelinée) |
| Cadence | **144 caisses/heure**, contre 119 en version une caisse à la fois (**+21 %**) |
| Structure du programme | **6 blocs de code**, 2 structures de données |
| Jumeau numérique | Scène Factory I/O *Sorting by Height (Advanced)*, 18 entrées et 17 sorties mappées |
| Étude électrique | **5 feuilles de schéma**, bilan 24 V de 2,80 A, arrêt d'urgence matériel |
| Affectation E/S | 14 entrées embarquées + 4 sur SM 1221 DI 8, 9 sorties embarquées + 6 sur SM 1222 DQ 8 |

## La ligne simulée

Le jumeau numérique est la scène Factory I/O **Sorting by Height (Advanced)**. Des caisses de deux hauteurs arrivent sur un convoyeur d'entrée et traversent un rideau lumineux qui les mesure. Un plateau tournant oriente ensuite chaque caisse vers le convoyeur de sortie gauche ou droit : caisses basses à gauche, caisses hautes à droite. Un pupitre opérateur fournit les boutons Start, Stop et Reset, l'arrêt d'urgence, un sélecteur Manuel/Auto et un afficheur de comptage.

L'automate cible est un Siemens S7-1200 CPU 1214C DC/DC/DC, programmé en Ladder, exécuté sur S7-PLCSIM et relié à la scène par le driver Siemens S7-PLCSIM.

## Technologies

| Outil | Version ou modèle | Rôle |
| --- | --- | --- |
| Siemens TIA Portal | V18 | Programmation de l'automate |
| Siemens S7-1200 | CPU 1214C DC/DC/DC, firmware V4.6 | Automate cible |
| S7-PLCSIM | V18 SP2 | Automate virtuel |
| Factory I/O | 2.5.10 Ultimate Edition | Jumeau numérique |
| QElectroTech | 0.90 | Schéma électrique, feuilles 1 et 2 |
| Python | 3.13 | Générateur de schéma, feuilles 3 à 5 |
| Git et GitHub | - | Gestion de versions et CI |

## Structure du dépôt

```
.
├── docs/          Documentation technique (en/, fr/, images/)
├── factory-io/    Notes et configuration de la scène
├── plc/           Exports lisibles du programme (XML, PDF)
├── tia-portal/    Archives des projets TIA Portal
├── electrical/    Schéma électrique (QElectroTech et feuilles générées)
├── kpi/           Définition et résultats des KPI
├── screenshots/   Captures d'écran du portfolio
├── videos/        Vidéo de démonstration et liens
├── report/        Rapport PDF final et sources LaTeX
└── scripts/       Contrôles du dépôt et hooks Git
```

## Documentation

- Index de la documentation anglaise : [docs/en](docs/en/README.md)
- Index de la documentation française : [docs/fr](docs/fr/README.md)
- Procédure de co-simulation : [docs/en/runbook-co-simulation.md](docs/en/runbook-co-simulation.md)
- Journal de tests : [docs/en/plc-test-log.md](docs/en/plc-test-log.md)
- Journal de dépannage : [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- Historique des changements : [CHANGELOG.md](CHANGELOG.md)

## Avancement du projet

| Phase | Contenu | Statut |
| --- | --- | --- |
| 1 | Fondations : périmètre, architecture, audit du poste, table d'E/S | Terminé |
| 2 | Sécurité et modes de l'automate (`FB_ModeManager`) | Terminé |
| 3 | Structure du dépôt et documentation bilingue | Terminé |
| 4 | Logique de tri et émission pipelinée (`FB_SortingLogic`) | Terminé |
| 5 | Tests de co-simulation (S7-PLCSIM et Factory I/O) | Terminé |
| 6 | Schéma électrique (5 feuilles) | Terminé |
| 7 | Bloc KPI (`FB_Kpi`), captures et tables de surveillance | Terminé |
| 8 | Rapport final et version 1.0 | Terminé |

## Prise en main

1. Cloner le dépôt.
2. Installer les outils listés dans [docs/en/software-versions.md](docs/en/software-versions.md).
3. Suivre la [procédure de co-simulation](docs/en/runbook-co-simulation.md) pour démarrer TIA Portal, S7-PLCSIM et Factory I/O dans le bon ordre.
4. Exécuter le plan de tests de [docs/en/plc-test-log.md](docs/en/plc-test-log.md) pour reproduire les 29 validations.

## Politique de langue

L'anglais est la langue de référence de ce dépôt. Les traductions françaises sont ajoutées progressivement dans `docs/fr` et dans ce fichier.

## Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence

Publié sous licence MIT. Voir [LICENSE](LICENSE).

## Auteur

[HoraEmbedded](https://github.com/HoraEmbedded)