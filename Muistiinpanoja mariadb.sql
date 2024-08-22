-- Luo paikallinen käyttäjä "Ira", jonka salasana on "lunni"
CREATE USER ira@localhost IDENTIFIED BY 'lunni'

-- jokainen komento päättyy: ; tai \g.



-- Poista tietokanta, jos se on jo olemassa
DROP DATABASE IF EXISTS ankkalinna;

-- tähän voi laittaa muistiinpanoja, kahden viivan jälkeen, jolloin sql ei huomioi

-- Luo ankkalinnatietokanta:
--CREATE DATABASE ankkalinna; kopioi alla olevat kappale kerrallaan mariadb:hen
              -- open in finder, valitse mariadb-testi -kansiosta??
CREATE DATABASE ankkalinna;
    USE ankkalinna;

create table ankkalinnalainen(
    ID int not null auto_increment,
    etunimi varchar(40),
    sukunimi varchar(40),
    primary key (id)
    );

create table lemmikki(
    ID int not null auto_increment,
    nimi varchar(40),
    primary key (id)
    );

create table omistaa(
    lemmikki_ID int,
    ankkalinnalainen_ID int,
    primary key (lemmikki_ID,ankkalinnalainen_ID),
    foreign key (lemmikki_ID) references lemmikki(ID),
    foreign key (ankkalinnalainen_ID) references ankkalinnalainen(ID)
    );

insert into ankkalinnalainen(etunimi, sukunimi)
    values("Aku", "Ankka"),("Roope", "Ankka"),
    ("Tupu", "Ankka"), ("Milla", "Magia"), ("Mikki", "Hiiri");

insert into lemmikki(nimi)
    values ("Pulivari"), ("Pluto"), ("Korri");

insert into omistaa(lemmikki_ID, ankkalinnalainen_ID)
values(1,1),(1,3),(2,5),(3,4);


-- Anna oikeudet fligt_game -tietokantaan, luku- ja päivitysoikeudet:
       -- usernameksi oma tunnus, asenna kanta ensin:
GRANT SELECT, INSERT, UPDATE ON database_name.* TO username@localhost;

-- esimerkki: hae lemmikit taulun kaikki sisältä:
SELECT * from lemmikki

--kirjautuminen omalla käyttäjällä: mysql -u käyttäjä -p , ennen sitä rootista exit.
    --kirjoita pelkästään exit
    --kirjautuminen:  mysql -u ira -p
    --  -p tarkoittaa, että kysyy salasanaa.