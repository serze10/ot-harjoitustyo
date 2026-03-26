```mermaid
sequenceDiagram
    autonumber

    participant main
    participant Hallinto as HKLLaitehallinto
    participant Lataaja as Lataajalaite
    participant Lukija6 as Lukijalaite (ratikka6)
    participant Lukija244 as Lukijalaite (bussi244)
    participant Kioski
    participant Kortti as Matkakortti

    %% OLIOIDEN LUOMINEN
    main->>Hallinto: new HKLLaitehallinto()
    activate Hallinto

    main->>Lataaja: new Lataajalaite()
    activate Lataaja

    main->>Lukija6: new Lukijalaite()
    activate Lukija6

    main->>Lukija244: new Lukijalaite()
    activate Lukija244

    %% LAITEHALLINNON METODIKUTSUT
    main->>Hallinto: lisaa_lataaja(Lataaja)
    Hallinto-->main: 

    main->>Hallinto: lisaa_lukija(Lukija6)
    Hallinto-->main:

    main->>Hallinto: lisaa_lukija(Lukija244)
    Hallinto-->main:

    %% KIOSKI JA MATKAKORTIN LUONTI
    main->>Kioski: new Kioski()
    activate Kioski

    main->>Kioski: osta_matkakortti("Kalle")
    activate Kioski
        Kioski->>Kortti: new Matkakortti("Kalle")
        activate Kortti
        Kortti-->Kioski:
    Kioski-->>main: Matkakortti
    deactivate Kioski

    %% LATAUS
    main->>Lataaja: lataa_arvoa(Kortti, 3)
        Lataaja->>Kortti: kasvata_arvoa(3)
        Kortti-->Lataaja:
    Lataaja-->main:

    %% LIPUN OSTO RATIKKA 6
    main->>Lukija6: osta_lippu(Kortti, 0)
        Lukija6->>Kortti: vahenna_arvoa(1.5)
        Kortti-->Lukija6:
    Lukija6-->main:

    %% LIPUN OSTO BUSSI 244
    main->>Lukija244: osta_lippu(Kortti, 2)
        Lukija244->>Kortti: vahenna_arvoa(3.5)
        Kortti-->Lukija244:
    Lukija244-->main:
