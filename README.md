# Sound-Lines

Takes as input a directory of `.m4a` files (`input`) and builds a directory of `.m4a` files (`output`) in which each song title/author/album is replaced by a public transpor line taken from `routes`.
To call it, use `python3 -m main -P`, it will read the routes by reading `routes/agency.csv`, then passing each listed `routes/agency_code.csv` file ('agency_code' field of agency passed as csv).

You can customize input, routes and output directories:

```
usage: main.py [-h] [-F] [-E] [-R] [-P] [-i INPUT] [-r ROUTES] [-o OUTPUT]

options:
  -h, --help            show this help message and exit
  -F, --fix-all-names   fix_all_names($CWD)
  -E, --enumerate       enumerate($CWD)
  -R, --routing         routing($CWD/routes)
  -P, --produce         produce($CWD/routes, $CWD, $CWD/output)
  -i INPUT, --input INPUT
                        input directory
  -r ROUTES, --routes ROUTES
                        routes directory
  -o OUTPUT, --output OUTPUT
                        output directory
```

# Sample Output

```
SETA-PC - 10 - Piazza S. Antonino - I Dossi.m4a                        SETA-PC - 9 - P.za Cittadella - Mortizza.m4a            Trenord - R2 - Bergamo-Treviglio.m4a                Trenord - R8 - Brescia-Piadena-Parma.m4a                                 Trenord - S13 - Pavia-Milano Passante-Milano Bovisa.m4a
SETA-PC - 11 - Piazza Cittadella - Ivaccari.m4a                        Trenord - R11 - Colico-Chiavenna.m4a                    Trenord - R31 - Mortara-Milano.m4a                  Trenord - RE11 - Mantova-Cremona-Codogno-Milano.m4a                      Trenord - S1 - Saronno-Milano Passante-Lodi.m4a
SETA-PC - 12 - P.za Cittadella - Montale - Roncaglia - I Dossi.m4a     Trenord - R12 - Sondrio-Tirano.m4a                      Trenord - R34 - Stradella-Pavia-Milano.m4a          Trenord - RE13 - Alessandria-Pavia-Milano.m4a                            Trenord - S2 - Mariano Comense-Seveso-Milano Passante-Milano Rogoredo.m4a
SETA-PC - 15 - P.za Cittadella - FS - Besurica.m4a                     Trenord - R13 - Lecco-Colico-Sondrio.m4a                Trenord - R35 - Pavia-Torreberetti-Alessandria.m4a  Trenord - RE1 - Laveno-Varese-Saronno-Milano.m4a                         Trenord - S30 - Cadenazzo-Luino-Gallarate.m4a
SETA-PC - 16 - Ferrovia - v.Boselli - Ospedale - FS.m4a                Trenord - R14 - Bergamo-Carnate-Milano.m4a              Trenord - R36 - Pavia-Mortara-Vercelli.m4a          Trenord - RE2 - Bergamo-Pioltello-Milano.m4a                             Trenord - S3 - Saronno-Milano Bovisa-Milano Cadorna.m4a
SETA-PC - 17 - FS - Ospedale - v.Boselli - FS.m4a                      Trenord - R16 - Asso-Milano.m4a                         Trenord - R37 - Pavia-Codogno.m4a                   Trenord - RE3 - Brescia-Iseo-Edolo.m4a                                   Trenord - S40 - Como Camerlata - Como S.G. - Chiasso - Mendrisio - Varese FS.m4a
SETA-PC - 18 - Giarona - Baia Del Re - FS - Cittadella.m4a             Trenord - R17 - Como-Saronno-Milano.m4a                 Trenord - R38 - Piacenza-Lodi-Milano.m4a            Trenord - RE4 - Domodossola-Milano.m4a                                   Trenord - S4 - Camnago-Milano Bovisa-Milano Cadorna.m4a
SETA-PC - 1 - Ferrovia - Belvedere - Ferrovia.m4a                      Trenord - R18 - Como-Molteno-Lecco.m4a                  Trenord - R39 - Codogno-Cremona.m4a                 Trenord - RE5 - Porto Ceresio-Varese-Gallarate-Milano.m4a                Trenord - S50 - Malpensa - Varese FS - Mendrisio - Bellinzona.m4a
SETA-PC - 2 - Montale - S.Lazzaro - S.Antonio.m4a                      Trenord - R1 - Bergamo-Brescia.m4a                      Trenord - R3 - Brescia-Iseo-Breno.m4a               Trenord - RE6 - Verona-Brescia-Milano.m4a                                Trenord - S5 - Varese-Milano Passante-Treviglio.m4a
SETA-PC - 3 - Farnesiana - FS - Veggioletta.m4a                        Trenord - R21 - Luino-Gallarate-Milano.m4a              Trenord - R40 - Cremona-Piadena-Mantova.m4a         Trenord - RE7 - Como-Saronno-Milano.m4a                                  Trenord - S6 - Novara-Milano Passante-Treviglio.m4a
SETA-PC - 4 - Camposanto Vecchio - Borgo Trebbia.m4a                   Trenord - R22 - Varese-Saronno-Milano.m4a               Trenord - R41 - Voghera-Piacenza.m4a                Trenord - RE80 - Locarno - Chiasso - Como - Milano.m4a                   Trenord - S7 - Lecco-Molteno-Monza-Milano.m4a
SETA-PC - 5 - P.za S.Antonino - Peep - Ospedale - P.za S.Antonino.m4a  Trenord - R23 - Domodossola-Arona-Gallarate-Milano.m4a  Trenord - R4 - Brescia-Treviglio-Milano.m4a         Trenord - RE8 - Tirano-Sondrio-Lecco-Milano.m4a                          Trenord - S8 - Lecco-Carnate-Monza-Milano Porta Garibaldi.m4a
SETA-PC - 6 - FS - v.Boselli -FS.m4a                                   Trenord - R25 - Novara-Mortara.m4a                      Trenord - R5 - Brescia-Cremona.m4a                  Trenord - S10 - Como Camerlata - Como S.G. - Mendrisio - Bellinzona.m4a  Trenord - S9 - Saronno-Seregno-Milano S.Cristoforo-Albairate.m4a
SETA-PC - 7 - FS - Ospedale.m4a                                        Trenord - R27 - Novara-Saronno-Milano.m4a               Trenord - R6 - Cremona-Treviglio.m4a                Trenord - S11 - Chiasso - Como - Milano - Rho.m4a                        Trenord - XP1 - Malpensa-Milano Cadorna.m4a
SETA-PC - 8 - FS - Stadio - FS.m4a                                     Trenord - R28 - Malpensa-Saronno-Milano Centrale.m4a    Trenord - R7 - Lecco-Bergamo.m4a                    Trenord - S12 - Melegnano-Milano Passante-Milano Bovisa-Cormano.m4a      Trenord - XP2 - Malpensa-Milano Centrale.m4a
```
