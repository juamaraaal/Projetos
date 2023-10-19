create schema exemplolivro;
use exemplolivro;

create table livro(
cd_livro int primary key not null auto_increment,
nome varchar (45) not null,
lingua varchar (45) not null,
ano int not null
);
create table editora(
cd_editora int primary key not null auto_increment,
nome varchar(45) not null,
telefone varchar (16) not null,
endereco varchar (100) not null
);
create table autor(
cd_autor int primary key not null auto_increment,
nome varchar (45) not null,
dataNascimento date not null,
paisNascimento varchar (45) not null,
notaBibliografica text not null
);
create table livro_autor(
cd_livro int not null,
cd_autor int not null, 
constraint foreign key (cd_livro) references livro(cd_livro), 
constraint foreign key (cd_autor) references autor(cd_autor)
);
create table edicao(
cd_edicao int primary key not null auto_increment,
ISBN varchar(45) not null,
preco decimal(10,2) not null,
ano int not null,
numPaginas int not null,
quantidade int not null,
cd_livro int null,
cd_editora int null,
constraint foreign key(cd_livro) references livro (cd_livro),
constraint foreign key (cd_editora) references editora (cd_editora)
);

