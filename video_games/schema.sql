drop table if exists videogame;
create table videogame (
  Rank integer, 
  Name text, 
  Platform text, 
  Year integer not null,
  Genre text, 
  Publisher text, 
  NA_Sales decimal(8,2) not null,
  EU_Sales decimal(8,2)not null,
  JP_Sales decimal(8,2) not null,
  Other_Sales decimal(8,2) not null, 
  Global_Sales decimal(8,2) not null 
);
